// EXEMPEL 4 OM ANALOG OUTPUT
// Ett program som låter en LED lysa i olika ljusstyrka beroende på potentiometer input.
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

#define LED_PIN 5 // vilken pin LED:en ska vara
#define pot_PIN 3 // vilken pin potentiometern ska vara


const int pwmFrequency = 5000; // Frekvens för PWM, 5000 är ett bra värde. Reglerar hur ofta vi har pulser.
const int pwmResolution = 8; // Upplösning för PWM, 8 är ett pra värde. Reglerar hur många steg vi kan ha i duty cycle (pulskvot). Här kommer vi att få steg mellan 0-255.
int brightness = 0; // Startvärde för ljusstyrka
int potValue = 0; // Variabel för att lagra värdet som läses från potentiometern

void setup() {
  Serial.begin(115200);
  pinMode(pot_PIN, INPUT); // vilken slags pin potentiometern ska vara
  ledcAttach(LED_PIN, pwmFrequency, pwmResolution); // Kopplar frekvens och upplösning till rätt pin
  analogReadResolution(12); // Ser till att upplösningen för analogRead stämmer överrens med mikrokontrollern
}

void loop() {
    potValue = analogRead(pot_PIN); // Läser av värdet från potentiometern
    brightness = map(potValue, 0, 4095, 0, 255); // Skalar om värdet från potentiometern till ett värde mellan 0-255
    ledcWrite(LED_PIN, brightness); // Skriver styrkan till LED:en
    delay(10); // Snabbar upp det, genom att köra loop lagom ofta, behöver ej vara med
}