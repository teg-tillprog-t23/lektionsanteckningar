import pygame

""" HÄR ÄR DET NYTT """
# Om vi tycker att det är rörigt att ha alla klasser i samma fil så kan vi dela upp det
# då kan vi bara sen importera klassen från filen sålänge de ligger i samma mapp
from player import Player


# KONSTANTER
WIDTH = 800
HEIGHT = 600
FPS = 60


# Huvudfunktionen som kör vårt spel
def main():
    pygame.init()

    """HÄR ÄR DET NYTT"""
    # Vi har lagt till lite saker för att se till att det inte laggar
    # Ni behöver inte kunna det utantill
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()

    # Vi skapar ett spelarobjekt, och placerar det mitt på skärmen
    player = Player(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        dt = clock.tick(FPS)

        # Hantera händelser (events)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Uppdatera spelvärlden/logiken
        keys = pygame.key.get_pressed()
        player.update(keys)

        # Rita ut spelvärlden
        screen.fill("black")
        player.draw(screen)

        # Flippa skärmen
        pygame.display.flip()

    pygame.quit()


# HUVUDPROGRAMMET
main()

