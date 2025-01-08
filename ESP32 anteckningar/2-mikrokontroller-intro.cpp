// Vad är ESP32?


/* ESP32 är en mikrokontroller. 

En mikrokontroller är en liten dator på ett chip som kan programmeras för 
att utföra specifika uppgifter. 
Den innehåller en processor, minne och in- och utgångar för att interagera 
med andra komponenter som sensorer, motorer eller displayer. 
Mikrokontrollers används för att styra och automatisera enkla elektroniska 
system.
De är mycket energieffektiva och används ofta i inbäddade system där de 
arbetar självständigt utan behov av en större dator. 

*/

/*
Användningsområden för mikrokontrollers i verkligheten:

Smarta hem:
Styrning av ljus, temperatur och andra smarta apparater via Wi-Fi/Bluetooth.

Hälsovård:
Bärbara hälsomonitorer som spårar vitala parametrar som hjärtfrekvens, syresättning, etc.
Integreras i medicinska apparater för att övervaka patienter och ge larm vid avvikelser.

Robotik:
Styrning av motorer, sensorer och kommunikation i robotar.

IoT-projekt:
Sensorer kopplade till internet som samlar in data och skickar den till molnet för analys.
Exempel: Vädertationssensorer, smarta parkeringslösningar, uppkopplade jordbrukssystem.

Säkerhetssystem:
Används i övervakningssystem, som kameror, larm och tillträdeskontroller.
Kan användas för att upptäcka rörelse, brand, gasläckage etc. och larma.

Miljöövervakning:
Sensorer för att övervaka luftkvalitet, vattennivåer, temperatur och andra miljöfaktorer.
Data kan användas för att varna om miljöförhållanden förändras.

*/

/*STARTKOD I WOKWI:

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Hello, ESP32-S2!");
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(10); // this speeds up the simulation
}

En anpassad typ av kod, med C++ -syntax

Ta reda på: vad betyder Serial.begin(115200);?

*/

// Serial: en pinne som går mellan 0/1

// Serial.begin: sätter hastigheten

// Serial.print
/* använder vi mest för att debugga */

// delay

//loop() körs om och om igen "av sig själv". 
// Det är inte en oändlig loop som vi är vana att konstruera den. 
//Vi behöver globala variabler för att hålla states mellan varven.

// I ett större projekt så försöker man ändå modularisera - men i mindre projekt och med begränsade resurser så är det ett pragmatiskt tillvägagångssätt.


// Dokumentation för c++ för mikrokontrollers (arduino)