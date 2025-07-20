import pygame
pygame.init()

FPS = 60  
screen_width = 800  
screen_height = 600  
clock = pygame.time.Clock()  

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mein Pygame Spiel")

example_image = pygame.image.load("Pygame/src/example_image.png")  # Bild laden    


while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen

    #Hier kommt die Logik des Spiels rein, z.B. das Zeichnen von Objekten, die Bewegung von Figuren, etc.

    screen.blit(example_image, (0, 0))  # Bild an Position (0,0) zeichnen

    clock.tick(FPS)  
    pygame.display.flip()  # Fenster aktualisieren
    for event in pygame.event.get():  # Wenn das Fenster geschlossen wird, wird das Spiel geschlossen.
        if event.type == pygame.QUIT:  
            pygame.quit()  
            exit()  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Wenn die Escape-Taste gedrückt wird, beendet sich das Spiel.
                pygame.quit()
                exit()