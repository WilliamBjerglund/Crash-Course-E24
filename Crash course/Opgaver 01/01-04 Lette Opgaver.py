# dette dokument indenholder øvelserne der er udenfor vores jupyter books altså dem fra moodle.
# Libraries to declare.
import math

# Øvelse 1 (let)
def CalculateSphereVolume():
    radius = [1, 3, 10]
    for i in radius:
        V = (4/3) * math.pi * i**3  
        print(f"Volume of sphere with radius {i} is: {V}")


# Øvelse 2 (let)
def PrintBla():
    print(" ".join(["bla"] * 10))


# Øvelse 3 (let)
def InvestigateType():
    values = ["hello World", 314, 3.14, -3.14, abs, abs(-2), 1 + 1j, True, False]
    for value in values:
        print(type(value))


# Øvelse 4 (let)
def evaluate_expressions():
    expr1 = (2 > 3) or (4 <= 6)
    expr2 = True and (not False)
    expr3 = ((not 1 < 2) and (True or False)) or 3 != 3
    
    print(f"(2 > 3) or (4 <= 6): {expr1}") # True or False = True
    print(f"True and (not False): {expr2}") # True and True = True
    print(f"((not 1 < 2) and (True or False)) or 3 != 3: {expr3}") # False or False = False


#Call all
CalculateSphereVolume()
PrintBla()
InvestigateType()
evaluate_expressions()