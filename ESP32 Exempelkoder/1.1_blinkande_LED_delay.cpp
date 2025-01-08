// EXEMPEL 1 OM DIGITAL OUTPUT
// En LED som blinkar jämnt med 1 sekund mellanrum.
// I detta exempel används delay() för att reglera hur snabbt LED:en blinkar.
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

#define LED 2 // Definierar att pin 2 ska kallas LED

void setup() {
  Serial.begin(115200); // Fixar med uppladdningshastighet
  pinMode(LED, OUTPUT); // Sätter pin 2 till output
}

void loop() {
  digitalWrite(LED, HIGH); // digital = hög eller låg, hög = LED:en lyser
  Serial.println("LED is on"); // syns i terminalen, kan användas som felsökning
  delay(1000);
  digitalWrite(LED, LOW);
  Serial.println("LED is off");
  delay(1000);
}