// EXEMPEL 3 OM DIGITAL OUTPUT
// Fyra LED som blinkar i rad.
// I detta exempel används delay() för att reglera hur LED:arna blinkar.
// Exemplet motsvarar E-nivå, för att klara kursen behöver du behärska kodens alla delar.

#include <Arduino.h>

// Vi namnger alla LED
#define LED1 2
#define LED2 3
#define LED3 4
#define LED4 5


int LED_array[4] = {LED1,LED2,LED3,LED4}; // Lista med alla LED
int LED_counter = 0; // Håller koll på vilken LED som ska blinka
int num_LED = 4; // Hur många LED vi har

void setup(){
  for(int i = 0;i<num_LED;i++){
    pinMode(LED_array[i], OUTPUT); // Sätter alla pinnar som vi ska använda till output
  }

}


void loop(){
digitalWrite(LED_array[LED_counter], LOW); // Då släcker vi LED:en som senast lyste


if(LED_counter == num_LED - 1){ // Om vi har kommit till den sista LED:en
    LED_counter = 0; // Så går vi till den första igen
}
else{
    LED_counter ++; // Annars vill vi bara gå vidare till nästa LED
}

digitalWrite(LED_array[LED_counter], HIGH); // Vi tänder också nästa LED

delay(500); // Vi väntar en lagom stund innan nästa LED ska blinka.

}