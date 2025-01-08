// EXEMPEL 3 OM ANALOG OUTPUT
// Ett program som låter en LED andas, dvs stiga långsamt i ljusstyrka och sedan sjunka och sedan stiga osv.
// I exemplet används delay för att kontrollera hur snabbt LED:en andas.
// Exemplet motsvarar C-nivå. Den exakta nivån beror som alltid på programmets struktur, variabelnamn och liknande.

#include <Arduino.h>

const int LED_PIN = 5; // vilken pin LED:en ska vara

const int pwmFrequency = 5000; // Frekvens för PWM, 5000 är ett bra värde. Reglerar hur ofta vi har pulser.
const int pwmResolution = 8; // Upplösning för PWM, 8 är ett pra värde. Reglerar hur många steg vi kan ha i duty cycle (pulskvot). Här kommer vi att få steg mellan 0-255.
int brightness = 0; // Start-ljusstyrka
bool goingUp = true; // En variabel som håller koll på om vi är påväg upp eller ner i ljusstyrka
int breathDelay = 20; // Reglerar hur lång tid det tar att andas, tiden att vänta medan värdet ändras

void setup() {
  Serial.begin(115200);
  ledcAttach(LED_PIN, pwmFrequency, pwmResolution); // Kopplar frekvens och upplösning till rätt pin

}

void loop() {
    ledcWrite(LED_PIN, brightness); // Skriver till LED:en den ljusstyrka vi är på
    if(goingUp){ // Om ljusstyrkan är påväg upp
        brightness += 1; // Lägger på 1 på ljusstyrkans värde
    }
    else if(!goingUp){ // Om ljusstyrkan är påväg ner
        brightness -= 1; // Tar bort 1 från ljusstyrkans värde
    }
    
    if(brightness == 255){ // Om vi har nått högsta ljusstyrka
      goingUp = false; // Nu ska vi vara påväg ner
    } 

    else if(brightness == 0){ // Om vi har nått lägsta ljusstyrka
        goingUp = true; // Nu ska vi vara påväg upp
    }
    delay(breathDelay); // Vänta den tid vi vill vänta
}