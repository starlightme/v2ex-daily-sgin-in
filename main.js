// ==UserScript==
// @name        a simple  script for v2ex sign
// @namespace   http://www.jimmy66.com
// @include     https://www.v2ex.com/*
// @version     1
// @grant       none
// ==/UserScript==
/*进入签到页面*/
function autoclick1() {
  var a = document.getElementsByTagName('a');
  for (var i = 0; i < a.length; i++) {
    if (a[i].firstChild.nodeValue == '领取今日的登录奖励') {
      var link = a[i];
      link.click();
      return 1;
    }
  }
  return 0;
}
/*点击按钮签到，有待修改*/
function autoclick2() {
  var input = document.getElementsByTagName('input');
  for (var i = 0; i < input.length; i++) {
    if (input[i].getAttribute('type') == 'button') {
      var button = input[i];
      button.click();
      return 1;
    }
  }
  return 0;
}
window.onload = function () {
  autoclick1();
  autoclick2();
//  setTimeout('autoclick2()', 1000);
}
