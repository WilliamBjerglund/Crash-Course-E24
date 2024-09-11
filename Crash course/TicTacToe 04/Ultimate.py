"""
Vi vil lave Ultimate Tic Tac Toe med GUI (hvis tiden er der).

Hvad er Ultimate Tic Tac Toe?
- Ultimate Tic Tac Toe er en udvidet version af det klassiske Tic Tac Toe.
- Spillet spilles på ni 3x3-brætter, som sammen udgør et større 3x3-bræt af brætter.
- Målet er at vinde tre små brætter på linje (vandret, lodret eller diagonalt) i det store bræt.
- Ved første træk er der frit "lege" for placering. Spilleren må sætte X i alle felter på alle de små brætter.
- Når en spiller placerer sit mærke i en af de små celler i et af de små brætter, bestemmes modstanderens næste træk.
- Altså placerer jeg et mærke i det midterste board, men i højre top hjørne, så skal modstanderen placere sit næste træk -
    I det øverst højre board (af de mindre boards), men med frit "lege" for placering. indenfor boardet.

# Hvordan vinder man spillet?
- Ultimate Tic Tac Toe vindes ligesom almindeligt Tic Tac Toe. Forskellen er i stedet kun at vinde 1 lille board af 3x3 felter.
    Så skal spilleren vinde 3 af disse små boards på linje (vandret, lodret eller diagonalt) i det store bræt.

# GUI implementering
- Min plan er at implementerer en GUI og evt. et scoring system, hvis tiden er der.
- Denne GUi, vil gøre spillerne kan interagere med spillet visuelt og nemt placere deres mærker.
- Det vil forhåbentligt gøre spillet nemt at følge med i som en der ser på, -
    men også som spiller selv da det er mere kompliceret end almindeligt Tic Tac Toe.
"""
# Import af nødvendige biblioteker
import pygame
from pygame.locals import *

# Funktion til at åbne GUI
def open_gui():
    # Initialisér pygame
    pygame.init()

    # Definér vinduets størrelse (Standard)
    window_size = (1280, 720)
    # Opret vinduet og gør det resizable
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

    # Baggrundsbillede
    backgroundImage = pygame.image.load("Crash course/TicTacToe 04/background.jpg")

    # Kør GUI-loop
    running = True
    while running:
        # Behandl events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:  # Handle window resize event
                window_size = event.size
                window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

        # Opdater vinduet
        pygame.display.update()

    # Luk pygame
    pygame.quit()

# Kald funktionen for at åbne GUI
open_gui()


