# I denna fil finns en helt vanlig spelar-klass
# Den är mycket lik det vi har skrivit förut, bara att den använder en bild för spelaren istället

import pygame
import math

class Player: # En klass för spelare
    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        self.dx = 0 # sätter hur x ska ändras
        self.dy = 0 # sätter hur y ska ändras

        """HÄR ÄR DET NYTT"""
        # Spelaren har nu ett attribut som är self.image, som anger vilken bild som ska representera spelaren
        # För att det ska fungera så måste vägen till bildfilen leda rätt, och hur den gör det beror på vilken mapp du är inne i
        # Om du i VSCode har öppnat endast den mappen som du har dina filer i (både kod och bild) så kommer det att fungera
        # att endast skriva kodnamnet.
        # Bra om bilden är png, då dessa ofta kan sakna bakgrund (ni kanske minns från webbutvecklingen?)
        # Bra tips är att ta från Open game art

        self.image = pygame.image.load("player.png")
        self.size = self.image.get_size() # spelarens storlek utgår ifrån bildens storlek

        self.is_alive = True
        self.speed = 5

    def update(self, keys): # Uppdaterar spelarens position utifrån nedtryckta tangenter
        self.dx = 0
        self.dy = 0
        if self.is_alive:
            if keys[pygame.K_LEFT]:
                self.dx = -1
            if keys[pygame.K_RIGHT]:
                self.dx = 1
            if keys[pygame.K_UP]:
                self.dy = -1
            if keys[pygame.K_DOWN]:
                self.dy = 1
            
            if self.dx != 0 or self.dy != 0:
                length = math.sqrt((self.dx)**2 + (self.dy)**2)
                self.dx = self.dx/length
                self.dy = self.dy/length
            
            self.x += self.dx * self.speed
            self.y += self.dy * self.speed

    """HÄR ÄR DET NYTT"""
    def draw(self, screen):
        # Istället för att rita en form så ritar vi ut bilden som en yta (surface) ovanpå en annan yta (surface)
        # Första argumentet är källan (vår self.image) och andra argumentet är var på skärmen den ska vara
        # screen som står i början är vår stora skärm som vi skapar först i huvudfunktionen och som skickas in som parameter till metoden
        screen.blit(self.image, (self.x,self.y))

    def get_rect(self):
        return pygame.Rect(self.x-self.size, self.y-self.size, self.size*2, self.size*2)