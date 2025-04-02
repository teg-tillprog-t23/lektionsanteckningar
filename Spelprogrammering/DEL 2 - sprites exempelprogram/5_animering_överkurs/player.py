import pygame


class Player(pygame.sprite.Sprite): # spelarklassen ärver av klassen Sprite från modulen sprite
    def __init__(self, x=100, y=100):
        super().__init__() # initialiserar förälderklassens attribut och metoder
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 5
        
        """HÄR ÄR DET NYTT"""
        # För att spelaren ska kunna se ut som att den går åt olika håll har vi använt ett sprite sheet (där spriten finns i olika versioner)
        # De olika versionerna finns sedan på olika delar av sprite sheet.
        # Hur stora delarna är varierar, men det är ofta 16*16, 32*32 eller 64*64
        # Ibland finns informationen om hur stora delarna är där man kan ladda ner sprite sheet (tex opengameart)
        # I detta fall är delarna 64*64
        image = pygame.image.load("player.png") # hela sprite sheet
        img_left_1 = image.subsurface((0,0,64,64)) # den del som går åt vänster
        img_left_2 = image.subsurface((0,64,64,64)) # den del som går åt vänster
        img_left_3 = image.subsurface((0,128,64,64)) # den del som går åt vänster
        img_left_4 = image.subsurface((0,192,64,64)) # den del som går åt vänster
        self.images_left = [img_left_1,img_left_2,img_left_3,img_left_4]

        self.img_up = image.subsurface((64,0,64,64)) # den del som går åt höger
        self.img_down = image.subsurface((128,0,64,64)) # den del som går nedåt
        
        img_right_1 = image.subsurface((192,0,64,64)) # den del som går uppåt
        img_right_2 = image.subsurface((192,64,64,64)) # den del som går uppåt
        img_right_3 = image.subsurface((192,128,64,64)) # den del som går uppåt
        img_right_4 = image.subsurface((192,192,64,64)) # den del som går uppåt
        self.images_right = [img_right_1,img_right_2,img_right_3,img_right_4]
        
        # Välj valfri bild att starta med för att initialisera attributet
        self.image = self.img_up

        self.rect = self.image.get_rect(topleft = (x,y)) # ett attribut som är hitbox


    def update(self, keys, walking_state):
        self.dx = 0
        self.dy = 0

        """HÄR ÄR DET NYTT"""
        # Eftersom att spelaren nu inte kan se ut som att den går diagonalt har vi ändrat så att den bara kan gå en riktning i taget
        # Då har vi även tagit bort normaliseringen eftersom att den inte går diagonalt
        if keys[pygame.K_LEFT]:
            self.dx = -1
            self.image = self.images_left[walking_state] # när vi går åt vänster så ska gubben se ut som att den går åt vänster
        elif keys[pygame.K_RIGHT]: # här är det elif istället för if, eftersom det bara kan vara en riktning i taget
            self.dx = 1
            self.image = self.images_right[walking_state] # när vi går åt höger så ska gubben se ut som att den går åt höger
        elif keys[pygame.K_UP]:
            self.dy = -1
            self.image = self.img_up # när vi går uppåt så ska gubben se ut som att den går uppåt
        elif keys[pygame.K_DOWN]:
            self.dy = 1
            self.image = self.img_down # när vi går nedåt så ska gubben se ut som att den går nedåt
            
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        self.rect.topleft = (self.x, self.y)
    
