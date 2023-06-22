#define EN 8
#define X_DIR 5
#define Y_DIR 6
#define Z_DIR 7

#define X_STP 2
#define Y_STP 3
#define Z_STP 4

char ch;

void step (boolean dir, byte dirPin, byte stepperPin, int steps) {
  digitalWrite(dirPin, dir);
  delay(50);
  for (int i = 0; i < steps; i++ ) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(1000);
  }
}

void setup() {
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT);
  pinMode(Y_STP, OUTPUT);
  pinMode(Z_DIR, OUTPUT);
  pinMode(Z_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    ch = Serial.read();
    Serial.print("input: ");
    Serial.println(ch);
  }
  switch (ch) {
    case 'x':
      Serial.println("X move");
      step (false, X_DIR, X_STP, 100);
      delay(1000);
      step (true, X_DIR, X_STP, 100);
      delay(1000);
      break;
    case 'y':
      Serial.println("Y move");
      step (false, Y_DIR, Y_STP, 100);
      delay(1000);
      step (true, Y_DIR, Y_STP, 100);
      delay(1000);
      break;
    case 'z':
      Serial.println("Z move");
      step (false, Z_DIR, Z_STP, 300);
      delay(1000);
      step (true, Z_DIR, Z_STP, 300);
      delay(1000);
      break;
  }
}
