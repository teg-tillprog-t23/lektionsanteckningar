import pygame
import time
from player import Player
from candy import Candy
"""HÄR ÄR DET NYTT"""
from enemy import Enemy # imporrterar fiendeklassen från fiendefilen

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
    candies = pygame.sprite.Group() # skapar en grupp med godisar
    """HÄR ÄR DET NYTT"""
    enemies = pygame.sprite.Group() # skapar en grupp med fiender

    player = Player(WIDTH // 2, HEIGHT // 2)
    players.add(player) 

    """HÄR ÄR DET NYTT"""
    enemy = Enemy() # Skapar ett fiendeobjekt
    enemies.add(enemy) # lägger till den i fiendegruppen

    # skaparr godisar
    for i in range(5):
        candy = Candy()
        candy.change_position(WIDTH,HEIGHT)
        candies.add(candy)


    last_updated_position = 0 # senaste gången godisarna uppdaterades
    last_updated_player = 0
    walking_state = 0
    score = 0
    running = True
    while running:
        dt = clock.tick(FPS)

        # Hantera händelser (events)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Uppdatera spelvärlden/logiken
        keys = pygame.key.get_pressed()

        current_time = time.time() # tar nuvarande tid i loopen

        if current_time - last_updated_player >= 0.1:
            walking_state += 1
            last_updated_player = current_time
            if walking_state == 4:
                walking_state = 0

        players.update(keys, walking_state) # istället för att uppdatera en spelare så uppdaterar vi hela gruppen
        """HÄR ÄR DET NYTT"""
        enemies.update(player) # uppdaterar fienden också

        if  current_time - last_updated_position >= 3: # om det har gått tre sekunder sedan positionen senast ändrades
            last_updated_position = current_time # uppdatera senast ändrad
            for candy in candies: # för varje godis
                candy.change_position(WIDTH, HEIGHT) # ändra positionen


        candies_hit = pygame.sprite.spritecollide(player, candies, True)
        """HÄR ÄR DET NYTT"""
        enemies_hit = pygame.sprite.spritecollide(player,enemies, False) # kollar om spelaren kolliderar med någon fiende, fienden dör inte då
 
        # serr till att räkna poäng och skapa nya godisar när de äts
        for candy in candies_hit:
            score += 1
            print(score)
            candy.change_position(WIDTH, HEIGHT)
            candies.add(candy)
        
        """HÄR ÄR DET NYTT"""
        if enemies_hit: # om någon fiende har krockat med spelaren
            print("Du dog") # skriver ut att man är död
            running = False # avbryter spelloopen

        # Rita ut spelvärlden
        screen.fill("black")

        players.draw(screen) # här ritar vi ut alla spelare i gruppen
        candies.draw(screen) # här ritar vi ut alla godisar i gruppen
        """HÄR ÄR DET NYTT"""
        enemies.draw(screen) # här ritar vi ut alla fiender i gruppen

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET
main()
