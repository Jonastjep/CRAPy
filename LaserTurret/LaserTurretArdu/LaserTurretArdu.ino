#include <Servo.h>

Servo serv1;
Servo serv2;
int val1;
int val2;

//FOR THE COMMUNICATION
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing

      // variables to hold the parsed data
int xVal = 0;
int yVal = 0;
int mClick = 0;
boolean newData = false;

void setup() {
  pinMode(2,OUTPUT);
  serv1.attach(9);
  serv2.attach(10);
  Serial.begin(9600);
}

void loop() {
  recvWithStartEndMarkers();
  if (newData == true) {
      strcpy(tempChars, receivedChars);

      parseData();
      newData = false;
      
      val1 = map(xVal, 0, 200, 0, 180);
      serv1.write(val1);
  
      val2 = map(yVal, 0, 200, 50, 180);
      serv2.write(val2);

      if(mClick == 1){
        digitalWrite(2,HIGH);
      }
      else{
        digitalWrite(2,LOW);
      }

  }
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index
 
    strtokIndx = strtok(tempChars, ","); // this continues where the previous call left off
    xVal = atoi(strtokIndx);     // convert this part to an integer

    strtokIndx = strtok(NULL, ",");
    yVal = atoi(strtokIndx);     // convert this part to a float

    strtokIndx = strtok(NULL, ",");
    mClick = atoi(strtokIndx);     // convert this part to a float

}
