try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient

from datetime import datetime
import json
import time

def current_time():
    now = datetime.now().isoformat()
    return now

host = '192.168.100.10'
port = 503
client = ModbusTcpClient(host, port)

while True:
    if not client.is_socket_open():
        client.connect()

    # Legge 10 registri di holding a partire dall'indirizzo 0
    rr = client.read_holding_registers(0, 50, unit=1)
    
    if rr is not None and rr.registers:
        data = {
            "time": current_time(),
            "values": rr.registers  # Lista di 10 registri letti
        }
        print(json.dumps(data, indent=4))  # Stampa i dati formattati in JSON
    else:
        print("Failed to read registers")

    time.sleep(10)
