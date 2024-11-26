// EXEMPEL 2 OM DIGITAL OUTPUT
// En LED som blinkar jämnt med 1 sekund mellanrum.
// I detta exempel används millis() för att reglera hur snabbt LED:en blinkar.
// Exemplet motsvarar runt C-nivå. Den exakta nivån beror som alltid på programmets struktur, variabelnamn och liknande.

#include <Arduino.h>

#define LED 2 // Definierar att pin 2 ska kallas LED
int last_update = 0; // Sätter när vi senast gjorde något med LED:en
int time_gap = 1000; // Avgör hur ofta LED:en ska blinka
int led_state = LOW; // Vad är LED:en på nu? Börjar med att vara släckt.

void setup() {
  Serial.begin(115200); // Fixar med uppladdningshastighet
  pinMode(LED, OUTPUT); // Sätter pin 2 till output
}

void loop() {
  int reading = millis(); //tiden nu, precis när raden körs, antal millisekunder från programmets start
  if(reading - last_update >= time_gap){ // Om det har gått 1 sekund eller mer sedan senaste uppdateringen
    last_update = reading; // Uppdatera last_update
    led_state = !led_state; // Ändra led_state så att den ändras, till exempel från LOW till HIGH
    digitalWrite(LED, led_state); // Skriver det nya led_state till lampan så att den tänds om den är släckt och släcks om den är tänd
  }
}