def first_word():
    word1 = input("Første ord er: ")
    word2 = input("Andet ord er: ")
    if word1 < word2:
        return word1
    else:
        return word2

print(f"Det første ord i alfabetisk rækkefølge er: {first_word()}")
