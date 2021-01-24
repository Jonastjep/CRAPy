/ mq2 | hcsro4 | dht11 | bmp280 | mh | gps6mv2 | nrf24l01

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <dht.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

// Solar sensor variables
int sens1 = A2; // photoresistor 1 is attached to (Bottom Left)
int sens2 = A3; //photoresistor 2 is attached to (Bottom Right)
int sens3 = A4; //photoresistor 3 is attached to (Top Left)
int sens4 = A5; //photoresistor 4 is attached to (Top Right)
char quadrant = 0;
String data = "";

// mq2 ------------------
#define MQ2pin (0)  // Arduino pin to which analog pin of MQ2 is connected
                    // DO in 8
float mqValue;      // Variable to store sensor value
//-----------------------

// hcsro4 ---------------
int trigPinA = 3;         // Trigger (sends the wave)
int echoPinA = 4;         // Echo (receives the wave)
long durationA, hcValueA; // Creates the variables to store sensor value

int trigPinB = 24;         
int echoPinB = 25;         
long durationB, hcValueB;  

int trigPinC = 26;         
int echoPinC = 27;         
long durationC, hcValueC;  

int trigPinD = 28;         
int echoPinD = 29;         
long durationD, hcValueD;  

int trigPinE = 30;         
int echoPinE = 31;         
long durationE, hcValueE;  
//-----------------------

// dht11 ----------------
#define outPin 7 // DO pin 7
dht DHT;         // Creates a DHT object
float dhtValueT; // Creates temperature variable to store sensor value
float dhtValueH; // Creates humidity variable to store sensor value
//-----------------------

// bmp280----------------
Adafruit_BMP280 bmp;// I2C
long bmpValueP;     // Creates pressure variable to store sensor value
long bmpValueA;     // Creates altitude variable to store sensor value
// ----------------------

// mh -------------------
int sensorPin = A1; // Analog pin
float mhValue;      // Creates moisture variable to store sensor value
// ----------------------

// gps6mv2 --------------
float latitude = 0;         // Creates latitude variable to store sensor value
float longitude = 0;        // Creates longitude variable to store sensor value
double alt = 0;             // Creates rel. altitude variable to store sensor value
SoftwareSerial ss (10 , 9); // Library, serial communication (Rx, Tx)- opposite conn. to arduino
TinyGPSPlus gps;            // Creates gps object
// ----------------------

// nrf24l01 -------------
#define CE_PIN  39  
#define CSN_PIN 40  

const byte slaveAddress[5] = {'R','x','A','A','A'}; 

RF24 radio(CE_PIN, CSN_PIN);           // Create a Radio object 

char dataToSend[32];                   // Must match [] of dataToReceive!!;

unsigned long currentMillis;           // Variables for waiting waiting time
unsigned long prevMillis;              
unsigned long txIntervalMillis = 1000; // Send once per second
// ----------------------


void setup() {

    Serial.begin(9600);      // starts serial communication

    Serial.println("Gas sensor warming up!"); 
    delay(20000);            // allows the mq2 to warm up

    Serial.println("Ultra-sound sensor starting!");
    
    // define inputs and outputs
    pinMode(trigPinA, OUTPUT);
    pinMode(echoPinA, INPUT); 
    
    pinMode(trigPinB, OUTPUT);
    pinMode(echoPinB, INPUT); 
  
    pinMode(trigPinC, OUTPUT);
    pinMode(echoPinC, INPUT); 
  
    pinMode(trigPinD, OUTPUT);
    pinMode(echoPinD, INPUT); 

    pinMode(trigPinE, OUTPUT);
    pinMode(echoPinE, INPUT); 
    
    Serial.println("Temperature/Humidity sensor starting!");

    Serial.println("Pressure/Altitude sensor starting!");
    bmp.begin();
    
    /* Default settings from datasheet. EXAMPLE*/
    bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,   /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */

    Serial.println("Soil moisture sensor starting!");

    Serial.println("GPS module starting!");
    ss.begin(9600); //SoftwareSerial
  
    Serial.println("Radio starting!");
    radio.begin();                       
    radio.setDataRate( RF24_250KBPS );   
    radio.setRetries(3,5);               // (delay, count)Sets the number and delay of retries upon failed submit.
    radio.openWritingPipe(slaveAddress); 

    // Solar tracker setup
    pinMode(sens1, INPUT);
    pinMode(sens2, INPUT);
    pinMode(sens3, INPUT);
    pinMode(sens4, INPUT);
}

