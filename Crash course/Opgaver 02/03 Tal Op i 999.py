import math

for numbers in range(1000):
    if numbers % 35 == 0:
        print(numbers)

"""

Forklaring: 
I denne for loop tager vi alle tal op til 1000 og herefter checker vi vha. modulus om de kan divideres med 35 og give 0.
35 virker eftersom 5*7 = 35 og derefter printer vi blot de tal.

"""
