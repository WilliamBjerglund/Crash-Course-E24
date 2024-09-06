"""
I denne funktion FizzBuzz er en paremeter diviserer som er en liste af tuples der hver indenholder en divisor -
og dens tilhørende label altså "Fizz" eller "Buzz"
Min anden paremeter Limit er blot en af mange måder at stoppe ved 100. og er altså blot en begrænser 
"""
def FizzBuzz(Deletal, limit = 100):
    # Looper igennem tal fra 1 til 100 / limit.
    for i in range (1, limit + 1):
        output = "" # Opretter blot en tom streng for vores resultat
        # dette for loop tager hver divisor i diviserer og tjekker om det er deleligt med diviserene fra rules.
        for divisor, label in Deletal:
            if i % divisor == 0:
                # Dette outputter vores resultat af i med sit tilhørende label ellers ingenting.
                output += label
        # Dette print udskriver hvis der er noget i output ellers hvis der er noget i "i".
        print(output or i)

# Dette er vores regler for hvad der skal printes.
rules = [(3, "Fizz"), (5, "Buzz")]

# Kør funktionen med paremetrene fra rules.
FizzBuzz(rules)