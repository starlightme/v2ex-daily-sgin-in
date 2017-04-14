#!/bin/env python
# -*- coding : utf-8 -*-


import requests,re

username = ''      
password = ''    
login_url = 'https://v2ex.com/signin'
home_url = 'https://www.v2ex.com'
mission_url = 'https://www.v2ex.com/mission/daily'


UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"

headers = {
        "User-Agent" : UA,
        "Host" : "www.v2ex.com",
        "Referer" : "https://www.v2ex.com/signin",
        "Origin" : "https://www.v2ex.com"
        }


def main():
  s = requests.session()
  d =  {'next':'/'}  

  page1 = s.get(login_url,headers=headers).text
  once1 = re.search(r'<input type="hidden" value="([0-9]+)" name="once" />',page1).group(1)
  d['once'] = once1
  
  name_code =  re.search(r'input type="text" class="sl" name="([0-9a-z]+)"',page1).group(1)
  pwd_code  =  re.search(r'input type="password" class="sl" name="([0-9a-z]+)"',page1).group(1)
  d[name_code] =  username
  d[pwd_code]  =  password
  s.post(login_url,data=d,headers=headers)

  page2 = s.get(mission_url,headers=headers).text
  once2 = re.search(r'/mission/daily/redeem\?once=[0-9]+',page2).group(0)
  sign_url = home_url + once2
  #sign
  page3 = s.get(sign_url,headers=headers).text
  print 'finished!'



if __name__ == '__main__':
  main()

