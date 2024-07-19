import math

def round_to_significant_figures(num, sig_figs):
    """
    Approssima un numero a un numero specifico di cifre significative e lo formatta in notazione esponenziale.
    
    Args:
    - num (float): Il numero da approssimare.
    - sig_figs (int): Il numero di cifre significative.

    Returns:
    - str: Il numero approssimato in notazione esponenziale.
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

# Esempio di utilizzo
num = 12345.6789
approx_num = round_to_significant_figures(num, 4)
print(f"{num} approssimato a 4 cifre significative è {approx_num}")

num = 0.00123456789
approx_num = round_to_significant_figures(num, 4)
print(f"{num} approssimato a 4 cifre significative è {approx_num}")

# Altri esempi di utilizzo
nums = [12345.6789, 0.00123456789, 987654321, 0.00009876]

for num in nums:
    approx_num = round_to_significant_figures(num, 4)
    print(f"{num} approssimato a 4 cifre significative è {approx_num}")
