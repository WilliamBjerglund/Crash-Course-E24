import math

# Funktion til at beregne den harmoniske sum op til n
def harmoniskSum(n):
    # Hvis n er 1, returnerer vi 1, da den harmoniske sum af 1 er 1
    if n == 1:
        return 1
    else:
        # Hvis n er større end 1, beregner vi summen rekursivt
        return 1/n + harmoniskSum(n - 1)

# Antal led i den harmoniske sum, vi vil beregne
N = 10

# Udskriv resultatet af den harmoniske sum for N = 10
print(f"Harmonisk sum for {N} led =", harmoniskSum(N))
