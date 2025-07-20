import pygame
pygame.init()

FPS = 60  
screen_width = 800  
screen_height = 600  
clock = pygame.time.Clock()  
Score = 0  # Beispiel für eine Variable, die den Punktestand speichert

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mein Pygame Spiel")

font = pygame.font.Font("Pygame/src/PixelifySans-Regular.ttf", 24)  # Schriftart von Datei laden und Größe festlegen

player_image = pygame.image.load("Pygame/src/example_image.png")  # Bild laden

player_position = [0, 0] # Startposition des Spielers

#Funktionen für das Spiel definieren:
def player_controls(player_position): #Funktion, um den Spieler zu bewegen
    if pygame.key.get_pressed()[pygame.K_UP]:
        player_position[1] -= 10
    if pygame.key.get_pressed()[pygame.K_DOWN]: 
        player_position[1] += 10
    if pygame.key.get_pressed()[pygame.K_LEFT]:  
        player_position[0] -= 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]: 
        player_position[0] += 10
    return player_position

def display_text(text, position): #Funktion, um Text an einer Position anzuzeigen
    score_text = font.render(text, True, (255,255,255))  # Text (in weiß) rendern
    screen.blit(score_text, position)  # Text an der angegebenen Position zeichnen


while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen

    #Hier kommt die Logik des Spiels rein, z.B. das Zeichnen von Objekten, die Bewegung von Figuren, etc.
    screen.blit(player_image, player_position)  #Spieler zeichnen
    
    display_text("Score:" + str(Score), (10, 10))  # den Punktestand anzeigen
 
    player_position = player_controls(player_position) # Position des Spielers aktualisieren

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