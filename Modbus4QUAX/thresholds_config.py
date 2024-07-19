class Thresholds:
    def __init__(self, alarm_thresholds=None, warning_thresholds=None):
        """
        Inizializza l'oggetto Thresholds con le soglie per allarmi e avvisi.

        :param alarm_thresholds: Lista di soglie float per gli allarmi.
        :param warning_thresholds: Lista di soglie float per gli avvisi.
        """#zao
        # Se non vengono forniti valori, inizializza gli array a liste vuote
        self.alarm_thresholds = alarm_thresholds if alarm_thresholds is not None else []
        self.warning_thresholds = warning_thresholds if warning_thresholds is not None else []
    
    def set_alarm_thresholds(self, thresholds):
        """
        Imposta le soglie per gli allarmi.

        :param thresholds: Lista di soglie float per gli allarmi.
        """
        if all(isinstance(t, float) for t in thresholds):
            self.alarm_thresholds = thresholds
        else:
            raise ValueError("Tutti i valori devono essere float")

    def set_warning_thresholds(self, thresholds):
        """
        Imposta le soglie per gli avvisi.

        :param thresholds: Lista di soglie float per gli avvisi.
        """
        if all(isinstance(t, float) for t in thresholds):
            self.warning_thresholds = thresholds
        else:
            raise ValueError("Tutti i valori devono essere float")
        
    def get_alarm_at(self, position):
        """
        Restituisce la soglia di allarme alla posizione specificata.

        :param position: Posizione nella lista di soglie di allarme.
        :return: Valore float della soglia di allarme o None se la posizione è fuori intervallo.
        """
        if 0 <= position < len(self.alarm_thresholds):
            return self.alarm_thresholds[position]
        else:
            print("Fuori intervallo")
            return None  # O lancia un'eccezione se la posizione è fuori intervallo

    def get_warning_at(self, position):
        """
        Restituisce la soglia di avviso alla posizione specificata.

        :param position: Posizione nella lista di soglie di avviso.
        :return: Valore float della soglia di avviso o None se la posizione è fuori intervallo.
        """
        if 0 <= position < len(self.warning_thresholds):
            return self.warning_thresholds[position]
        else:
            print("Fuori intervallo")
            return None  # O lancia un'eccezione se la posizione è fuori intervallo

    def print_thresholds(self):
        """
        Stampa le soglie per gli allarmi e gli avvisi.
        """
        print("Alarm Thresholds:")
        for i, threshold in enumerate(self.alarm_thresholds):
            print(f"  Alarm {i+1}: {threshold:.2f}")

        print("Warning Thresholds:")
        for i, threshold in enumerate(self.warning_thresholds):
            print(f"  Warning {i+1}: {threshold:.2f}")

#----------------------------------------------------------------------------------------------------------------
# # Esempio di utilizzo della classe
if __name__ == "__main__":
    # Crea un'istanza della classe con soglie iniziali
    thresholds = Thresholds(
        alarm_thresholds=[1.23, 2.34, 3.45],
        warning_thresholds=[4.56, 5.67]
    )
    
    thresholds.print_thresholds()

    # Modifica le soglie
    thresholds.set_alarm_thresholds([1.50, 2.60, 3.70])
    thresholds.set_warning_thresholds([4.80, 5.90, 6.00])

    # Stampa le soglie
    thresholds.print_thresholds()

    # Leggi la soglia di avviso alla posizione 2
    warning_value_at_pos_2 = thresholds.get_warning_at(2)
    
    if warning_value_at_pos_2 is not None:
        print(f"Warning value at position 2: {warning_value_at_pos_2:.2f}")
    else:
        print("La posizione specificata è fuori intervallo.")

#----------------------------------------------------------------------------------------------------------------
# CONFIGURAZIONE DELLE SOGLIE DI ALLARME E AVVISO QUAX
        """
        Ricordarsi che i valori impostati non vengono impostati nel PLC,
        pertanto possono essere diversi dalle effettive soglie di intervento

        la struttura dei dati delle soglie deve essere concorde all'ordine
        di rappresentazione dei dati nelle strutture di memoria e decodifica
        sono riportate di seguito:  (versione 1.0)
        PumpsHeader = ["IVC1", "IVC2", "1KP1", "1KP2", "EMOD1"]
        CCiHeader = ["ChA", "ChB", "ChC", "ChD", "ChE", "ChF", "ChG", "ChH"]
        PMGHeader = ["Gauge1", "Gauge2", "Gauge3", "Gauge4", "Gauge5", "Gauge6"]
        PSGHeader = ["Gauge1", "Gauge2"]
        """
 
# PMG_thresholds = Thresholds(
#         alarm_thresholds=[1.23, 2.34, 3.45],
#         warning_thresholds=[4.56, 5.67]
# )


def check_values_against_thresholds(values, thresholds, threshold_type='alarm'):
    """
    Verifica i valori di un array rispetto alle soglie di allarme o avviso e restituisce un codice basato sulle condizioni.

    :param values: Array di valori float da verificare.
    :param thresholds: Oggetto Thresholds contenente le soglie di allarme o avviso.
    :param threshold_type: Tipo di soglia da utilizzare ('alarm' o 'warning').
    :return: Lista di codici basati sulle condizioni:
             - 0 se il valore è diverso dalla soglia.
             - 1 se il valore è inferiore alla soglia.
             - 2 se il valore è superiore alla soglia.
             - 66 se c'è un errore di confronto o la lunghezza dell'array non corrisponde.
    """
    try:
        if threshold_type == 'alarm':
            thresholds_list = thresholds.get_alarm_thresholds()
        elif threshold_type == 'warning':
            thresholds_list = thresholds.get_warning_thresholds()
        else:
            raise ValueError("Tipo di soglia non valido. Utilizzare 'alarm' o 'warning'.")

        if len(values) != len(thresholds_list):
            return 66  # Errore: lunghezza dell'array non corrisponde

        results = []
        for value, threshold in zip(values, thresholds_list):
            if value < threshold:
                results.append(1)
            elif value > threshold:
                results.append(2)
            else:
                results.append(0)  # Il valore è uguale alla soglia

        return results

    except Exception as e:
        print(f"Errore: {e}")
        return 66

# Esempio di utilizzo della funzione
if __name__ == "__main__":
    # Crea un'istanza della classe Thresholds con soglie di esempio
    thresholds = Thresholds(
        alarm_thresholds=[10.0, 20.0, 30.0],
        warning_thresholds=[5.0, 15.0]
    )

    # Array di valori da verificare
    values = [9.0, 21.0, 29.0]

    # Verifica i valori rispetto alle soglie di allarme
    result_alarm = check_values_against_thresholds(values, thresholds, 'alarm')
    print(f"Result (Alarm): {result_alarm}")

    # Verifica i valori rispetto alle soglie di avviso
    result_warning = check_values_against_thresholds(values, thresholds, 'warning')
    print(f"Result (Warning): {result_warning}")

