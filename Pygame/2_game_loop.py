import pygame
pygame.init()

FPS = 60  
screen_width = 800 
screen_height = 600  
clock = pygame.time.Clock()


while True: #endlose Wiederholung, da Bedingung immer erfüllt, Game loop

    #Hier kommt die Logik des Spiels rein, z.B. das Zeichnen von Objekten, die Bewegung von Figuren, etc.

    clock.tick(FPS)  # Spielgeschwindigkeit auf FPS begrenzen
    for event in pygame.event.get():  # Wenn das Fenster geschlossen wird, wird das Spiel geschlossen.
        if event.type == pygame.QUIT: 
            pygame.quit()  # Pygame beenden
            exit()  # Programm beenden
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Wenn die Escape-Taste gedrückt wird, beendet sich das Spiel.
                pygame.quit()