# 3.1 fra ThinkPython2
# denne opgave beder os rykke en string så den altid vil printe på charecter position 70 (char 70)
# Opgaven beder os tage paremeteren s en string og rykke derud så sidste bogstav af stringen er 70

# først vil jeg definerer s min string udenfor funktion
s = str("monty") # note det er ikke nødvendigt at sætte str paremeteren op i Python men af princip gør jeg det alligvel.


# jeg definer min funktion med s som paremeter
def right_justify(s):
    LengthOfString = len(s) # længden af en hver givet string s
    position = 70 - LengthOfString # stedet, hvor s skal ende op minus længden af s giver mængden af spaces der skal tilføjes.
    RightJustifiedString = " " * position # Jeg udregner spaces der skal tilføjes.
    print(RightJustifiedString, s) # Vi printer stringen.
    
right_justify(s)