from thresholds_class import Thresholds


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

PumpsThresholds = Thresholds()
PumpsThresholds.set_alarm_thresholds([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,   #"IVC1", "IVC2"
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, #"1KP1", "1KP2"
                                        0.0, 0.0, 0.0, 0.0, ])                  #"EMOD1"
PumpsThresholds.set_warning_thresholds([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, #"IVC1", "IVC2"
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, #"1KP1", "1KP2"
                                        0.0, 0.0, 0.0, 0.0, ])                  #"EMOD1"

CCiThresholds = Thresholds()
CCiThresholds.set_alarm_thresholds([50.0, 50.0, 50.0,   # "ChA", "ChB", "ChC"
                                    50.0, 50.0, 50.0,   #"ChD", "ChE", "ChF"
                                    50.0, 50.0])        #"ChG", "ChH"
CCiThresholds.set_warning_thresholds([100.0, 100.0, 100.0,   # "ChA", "ChB", "ChC"
                                    100.0, 100.0, 100.0,   #"ChD", "ChE", "ChF"
                                    100.0, 100.0])        #"ChG", "ChH"

PMGThresholds = Thresholds()
PMGThresholds.set_alarm_thresholds([50.0, 50.0, 50.0,   #"Gauge1", "Gauge2", "Gauge3"
                                    50.0, 50.0, 50.0])  #"Gauge4", "Gauge5", "Gauge6"
PMGThresholds.set_warning_thresholds([100.0, 100.0, 100.0,   #"Gauge1", "Gauge2", "Gauge3"
                                    100.0, 100.0, 100.0])  #"Gauge4", "Gauge5", "Gauge6"

PSGThresholds = Thresholds()
PSGThresholds.set_alarm_thresholds([50.0, 50.0])   #"Gauge1", "Gauge2"
PSGThresholds.set_warning_thresholds([100.0, 100.0])   #"Gauge1", "Gauge2"

HDIThresholds = Thresholds()
HDIThresholds.set_alarm_thresholds([1300.0])   #"HDI"
HDIThresholds.set_warning_thresholds([1500.0])   #"HDI"