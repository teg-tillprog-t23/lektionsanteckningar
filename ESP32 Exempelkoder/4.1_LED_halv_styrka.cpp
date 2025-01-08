// EXEMPEL 1 OM ANALOG OUTPUT
// Ett program som låter en LED lysa i halv ljusstyrka
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

const int LED_PIN = 5; // vilken pin LED:en ska vara

const int pwmFrequency = 5000; // Frekvens för PWM, 5000 är ett bra värde. Reglerar hur ofta vi har pulser.
const int pwmResolution = 8; // Upplösning för PWM, 8 är ett pra värde. Reglerar hur många steg vi kan ha i duty cycle (pulskvot). Här kommer vi att få steg mellan 0-255.
int brightness = 127; // Hälften av 255, för att LED:en ska lysa med halv ljusstyrka.

void setup() {
  Serial.begin(115200);
  ledcAttach(LED_PIN, pwmFrequency, pwmResolution); // Kopplar frekvens och upplösning till rätt pin

}

void loop() {
    ledcWrite(LED_PIN, brightness); // Skriver styrkan till LED:en
    delay(10); // Snabbar upp det, genom att köra loop lagom ofta, behöver ej vara med
}