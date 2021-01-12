#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>            

#define potx_pin A0
#define poty_pin A1
#define f_pin 2
#define b_pin 3

int x_pos;
int y_pos;


RF24 radio(9,10);                            
const byte Address[6] = "00001";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(potx_pin,INPUT);
  pinMode(f_pin,INPUT);
  pinMode(b_pin,INPUT);
  //pinMode(poty_pin,INPUT);
  
  radio.begin ();
  radio.openWritingPipe (Address);
  radio.stopListening ();

  radio.setPALevel(RF24_PA_MAX);
}

void loop() {

  x_pos = analogRead (potx_pin) ;  //Reading the horizontal movement value
  //y_pos = analogRead (poty_pin) ;  //Reading the vertical movement value
  String fo = "0";
  String ba = "0";
  if(digitalRead(f_pin)==HIGH){
    fo = 1;
  }
  if(digitalRead(b_pin)==HIGH){
    ba = 1;
  }
  
  String data = fo + "," + ba + "," + x_pos  + "," + y_pos;
  char readyData[30];
  data.toCharArray(readyData, 30);
  
  radio.write(&readyData, sizeof(readyData));
  
  Serial.print("Transmitting Data : ");
  Serial.println(readyData);
}
