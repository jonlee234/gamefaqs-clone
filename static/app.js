// JQuery for Carosuel
$(document).ready(function () {
  $(".hero").css(
    "height",
    $(window).height() - $("header").outerHeight() + "px"
  );

  $("#scroll-hero").click(function () {
    $("html,body").animate({ scrollTop: $("#hero-bloc").height() }, "slow");
  });
});

$(window).resize(function () {
  $(".hero").css(
    "height",
    $(window).height() - $("header").outerHeight() + "px"
  );
});
// Cookie Consent
window.addEventListener("load", function () {
  window.cookieconsent.initialise({
    palette: {
      popup: {
        background: "#face02",
      },
      button: {
        background: "#7eaa41",
        text: "#face02",
      },
    },
    type: "opt-out",
    content: {
      message:
        "Cookie Notice: We and our partners use Cookies to improve and personalize your experience on the Site, measure the effectiveness of our Services, and show you ads and other content tailored to your interests as you navigate the web or interact with us across devices",
      href: "/static/assets/images/cookies.gif",
    },
  });
});
