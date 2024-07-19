try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
import struct
import time

# Indirizzo IP e porta del dispositivo Modbus
host = '192.168.100.10'
port = 503

# Crea il client Modbus
client = ModbusTcpClient(host, port)

try:
    # Tenta di connettersi al dispositivo
    connection = client.connect()
    if not connection:
        raise ConnectionException(f"Failed to connect to {host}:{port}")

    while True:
        try:
            # Legge i registri
            rr1 = client.read_holding_registers(0, 50, unit=1)
            if rr1.isError():
                raise ConnectionException(f"Error reading registers: {rr1}")
            
            rr2 = client.read_holding_registers(133, 50, unit=1)
            if rr2.isError():
                raise ConnectionException(f"Error reading registers: {rr2}")
            
            # Decodifica i valori reali (4 registri, 2 per ciascun valore)
            real1 = struct.unpack('>f', struct.pack('>HH', rr1.registers[0], rr1.registers[1]))[0]
            real2 = struct.unpack('>f', struct.pack('>HH', rr1.registers[2], rr1.registers[3]))[0]

            # Decodifica i valori booleani
            bool1 = bool(rr1.registers[4] & 0x0100)  # Controlla il bit 8
            bool2 = bool(rr1.registers[4] & 0x0200)  # Controlla il bit 9

            # Decodifica le stringhe (20 registri, 10 per ciascuna stringa, 20 caratteri al massimo per stringa)
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
            
            string1 = decode_string(6, 10, rr1.registers)
            string2 = decode_string(1, 10, rr2.registers)

            # Decodifica i caratteri (2 registri, 1 per ciascun carattere)
            char1 = chr(rr1.registers[25] & 0xFF) + chr((rr1.registers[25] >> 8) & 0xFF)
            char2 = chr(rr1.registers[26] & 0xFF) + chr((rr1.registers[26] >> 8) & 0xFF)

            # Stampa i risultati
            print(f"Real 1: {real1}")
            print(f"Real 2: {real2}")
            print(f"Bool 1: {bool1}")
            print(f"Bool 2: {bool2}")
            print(f"String 1: {string1}")
            print(f"String 2: {string2}")
            print(f"Char 1: {char1}")
            print(f"Char 2: {char2}")

        except ConnectionException as e:
            print(f"ConnectionException: {e}")

        # Attendi 5 secondi prima di eseguire un'altra lettura
        time.sleep(5)

finally:
    # Chiude la connessione
    client.close()
