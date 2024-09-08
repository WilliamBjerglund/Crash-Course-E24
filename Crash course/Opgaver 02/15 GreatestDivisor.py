
# User input for a og b
a = int(input("Indtast en værdi for a: "))
b = int(input("Indtast en værdi for b: "))
# dette check sikrer at vores a værdi altid er større end vores b værdi og derved kan vi bruge vores algorytme.
# hvis B er større end A sætter den b værdien til A og omvendt A værdien til B.
if b > a:
    a, b = b, a

# Vi bruger en vel kendt algorytme, nemlig Euclids Algorytme til at beregne GCD da den er meget effektiv.
def EuclidAlgorithm(a, b): # den tager vores værdier som paremetre
    if b == 0: # hvis b er 0 er vores GCD b og derfor return a.
        return a
    else: # hvis ikke b er 0 gentager Algorytmen sig selv efter at have taget modulus a og b og sat b som a samt resten af a % b som b.
        return EuclidAlgorithm(b, a % b) # dette gentager funktionen til resten af a % b er 0 og GCD derved er fundet.

print(f"Den Største fælles divisor for tallene {a} og {b} er {EuclidAlgorithm(a, b)}")

# Alternativt kunne jeg have lavet en løsning uden algorytmer, med et simpelt while loop der iterere ned fra b værdien til den rammer a % b = 0.
# men dette og evt. andre metoder jeg ville komme på er nok ikke nær så effektiv og ville tage mindst ligeså lang tid som bare at bruge den algorytme alle kender.
# koden er selvfølgelig min egen men algorytmen er Euclids.