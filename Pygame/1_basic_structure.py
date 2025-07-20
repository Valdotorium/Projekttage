#einfacher Aufbau eines Pygame-Programms:
#zu Beginn wird pygame importiert und initialisiert.

import pygame
pygame.init()

#dann müssen Funktionen und Variablen definiert werden, die das Spiel steuern

FPS = 60  # Frames per second, die das Spiel laufen soll
screen_width = 800  # Breite des Fensters
screen_height = 600  # Höhe des Fensters
clock = pygame.time.Clock()  # Uhr, um das Spiel mit der in FPS definierten Geschwindigkeit laufen zu lassen.

#danach folgt der sogenannte "game loop", der bei jedem Frame aufgerufen wird, und alle weiteren Abläufe im Spiel enthält

