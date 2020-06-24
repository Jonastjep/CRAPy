#include <Servo.h>

Servo serv1;
Servo serv2;
int val1;
int val2;

int xVal = 90;
int yVal = 90;
int mClick = 0;
boolean newData = false;



void setup() {
  serv1.attach(9);
  serv2.attach(10);
  Serial.begin(9600);

  
}

void loop() {
  int l0 = analogRead(0);
  int l1 = analogRead(1);
  int l2 = analogRead(2);
  int l3 = analogRead(3);

//  if(l3 < l1){
//    xVal += 1;
//    serv2.write(xVal);
//  }
//  if(l3 > l1){
//    xVal -= 1;
//    serv1.write(xVal);
//  }


  Serial.print(l0);
  Serial.print(",");
  Serial.print(l1);
  Serial.print(",");
  Serial.print(l2);
  Serial.print(",");
  Serial.print(l3);
  Serial.print("\n");
}

void calibration() {
  int maxVal1 = 0;
  int maxVal2 = 0;
  int serv1Val = 0;
  int serv2Val = 0;

  for(i=0; i>180; i++)
  {
    serv1.write(i);
    read1 = analogRead(1);

    if (read1 > maxVal1){
      maxVal1 = read1;
      serv1Val = i;
    }
 
  }

   for(i=20; i>145; i++)
  {
    serv2.write(i);
    read2 = analogRead(2);

    if (read2 > maxVal2){
      maxVal2 = read2;
      serv2Val = i;
    }

    
  }
  serv1.write(serv1Val);
  serv2.write(serv2Val);

  val0 = analogRead(0);
  val1 = analogRead(1);
  val2 = analogRead(2);
  val3 = analogRead(3);

  10 = map(10, 0, val0, 0, 100);
  11 = map(11, 0, val1, 0, 100);
  12 = map(12, 0, val2, 0, 100);
  13 = map(13, 0, val3, 0, 100);


  
}
