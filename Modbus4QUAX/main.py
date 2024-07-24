from QUAX_thresholds import ThresholdsResults, PumpsThresholds, CCiThresholds, PMGThresholds, PSGThresholds, HDIThresholds, AlarmParser, WarningParser
from thresholds_class import Thresholds, check_values_against_thresholds
from Functions import ReadPLC, PumpDecode
try:
    from pymodbus.client.sync import ModbusTcpClient
except ModuleNotFoundError:
    from pymodbus.client import ModbusTcpClient
    
from telegram import Update
from telegram.ext import ContextTypes
from QUAX_bot import send_message_sync

import time
import math

from datetime import datetime

# Funzione per gestire l'aggiornamento della pressione
async def PressureUpdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I'm QUAX_bot from MAIN! How can I help you?")  

def current_time():
    # Ottieni l'ora corrente
    now = datetime.now()
    # Formatta l'ora corrente come dd/mm/yyyy:hh:mm
    formatted_time = now.strftime("%d/%m/%Y:%H_%M")
    return formatted_time

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
    else:
        # Calcola il numero di cifre decimali a cui arrotondare
        rounded_num = round(num, sig_figs - int(math.floor(math.log10(abs(num)))) - 1)
        # Format in notazione esponenziale
        exp_format = f"{rounded_num:.{sig_figs-1}e}"
        # Trasforma la notazione per essere nel formato x.yzw e^kk
        base, exponent = exp_format.split('e')
        return f"{base} e^{int(exponent)}"
    # else:
    #     # Calcola il numero di cifre decimali a cui arrotondare
    #     rounded_num = round(num, sig_figs - int(math.floor(math.log10(abs(num)))) - 1)
    #     return rounded_num

#----------------------------------------------------------------------------------------------------------------
# MAIN QUAX
if __name__ == "__main__":
    host = '192.168.100.10'
    port = 503

    # Crea il client Modbus
    QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge, QUAXPfeiffereSingleGauge, QUAXPHeliumDI = ReadPLC(host, port)
    QUAX_devices = [QUAXPumps, QUAXCryoCon18i, QUAXPfeiffereMaxiGauge, QUAXPfeiffereSingleGauge, QUAXPHeliumDI]
    QUAX_limits = [PumpsThresholds, CCiThresholds, PMGThresholds, PSGThresholds, HDIThresholds]

    #------------------------------------------------------------------------------------------------------------
    # Gestione Update periodici

    # UpdateMsg = "🟢 Periodical QUAX's Log\n of: " + current_time() + "\n\n"

    # for device in QUAX_devices:
    #     UpdateMsg += f"{device.name}:\n"
    #     if device.name == QUAXPumps.name:
    #         UpdateMsg += PumpDecode(device)
    #     else:
    #         for ch_or_gauge in range(len(device.header)):
    #             if device.name == QUAXCryoCon18i.name:
    #                 UpdateMsg += f"{device.header[ch_or_gauge]}: {device.values[ch_or_gauge]} {device.unit}\n"
    #             else:                    
    #                 UpdateMsg += f"{device.header[ch_or_gauge]}: {round_to_significant_figures(device.values[ch_or_gauge],4)} {device.unit}\n"

    #     UpdateMsg += "\n"     

    # send_message_sync(f"Result test🈳🉑♻: {UpdateMsg}")



    # # Verifica i valori rispetto alle soglie delle pompe
    # pumpsWarningResult = check_values_against_thresholds(QUAXPumps.values, PumpsThresholds, 'warning')
    # print(f"Result Pumps: {pumpsWarningResult}")
    # send_message_sync(f"Result pompe: {pumpsWarningResult}")
    
    # # Verifica i valori rispetto alle soglie dei CCi
    # result_cci = check_values_against_thresholds(QUAXCryoCon18i.values, CCiThresholds, 'warning')
    # print(f"Result CCi: {result_cci}")
    # send_message_sync(f"Result CCi: {result_cci}")
    
    # # Verifica i valori rispetto alle soglie delle 
    # result_pmg = check_values_against_thresholds(QUAXPfeiffereMaxiGauge.values, PMGThresholds, 'warning')
    # print(f"Result PMG: {result_pmg}")
    # send_message_sync(f"Result PMG: {result_pmg}")
    
    # # Verifica i valori rispetto alle soglie delle PSG
    # result_psg = check_values_against_thresholds(QUAXPfeiffereSingleGauge.values, PSGThresholds, 'warning')
    # print(f"Result PSG: {result_psg}")    # send_message_sync(f"Result PSG: {result_psg}")
    
    # # Verifica i valori rispetto alle soglie dell'HDI
    # result_hdi = check_values_against_thresholds(QUAXPHeliumDI.values, HDIThresholds, 'warning')
    # print(f"Result HDI: {result_hdi}")
    # send_message_sync(f"Result HDI: {result_hdi}")

    #------------------------------------------------------------------------------------------------------------
    # Gestione Warning

    WarningMsg = "🔔⚠ WARNING QUAX ⚠🔔\n Issue at: " + current_time() + "\n\n"
    WarningResult = ThresholdsResults()
    WarningResult.Pumps = check_values_against_thresholds(QUAXPumps.values, PumpsThresholds, 'warning')
    WarningResult.CCi = check_values_against_thresholds(QUAXCryoCon18i.values, CCiThresholds, 'warning')
    WarningResult.PMG = check_values_against_thresholds(QUAXPfeiffereMaxiGauge.values, PMGThresholds, 'warning')
    WarningResult.PSG = check_values_against_thresholds(QUAXPfeiffereSingleGauge.values, PSGThresholds, 'warning')
    WarningResult.HDI = check_values_against_thresholds(QUAXPHeliumDI.values, HDIThresholds, 'warning')
                                               
    for idx in range(len(WarningResult.Pumps)):
        if WarningResult.Pumps[idx] == WarningParser.Pumps[idx]:
            WarningMsg += "boja can un warning\n"

    send_message_sync(f"🎌TEST WARNING🎌: {WarningMsg}")
    #------------------------------------------------------------------------------------------------------------
    # Gestione Alarm
    
    AlarmMsg = "‼⚠ WARNING QUAX ⚠‼\n Issue at: " + current_time() + "\n\n"