# Ett loop-program som skriver ut ditt namn

"""Detta program är skrivet utifrån att vi inte vill pausa programmet.
Tänk millis() istället för delay(). Vi vill att loopen ska fortsätta köra hela tiden
så att programmet inte avbryts och väntar. Risken om det vore ett spel är annars att
vi inte hela tiden känner av efter exempelvis knapptryck. Det skulle göra det mycket
frustrerande att spela spelet och till exempel försöka styra en gubbe"""

import time # importerar modulen time

namn = "Felicia"
senast_uppdaterad = time.time() # Håller koll på när vi senast skrev ut en bokstav
nuvarande_bokstav = 0 # Håller koll på vilken bokstav som ska skrivas ut

while True:
    #print(".", end = "") #Används endast för att visa att loopen körs hela tiden, inte bara när en bokstav skrivs ut
    if time.time()-senast_uppdaterad >= 1: # Om det har gått 1 sekund sedan senaste uppdateringen
        print(f"Ge mig ett {namn[nuvarande_bokstav]}") # Skriver ut den nuvarande bokstaven
        nuvarande_bokstav += 1
        senast_uppdaterad = time.time() # Uppdaterar när vi senast skrev ut en bokstav
    
    if nuvarande_bokstav == len(namn): # Om vi har kommit till slutet av ordet
        break # Då ska programmet sluta

print(f"Det blir {namn.upper()}")
