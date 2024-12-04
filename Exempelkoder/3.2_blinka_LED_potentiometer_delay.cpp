// EXEMPEL 2 OM ANALOG INPUT
// En LED som blinkar olika snabbt beroende på potentiometern
// I detta exempel används delay() för att reglera hur LED:en blinkar.
// Exemplet motsvarar runt C-nivå. Den exakta nivån beror som alltid på programmets struktur, variabelnamn och liknande.


#include <Arduino.h>

const int ledPin = 2;          // vilken pin LED:en är
const int potPin = 4;         // vilken pin potentiometern är

int potValue = 0;              // variabel för värdet som läses från potentiometern
int blinkDelay = 0;            // hur länge vi ska vänta mellan blinkningar

const int minDelay = 100;      // minsta väntetid för blinknigar, när LED:en blinkar snabbt
const int maxDelay = 1000;     // största väntetid för blinkningar, när LED:en blinkar långsamt

void setup() {
  pinMode(ledPin, OUTPUT);     // vilken slags pin LED:en ska vara
  pinMode(potPin, INPUT);      // vilken slags pin potentiometern ska vara
  Serial.begin(115200);
  analogReadResolution(12);     // ser till att upplösningen för analogRead stämmer överrens med mikrokontrollern
}

void loop() {
  potValue = analogRead(potPin); // läser av potentiometerns värde

  blinkDelay = map(potValue, 0, 4095, minDelay, maxDelay); // ser till att värdet från potentiometern skalas om till jämn skala mellan maximala och minimala blink-väntetid

  digitalWrite(ledPin, HIGH);  // tänder LED
  delay(blinkDelay);           // väntar korrekt tid
  digitalWrite(ledPin, LOW);   // stänger av LED
  delay(blinkDelay);           // väntar korrekt tid

}