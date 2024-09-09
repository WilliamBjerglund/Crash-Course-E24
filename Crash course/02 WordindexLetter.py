def wordindexletter(word, n):
    if 1 <= n <= len(word):
        return(word[n - 1])
    else:
        return "Indeks er uden for rækkevidde"
    
# test case
print(wordindexletter("python", 3))