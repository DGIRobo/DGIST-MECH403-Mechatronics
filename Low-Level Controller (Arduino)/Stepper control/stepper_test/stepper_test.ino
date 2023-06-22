#define EN 8
#define X_DIR 5
#define X_STP 2

void step (boolean dir, byte dirPin, byte stepperPin, int steps) {
  digitalWrite(dirPin, dir);
  delay(50);
  for (int i = 0; i < steps; i++ ) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(500);
  }
}

void setup() {
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);
}

void loop() {
  step (false, X_DIR, X_STP, 200);
  delay(1000);
  step (true, X_DIR, X_STP, 200);
  delay(1000);

}
