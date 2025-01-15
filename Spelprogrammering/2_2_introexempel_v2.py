import pygame # importerar biblioteket pygame

pygame.init() # initialiserar moduler
screen = pygame.display.set_mode((1280, 720)) # sätter skärmens storlek och sparar den i ett objekt
clock = pygame.time.Clock() # ett klockobjekt som håller koll på tiden
running = True
dt = 0 # delta_time, används för att se till att spelet går lika snabbt oberoende av FPS, håller koll på skillnaden mellan frames ungefär

# håller koll på en spelares position
# skapar en vektor med ett x och ett y-värde
# vi kommer att göra detta på ett lite annat sätt i framtiden (vi behöver bara gå igenom klasser ordentligt först)
# spelaren startar i mitten av skärmen
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get(): # kollar alla event i kön
        if event.type == pygame.QUIT: # om eventet är quit
            running = False # då ska loopen avslutas

    screen.fill("purple") # fyller hela skärmen med lila


    pygame.draw.circle(screen, "red", player_pos, 40) # ritar en cirkel
    # argumenten är: yta, färg, position (center), radie

    keys = pygame.key.get_pressed() # tar in vilka tangenter som är nedtryckta
    if keys[pygame.K_w]: # om w är nedtryckt
        player_pos.y -= 300 * dt # ändrar y-värdet så att cirkeln flyttas uppåt
    if keys[pygame.K_s]: # om s är nedtryckt
        player_pos.y += 300 * dt # ändrar y-värdet så att cirkeln flyttas nedåt
    if keys[pygame.K_a]: # om a är nedtryckt
        player_pos.x -= 300 * dt # ändrar x-värdet så att cirkeln flyttas åt vänster
    if keys[pygame.K_d]: # om d är nedtryckt
        player_pos.x += 300 * dt # ändrar x-värdet så att cirkeln flyttas åt höger
    # hur mycket cirkeln ändras beror av delta time för att FPS inte ska spela någon roll

    pygame.display.flip() # uppdaterar skärmen med det vi har ändrat

    dt = clock.tick(60) / 1000 # håller koll på delta time som beror av FPS
    # clock.tick() ger millisekunder

pygame.quit()