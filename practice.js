(function () {
  try {
    function checklist() {
      const none = document.getElementById("none");
      const button = document.getElementsByClassName(
        "btn btn--primary btn--block btn--m"
      );
      none.click();
      button[0].click();
    }

    function vaccinated() {
      const buttons = document.getElementsByClassName(
        "btn btn--primary btn--block btn--m"
      );
      for (let button of buttons) {
        if (button.innerText.toLowerCase() == "yes") {
          button.click();
        }
      }
    }

    function test() {
      const buttons = document.getElementsByClassName(
        "btn btn--primary btn--block btn--m"
      );
      for (let button of buttons) {
        if (button.innerText.toLowerCase() == "no") {
          button.click();
        }
      }

      if (buttons.length == 0) {
        alert("Done");
        return; // exit
      }
    }
  } finally {
    checklist();
    vaccinated();
    test();
  }
})();
