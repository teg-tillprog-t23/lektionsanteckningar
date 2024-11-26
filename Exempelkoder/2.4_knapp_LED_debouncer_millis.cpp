// EXEMPEL 4 OM DIGITAL INPUT
// En LED som sätts på och stängs av med en knapp.
// I detta exempel används millis() för att reglera debouncern.
// Exemplet motsvarar överkurs, du behöver inte behärska det här exemplet för någon nivå i kursen.


#include <Arduino.h>

const int BUTTON_PIN = 10; // Vilken pin knappen ska vara på
const int LED_PIN = 12; // Vilken pin LED:en ska vara på

int buttonState = HIGH; // Knappens börjar på uppsläppt
int lastButtonState = HIGH; // Senaste buttonstate är också uppsläppt
int ledState = LOW; // LED:en börjar vara släckt

unsigned long lastDebounceTime = 0; // Senaste gången vi startade debounce
unsigned long debounceDelay = 20; // Hur länge vi ska vänta för en debounce

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT); // Vilken slags pin det ska vara för knappen
  pinMode(LED_PIN, OUTPUT); // Vilken slags pin det ska vara för LED:en
}

void loop() {
  int reading = digitalRead(BUTTON_PIN); // Läser av knappen varje gång i loopen

  if (reading != lastButtonState) { // Om avläsningen inte stämmer med senaste buttonstate
    lastDebounceTime = millis(); // Vi startar en debounce och uppdaterar debounce time
    lastButtonState = reading; // Vi uppdaterar så att programmet vet vilket värde vi läste senast
    Serial.print(millis()); // För att felsöka
    Serial.print(": Last button state changed to "); // För att felsöka
    Serial.println(lastButtonState); // För att felsöka
  }

    // Det i nedanstående if sker alltså endast om knappens läge inte har ändrats under hela debouncen, annars kommer debounce-time att ha blivit uppdaterat
  if ((millis() - lastDebounceTime) > debounceDelay) { // Om det har gått tillräckligt länge sedan vi startade debouncen
    if (reading != buttonState) { // Om avläsningen inte stämmer med faktiska buttonstate
      buttonState = reading; // Uppdaterar buttonstate
      Serial.print(millis()); // För felsökning
      Serial.print(": Button state changed to "); // För felsökning
      Serial.println(buttonState); // För felsökning

      if (buttonState == LOW) { // Om värdet på knappen är intryckt
        ledState = !ledState; // Då ändrar vi ledstate
        digitalWrite(LED_PIN, ledState); // Och ser till att LED:en tänds/släcks

        Serial.print(millis()); // Felsökning
        Serial.print(": LED state changed to "); // Felsökning
        Serial.println(ledState); // Felsökning
      }

    }
  }

}
