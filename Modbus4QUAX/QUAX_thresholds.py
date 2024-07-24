from thresholds_class import Thresholds

class ThresholdsResults:
    def __init__(self):
        self.Pumps = []
        self.CCi = []
        self.PMG = []
        self.PSG = []
        self.HDI = []

#----------------------------------------------------------------------------------------------------------------
# QUAX datasets
"""
    PumpsHeader = ["IVC1", "IVC2", "1KP1", "1KP2", "EMOD1"]
    CCiHeader = ["ChA", "ChB", "ChC", "ChD", "ChE", "ChF", "ChG", "ChH"]
    PMGHeader = ["Gauge1", "Gauge2", "Gauge3", "Gauge4", "Gauge5", "Gauge6"]
    PSGHeader = ["Gauge1", "Gauge2"]
"""
#----------------------------------------------------------------------------------------------------------------
# QUAX configurations 
""" 
    N.B. I valori delle soglie sono da definire nelle variabili
    'DEVICE_NAMEThresholds = Thresholds()'

    
    Nelle variabili 
    'Alarm_or_WarningParser'
    si devono inserire i confronti di cui tenere conto per l'invio di allarmi o avvisi
            - 0 se il valore è diverso dalla soglia.
            - 1 se il valore è inferiore alla soglia.
            - 2 se il valore è superiore alla soglia.
    nello specifico i valori sono corrispondenti ai confronti fatti dalla funzione

    'check_values_against_thresholds(values, thresholds, alarm_or_warning)'
"""
AlarmParser = ThresholdsResults()
WarningParser = ThresholdsResults()

# VACUUM PUMPS
PumpsThresholds = Thresholds()

PumpsThresholds.set_alarm_thresholds([0.0, 0.0, 0.0, 0.0,           #"IVC1"
                                        0.0, 0.0, 0.0, 0.0,         #"IVC2"
                                        0.0, 0.0, 0.0, 0.0,         #"1KP1"
                                        0.0, 0.0, 0.0, 0.0,         #"1KP2"  
                                        0.0, 0.0, 0.0, 0.0, ])      #"EMOD1"

AlarmParser.Pumps = ([0, 0, 0, 0,                                   #"IVC1"
                        0, 0, 0, 0,                                 #"IVC2"
                        0, 0, 0, 0,                                 #"1KP1"     
                        0, 0, 0, 0,                                 #"1KP2"
                        0, 0, 0, 0 ])                               #"EMOD1"

PumpsThresholds.set_warning_thresholds([0.0, 0.0, 0.0, 0.0,         #"IVC1"
                                        0.0, 0.0, 0.0, 0.0,         #"IVC2"
                                        0.0, 0.0, 0.0, 0.0,         #"1KP1"
                                        0.0, 0.0, 0.0, 0.0,         #"1KP2"  
                                        0.0, 0.0, 0.0, 0.0, ])      #"EMOD1"

WarningParser.Pumps = ([0, 0, 0, 0,                                 #"IVC1"
                        0, 0, 0, 0,                                 #"IVC2"
                        0, 0, 0, 0,                                 #"1KP1"     
                        0, 0, 0, 0,                                 #"1KP2"
                        0, 0, 0, 0 ])                               #"EMOD1"

# CRYOCON 18i
CCiThresholds = Thresholds()
CCiThresholds.set_alarm_thresholds([50.0, 50.0, 50.0,               #"ChA", "ChB", "ChC"
                                    50.0, 50.0, 50.0,               #"ChD", "ChE", "ChF"
                                    50.0, 50.0])                    #"ChG", "ChH"

AlarmParser.CCi = [0, 0, 0,                                         #"ChA", "ChB", "ChC"
                    0, 0, 0,                                        #"ChD", "ChE", "ChF"
                    0, 0]                                           #"ChG", "ChH"

CCiThresholds.set_warning_thresholds([100.0, 100.0, 100.0,          #"ChA", "ChB", "ChC"
                                    100.0, 100.0, 100.0,            #"ChD", "ChE", "ChF"
                                    100.0, 100.0])                  #"ChG", "ChH"

WarningParser.CCi = [0, 0, 0,                                       #"ChA", "ChB", "ChC"
                    0, 0, 0,                                        #"ChD", "ChE", "ChF"
                    0, 0]                                           #"ChG", "ChH"

# PFEIFFERE MAXIGAUGE
PMGThresholds = Thresholds()
PMGThresholds.set_alarm_thresholds([50.0, 50.0, 50.0,               #"Gauge1", "Gauge2", "Gauge3"
                                    50.0, 50.0, 50.0])              #"Gauge4", "Gauge5", "Gauge6"

AlarmParser.PMG = [0, 0, 0,                                         #"Gauge1", "Gauge2", "Gauge3"
                0, 0, 0]                                            #"Gauge4", "Gauge5", "Gauge6"

PMGThresholds.set_warning_thresholds([100.0, 100.0, 100.0,          #"Gauge1", "Gauge2", "Gauge3"
                                    100.0, 100.0, 100.0])           #"Gauge4", "Gauge5", "Gauge6"

WarningParser.PMG = [0, 0, 0,                                       #"Gauge1", "Gauge2", "Gauge3"
                    0, 0, 0]                                        #"Gauge4", "Gauge5", "Gauge6"

# PFEIFFERE SINGLE GAUGE
PSGThresholds = Thresholds()
PSGThresholds.set_alarm_thresholds([50.0, 50.0])                    #"Gauge1", "Gauge2"

AlarmParser.PSG = [0, 0]                                            #"Gauge1", "Gauge2"

PSGThresholds.set_warning_thresholds([100.0, 100.0])                #"Gauge1", "Gauge2"

WarningParser.PSG = [0, 0]                                          #"Gauge1", "Gauge2"

# HELIUM DEPTH INDICATOR
HDIThresholds = Thresholds()
HDIThresholds.set_alarm_thresholds([1300.0])                        #"HDI"

AlarmParser.HDI = [0]                                               #"HDI"

HDIThresholds.set_warning_thresholds([1500.0])                      #"HDI"

WarningParser.HDI = [0]                                             #"HDI"