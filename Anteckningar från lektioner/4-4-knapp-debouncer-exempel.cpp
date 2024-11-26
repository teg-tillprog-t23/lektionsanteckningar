#include <Arduino.h>

#define LED 2
#define BUTTON 3

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);
}

void loop() {
  if(digitalRead(BUTTON)==LOW){
    delay(20);
    if(digitalRead(BUTTON)==LOW){
        digitalWrite(LED,!digitalRead(LED));
    }
    while (digitalRead(BUTTON) == LOW);
    delay(20);
    while (digitalRead(BUTTON) == LOW);
  }
  
}