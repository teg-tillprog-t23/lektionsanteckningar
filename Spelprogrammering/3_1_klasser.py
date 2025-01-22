# Python är ett så kallat objektorienterat språk, där klasser och objekt används för många saker.
# Vi har kort nämnt klasser i programmering 1, och vi kommer nu att gå igenom vad det är,
# några basbegrepp samt hur de används i pygame för att förenkla hanteringen av olika objekt i spel.

# En klass är som en samling eller ritning för ett objekt.
# Klassen kan innehålla olika objekt som har olika attribut.
# Klassen kan också innehålla metoder, som kan ändra eller göra saker med objekt i klassen.

# Till exempel kan vi ha en klass som heter Elev, där ett objekt är en elev.
# Ett attribut i den klassen skulle kunna vara namn eller program eller en lista med kurser eleven läser.
# En metod i klassen skulle kunna vara att ändra namn eller lägga till en kurs.

# Ni har stött på många klasser i Python utan att veta om det, till exempel listor.
# Ni har också stött på metoder, till exempel lista.append() som lägger till ett element i en lista.

# Vi tar ett enkelt exempel på en klass där vi endast skapar klassen.

class Elev:
    def __init__(self, namn, program):
        self.namn = namn
        self.program = program
        self.kurser = []
    
    def skriv_info(self):
        print(f"{self.namn} går {self.program}")


elev_1 = Elev("Alexander", "Teknik")
elev_2 = Elev("Simon", "Natur")

print(elev_1.namn)
print(elev_2.namn)
print(elev_1.program)
print(elev_1)
elev_2.skriv_info()



# Vi kan lägga till attribut

# Vi kan lägga till en konstruktor (__init__-metod)

# Vi kan lägga till metoder