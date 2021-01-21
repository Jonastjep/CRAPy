console.log("IN THE LOOP")
var slider1 = document.getElementById("myRange1");
var slider2 = document.getElementById("myRange2");

var output1 = document.getElementById("val1");
output1.innerHTML = slider1.value;

var output2 = document.getElementById("val2");
output2.innerHTML = slider2.value;

slider1.oninput = function() {
  output1.innerHTML = this.value;
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
}

slider1.onmouseup = function () {
  document.getElementById("form").submit();
}

slider2.onmouseup = function () {
  document.getElementById("form").submit();
}

