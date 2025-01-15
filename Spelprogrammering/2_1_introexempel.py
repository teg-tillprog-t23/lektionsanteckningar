import pygame # importerar pygame för att kunna använda alla saker i det biblioteket

pygame.init() # initialiserar pygames alla moduler
# Vissa moduler (saker som kan användas) kräver att bli initialiserade.
# För att slippa hålla koll på ovilka olika moduler som ska initialiseras så sköter sig allt med pygame.init()

screen = pygame.display.set_mode((1280,720)) # sätter upp skärmen där spelet ska vara
clock = pygame.time.Clock() # skapar en variabel som kan hjälpa till att hålla koll på tiden
running = True

while running: # spel-loopen (jämför med loop() för ESP32)
    # Här loopar vi igenom alla event som har skett som är i kön
    # Ett event är något som sker, till exempel att en knapp klickas på eller att musen rörs
    # Eventen hamnar i en kö (som mail i en inkörg)
    # Det är bra att hantera event i varje frame (varje loop) för att se till att kön inte blir full och event försvinner 
    # (vi kommer att prata mer om olika event)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # om eventet är det som är QUIT (sker när vi klickar bort fönstret)
            running = False # avbryt programmet
    
    screen.fill("purple") # fyller skärmen (som vi ju döpte till screen) med lila
    # detta görs varje frame (loop), tänk som stop motion

    pygame.display.flip() # gör alla uppdateringar som vi har bestämt (tex fyller skärmen med lila)
    clock.tick(60) # avgör FPS (frames per seconds)

pygame.quit() # avslutar programmet när loopen har brutits

