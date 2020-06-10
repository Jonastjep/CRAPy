import processing.serial.*;

Serial myPort;
String val;


void setup(){
  size(1000,1000);
  String portName = Serial.list()[1]; //change the 0 to a 1 or 2 etc. to match your port
  myPort = new Serial(this, portName, 9600);
}

void draw(){
  int click = 0;
  if (mousePressed == true){ 
    click = 1;
  } 
  else{
    click = 0;
  }   
  String mousePos = "<" + mouseX + "," + mouseY + "," + click + ">";
  myPort.write(mousePos);
}
