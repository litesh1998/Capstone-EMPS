int zpin = A2;
int ypin = A1;
int xpin = A0;

void setup() {
  Serial.begin(9600);
  pinMode(xpin, INPUT);
  pinMode(ypin, INPUT);
  pinMode(zpin, INPUT);
}

void loop() {
  Serial.print(analogRead(xpin));
  Serial.print("\t");
  Serial.print(analogRead(ypin));
  Serial.print("\t");
  Serial.print(analogRead(zpin));
  Serial.println();
  delay(10);
}
