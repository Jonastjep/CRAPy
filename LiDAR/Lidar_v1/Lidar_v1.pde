float pointx = 0;
float pointy = 0;
PShape shapeEx = makeShape();


void setup(){
  size(600, 400);
}

void draw(){
  background(255);
  
  // draw basic environment
  //shape(shapeEx);
  
    //stroke(100);
    //fill(0);
    //beginShape();
    //for(int x =0; x<10; x++){
    //  float xval = vectorList[x].x * 100;
    //  float yval = vectorList[x].y *100;
    //  vertex(xval + 3*width/4, yval+ 3*height/4);
    //}
    //vertex(vectorList[0].x *100, vectorList[0].y * 100);
    //endShape(CLOSE);
    
    //stroke(100);
    //fill(0);
    //beginShape();
    //for(int x =0; x<10; x++){
    //  float xval = vectorList2[x].x * 100;
    //  float yval = vectorList2[x].y *100;
    //  vertex(xval +width/4, yval+height/4);
    //}
    //vertex(vectorList2[0].x *100, vectorList2[0].y * 100);
    //endShape(CLOSE);
    
  pointx = mouseX; // set position to mouse location
  pointy = mouseY;
  circle(pointx, pointy, 5);
}

void mousePressed(){
  stroke(100);
  lidar(20, pointx, pointy, 150); 
}

void lidar(int angRes, float x, float y, float range){
  for(int i = 0; i<angRes; i++) {
    float angle = i*(2*PI)/angRes;
    stroke(100);
    line(x, y, (sin(angle)*range)+x, (cos(angle)*range)+y);
  }
}

PShape makeShape(){
  PShape shape = createShape();
  int n_vertex = int(random(3, 7)); 
  shape.beginShape(); 
  for (int i = 0; i < n_vertex; i++) { 
    shape.vertex(random(width), random(height)); 
  } 
  shape.endShape(CLOSE);
  return shape;
}
