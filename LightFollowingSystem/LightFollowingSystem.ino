#include <Servo.h>

Servo serv1;
Servo serv2;
int val0;
int val1;
int val2;
int val3;

int xVal = 90;
int yVal = 90;
int mClick = 0;
boolean newData = false;



void setup() {
  serv1.attach(9);
  serv2.attach(10);
  Serial.begin(9600);
  delay(100);
  calibration(&val0, &val1, &val2, &val3);

  Serial.print(val0);
  Serial.print(",");
  Serial.print(val1);
  Serial.print(",");
  Serial.print(val2);
  Serial.print(",");
  Serial.print(val3);
  Serial.print("\n");}

void loop() {
  int l0 = analogRead(0); //top
  int l1 = analogRead(1); //right
  int l2 = analogRead(2); //bottom
  int l3 = analogRead(3); //left
  int posX;
  int posY;
  delay(20);
  Serial.println(l1-l3);
  if(l0 - l2 > 5){
    posX = serv1.read();
    if(posX + (l0-l2)/5 < 145){ 
      serv1.write(posX + (l0-l2)/5);
    } else{
        serv1.write(145);
    }
  } else if(l0 - l2 < -5){
    posX = serv1.read();
    if(posX + (10-12)/5 > 30){
      serv1.write(posX + (l0-l2)/5);
    } else{
        serv1.write(30);
    }

  }

  if(l1 - l3 > 5){
    posY = serv2.read();
    if(posY + (l1-l3)/5 < 180){
      serv2.write(posY + (l1-l3)/5);
    } else{
        serv2.write(180);
    }
  } else if(l1 - l3 < -5){
    posY = serv2.read();
    if(posY + (l1-l3)/5 > 0){
      serv2.write(posY + (l1-l3)/5);
    } else{
        serv2.write(0);
    }
  }


//  if(l3 < l1){
//    xVal += 1;
//    serv2.write(xVal);
//  }
//  if(l3 > l1){
//    xVal -= 1;
//    serv1.write(xVal);
//  }


//  Serial.print(l0);
//  Serial.print(",");
//  Serial.print(l1);
//  Serial.print(",");
//  Serial.print(l2);
//  Serial.print(",");
//  Serial.print(l3);
//  Serial.print("\n");
}
void calibration(int *val0,int *val1, int *val2, int *val3) {
  int maxValX = 0;
  int maxValY = 0;
  int serv1Val = 0;
  int serv2Val = 0;
  int read0;
  int read1;
  int read2;
  int read3;


  for(int i=0; i<180; i++)
  {
    serv2.write(i);
    delay(20);
    read0 = analogRead(0);
    read2 = analogRead(2);

    if (read2+read0 > maxValX){
      maxValX = read2+read0;
      serv2Val = i;
    }
    
 
  }
  serv2.write(serv2Val);

  for(int i=30; i<145; i++)
  {
    serv1.write(i);
    delay(20);
    read1 = analogRead(1);
    read3 = analogRead(3);

    if (read1+read3 > maxValY){
      maxValY = read1+read3;
      serv1Val = i;
    }

    
  }
  serv1.write(serv1Val);
  serv2.write(serv2Val);

  *val0 = analogRead(0);
  *val1 = analogRead(1);
  *val2 = analogRead(2);
  *val3 = analogRead(3);

//  Serial.print(val0);
//  Serial.print(",");
//  Serial.print(val1);
//  Serial.print(",");
//  Serial.print(val2);
//  Serial.print(",");
//  Serial.print(val3);
//  Serial.print("\n");


  
}
