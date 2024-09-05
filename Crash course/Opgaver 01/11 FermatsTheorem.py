# Problemet her opstår på grund af flydende kommatal (floating-point) præcision.
# Når vi beregner store tal som a^n, b^n, og c^n med decimaltal (ikke heltal),
# introducerer computeren små afrundingsfejl på grund af den måde, flydende kommatal repræsenteres.
# Disse små fejl betyder, at a^n + b^n kan være meget tæt på, men ikke præcist lig med c^n,
# selvom Fermats sidste sætning burde forhindre ligheden for n > 2.
# Da programmet tjekker, om forskellen er meget lille (mindre end 1e-9), 
# kan det fejlagtigt tro, at Fermat tog fejl, når der i virkeligheden bare er tale om 
# flydende kommatalpræcision.

import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
n = float(input("Enter value for n: "))


PowerA = a**n
PowerB = b**n
PowerC = c**n


def FermatTheorem():
    if n == 2:
        if abs(PowerA + PowerB - PowerC) < 1e-9:
            print("Yes, That does indeed work.")
        else:
            print("No, No, No, No you silly fool, that doesn't work at all!")
    elif n > 2:
        if abs(PowerA + PowerB - PowerC) < 1e-9:
            print("Fermat's theorem holds no water and is totally wrong!")
        else:
            print("No, Fermat was right, it does not work for n > 2.")


FermatTheorem()