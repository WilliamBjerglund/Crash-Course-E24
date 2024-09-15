"""
README OBS! Dette spil har flere Gamemodes Also Please run in VSCode eller anden IDE.
Windows Terminal kan ikke vise ANSI farvekoder, så farvede print-udtryk vil ikke blive vist korrekt.

ALSO NOTE! Spillet fylder en smule i konsollen så alt efter din screen size kan det være nødvendigt at dragge din konsol lidt op (12 linjer). 
"""
# Importerer random modulet til AI's trækvalg. Og Time for sanity checks.
import time
import random

# Definerer farvekoder
Blå = '\033[94m'  
Cyan = '\033[36m'  
Rød = '\033[91m' 
Grøn = '\033[92m'  
Gul = '\033[93m'  
Magenta = '\033[95m'  
RESET = '\033[0m'  
BOLD = "\033[1m"  

# Opretter et board som en tom liste med 9 pladser, der kan opdateres med enten X eller O.
board = [str(i + 1) for i in range(9)]

"""Nulstiller brættet ved spilstart."""
def ResetBoard():
    global board # Vi bruger boardet globalt i denne funktion.
    board = [str(i + 1) for i in range(9)]  # Nulstil boardet ved spilstart


"""Printer Tic Tac Toe-boardet i konsollen."""
def PrintBoard():
    print(f'{Cyan}-------------')
    for i in range(3):
        row = []
        for j in range(3):
            value = board[i*3 + j]
            if value == 'X':
                row.append(f'{Rød}{value}{RESET}')
            elif value == 'O':
                row.append(f'{Grøn}{value}{RESET}')
            else:
                row.append(f'{RESET}{value}{RESET}')
        print(f'{Cyan}| {RESET}' + f'{Cyan} | {RESET}'.join(row) + f'{Cyan} |{RESET}')
        print(f'{Cyan}-------------{RESET}')


"""Returnerer True, hvis den angivne position er optaget, ellers False."""
def OptagetPladsTjek(position):
    return board[position] in ['X', 'O']


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
    if all(space in ["X", "O"] for space in board):
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
        board[valgtMærke] = str(valgtMærke + 1)
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


""" Denne funktion vælger vores AI's placement ved først at checke om den kan vinde på næste træk.
    Hvis AI'en ikke kan vinde, tjekker den om spilleren kan vinde på næste træk og blokerer det træk 50% af tiden.
    Hvis ingen af de ovenstående er sande, vælger AI'en en tilfældig tom plads."""
def AIMærkePlacering():
    for i in range(9): # Kan jeg vinde på næste træk (AI)?
        if not OptagetPladsTjek(i):
            board[i] = 'O'
            if is_game_over():
                board[i] = str(i + 1)
                return i
            board[i] = str(i + 1)
    for i in range(9): # Kan spilleren vinde på næste træk?
        if not OptagetPladsTjek(i):
            board[i] = 'X'
            if is_game_over(): # Blokerer spilleren 50% af tiden.
                board[i] = str(i + 1)
                if random.random() < 0.5:
                    return i
            board[i] = str(i + 1) 
    TommePladser = [i for i in range(9) if not OptagetPladsTjek(i)] # Vælg en tilfældig tom plads.
    return random.choice(TommePladser)


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
            position = AIMærkePlacering()
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


""" Viser menuen for vores Tic Tac Toe spilregler.
    Derudover håndterer den også spiller input for menuen."""
def SpilleReglersMenu():
    while True:
        print(f"{Blå}{'*' * 20}{RESET}\n{Gul}{BOLD} Spillets regelmenu{RESET}\n{Blå}{'*' * 20}{RESET}")
        print(f"{Cyan}{BOLD}Vælg spiltilstanden du ønsker at se reglerne for:{RESET}{Cyan}\n1. 2 spillere\n2. 1 spiller mod Maskine\n3. 3x3 Tic Tac Toe med flytbare symboler\n4. Tilbage til hovedmenu{RESET}")
        valg = input("Indtast dit valg (1-4): ")
        time.sleep(0.2)
        if not valg.isdigit() or int(valg) < 1 or int(valg) > 4:
            print(f"{Rød}Ugyldigt valg. Indtast venligst et nummer fra 1-4.{RESET}")
        else:
            if valg == "1":
                ReglerClassicPrint()
            elif valg == "2":
                ReglerSpillerVSMaskinePrint()
            elif valg == "3":
                Regler3x3FlytbareSymbolerPrint()
            elif valg == "4":
                break


""" Her håndteres bevægelsen mellem menuer. Så det er muligt at komme tilbage til regelmenuen. efter at have læst reglerne."""
def BevægelseMellemMenuer():
    while True:
        valg = input("Indtast 4 for at gå tilbage til regler menuen: ")
        if valg == "4":
            break
        else:
            print(f"{Rød}Ugyldigt valg. Indtast venligst 4 for at gå tilbage til regel menuen.{RESET}")


