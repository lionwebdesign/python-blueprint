$(document).ready(function () {
    $(".sidenav").sidenav();
    $(".parallax").parallax();
    $('.dropdown-trigger').dropdown();
    $('.materialboxed').materialbox();
  });
  
  let scrollPosition = window.pageYOffset;
window.onscroll = function() {
    let actualScrollPosition = window.pageYOffset;
    if(scrollPosition >= actualScrollPosition) {
        document.getElementById('nav-bar').style.top = '0';
    }
    else {
        document.getElementById('nav-bar').style.top = '-100px';
    }
    scrollPosition = actualScrollPosition
}