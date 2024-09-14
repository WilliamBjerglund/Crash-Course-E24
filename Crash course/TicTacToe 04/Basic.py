"""
README OBS! Dette spil har flere Gamemodes. 
! OBS Beklager, de mange store functions... i am not a sane person. 
Ultimate Tic Tac Toe fylder meget i terminal.
Derfor anbefales du at trække din terminal en smule op så det passer til spillet.
# TODO
Rename variabler og funktioner til i game mode 3.
Prettify kode. / lav ultimate tic tac toe.
MB: tilføj numre på hvert empty string plads i stedet, så man ved hvad 1-9 er.
"""
# Importerer random modulet til AI's trækvalg.
# Definerer ANSI farvekoder til farvede print-udtryk.
import random
Blå = '\033[94m'
Gul = '\033[93m'
Rød = '\033[91m'
Grøn = '\033[92m'
Pink = '\033[95m'
RESET = '\033[0m'


# Opretter et board som en tom liste med 9 pladser, der kan opdateres med enten X eller O.
board = [' ' for _ in range(9)]
"""Printer Tic Tac Toe-boardet i konsollen."""
def PrintBoard():
    print(f'{Gul}-------------')
    for i in range(3):
        # Printer en række ad gangen med tre elementer pr. række. i farve.
        print(f'{Gul}| {board[i*3]}{Gul} | {board[i*3 + 1]}{Gul} | {board[i*3 + 2]}{Gul} |')
        print(f'{Gul}-------------')



"""Returnerer True, hvis den angivne position er optaget, ellers False."""
def OptagetPladsTjek(position):
    return board[position] != ' '



"""Checker om spillet er ovre ved at tjekke om der er en vinder i rækker, kolonner og diagonaler."""
def is_game_over():
    # Tjekker rækker
    for i in range(0, 9, 3): 
        if board[i] == board[i+1] == board[i+2] != ' ': 
            return True
    # Tjekker kolonner
    for i in range(3): 
        if board[i] == board[i+3] == board[i+6] != ' ': 
            return True
    # Tjekker Diagonaler
    if board[0] == board[4] == board[8] != ' ': 
        return True
    if board[2] == board[4] == board[6] != ' ': 
        return True
    return False # Returnerer False hvis ingen vinder er fundet.



"""Gamemode 1: Starter et Tic Tac Toe-spil for to spillere, hvor de skiftes til at placere X og O.
               Spillet fortsætter indtil der er en vinder eller uafgjort."""
