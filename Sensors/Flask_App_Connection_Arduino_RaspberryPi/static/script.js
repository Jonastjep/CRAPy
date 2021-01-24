// Our labels along the x-axis
var poop;

fetch("static/arduino_data.json?nocache="+(new Date()).getTime())
.then(response => {
  return response.json();
})
.then(data => {
  poop = data
  console.log(poop);

  var timestamp = poop["datetime"];
  // For drawing the lines
  var ultrasound = poop["ultrasound"];
  var air_composition = poop["air_composition"];
  var temperature = poop["temperature"];
  var humidity = poop["humidity"];



  var ctx = document.getElementById('air_composition_data');
  var air_composition_data = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
      labels: timestamp,
      datasets: [
        {
          data: air_composition,
          label: "Air Composition Sensor Data",
          borderColor: "#8f924e",
          fill: false
        } ]
      },
      options: {
        scales: {
          xAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Date of Data Recording'
            },
            ticks: {
              major: {
                fontStyle: 'bold',
                fontColor: '#FF0000'
              }
            }
          } ],
          yAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Presence of methane, propane, CO2, smoke hydrogen, CO (ppm)'
            }
          } ]
        }
      }
    }
  );
  var ctx = document.getElementById('temperature_data');
  var temperature_data = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
      labels: timestamp,
      datasets: [
        {
          data: temperature,
          label: "Temperature Sensor Data",
          borderColor: "#c47c5f",
          fill: false
        } ]
      },
      options: {
        scales: {
          xAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Date of Data Recording'
            },
            ticks: {
              major: {
                fontStyle: 'bold',
                fontColor: '#FF0000'
              }
            }
          } ],
          yAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Temperature (C°)'
            }
          } ]
        }
      }
    }
  );
  var ctx = document.getElementById('humidity_data');
  var humidity_data = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
      labels: timestamp,
      datasets: [
        {
          data: humidity,
          label: "Humidity Distance Sensor Data",
          borderColor: "#772f67",
          fill: false
        } ]
      },
      options: {
        scales: {
          xAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Date of Data Recording'
            },
            ticks: {
              major: {
                fontStyle: 'bold',
                fontColor: '#FF0000'
              }
            }
          } ],
          yAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Humidity %'
            }
          } ]
        }
      }
    }
  );
  var ctx = document.getElementById('pressure_data');
  var pressure_data = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
      labels: timestamp,
      datasets: [ {
        data: pressure,
        label: "Pressure Sensor Data",
        borderColor: "#3e95cd",
        fill: false
      } ]
    },
    options: {
      scales: {
        xAxes: [ {
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Date of Data Recording'
          },
          ticks: {
            major: {
              fontStyle: 'bold',
              fontColor: '#FF0000'
            }
          }
        } ],
        yAxes: [ {
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Pressure (hPa)'
              }
            } ]
          }
        }
      }
    );
    var ctx = document.getElementById('altitude_data');
    var pressure_data = new Chart(ctx, {
      // The type of chart we want to create
      type: 'line',
      // The data for our dataset
      data: {
        labels: timestamp,
        datasets: [ {
          data: altitude,
          label: "Altitude Sensor Data",
          borderColor: "#4c3ecd",
          fill: false
        } ]
      },
      options: {
        scales: {
          xAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Date of Data Recording'
            },
            ticks: {
              major: {
                fontStyle: 'bold',
                fontColor: '#FF0000'
              }
            }
          } ],
          yAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Altitude (m))'
                }
              } ]
            }
          }
        }
      );
      var ctx = document.getElementById('moisture_of_the_soil_data');
      var moisture_of_the_soil_data = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',
        // The data for our dataset
        data: {
          labels: timestamp,
          datasets: [ {
            data: moisture_of_the_soil,
            label: "Soil Moisture Sensor Data",
            borderColor: "#4c3ecd",
            fill: false
          } ]
        },
        options: {
          scales: {
            xAxes: [ {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Date of Data Recording'
              },
              ticks: {
                major: {
                  fontStyle: 'bold',
                  fontColor: '#FF0000'
                }
              }
            } ],
            yAxes: [ {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Moisture (relative))'
                  }
                } ]
              }
            }
          }
        );
});




// Configuration options go here
// options: {

//}
