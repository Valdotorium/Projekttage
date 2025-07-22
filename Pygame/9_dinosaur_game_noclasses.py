import pygame
import random
pygame.init()

FPS = 60   
clock = pygame.time.Clock()  
Score = 0  # Beispiel für eine Variable, die den Punktestand speichert

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mein Pygame Spiel")

font = pygame.font.Font("Pygame/src/PixelifySans-Regular.ttf", 24)  # Schriftart von Datei laden und Größe festlegen

player_image = pygame.image.load("Pygame/src/example_image.png")  # Bild laden
obstacle_image = pygame.image.load("Pygame/src/example_image.png")  # Bild für Hindernis laden

player_position = [100, 500] # Startposition des Spielers
player_y_velocity = 0  # Vertikale Geschwindigkeit für Sprünge

obstacle_position = [800, 500]  # Startposition des Hindernisses

def update_obstacle(obstacle_position, Score):
    obstacle_position[0] -= 8  # Hindernis bewegt sich nach links
    if obstacle_position[0] < -100:  # Wenn das Hindernis den Bildschirm verlässt, wird es gelöscht
        obstacle_position[0] = random.randint(800, 1200)  # Neues Hindernis erscheint von rechts an zufälliger Position zwische 800 und 1200
        Score += 1  # Punktestand erhöhen
    return obstacle_position, Score

def move_player(player_position, player_y_velocity):
        #Spieler mit Pfeiltaste bewegen
    if pygame.key.get_pressed()[pygame.K_SPACE] and player_position[1] == 500:
        player_y_velocity = -25
    player_y_velocity += 1  # Schwerkraft
    player_position[1] += player_y_velocity  # Spieler in y-Richtung bewegen
    if player_position[1] > 500:  # Spieler darf nicht unter den Boden fallen
        player_position[1] = 500
        player_y_velocity = 0
    return player_position, player_y_velocity

def collision_check(player_position, obstacle_position):
    player_rect = pygame.Rect(player_position[0], player_position[1], player_image.get_width(), player_image.get_height()) #Rechteck um den Spieler 
    obstacle_rect = pygame.Rect(obstacle_position[0], obstacle_position[1], obstacle_image.get_width(), obstacle_image.get_height()) #Rechteck um das Hindernis
    return player_rect.colliderect(obstacle_rect)

def display_text(text, position): #Funktion, um Text an einer Position anzuzeigen
    score_text = font.render(text, True, (255, 255, 255))  # Text (in weiß) rendern
    screen.blit(score_text, position)  # Text an der angegebenen Position zeichnen

while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen

    #den Punktestand anzeigen
    display_text("Score:" + str(Score), (10, 10))  # den Punktestand anzeigen

    player_position, player_y_velocity = move_player(player_position, player_y_velocity)  # Spieler bewegen

    obstacle_position, Score = update_obstacle(obstacle_position, Score)  # Hindernis aktualisieren

    screen.blit(obstacle_image, obstacle_position)  # Hindernis zeichnen

    screen.blit(player_image, player_position)  #Spieler zeichnen

    if collision_check(player_position, obstacle_position):  # Wenn eine Kollision stattgefunden hat
        display_text("Game Over!", (screen.get_width() // 2 - 50, screen.get_height() // 2 - 20)) #Dann erscheint "Game Over"
        pygame.display.flip()
        pygame.time.delay(2000)  # 2 Sekunden warten, bevor das Spiel beendet
        pygame.quit() # Spiel beenden
        exit()

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