// this version has hidden objects, runs lidar when control pressed, and displays memorised contact points
//  - lidar host can only see objects in immediate vicinity, unlike previpus versions, objects not in FOV are invisible
//  - movement is changed from up/down left/right to forwards/backwards and rotation
//    - changed movement logic now it is smooth
//  - lidar host cannot cross geometric boundary

float locx = 20;
float locy = 20;
float heading = 0;
int objSize = 8; // number of random lines
int lidarStroke = 255;
int objStroke = 255;
int virtualBumperSize = 20;
int lidarRes = 36;
int movSpeed = 1;
float rotSpeed = 0.05;
boolean fw = false;
boolean bw = false;
boolean l = false;
boolean r = false;


ArrayList<Float> contact = new ArrayList<Float>(); // stores positions of potential intersection points // size must be even
PVector allStart[] = new PVector[objSize]; // stores start of lines
PVector allEnd[] = new PVector[objSize]; // stores end of lines

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
  
  stroke(100);
  fill(100,100,0);
  circle(locx, locy, 5);
  line(locx, locy, locx + 20*sin(heading), locy - 20*cos(heading));
  noFill();
  stroke(255, 0, 0);
  circle(locx, locy, virtualBumperSize);
    
  // draws obstacles
  for(int x = 0; x<objSize; x++){
    stroke(objStroke);
    line(allStart[x].x , allStart[x].y, allEnd[x].x , allEnd[x].y);
  }
  
  // draws all stored contact points
  for(int x = 0; x<contact.size(); x = x+2){
    float px = contact.get(x);
    float py = contact.get(x+1);
    stroke(255, 162, 0);
    fill(255, 162, 0);
    circle(px, py, 3);
  }
  
  //smoother movement
  if(fw && validFutLoc(1)){// forward
     locy = locy - movSpeed*cos(heading);
     locx = locx + movSpeed*sin(heading);
  }
  if(bw && validFutLoc(0)){// forward
     locy = locy + movSpeed*cos(heading);
     locx = locx - movSpeed*sin(heading);
  }
  if(l){
    heading = (heading -rotSpeed)%(2*PI);
  }
  if(r){
    heading = (heading +rotSpeed)%(2*PI);
  }
  
}

void keyPressed() {
  if ((keyPressed == true) && (key == CODED)) {
    if (keyCode == UP){// forward
     fw = true;
    } else if (keyCode == DOWN) {//backwads
     bw = true;
    } else if (keyCode == LEFT){//rotate left
      l = true;
    } else if (keyCode == RIGHT) {// rotate right
      r = true;
    } else if (keyCode == CONTROL){
      lidar(lidarRes, locx, locy, 120);
    }
  } 
}

void keyReleased() {
  if(key==CODED){
    if (keyCode == UP){// forward
     fw = false;
    } else if (keyCode == DOWN) {//backwads
     bw = false;
    } else if (keyCode == LEFT){//rotate left
      l = false;
    } else if (keyCode == RIGHT) {// rotate right
      r = false;
    } 
  }
}

void lidar(int angRes, float x, float y, float range){
  for(int i = 0; i<angRes; i++) {
    float angle = i*(2*PI)/angRes;
    stroke(lidarStroke);
    PVector thisLoc = new PVector(x, y);
    float curDist = range;
    PVector shortestContact = new PVector((sin(angle)*range)+x, (cos(angle)*range)+y);
    boolean isCont = false;
    
    // checks current lidar line on all vectos
    for(int xi = 0; xi<objSize; xi++){
      
    PVector cont =lineLine(x, y, (sin(angle)*range)+x, (cos(angle)*range)+y, allStart[xi].x , allStart[xi].y, allEnd[xi].x , allEnd[xi].y); // return possible contact point, if none then null
   
    //for all contact points 
    if (cont != null){
      stroke(100);// line visible if contact
      // check to see if it is shorter that the current shortest, if is, replace values
      if(thisLoc.dist(cont)<curDist){
        isCont = true;
        curDist = thisLoc.dist(cont);
        shortestContact = cont;
      }
    } 
  }
  // if contact exists, add data to global point cloud
  if(isCont){
    contact.add(shortestContact.x);
   contact.add(shortestContact.y);
  }
   // if there was no contact point line remains invisible
   line(x, y, shortestContact.x, shortestContact.y);
  }
}

// only runs lidar when mouse pressed
void mousePressed(){
  lidar(lidarRes, locx, locy, 120);
}

PVector lineLine(float x1, float y1, float x2, float y2, 
      float x3, float y3, float x4, float y4) { // takes two line and displays intecept
      
  // calculate the distance to intersection point
  float uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
  float uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));

  // if uA and uB are between 0-1, lines are colliding
  if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1) {
    // add contact point to global list
    float intersectionX = x1 + (uA * (x2-x1));
    float intersectionY = y1 + (uA * (y2-y1));
    return new PVector(intersectionX, intersectionY);
  }
  return null;
}

// takes as input forward (1) or backwards (0)
boolean validFutLoc(int fw){
  PVector futLoc;
  if(fw == 0){
  futLoc = new PVector(locx - movSpeed*sin(heading) ,locy + movSpeed*cos(heading));
  } else {
    futLoc = new PVector(locx + movSpeed*sin(heading) ,locy - movSpeed*cos(heading));
  }
 
  // checks every vector
  for(int xi = 0; xi<objSize; xi++){
  PVector cont =lineLine(locx, locy, futLoc.x, futLoc.y, allStart[xi].x , allStart[xi].y, allEnd[xi].x , allEnd[xi].y); // return possible contact point, if none then null
    //for all contact points if distance of future loc to contact point is less than bumper size, move is invalid
    if (cont != null && futLoc.dist(cont)<virtualBumperSize){
        return false;
    } 
  }
  return true;
}
