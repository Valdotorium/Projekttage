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
class Player(): #neue Klasse für den Spieler, die alle Daten für diesen speichert
    def __init__(self):
        self.image = pygame.image.load("Pygame/src/example_image.png")  # Bild laden
        self.position = [0,0] # Startposition des Spielers

    def update(self):
        if pygame.key.get_pressed()[pygame.K_UP]: # Steuerung des Spielers über Pfeiltasten
            self.position[1] -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]: 
            self.position[1] += 10
        if pygame.key.get_pressed()[pygame.K_LEFT]:  
            self.position[0] -= 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]: 
            self.position[0] += 10

        screen.blit(self.image, self.position)  # Spieler zeichnen
        
player = Player()  # Spieler erstellen

def display_text(text, position): #Funktion, um Text an einer Position anzuzeigen
    score_text = font.render(text, True, (255,255,255))  # Text (in weiß) rendern
    screen.blit(score_text, position)  # Text an der angegebenen Position zeichnen


while True:
    screen.fill((0, 0, 0))  # Fenster schwarz füllen
    
    display_text("Score:" + str(Score), (10, 10))  # den Punktestand anzeigen
 
    player.update() # Position des Spielers aktualisieren

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