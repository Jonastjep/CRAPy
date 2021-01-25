let canvas;

var coordinates;
const mappa = new Mappa('Leaflet');

// Can put "rastertiles/voyager" instead of "dark_all"
// http://basemaps.cartocdn.com/#15/50.8470/5.6979
const options = {
  lat: 50.84736613,
  lng: 5.70299142,
  zoom: 15,
  style: 'http://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png'
}

function preload(){
  // Here I had to add a timestamp at the end of the query link so that the browser
  //would not cache the json automatically when loading! :) Amazing that this works
  //in case there is no timestamp, the websote never updates because it considers the file as a static
  // https://stackoverflow.com/questions/15041603/how-to-prevent-the-browser-from-caching-a-json-file
  // https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file
  coordinates = loadJSON("static/coordinateOutput.json?nocache="+ (new Date()).getTime())
}

function setup(){
  canvas = createCanvas(800,700);
  myMap = mappa.tileMap(options);
  myMap.overlay(canvas);
  console.log(coordinates.coordinates.length)
}

function draw(){
  clear()
  noStroke()
  fill(0)

  for (var i = 0; i < coordinates.coordinates.length; i++) {
    let pos = myMap.latLngToPixel(coordinates.coordinates[i][0], coordinates.coordinates[i][1])
    ellipse(pos.x, pos.y, 5, 5);
  }
}
