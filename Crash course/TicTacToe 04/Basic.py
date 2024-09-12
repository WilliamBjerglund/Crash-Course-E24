# import random så vi ikke selv skal lave en randomizer funktion.
# Derudover definer vi vores farver til pæne print statements [Farver er ANSI].
import random
Blå = '\033[94m'
Gul = '\033[93m'
Rød = '\033[91m'
Grøn = '\033[92m'

"""
   TODO:
     Change the Names & Comments i Game mode 3.
     Add a way for the Game mode selection to ask again once a game is finished. (Currently it just ends the game.)
     If time prettify the code / make the board look better. Also Make AI for Game mode 2 smarter. 
"""

# Vi printer en velkomst besked til spilleren.
# Derudover beder vi spilleren om at vælge en spiltilstand. (2 spillere, 1 spiller mod maskine, 3x3 Tic Tac Toe med flytbare symboler, Afslut spillet)
while True:
    print(f"{Blå}Vælg spiltilstand:\n1. 2 spillere\n2. 1 spiller mod Maskine\n3. 3x3 Tic Tac Toe med flytbare symboler\n4. Afslut")
    GameMode = input("Indtast dit valg (1-4): ")
    if not GameMode.isdigit() or int(GameMode) < 1 or int(GameMode) > 4:
        print("Ugyldigt valg. Indtast venligst et nummer fra 1-4.")
    else:
        break


# Tic Tac Toe
# Først vil jeg lave et board der skal være en tom liste med 9 pladser.
# Denne liste indeneholder 9 pladser, som er tomme, men bliver opdateret med enten X eller O.
board = [' ' for _ in range(9)]


# Denne funktion skal lave vores visuelle board. Vi vil gerne have det til at se ud som et rigtigt Tic Tac Toe board.
def PrintBoard():
    # Vi printer en streg før hver række, så det ligner et rigtigt Tic Tac Toe board.
    print(f'{Gul}-------------')
    for i in range(3): # Dette loop sikrer sig vi laver 3 rows
        # Vi printer en række ad gangen, og vi printer de 3 elementer i rækken (nedadgående).
        print(f'{Gul}| {Grøn}{board[i*3]}{Gul} | {Grøn}{board[i*3 + 1]}{Gul} | {Grøn}{board[i*3 + 2]}{Gul} |')
        # Vi printer en streg efter hver række, så det ligner et rigtigt Tic Tac Toe board.
        print(f'{Gul}-------------')

# Nu skal vi bruge en funktion der kan tjekke om en plads er optaget.
def OptagetPladsTjek(position):
    # Vi tjekker om pladsen er optaget, ved at tjekke om pladsen er lig med et mellemrum (det den startede som).
    return board[position] != ' '

# Denne funktion checker om spillet er ovre, og returnerer True hvis det er.
def is_game_over():
    # Vi tjekker om der er en vinder i rækkerne.
    for i in range(0, 9, 3): # Vi tjekker hver rækk med et for loop.
        if board[i] == board[i+1] == board[i+2] != ' ': # Hvis alle 3 elementer i rækken er ens, og ikke tomme, så vinder X eller O.
            return True
    # Vi tjekker om der er en vinder i kolonnerne.
    for i in range(3): # Vi tjekker hver kolonne med et for loop.
        if board[i] == board[i+3] == board[i+6] != ' ': # Hvis alle 3 elementer i kolonnen er ens, og ikke tomme, så vinder X eller O.
            return True
    # Vi tjekker om der er en vinder i diagonalen.
    if board[0] == board[4] == board[8] != ' ': # Hvis alle 3 elementer i diagonalen er ens, og ikke tomme, så vinder X eller O.
        return True
    if board[2] == board[4] == board[6] != ' ': # Hvis alle 3 elementer i diagonalen er ens, og ikke tomme, så vinder X eller O.
        return True
    return False # Hvis ingen af de andre tjek er sande, så er spillet ikke ovre.

