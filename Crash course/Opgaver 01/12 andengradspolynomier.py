# Dette program udregner andengradsligninger og tager user input dertil samt displayer et billede af gradens shape.
import math  # Simple rødder.
import cmath # Komplekse rødder.
import numpy as np # Plotting library
import matplotlib.pyplot as plt # To display graph of 2. grads ligning.

# User input for vores koefficienter a, b, og c.
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Nu udregnes diskriminanten
discriminant = b**2 - 4*a*c

# Rødder baserede på diskriminant.
if discriminant > 0:  # Når diskriminant er større end 0, er der 2 udregninger.
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Da diskriminanten er større end 0, har vi 2 rødder: {root1} og {root2}")
elif discriminant == 0:  # Når diskriminant er 0, er der 1 udregning med en dobbelt rod.
    root3 = (-b) / (2*a)
    print(f"Diskriminanten er 0, og der er derfor en dobbelt rod: {root3}")
else:  # Når diskriminant er mindre end 0, er der 2 komplekse rødder.
    root4 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root5 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print(f"Diskriminanten er mindre end 0, og der er derfor 2 komplekse rødder: {root4} og {root5}")

# Nu vil vi plotte vores funktion ved at definere toppunktet og række af værdier.
toppunktX = -b / (2*a)
Xmin = toppunktX - 5
Xmax = toppunktX + 5

# Genererer x og y værdier for at plotte parablen.
xVærdier = np.linspace(Xmin, Xmax, 1000)
yVærdier = a*xVærdier**2 + b*xVærdier + c

# Justerer y-aksen omkring toppunktet.
toppunktY = a*toppunktX**2 + b*toppunktX + c
Ymin = toppunktY - 10
Ymax = toppunktY + 10

# Plotter grafen af andengradspolynomiet
plt.plot(xVærdier, yVærdier, label=f'{a}x² + {b}x + {c}')

# Tilføjer akse-linjer og grid til grafen for bedre overskuelighed.
# plt.axhline(0) tilføjer en vandret linje ved y=0 (x-aksen), som hjælper med at visualisere, hvor rødderne (nulpunkterne) ligger.
plt.axhline(0, color='black', linewidth=0.5)  # x-aksen
plt.axvline(0, color='black', linewidth=0.5)  # y-aksen
plt.title('Graf af andengradspolynomiet')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()