void loop() {

  // mq2 ----------------
  mqValue = analogRead(MQ2pin); // Reads analog input pin 0. Analog output voltage  
                                // proportional to concentration of smoke / gas.     
  // --------------------

  // sun tracker code
  int bl = analogRead(sens1); // read the value of sensor 1
  int br = analogRead(sens2); // read the value of sensor 2
  int tl = analogRead(sens3); // read the value of sensor 3
  int tr = analogRead(sens4); // read the value of sensor 4
  trackSun(bl, br, tl, tr)

  //hcsro ---------------
  digitalWrite(trigPinA, LOW);  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  delayMicroseconds(5);
  digitalWrite(trigPinA, HIGH); // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  delayMicroseconds(10);
  digitalWrite(trigPinA, LOW);
  pinMode(echoPinA, INPUT);             // Reads HIGH pulse (whose duration is the Time (in   
  durationA = pulseIn(echoPinA, HIGH);  // microseconds)from sending ping to receiving echo) 
  hcValueA = ((durationA/2) / 29.1);    // Convert the time into a distance ("Divide by 29.1 or multiply by 0.0343")
  delay(500); 
  
  digitalWrite(trigPinB, LOW);  
  delayMicroseconds(5);
  digitalWrite(trigPinB, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPinB, LOW);
  pinMode(echoPinB, INPUT);            
  durationB = pulseIn(echoPinB, HIGH);                                   
  hcValueB = ((durationB/2) / 29.1);    
  delay(500);
  
  digitalWrite(trigPinC, LOW);  
  delayMicroseconds(5);
  digitalWrite(trigPinC, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPinC, LOW);
  pinMode(echoPinC, INPUT);            
  durationC = pulseIn(echoPinC, HIGH);                                    
  hcValueC = ((durationC/2) / 29.1);    
  delay(500);
   
  digitalWrite(trigPinD, LOW);  
  delayMicroseconds(5);
  digitalWrite(trigPinD, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPinD, LOW);
  pinMode(echoPinD, INPUT);            
  durationD = pulseIn(echoPinD, HIGH);                                 
  hcValueD = ((durationD/2) / 29.1);    
  delay(500);

  digitalWrite(trigPinE, LOW);  
  delayMicroseconds(5);
  digitalWrite(trigPinE, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPinE, LOW);
  pinMode(echoPinE, INPUT);            
  durationE = pulseIn(echoPinE, HIGH);  
  hcValueE = ((durationE/2) / 29.1);
  //---------------------

  //dht11 ---------------
  int readData = DHT.read11(outPin); // Reads data from sensor
  dhtValueT = DHT.temperature;       // Reads temperature
  dhtValueH = DHT.humidity;          // Reads humidity
  // --------------------

  // bmp280 -------------
  bmp.readTemperature();                 // Reads temperature
  bmpValueP = bmp.readPressure();        // Reads pressure
  bmpValueA = bmp.readAltitude(1008);    // Reads Altitude
  // --------------------

  // mh -----------------
  mhValue = analogRead(sensorPin); //Reads moisture
  // --------------------

  // GPS CRAPy github code ------------
  while(ss.available()>0){
    
    if (gps.encode(ss.read())){
      
      latitude = (gps.location.lat());
      longitude = (gps.location.lng());
      alt = (gps.altitude.value()/100);
      } 
  }
  //-----------------------------------

  delay(1000); //dht11
  
  //TO TRANSMIT DATA IN *STRING* ------
  String data = "";
  data.concat(hcValueA);
  String ultrasound = "(" + data + ";" + hcValueB + + ";" + hcValueC + ";" + hcValueD + ";" + hcValueE + ")";
  Serial.println(ultrasound);
  String spaced = "<" + data + ";" + mqValue + ";" + dhtValueT + ";" + dhtValueH + ";" + bmpValueP + ";" + bmpValueA + ";" + mhValue + ";" + latitude + ";" + longitude + ";" + alt + ">";
  Serial.println(spaced);
  spaced = dataToSend;
  delay(250);
  // ----------------------------------

  // nrf24l01 -------------------------
  currentMillis = millis(); // Waiting time between messages
  if (currentMillis - prevMillis >= txIntervalMillis) 
  {                        
    send();
    prevMillis = millis();
  }
  //-----------------------------------
}

//nrf24l01 ----------------------------
void send() {

    bool rslt;
    rslt = radio.write( &dataToSend, sizeof(dataToSend) );
        // Always use sizeof() as it gives the size as the number of bytes.

    Serial.print(" Data Sent ");
    Serial.print(dataToSend);
    if (rslt) {
        Serial.println("");
        Serial.println("&Acknowledge received&");
    }
    else {
        Serial.println("");
        Serial.println("&Txt failed&");
    }
}

void trackSun(int bl, int br, int tl, int tr){
  if((tr < br) || (tr < tl) || (tr < bl)) {
    if((br < tl)) {
      char quadrant= 1;
    } else {
      char quadrant = 2;
    }
      data.concat(quadrant);
      String spaced= "(" + data + ")";
      Serial.print(spaced);
  } else if((tl < tr) || (tl < bl) || (tl < br)) {
      if((tr < bl)) {
      char quadrant= 3;
    } else {
      char quadrant = 4;
    }
      data.concat(quadrant);
      String spaced= "(" + data + ")";
      Serial.print(spaced);
  } else if((bl < br) || (bl < tl) || (bl < tr)) {
      if((tr < bl)) {
      char quadrant= 5;
    } else {
      char quadrant = 6;
    }
      data.concat(quadrant);
      String spaced= "(" + data + ")";
      Serial.print(spaced);
  } else if((br < tr) || (br < bl) || (br < tl)) {
      if((bl < tr)) {
      char quadrant= 7;
    } else {
      char quadrant = 8;
    }
      data.concat(quadrant);
      String spaced= "(" + data + ")";
      Serial.print(spaced);
  } else if (tr = br ){
    String quadrant = "to_the_right";
    String spaced= "(" + quadrant + ")";
    Serial.print(spaced);
  } else if (tr = tl ){
    String quadrant = "to_the_front";
    String spaced= "(" + quadrant + ")";
    Serial.print(spaced);
  }  else if (tl = bl ){
    String quadrant = "to_the_left";
    String spaced= "(" + quadrant + ")";
    Serial.print(spaced);
  }  else if (bl = br ){
    String quadrant = "to_the_back";
    String spaced= "(" + quadrant + ")";
    Serial.print(spaced);
  }  else {
    String quadrant = "at_zenith";
    String spaced= "(" + quadrant + ")";
    Serial.print(spaced);
  }
}
