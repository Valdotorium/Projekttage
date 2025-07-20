import pygame
pygame.init()

FPS = 60  
screen_width = 800  
screen_height = 600  
clock = pygame.time.Clock()  

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mein Pygame Spiel")

player_image = pygame.image.load("Pygame/src/example_image.png")  # Bild laden

player_position = [0, 0] # Startposition des Spielers



while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen

    #Hier kommt die Logik des Spiels rein, z.B. das Zeichnen von Objekten, die Bewegung von Figuren, etc.

    screen.blit(player_image, (200, 200))  #example_image zeichnen

    clock.tick(FPS)  
    pygame.display.flip()  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            exit()  
        if event.type == pygame.KEYDOWN: # Wenn das Fenster geschlossen wird, wird das Spiel geschlossen.
            if event.key == pygame.K_ESCAPE: # Wenn die Escape-Taste gedrückt wird, beendet sich das Spiel.
                pygame.quit()
                exit()
    #Spieler mit Pfeiltaste bewegen
    #solange eine Taste gedrückt wird, wird die Position des Spielers verändert
    if pygame.key.get_pressed()[pygame.K_UP]:
        player_position[1] -= 10
    if pygame.key.get_pressed()[pygame.K_DOWN]: 
        player_position[1] += 10
    if pygame.key.get_pressed()[pygame.K_LEFT]:  
        player_position[0] -= 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]: 
        player_position[0] += 10