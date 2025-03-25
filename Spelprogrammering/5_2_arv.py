class Person: # Här är en klass som är förälder-klassen som gäller för alla personer

    def __init__(self, namn, ålder): # En person har ett namn och en ålder
        self.namn = namn
        self.ålder = ålder
    
    def skriv_info(self): # Vi har en metod för att presentera personen
        print(f"Detta är {self.namn}, som är {self.ålder} år gammal.")


class Elev(Person): # Här är en klass som är barn till klassen Person, då skrivs Person i parentes efter klassens namn

    # Om vi vill kunna skapa objekt på ett bra sätt som har attributen från klassen person behöver vi ha med samma argument.
    # __init__ för ELev kommer att skriva över den för Person om vi inte ser till att vi tar med det som finns för Person.
    # Vi behöver också se till att kalla __init__ från Person-klassen och skicka med de argument som behövs

    def __init__(self, namn, ålder, klass):
        super().__init__(namn, ålder) # Här kallar vi __init__ från förälderklassen
        self.klass = klass # vu kan också ha helt egna attribut som bara är kopplade till elevklassen

ny_elev = Elev("Felicia","17","T23") # skapar en elev
ny_elev.skriv_info() # vi kan använda metoder från förälderklassen om vi vill

