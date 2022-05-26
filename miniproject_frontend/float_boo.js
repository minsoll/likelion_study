var boos = document.querySelectorAll(".Boo");
for (var i = 0; i < boos.length; i++) {
  boos[i].addEventListener("click", select);
}

function select() {
  var boo = this.getAttribute("src");
  window.open("decorate_boo.html?"+boo, "_self");
}
