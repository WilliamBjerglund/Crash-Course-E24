"""
Reglerne for Ultimate Tic Tac Toe der skal implementeres:
1. Ultimate Tic Tac Toe består af et 3x3 gitter af mindre 3x3 Tic Tac Toe boards.
2. Spilleren skal placere deres symbol (X eller O) på et af de mindre boards.
3. Placeringen af symbolet i et mindre board bestemmer, hvilket mindre board modstanderen skal spille i næste træk.
4. Hvis en spiller vinder et mindre board, tæller det som en plads i det større board.
5. Spillet er vundet, når en spiller har vundet tre mindre boards på stribe (vandret, lodret eller diagonalt) i det større board.
6. Hvis et mindre board allerede er vundet eller fuldt, kan spilleren vælge et hvilket som helst andet mindre board til deres træk.
7. Spillet slutter uafgjort, hvis alle pladser i det større board er fyldt uden en vinder.

README OBS! Dette spil har flere Gamemodes. Ultimate Tic Tac Toe fylder meget i terminal.
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
UltimateBoard = [[' ' for _ in range(9)] for _ in range(9)]

"""Printer Tic Tac Toe-boardet i konsollen."""
def PrintBoard():
    print(f'{Gul}-------------')
    for i in range(3):
        # Printer en række ad gangen med tre elementer pr. række. i farve.
        print(f'{Gul}| {board[i*3]}{Gul} | {board[i*3 + 1]}{Gul} | {board[i*3 + 2]}{Gul} |')
        print(f'{Gul}-------------')

def PrintUltimateBoard():
    for rækker in range(9):
        if rækker % 3 == 0 and rækker != 0:
            print(f'{Gul}---------------------')
        for kolonner in range(9):
            if kolonner % 3 == 0 and kolonner != 0:
                print(f'{Gul}|', end='')
            print(f'{UltimateBoard[rækker][kolonner]}', end='')
        print()



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
        #StartSpil()
        PrintUltimateBoard()
    #elif GameMode == '2':
        #tartSpilVSMachine()
    #elif GameMode == '3':
        #StartSpil3FlytbareSymboler()
    #elif GameMode == '4': 
        #print("Spillet er afsluttet.")
        #break
    #else:
        #print("Ugyldigt valg. Indtast venligst et nummer fra 1-4.")
