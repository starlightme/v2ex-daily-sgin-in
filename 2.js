// ==UserScript==
// @name        a simple  script for v2ex sign
// @namespace   http://www.jimmy66.com
// @include     https://www.v2ex.com/mission/daily
// @version     1
// @grant       none
// ==/UserScript==
function autoclick() {
  var input = document.getElementsByTagName("input");
  for (var i = 0; i < input.length; i++) {
    if (input[i].getAttribute("type") == "button") {
      var button = input[i];
      button.click();
    }
  }
}
window.onload = autoclick;
