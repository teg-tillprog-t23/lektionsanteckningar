import pygame

class Player:

    def __init__(self, color, radius, screen):
        self.color = color
        self.radius = radius
        self.screen = screen
        self.x = screen.get_width()/2
        self.y = screen.get_height()/2

    def update(self, keys):
        if keys[pygame.K_w]: # om w är nedtryckt
            self.y -= 30 # ändrar y-värdet så att cirkeln flyttas uppåt
        if keys[pygame.K_s]: # om s är nedtryckt
            self.y += 30 # ändrar y-värdet så att cirkeln flyttas nedåt
        if keys[pygame.K_a]: # om a är nedtryckt
            self.x -= 30  # ändrar x-värdet så att cirkeln flyttas åt vänster
        if keys[pygame.K_d]: # om d är nedtryckt
            self.x += 30  #
        
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # sätter skärmens storlek och sparar den i ett objekt
clock = pygame.time.Clock() # ett klockobjekt som håller koll på tiden
running = True
player_1 = Player("red", 40, screen)

while running:
    for event in pygame.event.get(): # kollar alla event i kön
        if event.type == pygame.QUIT: # om eventet är quit
            running = False # då ska loopen avslutas

    screen.fill("purple") # fyller hela skärmen med lila

    keys = pygame.key.get_pressed() # tar in vilka tangenter som är nedtryckta
    player_1.update(keys)
    
    pygame.display.flip() # uppdaterar skärmen med det vi har ändrat

    clock.tick(60)

pygame.quit()