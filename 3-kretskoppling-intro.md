# Kretskoppling intro
Vi ska nu börja koppla komponenter till ESP32, först i Wokwi, och senare på riktigt. Vi börjar med att titta på några baskomponenter.

## Kopplingsdäck (breadboard)

Vi har ju vår ESP32 med en massa pins och liknande (vi går igenom mer noga senare). För att kunna koppla kretsar med olika komponenter så använder vi något som kallas kopplingsdäck (breadboard). Breadboarden är kopplad på följande sätt:
[bild på kopplingar i breadboard](https://drive.google.com/file/d/1VpY8Iw3DK0x39SpjXRdX8oZWaAE6hbq-/view?usp=sharing).

Vi har förberett era bradboards så att vi har kopplat strömmen från 3,3V-pinnen till plussidan på breadboarden och GND (ground=jord) till minussidan av breadboarden. Markeringarna med + och - finns för att göra det enklare för oss att koppla kretsarna korrekt. Vi har även kopplat över mellanrummet som finns mellan halvorna av breadboarden så att vi enkelt ska kunna använda hela.

## LED

Vi har enkla LED-lampor som vi kommer att använda oss av i början. De är röda, gröna eller blå. LED är en typ av diod, vilket innebär att den endast fungerar om strömmen går åt rätt håll genom den. Om ni tittar på en LED så har den en lång pinne och en kort. Den långa är plus-pinnen, och ska kopplas till den positiva sidan därifrån strömmen från ESP32 kommer. Den korta pinnen är minus-pinnen och ska kopplas till jord (GND). För att inte skada LED:en när vi sedan kopplar i verkligheten behöver vi även ha en resistor.

## Resistor

En resistor är en komponent som tillför ett motstånd i en elektrisk krets. Resistorer kan ha olika stora motstånd, och de gör att strömmen minskar i en krets så länge spänningen är konstant. Spänningen mäts i Volt (V). Strömmen i Ampere (A) och resistansen i ohm ($\Omega$). Vi behöver ha med en resistor i kretsen för att LED:en inte klarar av en för stor ström.

Vi kan avgöra hur många ohm en resistor är, det vill säga hur starkt motståndet är, genom att titta på färgkodningen. Ni kan använda er av följande [diagram](https://drive.google.com/file/d/1JZhu2TDsmYKSEjUwbutuufWjmNZ0FIKH/view?usp=sharing) för att avgöra resistansen. Vi övar tillsammans på att hitta resistansen för några olika resistorer.

## Välja resistor
Vilken resistor vi väljer beror lite på vilken LED vi använder, och vilken spänning vi har från strömkällan. Vi har ju använt 


