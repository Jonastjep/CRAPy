var slider1 = document.getElementById("myRange1");
var slider2 = document.getElementById("myRange2");
var slider3 = document.getElementById("myRange3");
var slider4 = document.getElementById("myRange4");
var slider5 = document.getElementById("myRange5");
var slider6 = document.getElementById("myRange6");


var output1 = document.getElementById("ival1");
output1.innerHTML = slider1.value;

var output2 = document.getElementById("ival2");
output2.innerHTML = slider2.value;

var output3 = document.getElementById("ival3");
output3.innerHTML = slider3.value;

var output4 = document.getElementById("ival4");
output4.innerHTML = slider4.value;

var output5 = document.getElementById("ival5");
output5.innerHTML = slider5.value;

var output6 = document.getElementById("ival6");
output6.innerHTML = slider6.value;



slider1.oninput = function() {
  output1.innerHTML = this.value;
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
}

slider3.oninput = function() {
  output3.innerHTML = this.value;
}

slider4.oninput = function() {
  output4.innerHTML = this.value;
}

slider5.oninput = function() {
  output5.innerHTML = this.value;
}

slider6.oninput = function() {
  output6.innerHTML = this.value;
}

slider1.onmouseup = function () {
  document.getElementById("form").submit();
}

slider2.onmouseup = function () {
  document.getElementById("form").submit();
}

slider3.onmouseup = function () {
  document.getElementById("form").submit();
}

slider4.onmouseup = function () {
  document.getElementById("form").submit();
}

slider5.onmouseup = function () {
  document.getElementById("form").submit();
}

slider6.onmouseup = function () {
  document.getElementById("form").submit();
}



