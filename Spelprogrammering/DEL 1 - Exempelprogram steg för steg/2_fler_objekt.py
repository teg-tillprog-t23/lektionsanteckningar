
import pygame # Vi startar ALLTID med att importera bibliotek, tex pygame, random, math
import random

# Här har vi basvariabler, det är okej att de är globala
# Här har vi med skärmens bredd, höjd och FPS
WIDTH = 800
HEIGHT = 600
FPS = 60

# Efter det kommer klasser, vi kan ha fler olika klasser om vi har fler olika typer av objekt
class Player:
    # klassen ska starta med en konstruktor, en __init__ metod
    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        self.size = 20

    # Efter konstruktorn kommer en update-metod som uppdaterar objektets position
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2

    # Därefter har vi en metod som ritar upp objektet
    def draw(self, screen): # metoden tar in vilken skärrm objektet ska ritas på
        pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)
        
    # Efter det kan vi ha andra metoder, till exempel en metod som heter destruct som "förstör" objektet

class Candy:
    def __init__(self, color):
        self.size = 10
        self.x = random.randint(0+self.size, WIDTH-self.size)
        self.y = random.randint(0+self.size, HEIGHT-self.size)
        self.color = color
    
    def update(self):
        # Här kan vi sedan uppdatera om godiset ska studsa runt eller flytta sig eller något
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


# Efter klasserna har vi funktioner, vi kan ha fler funktioner än main om vi vill

# Sist av funktionerna har vi vår huvudfunktion, som sköter spelet
def main():
    # Det första som händer i vårt spel är en "setup" alltså ett antal saker som görs för att förbereda för uppstart
    pygame.init() # Det första är att initiera moduler i pygame
    screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Sedan definieras vår skärm som spelet ska ritas på
    clock = pygame.time.Clock() # Och sen sätter vi upp vår klocka som hjälper oss att hålla tiden

    #Vi skapar även de objekt som behöver skapas
    player = Player()
    color_list = ["gold", "purple", "green"]
    candy_list = []
    for i in range(5):
        candy_list.append(Candy(random.choice(color_list)))
    
    running = True # Det sista som händer innan spelloopen är att running = True
    
    while running:
        # Det första som händer i spelloopen är att klockan tickar och att vi sparar hur länge sen det var den tickade
        dt = clock.tick(FPS)
    
        # Därefter hanterar vi händelser (events)
        for evt in pygame.event.get():
            if evt.type==pygame.QUIT:
                running = False

        # Sedan uppdatera spelvärlden med alla objekt
        keys = pygame.key.get_pressed()
        player.update(keys)
        
        # Efter det finns plats för att hantera kollissioner, men det pratar vi noggrant om längre fram

        # Sedan ritar vi ut spelvärlden
        screen.fill("black")
        player.draw(screen)
        for object in candy_list:
            object.draw(screen)
       
        # Till sist flippar vi skärmen (ser till att saker och ting faktiskt hamnar på skärmen)
        pygame.display.flip()

    # Efter spelloopen behöver vi avsluta pygame
    pygame.quit()

# Main körs
main()