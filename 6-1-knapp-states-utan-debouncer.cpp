#include <Arduino.h>

const int BUTTON_PIN = 10;
const int LED_PIN = 12;

int buttonState = HIGH;
int ledState = LOW;

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);
  
  if (reading!=buttonState) {
    buttonState = reading;

    if (buttonState==LOW) {
      ledState = !ledState;
      digitalWrite(LED_PIN, ledState);
    }
    
    // Nedan är endast för att kunna leta fel.
    Serial.print(millis());
    Serial.print(": State Changed to ");
    Serial.println(buttonState);
  }

}