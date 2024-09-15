"""
README OBS! Dette spil har flere Gamemodes Also Please run in VSCode eller anden IDE.
Windows Terminal kan ikke vise ANSI farvekoder, så farvede print-udtryk vil ikke blive vist korrekt. 
"""
# Importerer random modulet til AI's trækvalg. Og Time for sanity checks.
# Definerer ANSI farvekoder til farvede print-udtryk.
import time
import random

# Definerer farvekoder
Blå = '\033[94m'  # Bright Blue
Cyan = '\033[36m'  # Cyan
Rød = '\033[91m'  # Bright Red
Grøn = '\033[92m'  # Bright Green
Gul = '\033[93m'  # Bright Yellow
Magenta = '\033[95m'  # Bright Magenta
RESET = '\033[0m'  # Reset to default color

# Opretter et board som en tom liste med 9 pladser, der kan opdateres med enten X eller O.
board = [' ' for _ in range(9)]

"""Nulstiller brættet ved spilstart."""
def ResetBoard():
    global board # Vi bruger boardet globalt i denne funktion.
    board = [' ' for _ in range(9)]  # Nulstil boardet ved spilstart


"""Printer Tic Tac Toe-boardet i konsollen."""
def PrintBoard():
    print(f'{Cyan}-------------')
    for i in range(3):
        # Printer en række ad gangen med tre elementer pr. række. i farve.
        print(f'{Cyan}| {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} |')
        print(f'{Cyan}-------------')


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


"""Håndterer spillerens input og returnerer en gyldig position."""
def PlayerInput(spiller):
    while True:
        position = input(f"{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: {RESET}")
        time.sleep(0.2)
        if not position.isdigit() or int(position) < 1 or int(position) > 9:
            PrintBoard()
            print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.{RESET}")
            continue
        position = int(position) - 1
        if OptagetPladsTjek(position):
            PrintBoard()
            print(f"{Rød}Pladsen er allerede optaget. Prøv igen.{RESET}")
            continue
        return position


"""Checker spillets status og returnerer True, hvis spillet er ovre."""
def GameStatus(spiller):
    if is_game_over():
        PrintBoard()
        print(f"{Grøn}Spiller {spiller} vinder! Vil I spille igen?{RESET}")
        return True
    if ' ' not in board:
        PrintBoard()
        print(f"{Gul}Det er uafgjort! Vil I have en omkamp?{RESET}")
        return True
    return False


"""Håndterer input for at vælge et mærke at flytte."""
def MærkeDerSkalFlyttes(spiller, symbol):
    while True:
        print(f"{Blå}Spiller {spiller}, vælg et mærke ({symbol}) at flytte:{RESET}")
        mærkeAtFlytte = input("Indtast positionen for mærket (1-9): ")
        time.sleep(0.2)
        if not mærkeAtFlytte.isdigit() or int(mærkeAtFlytte) < 1 or int(mærkeAtFlytte) > 9:
            PrintBoard()
            print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.{RESET}")
            continue
        mærkeAtFlytte = int(mærkeAtFlytte) - 1
        if board[mærkeAtFlytte] != symbol:
            PrintBoard()
            print(f"{Rød}Ugyldig indtastning. Vælg venligst et mærke ({symbol}) at flytte.{RESET}")
            continue
        return mærkeAtFlytte


"""Flytter et mærke til en ny position."""
def RykMærke(symbol, valgtMærke):
    while True:
        nyPosition = input("Indtast den nye position for mærket (1-9): ")
        time.sleep(0.2)
        if not nyPosition.isdigit() or int(nyPosition) < 1 or int(nyPosition) > 9:
            print(f"{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.{RESET}")
            continue
        nyPosition = int(nyPosition) - 1
        if OptagetPladsTjek(nyPosition):
            print(f"{Rød}Pladsen er allerede optaget. Prøv igen.{RESET}")
            continue
        board[valgtMærke] = ' '
        board[nyPosition] = symbol
        break


