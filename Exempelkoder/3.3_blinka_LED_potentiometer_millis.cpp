// EXEMPEL 3 OM ANALOG INPUT
// En LED som blinkar olika snabbt beroende på potentiometern
// I detta exempel används millis() för att reglera hur LED:en blinkar.
// Exemplet motsvarar runt A-nivå. Den exakta nivån beror som alltid på programmets struktur, variabelnamn och liknande.

#include <Arduino.h>

const int ledPin = 2;          // vilken pin LED ska vara
const int potPin = 4;         // vilken pin potentiometern ska vara

int potValue = 0;              // variabel för värdet som läses från potentiometern
int blinkDelay = 0;            // variabel för hur länge vi väntar mellan blinkningar

const int minDelay = 100;      // minsta tid mellan blinkningar (när den blinkar snabbt)
const int maxDelay = 1000;     // längsta tid mellan blinkningar (när den blinkar långsamt)

unsigned long lastLedChange = 0;  // senaste gången LED:en ändrades
bool ledState = LOW;               // LED:ens state

void setup() {
  pinMode(ledPin, OUTPUT);     // vilken slags pin LED:en ska vara
  pinMode(potPin, INPUT);      // vilken slags pin potentiometern ska vara
  Serial.begin(115200);
  analogReadResolution(12);     // ser till att upplösningen på analogRead stämmer med mikrokontrollen

}

void loop() {
  potValue = analogRead(potPin); // Läser potentiometerns värde

  blinkDelay = map(potValue, 0, 4095, minDelay, maxDelay); // skalar om värdet från potentiometern till värden mellan minsta och största blink-väntetid

  unsigned long currentTime = millis(); // nuvarande tid
  if (currentTime - lastLedChange >= blinkDelay) { // om det har gått tillräckligt länge sedan LED:en blinkade senast
    lastLedChange = currentTime; // uppdaterar när vi senast ändrade LED:en

    ledState = !ledState;         // ändrar ledstate (HIGH -> LOW, eller LOW -> HIGH)
    digitalWrite(ledPin, ledState); // skriver till LED:en (tänder eller släcker den)
  }

}
