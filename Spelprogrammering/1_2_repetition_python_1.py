# Skriv ett program som utifrån en mening kan plocka ut alla ord som har fler än 3 vokaler. 
# Programmet ska sedan skriva ut de orden på en rad efter varandra, med radbrytning mellan

# Programmet ska ha en funktion som tar in meningen som parameter och 
# returnerar en lista med de ord som ska skrivas ut

# Det ska finnas en huvudfunktion som hanterar input och output
# Det enda som ska hända när programmet körs är att huvudfunktionen kallas

# Inga globala variabler får finnas

def kolla_mening(mening):
    vokaler = ("a", "o", "u", "å", "e", "i", "y", "ä", "ö")
    lista_med_ord = []
    ord_i_mening = mening.split()
    for ordet in ord_i_mening:
        antal_vokaler = 0
        for bokstav in ordet:
            if bokstav.lower() in vokaler:
                antal_vokaler += 1
        if antal_vokaler > 3:
            lista_med_ord.append(ordet)
    
    return lista_med_ord

def main():
    mening = input("Skriv in din mening: ")
    lista_att_skriva = kolla_mening(mening)
    for element in lista_att_skriva:
        print(element)

main()

