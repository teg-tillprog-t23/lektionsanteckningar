// EXEMPEL 2 OM ANALOG OUTPUT
// Ett program som låter en LED stiga i ljusstyrka, sedan släckas, sedan stiga igen osv.
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

const int LED_PIN = 5; // vilken pin LED:en ska vara

const int pwmFrequency = 5000; // Frekvens för PWM, 5000 är ett bra värde. Reglerar hur ofta vi har pulser.
const int pwmResolution = 8; // Upplösning för PWM, 8 är ett pra värde. Reglerar hur många steg vi kan ha i duty cycle (pulskvot). Här kommer vi att få steg mellan 0-255.
int brightness = 0; // Start-ljusstyrka

void setup() {
  Serial.begin(115200);
  ledcAttach(LED_PIN, pwmFrequency, pwmResolution); // Kopplar frekvens och upplösning till rätt pin

}

void loop() {
    ledcWrite(LED_PIN, brightness); // SKriver till LED:en den ljusstyrka vi är på
    delay(10);
    brightness += 1; // Lägger på 1 på ljusstyrkans värde
    if(brightness == 255){ // Om vi har nått högsta ljusstyrka
      brightness = 0; // Ställ tillbaka ljusstyrkan till 0
    } 
}