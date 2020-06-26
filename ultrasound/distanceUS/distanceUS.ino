
const int trig = 12;
const int echo = 13;

long t;
int d;

void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9500);
}

void loop() {
  digitalWrite(trig, LOW);
  delay(0.002);
  
  digitalWrite(trig, HIGH);
  delay(0.01);
  digitalWrite(trig, LOW);

  t = pulseIn(echo, HIGH);
  d = (t*0.034)/2;
  
  Serial.print("Distance: ");
  Serial.println(d);

}
