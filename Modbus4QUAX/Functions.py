try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
from datetime import datetime
import json
import time
import struct
import math

#----------------------------------------------------------------------------------------------------------------
# DEFINIZIONE DELLE FUNZIONI

# Funzione per controllare i bit 8, 9, 10, 11
def check_bits(value):
    bit_8 = bool(value & 0x0100)
    bit_9 = bool(value & 0x0200)
    bit_10 = bool(value & 0x0400)
    bit_11 = bool(value & 0x0800)
    return bit_8, bit_9, bit_10, bit_11

# Decodifica la stringa (20 caratteri al massimo, 2 caratteri per registro)
def decode_string(start, length, register):
    result = ''
    for i in range(length):
        high_byte = (register[start + i] >> 8) & 0xFF
        low_byte = register[start + i] & 0xFF
        if high_byte != 0:
            result += chr(high_byte)
        if low_byte != 0:
            result += chr(low_byte)
    return result

# Converte una lista di registri dove sono salvati i valori float
def registers_to_float(registers):
    # Converte una lista di registri Modbus (16 bit) in una lista di valori floating point (32 bit)"""
    floats = []
    for i in range(0, len(registers), 2):
        # Combina due registri da 16 bit in un singolo valore a 32 bit
        high = registers[i]
        low = registers[i + 1]
        # Combina i registri in un intero a 32 bit
        combined = (high << 16) | low
        # Converte l'intero a 32 bit in un valore floating point
        float_value = struct.unpack('>f', struct.pack('>I', combined))[0]
        floats.append(float_value)
    return floats

# Converte dei all'interno dei registri di valori float a distanza costante
def convert_registers_to_float(high, low):
    """Converte due registri Modbus (high e low) in un valore float."""
    packed = struct.pack('>HH', high, low)
    return struct.unpack('>f', packed)[0]

def read_and_decode_floats(client, start_address, count, unit, jumper):
    """
    Legge e decodifica valori float dai registri Modbus ogni 15 registri.

    Args:
    - client: Il client Modbus.
    - start_address (int): L'indirizzo di partenza per la lettura.
    - count (int): Il numero di letture da fare.
    - unit (int): L'unità Modbus da cui leggere.

    Returns:
    - list of float: Lista di valori float decodificati.
    """
    floats = []
    for i in range(count):
        address = start_address + i * jumper
        rr = client.read_holding_registers(address, 2, unit=unit)
        if rr.isError():
            raise ConnectionException(f"Error reading registers at address {address}: {rr}")
        high = rr.registers[0]
        low = rr.registers[1]
        value = convert_registers_to_float(high, low)
        floats.append(value)
    return floats

# Funzione per arrotondare un numero a un numero specifico di cifre significative
def round_to_significant_figures(num, sig_figs):
    """
    Approssima un numero a un numero specifico di cifre significative e lo formatta in notazione esponenziale.
    
    Args:
    - num (float): Il numero da approssimare.
    - sig_figs (int): Il numero di cifre significative.

    Returns:
    - str: Il numero approssimato in notazione esponenziale
    - float: Il numero approssimato a cifre significative.
    """
    if num == 0:
        return f"{0:.{sig_figs-1}e}"
    # else:
    #     # Calcola il numero di cifre decimali a cui arrotondare
    #     rounded_num = round(num, sig_figs - int(math.floor(math.log10(abs(num)))) - 1)
    #     # Format in notazione esponenziale
    #     exp_format = f"{rounded_num:.{sig_figs-1}e}"
    #     # Trasforma la notazione per essere nel formato x.yzw e^kk
    #     base, exponent = exp_format.split('e')
    #     return f"{base} e^{int(exponent)}"
    else:
        # Calcola il numero di cifre decimali a cui arrotondare
        rounded_num = round(num, sig_figs - int(math.floor(math.log10(abs(num)))) - 1)
        return rounded_num

# Funzione per verificare se una variabile è una stringa e, in caso affermativo, assegna il valore 0
def check_and_reset_if_string(variable):
    """
    Verifica se la variabile è una stringa. Se vero, assegna il valore 0 alla variabile.

    Args:
    - variable: La variabile da verificare e potenzialmente modificare.

    Returns:
    - La variabile modificata se era una stringa, altrimenti la variabile originale.
    """
    if isinstance(variable, str):
        variable = 0
    return variable
    

# Funzione per ottenere l'ora corrente
def current_time():
    # Ottieni l'ora corrente
    now = datetime.now()
    # Formatta l'ora corrente come dd/mm/yyyy:hh:mm
    formatted_time = now.strftime("%d/%m/%Y:%H_%M")
    return formatted_time

