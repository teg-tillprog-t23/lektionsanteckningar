
// Define the LED and potentiometer pins
const int ledPin = 2;          // Pin for LED 
const int potPin = 4;         // Pin for Potentiometer (titta på pinkartan för att se vilka du kan använda)

// Variables to hold the potentiometer value and the delay
int potValue = 0;              // Variable to store the raw value from the potentiometer
int blinkDelay = 0;            // Variable to store the calculated delay in milliseconds

// Define the minimum and maximum delay for LED blinking
const int minDelay = 100;      // Minimum delay in milliseconds (fast blink)
const int maxDelay = 1000;     // Maximum delay in milliseconds (slow blink)

void setup() {
  pinMode(ledPin, OUTPUT);     // Set LED pin as output
  pinMode(potPin, INPUT);      // Set potentiometer pin as input
  Serial.begin(115200);        // Start serial communication for debugging (optional)
  analogReadResolution(12);     // Set resolution of analog read to make sure that we have the same as the board (important in Wokwi)
}

void loop() {
  // Read the potentiometer's analog value (range: 0 to 4095 on ESP32)
  potValue = analogRead(potPin);

  // Calculate the blink delay based on potentiometer value
  // Scale potValue from its range (0 to 4095) to the desired delay range (minDelay to maxDelay)
  blinkDelay = minDelay + ((maxDelay - minDelay) * potValue) / 4095;

  // Blink the LED
  digitalWrite(ledPin, HIGH);  // Turn the LED on
  delay(blinkDelay);           // Wait for the calculated delay
  digitalWrite(ledPin, LOW);   // Turn the LED off
  delay(blinkDelay);           // Wait for the same delay

  // Print the delay value for debugging (optional)
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print(" | Blink Delay: ");
  Serial.println(blinkDelay);
}