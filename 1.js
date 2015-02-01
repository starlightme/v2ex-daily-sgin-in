// ==UserScript==
// @name        a simple  script for v2ex sign
// @namespace   http://www.jimmy66.com
// @include     https://www.v2ex.com/
// @version     1
// @grant       none
// ==/UserScript==
function autoclick() {
  var a = document.getElementsByTagName('a');
  for (var i = 0; i < a.length; i++) {
    if (a[i].firstChild.nodeValue == '领取今日的登录奖励') {
      var link = a[i];
      link.click();
      return true;
    }
  }
}
window.onload = autoclick;
