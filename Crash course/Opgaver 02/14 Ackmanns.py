# AckermannFunction funktionen kalder sig selv rekursivt, afhængig af værdierne for m og n
def AckermannFunction(m, n):
    # Udskriver hvert kald af funktionen for at visualisere rekursionen
    print(f"AckermannFunction({m}, {n}) called")
    
    # Base case: Hvis m er 0, returner n + 1
    if m == 0:
        return n + 1
    
    # Hvis m > 0 og n er 0, så kald AckermannFunction med m-1 og 1
    if m > 0 and n == 0:
        return AckermannFunction(m - 1, 1)
    
    # Hvis både m og n er større end 0, kald AckermannFunction rekursivt
    if m > 0 and n > 0:
        return AckermannFunction(m - 1, AckermannFunction(m, n - 1))

# Test af funktionen med værdierne m = 3, n = 4
test = AckermannFunction(3, 4)
print(f"Resultat: {test}")

# Jeg testede med værdierne m = 4, n = 1, men det overskred rekursionsgrænsen
# sys-biblioteket kan bruges til at hæve rekursionsgrænsen, hvis det er nødvendigt
# Her kan vi øge rekursionsgrænsen:
# import sys
# sys.setrecursionlimit(3000)