def StartSpil():
    global board # Vi bruger boardet globalt i denne funktion.
    board = [' ' for _ in range(9)]  # Nulstil boardet ved spilstart

    spiller = 1 # Spiller 1 starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() 
        position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") 
        if not position.isdigit() or int(position) < 1 or int(position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
            print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
            continue # Hvis ikke gyldigt, så fortsætter vi loopet.

        position = int(position) - 1 # Vi konverterer inputtet til en index værdi.

        if OptagetPladsTjek(position): # Vi tjekker om pladsen er optaget.
            print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") 
            continue 

        if spiller == 1: # Opdaterer pladsen med X hvis det er spiller 1's tur. Ellers med O.
            board[position] = 'X' 
        else: 
            board[position] = 'O' 
        
        # Tjekker om spillet er ovre.
        if is_game_over(): 
            PrintBoard() 
            print(f"{Grøn}Spiller {spiller} vinder! Vil I spille igen?") 
            break 
        # Hvis der ikke er flere tomme pladser er det uafgjort.
        if ' ' not in board: 
            PrintBoard() 
            print(f"{Pink}Det er uafgjort! Vil I have en omkamp?") 
            break 
        spiller = 3 - spiller # Vi skifter mellem spiller 1 og 2.



"""Gamemode 2: Starter et Tic Tac Toe-spil mod en maskine, hvor spilleren skifter tur med en AI.
               Spilleren spiller som X, og maskinen vælger tilfældigt en tom plads som O."""
def StartSpilVSMachine():
    global board # Vi bruger boardet globalt i denne funktion.
    board = [' ' for _ in range(9)]  # Nulstil boardet ved spilstart

    spiller = 1 # Spilleren starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() 
        if spiller == 1: 
            position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") 
            if not position.isdigit() or int(position) < 1 or int(position) > 9: # Vi tjekker om inputtet er et tal fra 1-9.
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
                continue # Hvis ikke gyldigt, så fortsætter vi loopet.

            position = int(position) - 1 # Vi konverterer inputtet til en index værdi.

            if OptagetPladsTjek(position): # Vi tjekker om pladsen er optaget.
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") 
                continue

            board[position] = 'X' # Spilleren opdaterer pladsen med X.

        else: # Maskinens tur.
            # Vi finder alle tomme pladser på boardet. Derefter vælger vi en tilfældig plads og opdaterer den med O.
            empty_positions = [i for i in range(9) if OptagetPladsTjek(i) == False] 
            position = random.choice(empty_positions) 
            board[position] = 'O' 

        if is_game_over(): 
            PrintBoard() 
            print(f"{Grøn}Spiller {spiller} vinder!") 
            break 
        if ' ' not in board: # Hvis der ikke er flere tomme pladser.
            PrintBoard() 
            print(f"{Pink}Det er uafgjort!") 
            break 
        spiller = 3 - spiller # Vi skifter mellem spiller 1 og 2.



"""Gamemode 3: Starter et Tic Tac Toe-spil med flytbare symboler.
               Når en spiller har 3 mærker på brættet, kan de flytte et af deres mærker til en tom plads."""
def StartSpil3FlytbareSymboler():
    global board # Vi bruger brættet globalt i denne funktion.
    board = [' ' for _ in range(9)]  # Nulstil brættet ved spilstart

    spiller = 1 # Spiller 1 starter.
    valgt_X = None # Gemmer positionen for det valgte X-mærke.
    valgt_O = None # Gemmer positionen for det valgte O-mærke.
    trækTæller = 0 # Tæller antal træk.
    maxTræk = 46 # Max antal træk før uafgjort.

    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard() 
        # Hvis spiller 1 har 3 mærker på brættet. Kan de vælge et mærke at flytte.
        if board.count('X') == 3 and spiller == 1: 
            if valgt_X is None: 
                print(f"{Blå}Spiller 1, vælg et mærke (X) at flytte:")
                mærkeAtFlytte = input("Indtast positionen for mærket (1-9): ")

                if not mærkeAtFlytte.isdigit() or int(mærkeAtFlytte) < 1 or int(mærkeAtFlytte) > 9: # Tjekker om inputtet er et tal fra 1-9.
                    print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
                    continue 
                mærkeAtFlytte = int(mærkeAtFlytte) - 1

                if board[mærkeAtFlytte] != 'X': 
                    print(f"{Rød}Ugyldig indtastning. Vælg venligst et mærke (X) at flytte.") 
                    continue 

                valgt_X = mærkeAtFlytte # Gemmer valgt X position.

            nyPosition = input("Indtast den nye position for mærket (1-9): ") # Spilleren vælger en ny position.

            if not nyPosition.isdigit() or int(nyPosition) < 1 or int(nyPosition) > 9: 
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
                continue 
            nyPosition = int(nyPosition) - 1 

            if OptagetPladsTjek(nyPosition): 
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") 
                continue 

            board[valgt_X] = ' ' # Fjerner gammel X position.
            board[nyPosition] = 'X' # Opdaterer ny X position.
            valgt_X = None # Nulstiller X position Memory.

        elif board.count('O') == 3 and spiller == 2: # Hvis spiller 2 har 3 mærker på brættet. Kan de vælge et mærke at flytte.
            if valgt_O is None: 
                print(f"{Blå}Spiller 2, vælg et mærke (O) at flytte:")
                mærkeAtFlytte = input("Indtast positionen for mærket (1-9): ")

                if not mærkeAtFlytte.isdigit() or int(mærkeAtFlytte) < 1 or int(mærkeAtFlytte) > 9: # Tjek Input er tal.
                    print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
                    continue 
                mærkeAtFlytte = int(mærkeAtFlytte) - 1 

                if board[mærkeAtFlytte] != 'O': # Hvis forkert input giv fejl.
                    print(f"{Rød}Ugyldig indtastning. Vælg venligst et mærke (O) at flytte.") 
                    continue 
                valgt_O = mærkeAtFlytte # Gemmer O position.
            nyPosition = input("Indtast den nye position for mærket (1-9): ")

            if not nyPosition.isdigit() or int(nyPosition) < 1 or int(nyPosition) > 9: # Tjek Input er tal.
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
                continue 
            nyPosition = int(nyPosition) - 1 

            if OptagetPladsTjek(nyPosition): 
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") 
                continue 
            board[valgt_O] = ' ' # Fjerner gammel O position.
            board[nyPosition] = 'O' # Opdaterer ny O position.
            valgt_O = None # Nulstiller O position Memory.

        else: # Hvis ingen af spillerne har 3 mærker på brættet eller det ikke er deres tur.
            position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: ") 
            if not position.isdigit() or int(position) < 1 or int(position) > 9: 
                print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.") 
                continue 
            position = int(position) - 1 

            if OptagetPladsTjek(position): 
                print(f"{Rød}Pladsen er allerede optaget. Prøv igen.") 
                continue 

            if spiller == 1: # Hvis spiller 1 er i gang.
                board[position] = 'X' 
            else: 
                board[position] = 'O' 
            
        trækTæller += 1 # Tæller antal træk.

        if is_game_over(): 
            PrintBoard() 
            print(f"{Grøn}Spiller {spiller} vinder!") 
            break 
        if trækTæller >= maxTræk:
            print(f"{Pink}Det er uafgjort!") 
            break

        spiller = 3 - spiller # Skifter mellem spiller 1 og 2.



# Funktion til at vælge spiltilstand.
def VelkomstOgSpilValg():
    while True:
        print(f"{Blå}Vælg spiltilstand:\n1. 2 spillere\n2. 1 spiller mod Maskine\n3. 3x3 Tic Tac Toe med flytbare symboler\n4. Afslut")
        GameMode = input("Indtast dit valg (1-4): ")
        if not GameMode.isdigit() or int(GameMode) < 1 or int(GameMode) > 4:
            print("Ugyldigt valg. Indtast venligst et nummer fra 1-4.")
        else:
            return GameMode



# Starter spillet ved at vælge en spiltilstand.
while True:
    GameMode = VelkomstOgSpilValg()

    if GameMode == '1':
        StartSpil()
    elif GameMode == '2':
        StartSpilVSMachine()
    elif GameMode == '3':
        StartSpil3FlytbareSymboler()
    elif GameMode == '4': 
        print("Spillet er afsluttet.")
        break
    else:
        print("Ugyldigt valg. Indtast venligst et nummer fra 1-4.")
