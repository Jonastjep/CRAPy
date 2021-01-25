var n = 100;
var x = [], y = [], r = [], ang = [];
var dt = 0.015;

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}


for (i = 0; i < n; i++) {

  ang[i] = getRandomArbitrary(0, 2*Math.PI);
  r[i] = 20//Math.random() * 2 - 1;
  x[i] = r[i] * Math.cos(ang[i])
  y[i] = r[i] * Math.sin(ang[i])

}

Plotly.plot('graph', [{
  x: x,
  y: y,
  mode: 'markers'
}], {
  xaxis: {range: [-40, 40]},
  yaxis: {range: [-40, 40]}
}, {showSendToCloud:true})

function compute () {

  for (var i = 0; i < n; i++) {
    ang[i] = Math.random() * 2 - 1;
    r[i] = 20//Math.random() * 2 - 1;
    ang[i] = getRandomArbitrary(0, 2*Math.PI);
    x[i] = r[i] * Math.cos(ang[i])
    y[i] = r[i] * Math.sin(ang[i])
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
