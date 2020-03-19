function showMenu() {
      var x = document.getElementById("hidden_menu");
      var y = document.getElementsByClassName('t-site-header__menu');
      if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
  }

