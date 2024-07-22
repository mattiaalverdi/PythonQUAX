from QUAX_thresholds import PumpsThresholds, CCiThresholds, PMGThresholds, PSGThresholds, HDIThresholds
from thresholds_class import Thresholds, check_values_against_thresholds
from Functions import ReadPLC
try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient
#----------------------------------------------------------------------------------------------------------------
# MAIN QUAX
if __name__ == "__main__":
    host = '192.168.100.10'
    port = 503

    # Crea il client Modbus
    # QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge, QUAXPfeiffereMaxiGauge, QUAXPHeliumDI = ReadPLC(host, port)

    values = [15]
    
    # Verifica i valori rispetto alle soglie delle pompe
    # result_pumps = check_values_against_thresholds(values, PumpsThresholds)
    # print(f"Result Pumps: {result_pumps}")
    
    # Verifica i valori rispetto alle soglie dei CCi
    # result_cci = check_values_against_thresholds(values, CCiThresholds)
    # print(f"Result CCi: {result_cci}")
    
    # # Verifica i valori rispetto alle soglie delle PMG
    # result_pmg = check_values_against_thresholds(values, PMGThresholds)
    # print(f"Result PMG: {result_pmg}")
    
    # # Verifica i valori rispetto alle soglie delle PSG
    # result_psg = check_values_against_thresholds(values, PSGThresholds)
    # print(f"Result PSG: {result_psg}")
    
    # Verifica i valori rispetto alle soglie dell'HDI
    result_hdi = check_values_against_thresholds(values, HDIThresholds)
    print(f"Result HDI: {result_hdi}")


