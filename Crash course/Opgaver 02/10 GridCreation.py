# Funktion til at printe en vandret linje for et 2x2 gitter
def vandretlinje2x2():
    # Printer to dele af linjen adskilt af '+' med fire '-' mellem hver
    print("+", " ".join(["-"] * 4), "+", " ".join(["-"] * 4), "+")

# Funktion til at printe en vandret linje for et 4x4 gitter
def vandretlinje4x4():
     # Printer fire dele af linjen adskilt af '+' med fire '-' mellem hver
     print("+", " ".join(["-"] * 4), "+", " ".join(["-"] * 4), "+", " ".join(["-"] * 4), "+", " ".join(["-"] * 4), "+")


# Funktion til at printe lodrette linjer for et 2x2 gitter
def lodretlinje2x2():
    # Printer fire lodrette linjer med mellemrum for at repræsentere cellerne i gitteret
    print("|         |         |\n|         |         |\n|         |         |\n|         |         |")

# Funktion til at printe lodrette linjer for et 4x4 gitter
def lodretlinje4x4():
    # Printer fire rækker af lodrette linjer for at repræsentere cellerne i et 4x4 gitter
    print("|         |         |         |         |\n|         |         |         |         |\n|         |         |         |         |\n|         |         |         |         |")


# Funktion til at printe et 2x2 gitter
def Grid2X2():
    # Printer vandrette og lodrette linjer for at skabe et 2x2 gitter
    vandretlinje2x2(); lodretlinje2x2(); vandretlinje2x2(); lodretlinje2x2(); vandretlinje2x2()

# Funktion til at printe et 4x4 gitter
def Grid4x4():
    # Printer vandrette og lodrette linjer for at skabe et 4x4 gitter
    vandretlinje4x4(); lodretlinje4x4(); vandretlinje4x4(); lodretlinje4x4(); vandretlinje4x4(); lodretlinje4x4(); vandretlinje4x4(); lodretlinje4x4(); vandretlinje4x4()

# Kald til funktioner
Grid2X2()
Grid4x4()