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
