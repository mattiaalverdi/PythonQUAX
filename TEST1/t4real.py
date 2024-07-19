try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient

from datetime import datetime
import json
import time
import struct

def current_time():
    now = datetime.now().isoformat()
    return now

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

host = '192.168.100.10'
port = 503
client = ModbusTcpClient(host, port)

while True:
    if not client.is_socket_open():
        client.connect()

    # Legge 20 registri di holding a partire dall'indirizzo 0 (10 valori floating point richiedono 20 registri)
    rr = client.read_holding_registers(125, 12, unit=1)
    
    if rr is not None and rr.registers:
        float_values = registers_to_float(rr.registers)
        data = {
            "time": current_time(),
            "values": float_values  # Lista di 10 valori floating point
        }
        print(json.dumps(data, indent=4))  # Stampa i dati formattati in JSON
    else:
        print("Failed to read registers")

        float_values = registers_to_float(rr.registers)
    print(f"CryCon 18i {float_values}")

    time.sleep(30)
