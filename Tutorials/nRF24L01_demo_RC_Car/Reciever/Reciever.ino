#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>
#include <string.h>

#define CE 8
#define CSN 10
#define DCin1 2
#define DCin2 3
#define DCin3 4
#define DCin4 7
#define ENA 5
#define ENB 6

int motor_speed;
int motor_speed1;

RF24 radio(CE,CSN);
const byte Address[6] = "00001";

//For the Parsing
char *ParsedStr[10];

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, Address);
  radio.startListening();

  pinMode(DCin1 , OUTPUT);
  pinMode(DCin2, OUTPUT);
  pinMode(DCin3, OUTPUT);
  pinMode(DCin4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  
  digitalWrite(DCin1 , LOW);
  digitalWrite(DCin2, LOW);
  digitalWrite(DCin3, LOW);
  digitalWrite(DCin4, LOW);
  digitalWrite(ENA, LOW);
  digitalWrite(ENB, LOW);

  radio.setPALevel(RF24_PA_MAX);
}

void loop() {
  if (radio.available()){
    while (radio.available()){
      // COTROL DATA COLLECTION //
      char ctrl[32] = "";
      radio.read(&ctrl, sizeof(ctrl));
      Serial.print("Received Data : ");
      Serial.println(ctrl);
      
      byte index = 0;
      char *tok = ctrl;
      while((tok = strtok(tok,",")) != NULL){
        ParsedStr[index] = tok;
        index++;
        tok = NULL;
      }
      for(int i = 0; i<index;i++){
        Serial.println(ParsedStr[i]);
      }

      // CAR CONTROL //
      //Forward
      if((atoi(ParsedStr[0]) == 1 && atoi(ParsedStr[1]) == 0) && (atoi(ParsedStr[2]) > 492 && atoi(ParsedStr[2]) < 532)){
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, 255);
        analogWrite(ENB, 255);
        Serial.println("HEYYYY");
      }
      //Forward RIGHT
      else if((atoi(ParsedStr[0]) == 1 && atoi(ParsedStr[1]) == 0) && (atoi(ParsedStr[2]) > 532)){
        motor_speed = map(atoi(ParsedStr[2]), 532, 1023, 255, 0);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, 255);
        analogWrite(ENB, motor_speed);
      }
      //Forward LEFT
      else if((atoi(ParsedStr[0]) == 1 && atoi(ParsedStr[1]) == 0) && (atoi(ParsedStr[2]) < 492)){
        motor_speed = map(atoi(ParsedStr[2]), 492, 0, 255, 0);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed);
        analogWrite(ENB, 255);
      }
      //Backwards
      else if((atoi(ParsedStr[0]) == 0 && atoi(ParsedStr[1]) == 1) && (atoi(ParsedStr[2]) > 492 && atoi(ParsedStr[2]) < 532)){
        digitalWrite(DCin1, LOW);
        digitalWrite(DCin2, HIGH);
        digitalWrite(DCin3, LOW);
        digitalWrite(DCin4, HIGH);
        analogWrite(ENA, 255);
        analogWrite(ENB, 255);
      }
      //Backwards RIGHT
      else if((atoi(ParsedStr[0]) == 0 && atoi(ParsedStr[1]) == 1) && (atoi(ParsedStr[2]) > 532)){
        motor_speed = map(atoi(ParsedStr[2]), 532, 1023, 255, 0);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, 255);
        analogWrite(ENB, motor_speed);
      }
      //Backwards LEFT
      else if((atoi(ParsedStr[0]) == 0 && atoi(ParsedStr[1]) == 1) && (atoi(ParsedStr[2]) < 492)){
        motor_speed = map(atoi(ParsedStr[2]), 492, 0, 255, 0);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed);
        analogWrite(ENB, 255);
      }
      else{
        digitalWrite(DCin1, LOW);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, LOW);
        digitalWrite(DCin4, LOW);
      }

      //WITH POTENTIOMETER !!!!! NOT WORKING YET, BAD QUALITY POT
      /*// CAR CONTROL //
      //STOP
      if ((atoi(ParsedStr[2]) > 502 && atoi(ParsedStr[2]) < 522) && (atoi(ParsedStr[3])>502 && atoi(ParsedStr[3]) <522)){
        digitalWrite(DCin1, LOW);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, LOW);
        digitalWrite(DCin4, LOW);

        //digitalWrite(ENA, LOW);
        //digitalWrite(ENB, LOW);
      }
      //FORWARD
      else if (atoi(ParsedStr[2]) < 502 && (atoi(ParsedStr[3])>502 && atoi(ParsedStr[3]) <522)){
        motor_speed = map(atoi(ParsedStr[2]), 502, 0, 0, 255);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed);
        analogWrite(ENB, motor_speed);
      }
      //FORWARD RIGHT
      else if(atoi(ParsedStr[2]) < 502 && atoi(ParsedStr[3])>522 ){
        motor_speed = map(atoi(ParsedStr[2]), 502, 0, 0, 255);
        motor_speed1 = map(atoi(ParsedStr[3]), 522, 1023, 255, 0); //This makes right motor gradually turn slower
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed);
        analogWrite(ENB, motor_speed1);
      }
      //RIGHT
      else if((atoi(ParsedStr[2])>502 && atoi(ParsedStr[2]) <522) && atoi(ParsedStr[3]) > 522 ){
        motor_speed = map(atoi(ParsedStr[2]), 502, 0, 0, 255);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed);
        analogWrite(ENB, motor_speed1);
      }
      //BACKWARDS
      else if(atoi(ParsedStr[2]) > 560 && (atoi(ParsedStr[3])>502 && atoi(ParsedStr[3]) <522)){
        motor_speed = map(atoi(ParsedStr[2]), 522, 1023, 0, 255);
        digitalWrite(DCin1, LOW);
        digitalWrite(DCin2, HIGH);
        digitalWrite(DCin3, LOW);
        digitalWrite(DCin4, HIGH);
        analogWrite(ENA, motor_speed);
        analogWrite(ENB, motor_speed);
      }
      
      //FORWARD LEFT
      else if(atoi(ParsedStr[2]) < 502 && atoi(ParsedStr[3])<502 ){
        motor_speed = map(atoi(ParsedStr[2]), 502, 0, 0, 255);
        motor_speed1 = map(atoi(ParsedStr[3]), 502, 0, 255, 0);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed1);
        analogWrite(ENB, motor_speed);
      }
      //BACKWARD RIGHT
      else if(atoi(ParsedStr[2]) > 522 && atoi(ParsedStr[3])>522 ){
        motor_speed = map(atoi(ParsedStr[2]), 522, 1023, 0, 255);
        motor_speed1 = map(atoi(ParsedStr[3]), 522, 1023, 0, 255);
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENA, motor_speed1);
        analogWrite(ENB, motor_speed);
      }
      //BACKWARD LEFT
      
      // MOTOR CTRL
      if (atoi(ParsedStr[2]) < 480){     //Rotating the left motor in clockwise direction
        motor_speed = map(atoi(ParsedStr[2]), 480, 0, 0, 255);   //Mapping the values to 0-255 to move the motor
        digitalWrite(DCin1, HIGH);
        digitalWrite(DCin2, LOW);
        analogWrite(ENA, motor_speed);
      }
      else if (atoi(ParsedStr[2])>480 && atoi(ParsedStr[2]) <560){  //Motors will not move when the joystick will be at center
        digitalWrite(DCin1, LOW);
        digitalWrite(DCin2, LOW);
      }
      
      else if (atoi(ParsedStr[2]) > 560){    //Rotating the left motor in anticlockwise direction
        motor_speed = map(atoi(ParsedStr[2]), 560, 1023, 0, 255);
        digitalWrite(DCin1, LOW);
        digitalWrite(DCin2, HIGH);
        analogWrite(ENA, motor_speed);
      }
       
      if (atoi(ParsedStr[3]) < 480){         //Rotating the right motor in clockwise direction
        motor_speed1 = map(atoi(ParsedStr[3]), 480, 0, 0, 255);
        digitalWrite(DCin3, HIGH);
        digitalWrite(DCin4, LOW);
        analogWrite(ENB, motor_speed1);
      }
      else if (atoi(ParsedStr[3])>480 && atoi(ParsedStr[3]) <560){
        digitalWrite(DCin3, LOW);
        digitalWrite(DCin4, LOW);
      }
      
      else if (atoi(ParsedStr[3]) > 560){        //Rotating the right motor in anticlockwise direction
        motor_speed1 = map(atoi(ParsedStr[3]), 560, 1023, 0, 255);
        digitalWrite(DCin3, LOW);
        digitalWrite(DCin4, HIGH);
        analogWrite(ENB, motor_speed1);
      }*/
    }
  }
}
