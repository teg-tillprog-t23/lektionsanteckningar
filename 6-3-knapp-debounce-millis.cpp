#include <Arduino.h>

const int BUTTON_PIN = 10;
const int LED_PIN = 12;

int buttonState = HIGH;
int lastButtonState = HIGH;
int ledState = LOW;

unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 20; // Debounce time in milliseconds

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  if (reading != lastButtonState) {
    lastDebounceTime = millis(); // Reset the debouncing timer
    lastButtonState = reading;
    Serial.print(millis());
    Serial.print(": Last button state changed to ");
    Serial.println(lastButtonState);
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      Serial.print(millis());
      Serial.print(": Button state changed to ");
      Serial.println(buttonState);

      if (buttonState == LOW) {
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);

        Serial.print(millis());
        Serial.print(": LED state changed to ");
        Serial.println(ledState);
      }

    }
  }

  // No delay here; the loop runs continuously
}
