# Lav en funktion, even_before_n, der opretter en liste med alle lige tal fra 1 til og med n.  
def EvenBeforeN(n):
    list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            list.append(i)
    return list

print(EvenBeforeN(10))