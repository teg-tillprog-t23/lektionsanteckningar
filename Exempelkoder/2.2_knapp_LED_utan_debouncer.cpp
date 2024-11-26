// EXEMPEL 2 OM DIGITAL INPUT
// En LED som kan tändas och släckas med en knapp.
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

const int BUTTON_PIN = 10; // Sätter vilken pin knappen ska vara på
const int LED_PIN = 12; // sätter vilken pin LED:en ska vara på

int buttonState = HIGH; // sätter state för knappen i början, den är inte intryckt
int ledState = LOW; // sätter state för LED:en i början

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT_PULLUP); // sätter vilken typ av pin den ska vara
  pinMode(LED_PIN, OUTPUT); // sätter vilken typ av pin den ska vara
}

void loop() {
  int reading = digitalRead(BUTTON_PIN); // läser av om knappen är HIGH eller LOW varje loop
  
  if (reading!=buttonState) { // tittar om något har ändrats med knappen, om den inte är samma som innan
    buttonState = reading; // då ändrar vi buttonState så att den är som den nya

    if (buttonState==LOW) { // om knappen intryckt
      ledState = !ledState; // ändra LED:en
      digitalWrite(LED_PIN, ledState); // ser till att LED:en ändras på riktigt
    }
    
  }

}