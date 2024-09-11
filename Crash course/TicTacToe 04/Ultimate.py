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
        backgroundScaled = pygame.transform.scale(backgroundImage, window_size)
        window.blit(backgroundScaled, (0, 0))
        # Opdater vinduet
        pygame.display.update()
    # Luk pygame
    pygame.quit()


# Kald funktionen for at åbne GUI
open_gui()


