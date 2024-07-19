try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
import struct

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

# Configurazione del client Modbus
host = '192.168.100.10'
port = 503
unit = 1

# Crea il client Modbus
client = ModbusTcpClient(host, port)

try:
    # Tenta di connettersi al dispositivo
    connection = client.connect()
    if not connection:
        raise ConnectionException(f"Failed to connect to {host}:{port}")

    # Leggi e decodifica 20 valori float, due registri ogni 15 registri
    start_address = 5
    count = 8
    float_values = read_and_decode_floats(client, start_address, count, unit, 15)

    # Stampa i valori float
    for idx, value in enumerate(float_values):
        print(f"Value {idx + 1}: {value}")

except ConnectionException as e:
    print(f"ConnectionException: {e}")

finally:
    # Chiude la connessione
    client.close()
