// Automatically collapses the Bootstrap navbar when clicking outside of it on small screens
document.addEventListener("click", function (event) {
    const navbarCollapse = document.getElementById("navbarSupportedContent");
    const isClickInsideNavbar = navbarCollapse.contains(event.target);
    const isToggler = event.target.closest(".navbar-toggler");

    if (!isClickInsideNavbar && !isToggler && navbarCollapse.classList.contains("show")) {
      const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
      if (bsCollapse) {
        bsCollapse.hide();
      }
    }
});


// Script to dynamically change the navbar toggler icon:
// When the navbar is expanded (opened), it shows a "times (X)" icon.
// When the navbar is collapsed (closed), it shows the default hamburger icon.

document.addEventListener("DOMContentLoaded", function() {
    const toggler = document.getElementById("navbarToggler");
    const navbarCollapse = document.getElementById("navbarSupportedContent");

    navbarCollapse.addEventListener('shown.bs.collapse', function () {
        // Navbar is expanded
        toggler.innerHTML = '<i class="fas fa-times text-white" style="font-size: 24px;"></i>'; // FontAwesome "X" icon
    });

    navbarCollapse.addEventListener('hidden.bs.collapse', function () {
        // Navbar is collapsed
        toggler.innerHTML = '<span class="navbar-toggler-icon"></span>'; // Restore default hamburger
    });
});
