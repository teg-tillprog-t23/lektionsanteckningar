// EXEMPEL 1 OM DIGITAL INPUT
// En LED lyser om knappen hålls intryckt
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

#define LED 2 // Definierar namn på pin till LED
#define BUTTON 3 // Definierar namn på pin till knapp

void setup() {
  Serial.begin(115200); // Sätter överföringshastigheten
  pinMode(LED, OUTPUT); // LED ska vara output
  pinMode(BUTTON, INPUT_PULLUP); // Knappen är input, input_pullup gör att vi undviker flytande pins och inte behöver pullup-resistor
}

void loop() {
  if(digitalRead(BUTTON)==LOW){ // Om knappen är nedtryckt
    digitalWrite(LED,HIGH); // Då ska LED:en lysa
  }
  else{
    digitalWrite(LED,LOW); // Annars ska den vara släckt
  }
}