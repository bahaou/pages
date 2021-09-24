$(document).ready(function(){
scrollFunction()
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    $("#navbar").removeClass("navtransparent");
  } else {
    $("#navbar").addClass("navtransparent");
  }
}

});
