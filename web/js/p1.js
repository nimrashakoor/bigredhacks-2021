//timer
var num = document.getElementById("count");
var add = document.getElementById("add");
var minus = document.getElementById("minus");

var count = 0;

add.addEventListener("click", () => {
  count++;
  updateDisplay();
});

minus.addEventListener("click", () => {
  count--;
  updateDisplay();
});

function updateDisplay() {
  num.innerHTML = count;
};

updateDisplay();