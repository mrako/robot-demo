$(function(){

  var click_counter=0;

  function render_msg() {
    if (click_counter == 1) {
      return "You have clicked once";
    }
    if (click_counter > 1) {
      return "You have clicked " + click_counter + " times";
    }
  }

  function increment_clicks() {
    click_counter = click_counter + 1;
    $("div#output").text(render_msg());
  }

  if (("#js-test")[0]) {
    $('button[name="button"]').click(increment_clicks);
  }

});
