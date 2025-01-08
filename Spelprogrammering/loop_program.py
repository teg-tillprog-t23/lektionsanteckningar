# Ett loop-program som skriver ut ditt namn
import time

namn = "Felicia"
senast_uppdaterad = time.time()
nuvarande_bokstav = 0

while True:
    print(".", end = "")
    if time.time()-senast_uppdaterad >= 1:
        print(f"Ge mig ett {namn[nuvarande_bokstav]}")
        nuvarande_bokstav += 1
        senast_uppdaterad = time.time()
    
    if nuvarande_bokstav == 7:
        break

print(f"Det blir {namn.upper()}")
