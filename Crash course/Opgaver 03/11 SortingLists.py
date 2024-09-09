"""
    Tjekker om en liste er sorteret i stigende rækkefølge.
    
    Parametre:
    lst (list): En liste af tal.
    
    Returnerer:
    bool: True hvis listen er sorteret i stigende rækkefølge, False ellers.
    
    Funktion:
    Funktionen går igennem listen og sammenligner hvert element med det næste. 
    Hvis et element er større end det næste, returneres False, da listen ikke er 
    sorteret. Hvis hele listen gennemgås uden problemer, returneres True.
"""

while True:
    user_input = input("Skriv venligst en række tal adskilt af mellemrum: ")
    if " " in user_input:
        list = [int(x) for x in user_input.split()]  # Konverterer input til en liste af tal
        break
    else:
        print("Der skal være mellemrum mellem tallene. Prøv igen.")

def IsSorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
        elif list[i] <= list[i + 1]:
            return True

print(IsSorted(list))