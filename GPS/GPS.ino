#include <TinyGPS++.h>
#include <SoftwareSerial.h>

float latitude = 0;
float longitude = 0;
double alt = 0;

SoftwareSerial softwareSerial(9,8);
TinyGPSPlus gps;

void setup() {
  Serial.begin(9600);
  softwareSerial.begin(9600);
  Serial.println("STARTING UP GPS MODULE");
}

void loop() {
  while(softwareSerial.available()>0){
    
    if (gps.encode(softwareSerial.read())){
      
      latitude = (gps.location.lat());
      longitude = (gps.location.lng());
      alt = (gps.altitude.value()/100);
      
      Serial.println(String(latitude,6)+";"+String(longitude,6)+";"+String(alt,2));
    
      delay(3000);
      
    } 
  }
}

float getLatitude(){
  return latitude;
}

float getLongitude(){
  return longitude;
}

String getTimeString(int hr, int minutes){
  return String(hr)+":"+String(minutes);
}

String getDate(int dd, int mm, int yy){
  return String(dd)+"/"+String(mm)+"/"+String(yy);
}
