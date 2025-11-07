// Problem: Write an Arduino/Raspberry Pi program for interfacing with PIR sensor

const int pirPin = 2;   // PIR sensor output pin
const int ledPin = 13;  // LED pin

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("PIR Motion Detection Started...");
}

void loop() {
  if (digitalRead(pirPin) == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("⚠ Motion Detected!");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("No Motion.");
  }
  delay(1000);
}
