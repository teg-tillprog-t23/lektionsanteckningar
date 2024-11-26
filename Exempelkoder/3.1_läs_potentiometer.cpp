// EXEMPEL 1 OM ANALOG INPUT
// Ett progrram som läser och skriver ut voltvärdet baserat på potentiometerns läge
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

#define POT 3 // Vilken pin potentiometern är inkopplad på

void setup() {
  Serial.begin(115200);
  analogReadResolution(12); // För att se till att upplösningen på analogRead stämmer med mikrokontrollern
  pinMode(POT, INPUT); // Vilken slags pin POT ska vara
}

void loop() {
  int sensorValue = analogRead(POT); // Läser av värdet på potentiometern
  
  float voltage = map(sensorValue, 0, 4095, 0, 3.3); // Anpassar skalan så att det vi läser av från potentiometern (mellan 0 och 4095) omvandlas till värden mellan 0 och 3.3
  Serial.println(voltage); // Skriver ut värdet
}