"""Placerer et nyt mærke på brættet."""
def PlacerNyMærke(spiller, symbol):
    while True:
        NyPosition = input(f'{Blå}Spiller {spiller}, indtast et tal fra 1-9 for at placere dit mærke: {RESET}')
        time.sleep(0.2)
        if not NyPosition.isdigit() or int(NyPosition) < 1 or int(NyPosition) > 9:
            print(f'{Rød}Ugyldig indtastning. Indtast venligst et tal fra 1-9.{RESET}')
            continue
        NyPosition = int(NyPosition) - 1
        if OptagetPladsTjek(NyPosition):
            print(f'{Rød}Pladsen er allerede optaget. Prøv igen.{RESET}')
            continue
        board[NyPosition] = symbol
        break


"""Gamemode 1: Starter et Tic Tac Toe-spil for to spillere, hvor de skiftes til at placere X og O.
               Spillet fortsætter indtil der er en vinder eller uafgjort."""
def StartSpil():
    ResetBoard()

    spiller = 1 # Spiller 1 starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard()
        position = PlayerInput(spiller)
        board[position] = 'X' if spiller == 1 else 'O'
        if GameStatus(spiller):
            break
        spiller = 3 - spiller


"""Gamemode 2: Starter et Tic Tac Toe-spil mod en maskine, hvor spilleren skifter tur med en AI.
               Spilleren spiller som X, og maskinen vælger tilfældigt en tom plads som O."""
def StartSpilVSMachine():
    ResetBoard()

    spiller = 1 # Spilleren starter.
    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard()
        if spiller == 1:
            position = PlayerInput(spiller)
            board[position] = 'X'
        else:
            TommePladser = [i for i in range(9) if not OptagetPladsTjek(i)]
            position = random.choice(TommePladser)
            board[position] = 'O'

        if GameStatus(spiller):
            break
        spiller = 3 - spiller


"""Gamemode 3: Starter et Tic Tac Toe-spil med flytbare symboler.
               Når en spiller har 3 mærker på brættet, kan de flytte et af deres mærker til en tom plads."""
def StartSpil3FlytbareSymboler():
    ResetBoard()

    spiller = 1 # Spiller 1 starter.
    trækTæller = 0 # Tæller antal træk.
    maxTræk = 46 # Max antal træk før uafgjort.

    while True: # Vi laver et loop der kører indtil vi har en vinder eller uafgjort.
        PrintBoard()
        if board.count('X') == 3 and spiller == 1:
            valgtMærke = MærkeDerSkalFlyttes(spiller, 'X')
            RykMærke('X', valgtMærke)
        elif board.count('O') == 3 and spiller == 2:
            valgtMærke = MærkeDerSkalFlyttes(spiller, 'O')
            RykMærke('O', valgtMærke)
        else:
            PlacerNyMærke(spiller, 'X' if spiller == 1 else 'O')
        
        trækTæller += 1

        if is_game_over():
            PrintBoard()
            print(f"{Grøn}Spiller {spiller} vinder! Vil I spille igen?{RESET}")
            break
        if trækTæller >= maxTræk:
            print(f'{Gul} Det er uafgjort! Vil I have en omkamp?{RESET}')
            break
        spiller = 3 - spiller


"""Funktion til at vælge spiltilstand."""
def VelkomstOgSpilValg():
    while True:
        print(f"{Magenta}Vælg spiltilstand:\n1. 2 spillere\n2. 1 spiller mod Maskine\n3. 3x3 Tic Tac Toe med flytbare symboler\n4. Afslut{RESET}")
        GameMode = input("Indtast dit valg (1-4): ")
        time.sleep(0.2)
        if not GameMode.isdigit() or int(GameMode) < 1 or int(GameMode) > 4:
            print(f"{Rød}Ugyldigt valg. Indtast venligst et nummer fra 1-4.{RESET}")
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
        print(f"{Rød}Ugyldigt valg. Indtast venligst et nummer fra 1-4.{RESET}")