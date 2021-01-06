// this version has hidden objects, runs lidar when mouse pressed, and displays memorised contact points

float pointx = 0;
float pointy = 0;
int objSize = 5; // number of random lines
int lidarStroke = 255;
int objStroke = 255;

ArrayList<Float> contact = new ArrayList<Float>(); // stores positions of potential intersection points // size must be even
PVector allStart[] = new PVector[5]; // stores start of lines
PVector allEnd[] = new PVector[5]; // stores end of lines

void setup(){
  size(600, 400);
  
  // makes number of random lines to serve as obstacles
  for(int i =0; i<objSize; i++){
    float x1 = random(width);
    float x2 = random(width);
    float y1 = random(height);
    float y2 = random(height);
    allStart[i] = new PVector(x1, y1);
    allEnd[i] = new PVector(x2, y2);
  }
  
}

void draw(){
  background(255);
  pointx = mouseX; // set position to mouse location
  pointy = mouseY;
  circle(pointx, pointy, 5);
    
  // draws obstacles
  for(int x = 0; x<objSize; x++){
    stroke(objStroke);
    line(allStart[x].x , allStart[x].y, allEnd[x].x , allEnd[x].y);
  }
  
  // draws all stored contact points
  for(int x = 0; x<contact.size(); x = x+2){
    float px = contact.get(x);
    float py = contact.get(x+1);
    stroke(100);
    circle(px, py, 5);
  }

}

void lidar(int angRes, float x, float y, float range){
  for(int i = 0; i<angRes; i++) {
    float angle = i*(2*PI)/angRes;
    stroke(lidarStroke);
    
    // if there is contact with lidar point -> added to global contact list
    for(int xi = 0; xi<objSize; xi++){
    if (lineLine(x, y, (sin(angle)*range)+x, (cos(angle)*range)+y, allStart[xi].x , allStart[xi].y, allEnd[xi].x , allEnd[xi].y)){
      stroke(100);
    }
  }
    line(x, y, (sin(angle)*range)+x, (cos(angle)*range)+y);
   
  }
}

// only runs lidar when mouse pressed
void mousePressed(){
  lidar(20, pointx, pointy, 120);
}


boolean lineLine(float x1, float y1, float x2, float y2, 
      float x3, float y3, float x4, float y4) { // takes two line and displays intecept
      
  // calculate the distance to intersection point
  float uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
  float uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));

  // if uA and uB are between 0-1, lines are colliding
  if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1) {

    // optionally, draw a circle where the lines meet
    float intersectionX = x1 + (uA * (x2-x1));
    float intersectionY = y1 + (uA * (y2-y1));
    //fill(255,0,0);
    //noStroke();
    //ellipse(intersectionX,intersectionY, 20,20);
    contact.add(intersectionX);
    contact.add(intersectionY);

    return true;
  }
  return false;
}
