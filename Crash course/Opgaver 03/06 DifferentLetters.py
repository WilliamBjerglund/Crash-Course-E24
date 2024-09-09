"""
    Denne funktion tager to ord som input (word1 og word2), konverterer dem til sæt (sets), 
    og finder forskellen mellem de to sæt. 
    Funktionen printer derefter alle bogstaver, som optræder i word1, men ikke i word2.

    - word1: Første ord (string).
    - word2: Andet ord (string).

    Resultat:
    Funktionen printer bogstaver, som kun findes i word1.
    """
word1 = str("Seraphine")
word2 = str("Soraka")

def DifferentLetters(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    difference = set1 - set2 
    for letter in difference:
        print(letter)


DifferentLetters(word1, word2)
