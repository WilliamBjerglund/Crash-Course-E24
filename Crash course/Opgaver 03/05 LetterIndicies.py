word = "ComputerTechnology"

def LetterIndicies(word):
    initialindex = 0
    while initialindex < len(word):
        print(f"Bogstav {word[initialindex]}, index: {initialindex}")
        initialindex += 1


LetterIndicies(word)