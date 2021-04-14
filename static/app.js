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
