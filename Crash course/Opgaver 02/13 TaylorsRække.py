from math import sin, cos, pi

# Vi laver en simpel version af Factorial.
def factorial(n):
    # hvis n er 0 eller 1 vil den altid være 1, og vi returnerer derfor 1.
    if n == 0 or n == 1:
        return 1
    # Hvis ikke det er opfyldt, initialiserer vi resultatet som 1 og laver et for-loop til factorial-udregningen.
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Vi laver en funktion til at beregne sinus ved hjælp af Taylorrækken og vores egen factorial-funktion.
# x er vores vinkel og er defineret i radianer mens n er antallet af led i vores taylorrække.
def TaylorSin(x, n):
    # først sættes værdien af sinus til 0
    sin_værdi = 0
    # nu loopes der for at udregne Taylorrækkens led.
    for i in range(n): 
        # Beregner hvert led i Taylorrækken og tilføjer det til den totale sum.
        sinusled = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_værdi += sinusled
    return sin_værdi

# Vi laver en funktion til at beregne cosinus ved hjælp af Taylorrækken og vores egen factorial-funktion.
def TaylorCos(x, n):
    # først sættes værdien af sinus til 0
    cos_værdi = 0
    # der loopes for at beregne taylorrækkens led.
    for i in range(n):
        # Beregner hvert led i Taylorrækken og tilføjer det til den totale sum.
        cosinusled = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_værdi += cosinusled
    return cos_værdi

# Funktion til at beregne den absolutte fejl
def BeregnAbsolutteFejl(næsten, præcis):
    return abs(næsten - præcis)

# Funktion til at finde det nødvendige antal led (n) for en given præcision (standard er 0.001).
def PræcisionAfFunktioner(x, Næstenfunktion, PræcisFunktion, præcision=0.001):
    n = 1
    # vi bruger loopet til at finde den mindste n værdi hvor Taylorrækken giver fejl mindre end præcisionen.
    while True:
        # beregner taylorrækkens værdi og den præcise værdi
        NæstenVærdi = Næstenfunktion(x, n)
        PræcisVærdi = PræcisFunktion(x)
        # beregner vores absolutte fejl
        fejl = BeregnAbsolutteFejl(NæstenVærdi, PræcisVærdi)
        # er fejlen mindre end vores præcision  returnerer vi n
        if fejl < præcision:
            return n
        # vi øger n hvis vi ikke opnåede den ønskede præcision
        n += 1

# Optimeringsfunktion for store værdier af x ved hjælp af modulo 2π (sinus og cosinus er periodiske)
def OptimeretX(x):
    return x % (2 * pi)

# Nu tester vi for forskellige x-værdier og sammenligner Taylorrækker med math.sin og math.cos
XVærdier = [0, pi / 4, pi / 2, pi, 2 * pi, 3 * pi, 4 * pi]
n = 5  # Antal led i Taylorrækken til første test

# For hver vinkel i listen beregner vi sinus og cosinus og sammenligner dem med de præcise værdier.
for x in XVærdier:
    # Beregner sinus og cosinus med Taylorrækken
    næstenSinus = TaylorSin(x, n)
    præcisSinus = sin(x)
    FejlSin = BeregnAbsolutteFejl(næstenSinus, præcisSinus)
    
    næstenCosinus = TaylorCos(x, n)
    præcisCosinus = cos(x)
    FejlCos = BeregnAbsolutteFejl(næstenCosinus, præcisCosinus)
    
    # Print resultaterne for hver enkelt vinkel
    print(f"x = {x}")
    print(f"Taylor sin(x) = {næstenSinus}, math.sin(x) = {præcisSinus}, fejl = {FejlSin}")
    print(f"Taylor cos(x) = {næstenCosinus}, math.cos(x) = {præcisCosinus}, fejl = {FejlCos}")
    print("-" * 40)

# Nu undersøger vi, hvor mange led (n) der kræves for at få fejlen ned på 3 decimaler for forskellige værdier af x
for x in [pi, 2 * pi, 3 * pi, 4 * pi]:
    # beregner led vi har brug for til sinus
    n_sin = PræcisionAfFunktioner(x, TaylorSin, sin)
    # beregner led vi har brug for til cosinus
    n_cos = PræcisionAfFunktioner(x, TaylorCos, cos)
    # vi printer resultaterne på en pæn måde   
    print(f"x = {x}")
    print(f"Antal led nødvendige for sin(x) med præcision på 3 decimaler: {n_sin}")
    print(f"Antal led nødvendige for cos(x) med præcision på 3 decimaler: {n_cos}")
    print("-" * 40)

# Til sidst undersøger vi store værdier af x som 20π
x = 20 * pi
# vi optimerer med Modulus 2 pi.
optimeret_x = OptimeretX(x)

# Beregner sinus med optimerede x
næstenSinus = TaylorSin(optimeret_x, n)
præcisSinus = sin(optimeret_x)
fejlSinus = BeregnAbsolutteFejl(næstenSinus, præcisSinus)
# beregner cosinus med optimerede x
næstenCosinus = TaylorCos(optimeret_x, n)
præcisCosinus = cos(optimeret_x)
fejlCosinus = BeregnAbsolutteFejl(næstenCosinus, præcisCosinus)
# printer Taylor resultaterne for 20 pi.
print(f"Taylor sin(20π) = {næstenSinus}, math.sin(20π) = {præcisSinus}, fejl = {fejlSinus}")
print(f"Taylor cos(20π) = {næstenCosinus}, math.cos(20π) = {præcisCosinus}, fejl = {fejlCosinus}")