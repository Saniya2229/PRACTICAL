const int tempPin = A0, buzzerPin = 9;
float temp;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
  Serial.println("Env Alert System Started...");
}

void loop() {
  temp = (analogRead(tempPin) * 5.0 * 100.0) / 1024.0;
  Serial.print("Temp: "); Serial.print(temp); Serial.println(" °C");

  if (temp > 35) {                     // High temp alert
    Serial.println("⚠ High Temp!");
    tone(buzzerPin, 1000, 1000);
  } 
  else if (temp < 15) {                // Low temp alert
    Serial.println("⚠ Low Temp!");
    tone(buzzerPin, 500, 500);
  } 
  else {                               // Normal temp
    Serial.println("✅ Normal");
    noTone(buzzerPin);
  }

  delay(2000);
}
