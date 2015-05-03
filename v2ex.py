#!/bin/env python
# -*- coding : utf-8 -*-

#导入模块
import requests,re

username = ''      #用户名
password = ''    #密码
login_url = 'http://v2ex.com/signin'
home_url = 'http://www.v2ex.com'
mission_url = 'http://www.v2ex.com/mission/daily'


UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"

headers = {
        "User-Agent" : UA,
        "Host" : "www.v2ex.com",
        "Referer" : "https://www.v2ex.com/signin",
        "Origin" : "https://www.v2ex.com"
        }


def main():
  s = requests.session()
  d = {'u':username,'p':password,'next':'/'}
  page1 = s.get(login_url,headers=headers).text
  #利用正则取出第一次的once值
  once1 = re.search(r'<input type="hidden" value="([0-9]+)" name="once" />',page1).group(1)
  d['once'] = once1
  #模拟登陆
  s.post(login_url,data=d,headers=headers)
  page2 = s.get(mission_url,headers=headers).text
  #取出第二次的once，这次进行字符串拼接成url后用get请求进行签到
  once2 = re.search(r'/mission/daily/redeem\?once=[0-9]+',page2).group(0)
  sign_url = home_url + once2
  #签到
  page3 = s.get(sign_url,headers=headers).text


if __name__ == '__main__':
  main()