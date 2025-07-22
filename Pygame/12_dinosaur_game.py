import pygame
import random
pygame.init()

FPS = 60  
screen_width = 800  
screen_height = 600  
clock = pygame.time.Clock()  
Score = 0  # Beispiel für eine Variable, die den Punktestand speichert

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mein Pygame Spiel")

font = pygame.font.Font("Pygame/src/PixelifySans-Regular.ttf", 24)  # Schriftart von Datei laden und Größe festlegen
class Player(): #neue Klasse für den Spieler, die alle Daten für diesen speichert
    def __init__(self):
        self.image = pygame.image.load("Pygame/src/example_image.png")  # Bild laden
        self.position = [100,0] # Startposition des Spielers
        self.y_velocity = 0  # Vertikale Geschwindigkeit für Sprünge
        
    def update(self):
        self.rect = self.image.get_rect(topleft=self.position)  # Rechteck für Kollisionen

        self.y_velocity += 1  # Schwerkraft
        self.position[1] += self.y_velocity  # Spieler in y-Richtung bewegen
        if self.rect.bottom > screen_height:  # Spieler darf nicht unter den Boden fallen
            self.rect.bottom = screen_height
            self.y_velocity = 0
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.rect.bottom == screen_height:
            self.y_velocity = -25 #Sprung: Wird space gedrückt, springt der Spieler nach oben

        screen.blit(self.image, self.rect)  # Spieler zeichnen, an der Position des Rechtecks

class Obstacle():  # Klasse für Hindernisse
    def __init__(self):
        self.image = pygame.image.load("Pygame/src/example_image.png")
        self.position = [800,500]  # Beispielposition
        self.rect = self.image.get_rect(topleft=self.position)  # Rechteck für das Hindernis
        self.collision = False  # Variable, um Kollisionen zu erkennen

    def update(self, Score):
        self.position[0] -= 8 # Hindernis bewegt sich nach links
        if self.position[0] < -100:  # Wenn das Hindernis den Bildschirm verlässt, wird es gelöscht
            self.position[0] = random.randint(800, 1200)  # Neues Hindernis erscheint von rechts an zufälliger Position zwische 800 und 1200
            Score += 1  # Punktestand erhöhen
        self.rect.topleft = self.position

        screen.blit(self.image, self.rect) # Hindernis zeichnen

        if self.rect.colliderect(player.rect):  # Falls sich das Hindernis und Player überschneiden:
            self.collision = True # findet eine Kollision statt
        return Score
        
player = Player()  # Spieler erstellen
obstacle = Obstacle()  # Hindernis erstellen

def display_text(text, position): #Funktion, um Text an einer Position anzuzeigen
    score_text = font.render(text, True, (255,255,255))  # Text (in weiß) rendern
    screen.blit(score_text, position)  # Text an der angegebenen Position zeichnen

while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen
    
    display_text("Score:" + str(Score), (10, 10))  # den Punktestand anzeigen
 
    player.update() # Position des Spielers aktualisieren
    Score = obstacle.update(Score)  # Hindernis aktualisieren

    if obstacle.collision:  # Wenn eine Kollision stattgefunden hat
        display_text("Game Over!", (screen_width // 2 - 50, screen_height // 2 - 20)) #"Game Over!" anzeigen
        pygame.display.flip()  # Bildschirm aktualisieren
        pygame.time.delay(2000)  # 2 Sekunden warten, bevor das Spiel beendet wird
        exit() # Spiel beenden
    
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