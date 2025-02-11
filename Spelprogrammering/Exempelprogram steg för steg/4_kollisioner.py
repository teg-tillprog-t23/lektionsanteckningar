
import pygame # Vi startar ALLTID med att importera bibliotek, tex pygame, random, math
import random
import math

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
        self.dx = 0 # sätter hur x ska ändras
        self.dy = 0 # sätter hur y ska ändras
        self.size = 20
        self.speed = 5 # avgör hastigheten som spelaren rör sig

    # Efter konstruktorn kommer en update-metod som uppdaterar objektets position
    def update(self, keys):
        self.dx = 0 # nollställer dx så att spelaren inte rör sig om inga knappar trycks ner
        self.dy = 0 # nollställer dy så att spelaren inte rör sig om  inga knappar trycks ner

        if keys[pygame.K_LEFT]:
            self.dx = -1
        if keys[pygame.K_RIGHT]:
            self.dx = 1
        if keys[pygame.K_UP]:
            self.dy = -1
        if keys[pygame.K_DOWN]:
            self.dy = 1
        
        if self.dx != 0 or self.dy != 0: # om spelaren rör sig (annars skulle det bli division med 0)
            length = math.sqrt((self.dx)**2 + (self.dy)**2) # beräkna längden på vektorn som bildas med rörelsen
            self.dx = self.dx/length # ser till att längden blir 1 oavsett om vi rör oss diagonalt eller inte
            self.dy = self.dy/length # samma som raden ovan fast för y
        
        self.x += self.dx * self.speed # ändrar spelarens position i x-led enligt hastighet och riktning
        self.y += self.dy * self.speed # ändrar spelarens position i y-led enligt hastighet och riktning


    # Därefter har vi en metod som ritar upp objektet
    def draw(self, screen): # metoden tar in vilken skärrm objektet ska ritas på
        pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)

    """HÄR FINNS DET NYTT"""
    def get_rect(self): # Metoden get_rect returnerar en hitbox för spelaren som används för att avgöra om den har krockat i något
        # Rect(left, top, width, height)
        # left blir x (centerpunkten) minus storleken (radien), samma för top eftersom att en rektangel utgår från högsta vänstra hörnet
        # width och height blir cirkelns diameter
        return pygame.Rect(self.x-self.size, self.y-self.size, self.size*2, self.size*2)
        
    # Efter det kan vi ha andra metoder, till exempel en metod som heter destruct som "förstör" objektet

""" I KLASSEN CANDY FINNS DET NYTT """
class Candy:
    def __init__(self, color):
        self.size = 10
        self.x = random.randint(0+self.size, WIDTH-self.size)
        self.y = random.randint(0+self.size, HEIGHT-self.size)
        self.color = color
        self.is_alive = True # Ett attribut som håller koll på om godisen lever eller inte
    
    def update(self):
        # Här kan vi sedan uppdatera om godiset ska studsa runt eller flytta sig eller något
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    
    def die(self): # En metod för det som ska göras när godisen dör. Det kan vara mer än att bara sätta is_alive, tex att den först blinkar
        self.is_alive = False

    def get_rect(self): # Samma som i player, ger en hitbox för godisen
        return pygame.Rect(self.x-self.size, self.y-self.size, self.size*2, self.size*2)


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
        
        """ HÄR ÄR DET NYTT """
        # Efter det finns plats för att hantera kollissioner

        for candy in candy_list: # För varje godis som finns
            if player.get_rect().colliderect(candy.get_rect()): # om godisen och spelaren kolliderar
                candy.die() # då ska godisen dö
        
        active_candy = [] # en lista för att kunna rensa bort döda godisar
        for candy in candy_list: # för alla godisar
            if candy.is_alive: # om godisen lever
                active_candy.append(candy) # då ska den ligga i den nya listan
        candy_list = active_candy # ändra så att candy_list är den nya listan och bara innehåller levande godisar


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