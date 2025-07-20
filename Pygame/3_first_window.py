import pygame
pygame.init()

FPS = 60  
screen_width = 800  
screen_height = 600  
clock = pygame.time.Clock()  

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mein Pygame Spiel")

#----

while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen

    #----

    clock.tick(FPS)  
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()  
            exit()  




