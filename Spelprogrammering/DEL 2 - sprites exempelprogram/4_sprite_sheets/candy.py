import pygame
import random

# godisklassen är likadan som det tidigare exemplet "3_kollidera_sprites"

class Candy(pygame.sprite.Sprite): # godisklassen ärver av klassen Sprite från modulen sprite
    def __init__(self):
        super().__init__() # initialiserar förälderklassens attribut och metoder
        self.x = 100
        self.y = 100
        
        self.image = pygame.image.load("candy.png")
        self.rect = self.image.get_rect(topleft = (self.x,self.y)) # ett attribut som är hitbox
        self.size = self.image.get_size()

    def change_position(self, width, height):
        self.x = random.randint(0+self.size[0], width-self.size[0]) # väljer ett nytt random x-värde för positionen
        self.y = random.randint(0+self.size[1], height-self.size[1]) # väljer ett nytt random y-värde för positionen

        self.rect.topleft = (self.x, self.y)


