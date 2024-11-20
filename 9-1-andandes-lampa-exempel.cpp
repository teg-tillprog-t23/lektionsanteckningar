#include <Arduino.h>

const int RED_PIN = 5;

const int pwmFrequency = 5000;
const int pwmResolution = 8;
int red = 127;

void setup() {
  Serial.begin(115200);

  ledcAttach(RED_PIN, pwmFrequency, pwmResolution);

  ledcWrite(RED_PIN, 127);
}

void loop() {
    ledcWrite(RED_PIN, red);
    delay(10);
    red -= 1;
    if(red == 0){
      red = 255;
    }
}