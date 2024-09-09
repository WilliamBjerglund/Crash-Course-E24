alphabet = "abcdefghijklmnopqrstuvwxyz"

# Dette er del 1. af opgaven
Hvertandet = alphabet[::2]
print(Hvertandet)  # Output: acegikmoqsuwy
Hverttredje = alphabet[::3]
print(Hverttredje)  # Output: adgjmpsvy
Hvertfjerde = alphabet[::4]
print(Hvertfjerde)  # Output: aeimquy

# Dette er del 2. af opgaven
HvertAndet10Første = alphabet[0:10:2]
print(HvertAndet10Første)

# Dette er del 3. af opgaven
HvertTredje10Sidste = alphabet[16::3]
print(HvertTredje10Sidste)

# Dette er del 4. af opgaven
BaglænsAlphabet = alphabet[::-1]
print(BaglænsAlphabet)