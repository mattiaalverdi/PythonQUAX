from QUAX_thresholds import PumpsThresholds, CCiThresholds, PMGThresholds, PSGThresholds, HDIThresholds
from thresholds_class import Thresholds, check_values_against_thresholds
from Functions import ReadPLC
try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient
    
from telegram import Bot, Update
from telegram.ext import ContextTypes
import asyncio
from QUAX_bot import sendStringToGroup

# Funzione per gestire l'aggiornamento della pressione
async def PressureUpdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot from MAIN! How can I help you?")  



#----------------------------------------------------------------------------------------------------------------
# MAIN QUAX
if __name__ == "__main__":
    host = '192.168.100.10'
    port = 503

    # Crea il client Modbus
    QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge, QUAXPfeiffereSingleGauge, QUAXPHeliumDI = ReadPLC(host, port)

    # values = [15]
    
    # # Verifica i valori rispetto alle soglie delle pompe
    # result_pumps = check_values_against_thresholds(QUAXPumps.values, PumpsThresholds, 'warning')
    # print(f"Result Pumps: {result_pumps}")
    # asyncio.run(sendStringToGroup(f"Result pompe: {result_pumps}"))
    
    # # Verifica i valori rispetto alle soglie dei CCi
    # result_cci = check_values_against_thresholds(QUAXCryoCon18i.values, CCiThresholds, 'warning')
    # print(f"Result CCi: {result_cci}")
    # asyncio.run(sendStringToGroup(f"Result CCi: {result_cci}"))
    
    # # Verifica i valori rispetto alle soglie delle 
    # result_pmg = check_values_against_thresholds(QUAXPfeiffereMaxiGauge.values, PMGThresholds, 'warning')
    # print(f"Result PMG: {result_pmg}")
    # asyncio.run(sendStringToGroup(f"Result PMG: {result_pmg}"))
    
    # # Verifica i valori rispetto alle soglie delle PSG
    # result_psg = check_values_against_thresholds(QUAXPfeiffereSingleGauge.values, PSGThresholds, 'warning')
    # print(f"Result PSG: {result_psg}")    # asyncio.run(sendStringToGroup(f"Result PSG: {result_psg}"))
    
    # # Verifica i valori rispetto alle soglie dell'HDI
    # result_hdi = check_values_against_thresholds(QUAXPHeliumDI.values, HDIThresholds, 'warning')
    # print(f"Result HDI: {result_hdi}")
    # asyncio.run(sendStringToGroup(f"Result HDI: {result_hdi}"))

