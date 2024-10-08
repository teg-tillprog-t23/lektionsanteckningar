#include <Arduino.h>

const int BUTTON_PIN = 10;
const int LED_PIN = 12;

int buttonState = LOW;
int ledState = HIGH;

void setup() {
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  if (reading != buttonState) {
    delay(50); 
    reading = digitalRead(BUTTON_PIN); 

    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == LOW) {
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
      }

      Serial.print(millis());
      Serial.print(": State Changed to ");
      Serial.println(buttonState);
    }
  }

}
