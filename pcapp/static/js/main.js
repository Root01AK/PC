// Scroll Effect SATRT
window.onscroll = function()
{topbar()};

let topButton = document.getElementById('topnav');

function topbar() {
  if(document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("topbar").style.top = "0";
    topButton.style.display = "block";
  } else {
    document.getElementById("topbar").style.top = "-100px";
    topButton.style.display = "none";
  }
}
// Scroll Efeect END

// GoTop Button Effect START
function goTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;

  document.body.style.scrollBehavior = 'smooth';
  document.documentElement.style.scrollBehavior = 'smooth';

  setTimeout(() => {
    document.body.style.scrollBehavior = 'smooth';
    document.documentElement.style.scrollBehavior = 'smooth';
  }, 1000);
}
// GoTop Button Effect END

// CopRights Automatice Year Running START
const year = document.getElementById('curentYear');
year.innerHTML = new Date().getFullYear();
// CopRights Automatice Year Running END

// PopUp Form Open & Close Function START
function openForm() {
  var openForm = document.getElementById('myForm');
  var bgForm = document.getElementById('form-bg');
  bgForm.classList.add('form-bg');
  openForm.style.display = "block";
  openForm.offsetHeight;
  openForm.style.opacity = "1";    
}

function closeForm() {
  var closeForm = document.getElementById('myForm');
  var bgForm = document.getElementById('form-bg');

  closeForm.style.opacity = "0";

  bgForm.classList.remove('form-bg');

  setTimeout(function () {
    close.style.display = "none";
  }, 500);
}
// PopUp Form Open & Close Function START

// Humbuger Toggle Function SATRT
const toggleBtn = document.querySelector('.toggle-btn');
const toggleBtnIcon = document.querySelector('.toggle-btn i');
const dropDownMenu = document.querySelector('.dropdown-menu');

toggleBtn.onclick = function () {
  dropDownMenu.classList.toggle('open');
}
// Humbuger Toggle Function END


// Blog AutoPlay START
$('.owl-carousel').owlCarousel({
  loop: true,
  autoplay: true,
  autoplayTimeout: 2000, //2000ms = 2s;
  autoplayHoverPause: true,
  responsive:{
      0:{
          items:1,
      },
      600:{
          items:2,
      },
      1000:{
          items:3,
          loop:true
      }
  }
});
// Blog AutoPlay END