#----------------------------------------------------------------------------------------------------------------
# CLASS DEFINITION
class QUAXDevice:
    def __init__(self, time, name, header, values, unit, state):
        self.time = time
        self.name = name
        self.header = header
        self.values = values
        self.unit = unit
        self.state = state

def PumpDecode(pump_device):
    pumpIdx = 0
    outStr = ''
    for pump in pump_device.header:
        outStr += f"{pump}'s PUMP:"   
        # START/OK/WARNING/ALARM
        outStr += f"  {'ON' if pump_device.values[0+4*pumpIdx] else '💤OFF'}" + "\n"    
        outStr += f"  {'🟢' if pump_device.values[1+4*pumpIdx] else '🟡'}"       
        outStr += f"  {'🟢' if pump_device.values[2+4*pumpIdx] else '🟡'}"
        outStr += f"  {'🟢' if pump_device.values[3+4*pumpIdx] else '🔴'}" + "\n"
        
        outStr += f"  {'' if pump_device.values[2+4*pumpIdx] else ' WARNING -'}"
        outStr += f"  {'' if pump_device.values[3+4*pumpIdx] else 'ALARM'}"
        outStr += "\n\n"
        pumpIdx += 1
    return outStr

#----------------------------------------------------------------------------------------------------------------
# MAIN CODE FOR READING REGISTERS AND DECODING VALUES
def ReadPLC(host, port):

    PumpsHeader = ["IVC1", "IVC2", "1KP1", "1KP2", "EMOD1"]
    CCiHeader = ["ChA", "ChB", "ChC", "ChD", "ChE", "ChF", "ChG", "ChH"]
    PMGHeader = ["Gauge1", "Gauge2", "Gauge3", "Gauge4", "Gauge5", "Gauge6"]
    PSGHeader = ["Gauge1", "Gauge2"]
    PumpsValues = [0.0]*20
    CCiValues = [0.0]*8
    PMGValues = [0.0]*6
    PSGValues = [0.0]*2
    HDIValues = [0.0]

    # Crea il client Modbus
    client = ModbusTcpClient(host, port)
    try:
        # Tenta di connettersi al dispositivo
        connection = client.connect()
        if not connection:
            raise ConnectionException(f"Failed to connect to {host}:{port}")
        
        #----------------------------------------------------------------------------------------------------
        # LETTURA DEI REGISTRI
        start_address = 0
        count = 0
        unit = 1
        jumper = 1
        # Legge i registri degli stati dell pompe
        start_address = start_address + count * jumper
        count = 5 
        jumper = 1
        pumps_rr = client.read_holding_registers(start_address, count, unit)
        if pumps_rr.isError():
            raise ConnectionException(f"Error reading pumps registers: {pumps_rr}")
                
        # Legge 2 registri ogni 15 per gli 8 canali del CCi
        start_address = start_address + count * jumper
        count = 8 
        jumper = 15
        CCi_channels = read_and_decode_floats(client, start_address, count, unit, jumper)
                
        # Legge i registri delle letture delle gauges della PMG
        start_address = start_address + count * jumper
        count = 12 
        jumper = 1
        PMG_gauges_rr = client.read_holding_registers(start_address, count, unit)
        if PMG_gauges_rr.isError():
                raise ConnectionException(f"Error reading PMG registers: {PMG_gauges_rr}")
                
        # Legge i registri delle letture delle gauges della PSG
        start_address = start_address + count * jumper
        count = 4 
        jumper = 1
        PSG_gauges_rr = client.read_holding_registers(start_address, count, unit)
        if PSG_gauges_rr.isError():
            raise ConnectionException(f"Error reading PSG registers: {PSG_gauges_rr}")
                
        # Legge i registri della lettura dell'HDI
        start_address = start_address + count * jumper
        count = 2 
        jumper = 1
        HDI_read_rr = client.read_holding_registers(start_address, count, unit)
        if HDI_read_rr.isError():
            raise ConnectionException(f"Error reading HDI registers: {HDI_read_rr}")
                
        start_address = start_address + count * jumper
        count = 9 
        jumper = 1
        HDI_unit_rr = client.read_holding_registers(start_address, count, unit)
        if HDI_unit_rr.isError():
            raise ConnectionException(f"Error reading HDI registers: {HDI_unit_rr}")
        HDI_unit = decode_string(0, 4, HDI_unit_rr.registers)
                
        start_address = start_address + count * jumper
        count = 8 
        jumper = 1
        HDI_state_rr = client.read_holding_registers(start_address, count, unit)
        if HDI_state_rr.isError():
            raise ConnectionException(f"Error reading HDI registers: {HDI_state_rr}")
        HDI_state = decode_string(0, 4, HDI_state_rr.registers)
                
        start_address = start_address + count * jumper
        count = 12 
        jumper = 1
        HDI_ch_rr = client.read_holding_registers(start_address, count, unit)
        if HDI_ch_rr.isError():
            raise ConnectionException(f"Error reading HDI registers: {HDI_ch_rr}")
        HDI_ch = decode_string(0, 2, HDI_ch_rr.registers)
                
        #----------------------------------------------------------------------------------------------------
        # DECODIFICA DELLE LETTURE
        print(f"LOG of {current_time()}")

        # Decodifica degli stati delle pompe
        i = 0
        for idx in PumpsHeader:                  
            register_value = pumps_rr.registers[i]               
            bit_8, bit_9, bit_10, bit_11 = check_bits(register_value)
            status = [bit_8, bit_9, bit_10, bit_11]
            for j in range(4):
                if status[j]:
                   PumpsValues[i*4+j] = 1
                else:
                   PumpsValues[i*4+j] = 0
            i += 1
        # salvataggio della classe                    
        QUAXPumps = QUAXDevice(time = current_time(),
                                name = 'PUMPS',
                                header = PumpsHeader, 
                                values = PumpsValues,
                                unit = 'HIGH/LOW',
                                state = 'START/OK/WARNING/ALARM')    

        # Decodifica delle letture dei CH del CCi
        for idx, value in enumerate(CCi_channels):
            CCiValues[idx] = check_and_reset_if_string(round_to_significant_figures(value, 4)) 
        # salvataggio della classe                    
        QUAXCryoCon18i = QUAXDevice(time = current_time(),
                                name = 'CryoCon18i',
                                header = CCiHeader, 
                                values = CCiValues,
                                unit = 'K',
                                state = 'State Not Available')    

        # Decodifica delle letture delle gauges della PMG
        float_values = registers_to_float(PMG_gauges_rr.registers)
        for i in range(6):
           PMGValues[i] = check_and_reset_if_string(round_to_significant_figures(float_values[i], 4))  
        # salvataggio della classe                    
        QUAXPfeiffereMaxiGauge = QUAXDevice(time = current_time(),
                                name = 'Pfeiffer MaxiGauge',
                                header = PMGHeader, 
                                values = PMGValues,
                                unit = 'mbar',
                                state = 'State Not Available')    

        # Decodifica delle letture delle gauges della PSG
        float_values = registers_to_float(PSG_gauges_rr.registers)
        for i in range(2):
            PSGValues[i] = check_and_reset_if_string(round_to_significant_figures(float_values[i], 4))  
        # salvataggio della classe                    
        QUAXPfeiffereSingleGauge = QUAXDevice(time = current_time(),
                                name = 'Pfeiffer SingleGauge',
                                header = PSGHeader, 
                                values = PSGValues,
                                unit = 'mbar',
                                state = 'State Not Available') 

        # Decodifica delle letture dell'a HDI
        float_values = registers_to_float(HDI_read_rr.registers)
        HDIValues[0] = check_and_reset_if_string(round_to_significant_figures(float_values[0], 4))
        # salvataggio della classe                    
        QUAXPHeliumDI = QUAXDevice(time = current_time(),
                                name = 'Helium Depth Indicator',
                                header = HDI_ch, 
                                values = HDIValues,
                                unit = HDI_unit,
                                state = HDI_state) 

    finally:
        # Chiude la connessione
        client.close()

    return QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge, QUAXPfeiffereSingleGauge, QUAXPHeliumDI
        

#----------------------------------------------------------------------------------------------------------------
# Esempio di utilizzo

# MOPDBUS CLIENT CONFIGURATION
# Indirizzo IP e porta del dispositivo Modbus
if __name__ == "__main__":
    host = '192.168.100.10'
    port = 503

    # Crea il client Modbus
    client = ModbusTcpClient(host, port)
    QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge, QUAXPfeiffereSingleGauge, QUAXPHeliumDI = ReadPLC(host, port)
    results = [QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge,
                QUAXPfeiffereSingleGauge, QUAXPHeliumDI]
    for result in results:
        print(result.time)
        print(result.header)
        print(result.values)
        print(result.unit)
        print(result.state)
