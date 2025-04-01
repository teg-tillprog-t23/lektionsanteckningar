import pygame
import time
from player import Player
"""HÄR ÄR DET NYTT"""
from candy import Candy # importerar godisklassen från godisfilen

# KONSTANTER
WIDTH = 800
HEIGHT = 600
FPS = 60


# Huvudfunktionen som kör vårt spel
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()

    players = pygame.sprite.Group() # här skapar vi en grupp med sprites som är spelare
    """HÄR ÄR DET NYTT"""
    candies = pygame.sprite.Group() # här skapar vi en grupp för godisar

    player = Player(WIDTH // 2, HEIGHT // 2) # vi skapar ett spelarobjekt som vanligt
    players.add(player) # här lägger vi till vår spelare i gruppen, just i det här spelet har vi bara en

    """HÄR ÄR DET NYTT"""
    for i in range(5): # här skapas fem godisar
        candy = Candy() # skapar godisobjekt
        candy.change_position(WIDTH,HEIGHT) # gör att den får en random position
        candies.add(candy) # lägger till i godisgruppen

    """HÄR ÄR DET NYTT"""
    last_updated_position = 0 # senaste gången godisarna uppdaterades
    score = 0 # räknar poäng (ett för varje äten godis)
    running = True
    while running:
        dt = clock.tick(FPS)

        # Hantera händelser (events)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Uppdatera spelvärlden/logiken
        keys = pygame.key.get_pressed()

        players.update(keys) # istället för att uppdatera en spelare så uppdaterar vi hela gruppen

        """HÄR ÄR DET NYTT"""
        current_time = time.time() # tar nuvarande tid i loopen

        if  current_time - last_updated_position >= 3: # om det har gått tre sekunder sedan positionen senast ändrades
            last_updated_position = current_time # uppdatera senast ändrad
            for candy in candies: # för varje godis i godisgruppen
                candy.change_position(WIDTH, HEIGHT) # ändra positionen

        """HÄR ÄR DET NYTT"""
        # Här kollar vi kollision mellan en sprite och en grupp
        # Vi kollar om spelaren har kolliderat i någon godis
        # Alla godisar som har kolliderat hamnar i listan candies_hit
        # Argumentet True står för att godisen ska dö om den kolliderar, den tas då bort från gruppen
        candies_hit = pygame.sprite.spritecollide(player, candies, True)
 
        # Vi kan använda listan med ätna godisar till olika saker, tex räkna poäng
        for candy in candies_hit:
            score += 1
            print(score)
            # gör så att det dyker upp en ny godis när en dör
            candy.change_position(WIDTH, HEIGHT) # den nya godisen är egentligen en gammal som byter plats
            candies.add(candy) # den nya godisen måste läggas till i gruppen

        # Rita ut spelvärlden
        screen.fill("black")

        players.draw(screen) # här ritar vi ut alla spelare i gruppen
        """HÄR ÄR DET NYTT"""
        candies.draw(screen) # här ritar vi ut alla godisar i gruppen

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET
main()
