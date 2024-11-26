// EXEMPEL 3 OM DIGITAL INPUT
// En LED som sätts på och stängs av med en knapp.
// I detta exempel används delay() för att reglera debouncern.
// Exemplet motsvarar runt C-nivå. Den exakta nivån beror som alltid på programmets struktur, variabelnamn och liknande.

#include <Arduino.h>

const int BUTTON_PIN = 10; // Sätter vilken pin knappen är på
const int LED_PIN = 12; // Sätter vilken pin LED:en är på

int buttonState = HIGH; // Knappen är uppsläppt först.
int ledState = LOW; // LED:en är släckt först

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT_PULLUP); // Sätter typ av pin för knappen
  pinMode(LED_PIN, OUTPUT); // Sätter typ av pin för LED:en
}

void loop() {
  int reading = digitalRead(BUTTON_PIN); // Läser av knappens värde varje gång i loop

  if (reading != buttonState) { // Om värdet inte är som buttonstate, dvs något har ändrats
    delay(50); // Väntar 50 millisekunder för att se att det inte är en bounce
    reading = digitalRead(BUTTON_PIN); // Läser av värdet igen

    if (reading != buttonState) { // Om det fortfarande är annorlunda
      buttonState = reading; // Då kan vi ändra buttonstate eftersom knappen har ändrats på riktigt

      if (buttonState == LOW) { // Om knappen trycktes ner
        ledState = !ledState; // Då ändrar vi ledstate
        digitalWrite(LED_PIN, ledState); // Skriver nya ledstate till LED:en
      }

    }
  }

}
