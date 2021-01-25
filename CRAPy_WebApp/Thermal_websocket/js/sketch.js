// Open Connection to the Server
var ws = new WebSocket("ws://192.168.4.1:5678/");
ws.onmessage = function (event) {
  window.sensordata = JSON.parse(event.data);
  // window.sensordata = event.data;
};
const scaling = 10
var data = []

function setup() {
  // put setup code here
  createCanvas(window.innerWidth, window.innerHeight);
  noStroke();
  frameRate(10);
}
var ti = 0

function draw() {
  // Get the sensor variables defined if they exist
  if(typeof window.sensordata === "undefined"){
    // hard code the vars to avoid error
    data = null
    // let data = []
    // for (let i = 0; i < 50 ; i++){
    //   data.push([])
    //   for (var j = 0; i < 50; i++) {
    //     data[i][j] = random(0,1)
    //   }
    // }
    // console.log(window.sensordata);
  } else {
    // read them from the sensors
    data = window.sensordata.data;
  }

  // console.log(data[0])
  // The drawing
  //    background(0);
  // rectMode(CENTER);

  // to protect from empty array
  if (data == null){

  }
  else{
    for(let i = 0; i < 64; i++){
      for(let j = 0; j < 64; j++){
        fill(data[i][j])
        rect(i*scaling,j*scaling,scaling,scaling)
      }
    }
  }
}
