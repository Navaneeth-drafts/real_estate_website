'use strict';


/**
 * navbar toggle in mobile
 */

const /** {NodeElement} */ $navbar = document.querySelector("[data-navbar]");
const $navToggler   = document.querySelector("[data-nav-toggler]");

$navToggler.addEventListener("click", () => {
    $navbar.classList.toggle("active");
    // $navToggler.classList.toggle("active");
});

// header scroll state

const /** {NodeElement} */ $header = document.querySelector("[data-header]");
window.addEventListener("scroll", e => {
    $header.classList[window.scrollY > 50 ? "add" : "remove"]("active");
});


// adding to favourite button toggle
  const/**  {nodelist}*/ $toggleBtns = document.querySelectorAll("[data-toggle-btn]");

  $toggleBtns.forEach($toggleBtn => {
    $toggleBtn.addEventListener("click", () => {
      $toggleBtn.classList.toggle("active");
    });
  });   