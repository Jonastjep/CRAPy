// Open Connection to the Server
var ws = new WebSocket("ws://127.0.0.1:5678/");
ws.onmessage = function (event) {
  window.sensordata = JSON.parse(event.data);
  // window.sensordata = event.data;
};

var x = []
var y = []
var ang = []
var d = []
if(typeof window.sensordata === "undefined"){
  d = [0]
  ang = [0]
}else {
  d = window.sensordata.d
  ang = window.sensordata.ang
}

for (i = 0; i < ang.length; i++) {

  x[i] = d[i] * Math.cos(ang[i]* (Math.PI/180))
  y[i] = d[i] * Math.sin(ang[i]* (Math.PI/180))

}
Plotly.plot('graph', [{
  x: x,
  y: y,
  mode: 'markers'
}], {
  autosize: false,
  width: 500,
  height: 500
  xaxis: {range: [-500, 500]},
  yaxis: {range: [-500, 500]}
}, {showSendToCloud:true})

function compute () {

  if(typeof window.sensordata === "undefined"){
    d = [0]
    ang = [0]
  }else {
    d = window.sensordata.d
    ang = window.sensordata.ang
  }
  for (i = 0; i < ang.length; i++) {

  x[i] = d[i] * Math.cos(ang[i]* (Math.PI/180))
  y[i] = d[i] * Math.sin(ang[i]* (Math.PI/180))

  }
}

function update () {
  compute();

  Plotly.animate('graph', {
    data: [{x: x, y: y}]
  }, {
    transition: {
      duration: 0,
    },
    frame: {
      duration: 0,
      redraw: false,
    }
  });

  requestAnimationFrame(update);
}

requestAnimationFrame(update);
