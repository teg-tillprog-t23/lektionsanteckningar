import pygame
# spelarklassen är likadan som i tidigare exemplet (2_första riktiga spriten)

class Player(pygame.sprite.Sprite): # spelarklassen ärver av klassen Sprite från modulen sprite
    def __init__(self, x=100, y=100):
        super().__init__() # initialiserar förälderklassens attribut och metoder
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 5
        
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect(topleft = (x,y)) # ett attribut som är hitbox


    def update(self, keys):
        self.dx = 0
        self.dy = 0

        if keys[pygame.K_LEFT]:
            self.dx = -1
        if keys[pygame.K_RIGHT]:
            self.dx = 1
        if keys[pygame.K_UP]:
            self.dy = -1
        if keys[pygame.K_DOWN]:
            self.dy = 1
            
        if self.dx != 0 or self.dy != 0:
            length = (self.dx ** 2 + self.dy ** 2) ** 0.5
            self.dx = self.dx/length
            self.dy = self.dy/length
            
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        self.rect.topleft = (self.x, self.y)
    
