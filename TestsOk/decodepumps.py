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
            # Legge 4 registri consecutivi
            rr = client.read_holding_registers(0, 4, unit=1)
            if rr.isError():
                raise ConnectionException(f"Error reading registers: {rr}")

            # Funzione per controllare i bit 8, 9, 10, 11
            def check_bits(value):
                bit_8 = bool(value & 0x0100)
                bit_9 = bool(value & 0x0200)
                bit_10 = bool(value & 0x0400)
                bit_11 = bool(value & 0x0800)
                return bit_8, bit_9, bit_10, bit_11

            # Itera sui 4 registri e controlla i bit specifici
            for i in range(4):
                register_value = rr.registers[i]
                bit_8, bit_9, bit_10, bit_11 = check_bits(register_value)
                print(f"Register {i}:")
                print(f"  Bit 8: {'High' if bit_8 else 'Low'}")
                print(f"  Bit 9: {'High' if bit_9 else 'Low'}")
                print(f"  Bit 10: {'High' if bit_10 else 'Low'}")
                print(f"  Bit 11: {'High' if bit_11 else 'Low'}")

        except ConnectionException as e:
            print(f"ConnectionException: {e}")

        # Attendi 5 secondi prima di eseguire un'altra lettura
        time.sleep(5)

finally:
    # Chiude la connessione
    client.close()
