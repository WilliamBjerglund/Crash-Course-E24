# Definerer funktionen do_twice, som tager en funktion (f) og en værdi (value).
# Hvis en værdi gives, kaldes funktionen to gange med denne værdi.
# Hvis ingen værdi gives, kaldes funktionen to gange uden argumenter.
def do_twice(f, value=None):
    if value is not None:
        f(value)
        f(value)
    else:
        f()
        f()

# Definerer en simpel funktion, der printer "spam".
def print_spam():
    print("spam")

# Kalder do_twice med print_spam-funktionen, som ikke kræver en værdi.
do_twice(print_spam)


# Definerer en funktion, der printer det samme argument to gange.
def print_twice(bruce):
    print(bruce)
    print(bruce)

# Kalder do_twice med print_twice-funktionen og "spam" som argument.
do_twice(print_twice, "spam")


# Definerer funktionen do_four, som bruger do_twice til at kalde en funktion fire gange.
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

# Kalder do_four med print_twice-funktionen og "spam" som argument.
do_four(print_twice, "spam")
