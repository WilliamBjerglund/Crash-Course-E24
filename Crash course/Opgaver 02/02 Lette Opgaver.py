import math

n = int(input("Indtast en værdi for n: "))
n = int(n)
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print(f"Summen af de første", n, "naturlige tal er:", sum)