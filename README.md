##Introduction

`v2ex.py` is a simple python scrpit that you can use it to automatically sign up v2ex daily.

Inspired by [v2ex\_daily\_mission](https://github.com/yxjxx/v2ex_daily_mission) project and create this project for `Python2` users and easier employment in `vps`.

You can view more details or find chinese instruction in the [`README_cn.md`](https://github.com/starlightme/v2ex-daily-sgin-in/blob/master/README_CN.md)  and [`v2ex_original.py`](https://github.com/starlightme/v2ex-daily-sgin-in/blob/master/v2ex_original.py).


##Package Requirements 


* `re`
* `requests`

`re` is already contained in default python program so you don't need to install it, while you should install `requests` library by youself before you use this script.

	sudo pip install requests
	
##Version

**Python2**

##Usage##

	python v2ex.py
	
Or in the other way, suits to users of ArchLinux or  Debian 8 system
	
	python2 v2ex.py
	

##Reminder##

* fill your v2ex username and password in the code
* Remove all chinese comments before you use it
* `chmod u+x v2ex.py`
* `corntab -e` add your setting
* use absolute direction in `crontab` setting
* make sure the role of script owner and crontab mission creater are the same

##Crontab##

	0 5 * * * python /root/python/v2ex.py >/dev/null 2>&1
	
Crontab setting is not unique. You need to set it according to the datetime of your `vps` which can be got by using `date` command.

##Screenshoot##
![v2ex_sign_in](http://7o52g5.com1.z0.glb.clouddn.com/屏幕快照%202015-12-11%20下午5.13.28.jpg)

##Gratitude List##

* yxjxx
* Puteulanus
* yuetsh
* wenketel
* DIYgod

##License

Apache License 2.0