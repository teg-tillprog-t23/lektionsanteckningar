#include <Arduino.h>

const int BUTTON_PIN = 10; // Sätter vilken pin knappen ska vara på
const int LED_PIN = 12; // sätter vilken pin LED:en ska vara på

int buttonState = HIGH; // sätter state för knappen i början
int ledState = LOW; // sätter state för LED:en i början

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT_PULLUP); // sätter vilken typ av pin den ska vara
  pinMode(LED_PIN, OUTPUT); // sätter vilken typ av pin den ska vara
}

void loop() {
  int reading = digitalRead(BUTTON_PIN); // läser av om knappen är HIGH eller LOW varje loop
  
  if (reading!=buttonState) { // tittar om något har ändrats med knappen
    buttonState = reading; // nytt buttonState

    if (buttonState==LOW) { // om knappen intryckt
      ledState = !ledState; // ändra LED:en
      digitalWrite(LED_PIN, ledState); // ser till att LED:en ändras på riktigt
    }
    
    // Nedan är endast för att kunna leta fel.
    Serial.print(millis());
    Serial.print(": State Changed to ");
    Serial.println(buttonState);
  }

}