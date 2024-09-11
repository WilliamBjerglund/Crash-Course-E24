# Tic Tac Toe
# Først vil jeg lave et board der skal være en tom liste med 9 pladser.
# Denne liste indeneholder 9 pladser, som er tomme, men bliver opdateret med enten X eller O.
board = [' ' for _ in range(9)]

# Denne funktion skal lave vores visuelle board. Vi vil gerne have det til at se ud som et rigtigt Tic Tac Toe board.
def PrintBoard():
    # Vi printer en streg før hver række, så det ligner et rigtigt Tic Tac Toe board.
    print('-------------')
    for i in range(3): # Dette loop sikrer sig vi laver 3 rows
        # Vi printer en række ad gangen, og vi printer de 3 elementer i rækken (nedadgående).
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        # Vi printer en streg efter hver række, så det ligner et rigtigt Tic Tac Toe board.
        print('-------------')

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

# Nu skal vi bruge en funktion til selve spillet. Der skal tage både user input og opdatere boardet.
# Vi vil også gerne have at spillet kan skifte mellem spiller 1 og 2.
# Derudover tjekker vi om spillet er ovre og hvis det er printer en vinder besked.
# Hvis ingen vinder, så vil vi gerne have en besked for en lige / tied match.
def StartSpil():
    # Først laver vi en variabel der holder styr på hvilken spiller der er i gang.
    spiller = 1 # Spiller 1 starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() # Vi printer boardet.
        position = input(f"Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") # Vi beder spilleren om at indtaste en plads.
        if not position.isdigit() or int(position) < 1 or int(position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
            print("Ugyldig indtastning. Indtast venligst et tal fra 1-9.") # Hvis det ikke er, så printes en besked.
            continue # Vi fortsætter loopet.
        position = int(position) - 1 # Vi konverterer inputtet til en index værdi.
        if OptagetPladsTjek(position): # Vi tjekker om pladsen er optaget.
            print("Pladsen er allerede optaget. Prøv igen.") # Hvis den er, så printes en besked.
            continue # Vi fortsætter loopet.
        if spiller == 1: # Hvis spiller 1 er i gang.
            board[position] = 'X' # Så opdateres pladsen med X.
        else: # Hvis spiller 2 er i gang.
            board[position] = 'O' # Så opdateres pladsen med O.
        if is_game_over(): # Vi tjekker om spillet er ovre.
            PrintBoard() # Vi printer boardet.
            print(f"Spiller {spiller} vinder!") # Vi printer en vinder besked.
            break # Vi bryder loopet.
        if ' ' not in board: # Hvis der ikke er flere tomme pladser.
            PrintBoard() # Vi printer boardet.
            print("Det er uafgjort!") # Vi printer en uafgjort besked.
            break # Vi bryder loopet.
        spiller = 3 - spiller # Vi skifter mellem spiller 1 og 2.

StartSpil() # Vi starter spillet.