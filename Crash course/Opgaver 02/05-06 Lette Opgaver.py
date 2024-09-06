import math

def TriangleArea(g, h):
    Area = (h * 0.5) * g
    return Area
"""
Denne funktion har paremeterne g og h lokalt. Den tager og udregner Area lokalt baserede på de paremeter den har variablerne g og h.
Derefter returnerer den blot resultat af dens udregning Area    

"""
g = 4
h = 3
AreaofTriangle = TriangleArea(g, h)
print(f"dit areal af trekanten er: {AreaofTriangle}")
"""
jeg har givet g og h en værdi udenfor min funktion og laver derfor endnu en variable at printe.
denne variable tager blot og kalder funktionen TriangleArea som inputter de g og h værdier der er defineret.
og printer den til sidst vha. en f string.

"""