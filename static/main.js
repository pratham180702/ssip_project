menu = document.getElementById("mobile-nav");

function MobileMenu() {
  console.log("asdasdhb");
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
  } else {
    menu.classList.add("hidden");
  }
}
