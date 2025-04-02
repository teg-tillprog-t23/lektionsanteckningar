import pygame
import random


class Candy(pygame.sprite.Sprite): # godisklassen ärver av klassen Sprite från modulen sprite
    def __init__(self):
        super().__init__() # initialiserar förälderklassens attribut och metoder
        self.x = 100
        self.y = 100
        
        self.image = pygame.image.load("candy.png") # godisen ska se ut som en godis, nödvändigt attribut för en sprite
        self.rect = self.image.get_rect(topleft = (self.x,self.y)) # ett attribut som är hitbox, detta är nodvändigt för en sprite
        
        """HÄR ÄR DET NYTT"""
        self.size = self.image.get_size() # såhär kan vi få storleken, så att vi kan se till att spriten inte hamnar utanför skärmen

    """HÄR ÄR DET NYTT"""
    def change_position(self, width, height): # en metod som flyttas godisen till en random plats
        self.x = random.randint(0, width-self.size[0]) # väljer ett nytt random x-värde för positionen
        self.y = random.randint(0, height-self.size[1]) # väljer ett nytt random y-värde för positionen

        self.rect.topleft = (self.x, self.y) # uppdaterar positionen för hitboxen också


