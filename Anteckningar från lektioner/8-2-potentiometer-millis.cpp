// Define the LED and potentiometer pins
const int ledPin = 2;          // Pin for LED (e.g., GPIO 2 on ESP32-S2)
const int potPin = 34;         // Pin for Potentiometer (e.g., GPIO 34 on ESP32-S2)

// Variables to hold potentiometer value and delay
int potValue = 0;              // Variable to store the raw value from the potentiometer
int blinkDelay = 0;            // Variable to store the calculated delay in milliseconds

// Define the minimum and maximum delay for LED blinking
const int minDelay = 100;      // Minimum delay in milliseconds (fast blink)
const int maxDelay = 1000;     // Maximum delay in milliseconds (slow blink)

// Variables to manage the LED state
unsigned long previousMillis = 0;  // Stores the last time the LED was toggled
bool ledState = LOW;               // Current state of the LED (on or off)

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

  // Check if it's time to toggle the LED state
  unsigned long currentMillis = millis(); // Get the current time
  if (currentMillis - previousMillis >= blinkDelay) {
    // Save the last time we toggled the LED
    previousMillis = currentMillis;

    // Toggle the LED state
    ledState = !ledState;         // Toggle the LED state (HIGH -> LOW, or LOW -> HIGH)
    digitalWrite(ledPin, ledState); // Set the LED to the new state
  }

  // Print the delay value for debugging (optional)
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print(" | Blink Delay: ");
  Serial.println(blinkDelay);
}