# Gamemode 1. 2 spillere
# Nu skal vi bruge en funktion til selve spillet. Der skal tage både user input og opdatere boardet.
# Vi vil også gerne have at spillet kan skifte mellem spiller 1 og 2.
# Derudover tjekker vi om spillet er ovre og hvis det er printer en vinder besked.
# Hvis ingen vinder, så vil vi gerne have en besked for en lige / tied match.
def StartSpil():
    # Først laver vi en variabel der holder styr på hvilken spiller der er i gang.
    spiller = 1 # Spiller 1 starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() # Vi printer boardet.
        position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") # Vi beder spilleren om at indtaste en plads.
        if not position.isdigit() or int(position) < 1 or int(position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
            print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
            continue # Vi fortsætter loopet.
        position = int(position) - 1 # Vi konverterer inputtet til en index værdi.
        if OptagetPladsTjek(position): # Vi tjekker om pladsen er optaget.
            print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") # Hvis den er, så printes en besked.
            continue # Vi fortsætter loopet.
        if spiller == 1: # Hvis spiller 1 er i gang.
            board[position] = 'X' # Så opdateres pladsen med X.
        else: # Hvis spiller 2 er i gang.
            board[position] = 'O' # Så opdateres pladsen med O.
        if is_game_over(): # Vi tjekker om spillet er ovre.
            PrintBoard() # Vi printer boardet.
            print(f"{Grøn}Spiller {spiller} vinder!") # Vi printer en vinder besked.
            break # Vi bryder loopet.
        if ' ' not in board: # Hvis der ikke er flere tomme pladser.
            PrintBoard() # Vi printer boardet.
            print(f"{Blå}Det er uafgjort!") # Vi printer en uafgjort besked.
            break # Vi bryder loopet.
        spiller = 3 - spiller # Vi skifter mellem spiller 1 og 2.


# Gamemode 2. 1 spiller mod maskine.
# Læs Komment til Gamemode 1 for forklaring af funktion.
# Forskellen på denne og Gamemode 1 er at vi har en AI der vælger en tilfældig plads for O i stedet for en spiller.
def StartSpilVSMachine():
    spiller = 1 # Spilleren starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() # Vi printer boardet.
        if spiller == 1: # Hvis det er spiller 1's tur.
            position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") # Vi beder spilleren om at indtaste en plads.
            if not position.isdigit() or int(position) < 1 or int(position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en fejlbesked.
                continue # Vi fortsætter loopet.
            position = int(position) - 1 # Vi konverterer inputtet til en index værdi.
            if OptagetPladsTjek(position): # Vi tjekker om pladsen er optaget med funktionen derfor.
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") # Hvis den er, så printes en fejlbesked.
                continue # Vi fortsætter loopet.
            board[position] = 'X' # Hvis pladsen ikke er optaget, så opdateres pladsen med X.

        else: # Hvis det er maskinens tur.
            empty_positions = [i for i in range(9) if OptagetPladsTjek(i) == False] # Finder alle tomme positioner.
            position = random.choice(empty_positions) # Vælger en tilfældig tom position.
            board[position] = 'O' # Så opdateres pladsen med O.
        if is_game_over(): # Vi tjekker om spillet er ovre.
            PrintBoard() # Vi printer boardet.
            print(f"{Grøn}Spiller {spiller} vinder!") # Vi printer en vinder besked.
            break # Vi bryder loopet.
        if ' ' not in board: # Hvis der ikke er flere tomme pladser.
            PrintBoard() # Vi printer boardet.
            print(f"{Blå}Det er uafgjort!") # Vi printer en uafgjort besked.
            break # Vi bryder loopet.
        spiller = 3 - spiller # Vi skifter mellem spiller 1 og 2.

# Gamemode 3. 3x3 Tic Tac Toe med flytbare symboler.
# Princippet er det samme som 1 og 2. gamemode forskellen er vi her også tjekker for om der er 3 mærker på boardet.
# Hvis der er 3 mærker på boardet, så kan spilleren flytte et af sine mærker til en anden position.
def StartSpil3FlytbareSymboler():
    spiller = 1 # Spiller 1 starter (styringsvariable for spillerrækkefølge).
    selected_X = None # Variabel til at gemme positionen for det valgte X-mærke.
    selected_O = None # Variabel til at gemme positionen for det valgte O-mærke.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() # Vi printer boardet.
        if board.count('X') == 3 and spiller == 1: # Hvis spiller 1 har 3 mærker på boardet.
            if selected_X is None: # Hvis der ikke er valgt et X-mærke endnu.
                print(f"{Blå}Spiller 1, vælg et mærke (X) at flytte:")
                mark_to_move = input("Indtast positionen for mærket (1-9): ")
                if not mark_to_move.isdigit() or int(mark_to_move) < 1 or int(mark_to_move) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                    print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
                    continue # Vi fortsætter loopet.
                mark_to_move = int(mark_to_move) - 1 # Vi konverterer inputtet til en index værdi.
                if board[mark_to_move] != 'X': # Vi tjekker om den valgte position indeholder et X-mærke.
                    print(f"{Rød}Ugyldig indtastning. Vælg venligst et mærke (X) at flytte.") # Hvis det ikke er, så printes en besked.
                    continue # Vi fortsætter loopet.
                selected_X = mark_to_move # Gemmer positionen for det valgte X-mærke.
            new_position = input("Indtast den nye position for mærket (1-9): ")
            if not new_position.isdigit() or int(new_position) < 1 or int(new_position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
                continue # Vi fortsætter loopet.
            new_position = int(new_position) - 1 # Vi konverterer inputtet til en index værdi.
            if OptagetPladsTjek(new_position): # Vi tjekker om den nye position er optaget.
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") # Hvis den er, så printes en besked.
                continue # Vi fortsætter loopet.
            board[selected_X] = ' ' # Fjerner det gamle mærke fra den gamle position.
            board[new_position] = 'X' # Så opdateres den nye position med X.
            selected_X = None # Nulstiller den valgte X-variabel.
        elif board.count('O') == 3 and spiller == 2: # Hvis spiller 2 har 3 mærker på boardet.
            if selected_O is None: # Hvis der ikke er valgt et O-mærke endnu.
                print(f"{Blå}Spiller 2, vælg et mærke (O) at flytte:")
                mark_to_move = input("Indtast positionen for mærket (1-9): ")
                if not mark_to_move.isdigit() or int(mark_to_move) < 1 or int(mark_to_move) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                    print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
                    continue # Vi fortsætter loopet.
                mark_to_move = int(mark_to_move) - 1 # Vi konverterer inputtet til en index værdi.
                if board[mark_to_move] != 'O': # Vi tjekker om den valgte position indeholder et O-mærke.
                    print(f"{Rød}Ugyldig indtastning. Vælg venligst et mærke (O) at flytte.") # Hvis det ikke er, så printes en besked.
                    continue # Vi fortsætter loopet.
                selected_O = mark_to_move # Gemmer positionen for det valgte O-mærke.
            new_position = input("Indtast den nye position for mærket (1-9): ")
            if not new_position.isdigit() or int(new_position) < 1 or int(new_position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
                continue # Vi fortsætter loopet.
            new_position = int(new_position) - 1 # Vi konverterer inputtet til en index værdi.
            if OptagetPladsTjek(new_position): # Vi tjekker om den nye position er optaget.
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") # Hvis den er, så printes en besked.
                continue # Vi fortsætter loopet.
            board[selected_O] = ' ' # Fjerner det gamle mærke fra den gamle position.
            board[new_position] = 'O' # Så opdateres den nye position med O.
            selected_O = None # Nulstiller den valgte O-variabel.
        else: # Hvis ingen af spillerne har 3 mærker på boardet eller det ikke er deres tur.
            position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") # Vi beder spilleren om at indtaste en plads.
            if not position.isdigit() or int(position) < 1 or int(position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
                continue # Vi fortsætter loopet.
            position = int(position) - 1 # Vi konverterer inputtet til en index værdi.
            if OptagetPladsTjek(position): # Vi tjekker om pladsen er optaget.
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") # Hvis den er, så printes en besked.
                continue # Vi fortsætter loopet.
            if spiller == 1: # Hvis spiller 1 er i gang.
                board[position] = 'X' # Så opdateres pladsen med X.
            else: # Hvis spiller 2 er i gang.
                board[position] = 'O' # Så opdateres pladsen med O.
        if is_game_over(): # Vi tjekker om spillet er ovre.
            PrintBoard() # Vi printer boardet.
            print(f"{Grøn}Spiller {spiller} vinder!") # Vi printer en vinder besked.
            break # Vi bryder loopet.
        if ' ' not in board: # Hvis der ikke er flere tomme pladser.
            PrintBoard() # Vi printer boardet.
            print(f"{Blå}Det er uafgjort!") # Vi printer en uafgjort besked.
            break # Vi bryder loopet.
        spiller = 3 - spiller # Vi skifter mellem spiller 1 og 2.

if GameMode == '1':
    StartSpil()
elif GameMode == '2':
    StartSpilVSMachine()
    pass
elif GameMode == '3':
    StartSpil3FlytbareSymboler()
elif GameMode == '4': # Dette er gamemode select for 4. det gøre også koden for game mode 4. Og afslutter spillet.
    print("Spillet er afsluttet.") # sanitycheck for spilleren.
else:
    print("Ugyldigt valg. Indtast venligst et nummer fra 1-4.")



print("Sanity Check")