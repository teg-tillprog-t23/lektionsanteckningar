# Arv och sprites

Nästa steg blir nu att göra sprites. Här är en liten introduktion till sprites, och till något som heter arv, som behövs för att kunna skapa sprites.

## Arv
När man skapar en klass i Python kan den vara ett barn till en annan klass. Det innebär att den kan ärva attribut och metoder från en annan klass. Det kan vara praktiskt om det finns flera olika klasser osm ska baseras på en klass, antingen en man har skrivit själv eller en som finns inbyggd i någon modul. Se filen "5_2_arv.py" för exempel.

## Sprites
En sprite är i spelprogrammering ett objekt (ofta en bild) som ritas ut på skärmen. Det kan vara en spelare som rör sig, godis som kan ätas eller något annat. Man kan också animera sprites så att de ser ut att till exempel snurra, gå eller blinka. I Pygame finns en massa inbyggd logik för sprites i en modul som heter pygame.sprite. I modulen finns två klasser som vi kommer att använda oss av, och det är pygame.sprite.Sprite och pygame.sprite.Group.