""" Printer reglerne for Classic Tic Tac Toe."""
def ReglerClassicPrint():
    print(f"{Blå}{'*' * 34}{RESET}\n{Gul}{BOLD} Reglerne for Classic Tic Tac Toe{RESET}\n{Blå}{'*' * 34}{RESET}")
    print (f"{Cyan}1. Classic Tic Tac Toe spilles på et 3x3 Gitter board.\n2. Spillet spilles af 2 spillere, hvor den ene spiller med X og den anden med O.{RESET}")
    print(f"{Cyan}3. Spillerne skiftes til at placere deres mærker på brættet.\n4. Målet er at få 3 af deres mærker på en vandret, lodret eller diagonal linje.{RESET}")
    print(f"{Cyan}5. Spillet slutter, når en spiller har 3 mærker på en linje, eller der ikke er flere træk tilbage (Uafgjort).{RESET}")
    BevægelseMellemMenuer()

""" Printer reglerne for Tic Tac Toe VS AI."""
def ReglerSpillerVSMaskinePrint():
    print(f"{Blå}{'*' * 34}{RESET}\n{Gul}{BOLD} Reglerne for Tic Tac Toe VS AI{RESET}\n{Blå}{'*' * 34}{RESET}")
    print (f"{Cyan}1. Tic Tac Toe VS AI spilles på et 3x3 Gitter board.\n2. Spillet spilles af 1 spiller mod en AI, hvor spilleren spiller med X og AI'en med O.{RESET}")
    print(f"{Cyan}3. Spilleren starter med at placere deres mærke på brættet.\n4. Målet er at få 3 af deres mærker på en vandret, lodret eller diagonal linje.{RESET}")
    print(f"{Cyan}5. Spillet slutter, når spilleren eller vores AI har 3 mærker på en linje, eller der ikke er flere træk tilbage (Uafgjort).{RESET}")
    BevægelseMellemMenuer()

""" Printer reglerne for Tic Tac Toe med Flytbare Symboler."""
def Regler3x3FlytbareSymbolerPrint():
    print(f"{Blå}{'*' * 48}{RESET}\n{Gul}{BOLD} Reglerne for Tic Tac Toe med Flytbare Symboler{RESET}\n{Blå}{'*' * 48}{RESET}")
    print(f"{Cyan}1. Tic Tac Toe med Flytbare Symboler spilles på et 3x3 Gitter board.\n2. Spillet spilles af 2 spillere, hvor den ene spiller med X og den anden med O.{RESET}")
    print(f"{Cyan}3. Spillerne skiftes til at placere deres mærker på brættet.\n4. Når en spiller har 3 mærker på brættet, kan de flytte et af deres mærker til en tom plads.{RESET}")
    print(f"{Cyan}5. Målet er at få 3 af deres mærker på en vandret, lodret eller diagonal linje.{RESET}")
    print(f"{Cyan}6. Spillet slutter, når en spiller har 3 mærker på en linje, eller der ikke er fundet en vinder efter 46 træk (uafgjort).{RESET}")
    BevægelseMellemMenuer()


"""Velkomstmenu. Her vises spiltilstandene, og spilleren kan vælge en spiltilstand eller se reglerne for spillet samt afslutte det."""
def VelkomstOgSpilValg():
    while True:
        print(f'{Blå}{"*" * 28}{RESET}\n{Gul}{BOLD} Velkommen til Tic Tac Toe!{RESET}\n{Blå}{"*" * 28}{RESET}')
        print(f"{Cyan}{BOLD}Vælg spiltilstand:{RESET}{Cyan}\n1. 2 spillere\n2. 1 spiller mod Maskine\n3. 3x3 Tic Tac Toe med flytbare symboler\n4. Reglerne\n5. Afslut{RESET}")
        GameMode = input("Indtast dit valg (1-5): ")
        time.sleep(0.2)
        if not GameMode.isdigit() or int(GameMode) < 1 or int(GameMode) > 5:
            print(f"{Rød}Ugyldigt valg. Indtast venligst et nummer fra 1-4.{RESET}")
        else:
            return GameMode

""" Starter spillet ved at vælge en spiltilstand."""
while True:
    GameMode = VelkomstOgSpilValg()

    if GameMode == "1":
        StartSpil()
    elif GameMode == "2":
        StartSpilVSMachine()
    elif GameMode == "3":
        StartSpil3FlytbareSymboler()
    elif GameMode == "4": 
        SpilleReglersMenu()
    elif GameMode == "5":
        print("Spillet er afsluttet.")
        break
    else:
        print(f"{Rød}Ugyldigt valg. Indtast venligst et nummer fra 1-5.{RESET}")