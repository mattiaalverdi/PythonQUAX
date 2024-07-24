#----------------------------------------------------------------------------------------------------------------
# CLASS DEFINITION
class Thresholds:
    def __init__(self):
        """
        Inizializza l'oggetto Thresholds con array vuoti per le soglie di allarme e avviso.
        """
        self.alarm_thresholds = []
        self.warning_thresholds = []

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
        
    def get_alarm_thresholds(self):
        """
        Restituisce le soglie di allarme.

        :return: Lista di soglie di allarme.
        """
        return self.alarm_thresholds
    
    def get_warning_thresholds(self):
        """
        Restituisce le soglie di avviso.

        :return: Lista di soglie di avviso.
        """
        return self.warning_thresholds

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

#----------------------------------------------------------------------------------------------------------------
# TEST of the CLASS functionality
if __name__ == "__main__":
    # Crea un'istanza della classe Thresholds
    thresholds = Thresholds()

    # Imposta le soglie
    thresholds.set_alarm_thresholds([10.0, 20.0, 30.0])
    thresholds.set_warning_thresholds([5.0, 15.0])

    # Stampa le soglie
    thresholds.print_thresholds()

    # Leggi la soglia di avviso alla posizione 2
    warning_value_at_pos_2 = thresholds.get_warning_at(1)
    warning_value_at_pos_2 = thresholds.warning_thresholds[0]
    if warning_value_at_pos_2 is not None:
        print(f"Warning value at position 2: {warning_value_at_pos_2:.2f}")
    else:
        print("La posizione specificata è fuori intervallo.")

# END OF FILE
#----------------------------------------------------------------------------------------------------------------