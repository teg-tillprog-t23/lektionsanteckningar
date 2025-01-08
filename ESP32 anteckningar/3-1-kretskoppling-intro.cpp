#define LED 2 // Definierar att pin 2 ska kallas LED

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // Fixar med uppladdningshastighet
  pinMode(LED, OUTPUT); // Sätter pin 2 till output
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED, HIGH); // digital = hög eller låg, hög = lLED:en lyser
  Serial.println("LED is on"); // syns i terminalen, kan användas som felsökning
  delay(1000);
  digitalWrite(LED, LOW);
  Serial.println("LED is off");
  delay(1000);
}