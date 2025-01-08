// EXEMPEL 4 OM DIGITAL OUTPUT
// Fyra LED som blinkar en i taget.
// I detta exempel används millis() för att reglera hur snabbt LED:arna blinkar.
// Exemplet motsvarar runt C-nivå. Den exakta nivån beror som alltid på programmets struktur, variabelnamn och liknande.

#include <Arduino.h>

// Vi namnger alla LED
#define LED1 2
#define LED2 3
#define LED3 4
#define LED4 5


int LED_array[4] = {LED1,LED2,LED3,LED4}; // Lista med alla LED
int LED_counter = 0; // Håller koll på vilken LED som ska blinka
int last_update = 0; // När vi senast uppdaterade, dvs när vi senast blinkade en LED
int time_gap = 1000; // Hur långt vi vill att det ska vara mellan blinkningar
int num_LED = 4; // Hur många LED vi har

void setup(){
  for(int i = 0;i<num_LED;i++){
    pinMode(LED_array[i], OUTPUT); // Sätter alla pinnar som vi ska använda till output
  }

}


void loop(){
  if(millis() - last_update > time_gap){ // Om det har gått mer än 1 sekund sedan vi senast blinkade
    digitalWrite(LED_array[LED_counter], LOW); // Då släcker vi LED:en som senast lyste
    last_update = millis(); // Vi ser till att senast uppdatering är rätt
    if(LED_counter == num_LED - 1){ // Om vi har kommit till den sista LED:en
      LED_counter = 0; // Så går vi till den första igen
    }
    else{
      LED_counter ++; // Annars vill vi bara gå vidare till nästa LED
    }
    digitalWrite(LED_array[LED_counter], HIGH); // Vi tänder också nästa LED

  }
}