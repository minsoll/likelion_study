var bigPic = document.querySelector("#main_pic");
var smallPics = document.querySelectorAll(".mini");

for (var i = 0; i < smallPics.length; i++) {
  smallPics[i].addEventListener("click", changeimg);
}

function changeimg() {
  var smallPicAttribute = this.getAttribute("src");
  bigPic.setAttribute("src", smallPicAttribute);
}
