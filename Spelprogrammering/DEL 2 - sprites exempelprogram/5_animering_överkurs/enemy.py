import pygame

"""HÄR ÄR DET NYTT"""
# fiendeklassen liknar tidigare fiendeklasser vi har haft, men med sprites

class Enemy(pygame.sprite.Sprite): # fiendeklassen ärver av klassen Sprite från modulen sprite
    def __init__(self, x=0, y=0):
        super().__init__() # initialiserar förälderklassens attribut och metoder
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 1
        
        self.image = pygame.image.load("enemy.png") # en fiendebild
        self.rect = self.image.get_rect(topleft = (x,y)) # ett attribut som är hitbox


    def update(self, player): # Det är en jagande fiende som följer efter spelaren
        self.dx = player.x - self.x # sätter riktningen mot spelaren
        self.dy = player.y - self.y # sätter riktningen mot spelaren
            
        if self.dx != 0 or self.dy != 0: # om spelaren rör sig (annars skulle det bli division med 0)
            length = ((self.dx)**2 + (self.dy)**2)**0.5 # beräkna längden på vektorn som bildas med rörelsen
            self.dx = self.dx/length # ser till att längden blir 1 oavsett om vi rör oss diagonalt eller inte
            self.dy = self.dy/length # samma som raden ovan fast för y
                
        self.x += self.dx * self.speed # ändrar spelarens position i x-led enligt hastighet och riktning
        self.y += self.dy * self.speed # ändrar spelarens position i y-led enligt hastighet och riktning
        # Här ser vi till att potitionen för hitboxen också uppdateras när spelaren flyttas
        self.rect.topleft = (self.x, self.y)
    
