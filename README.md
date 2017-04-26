## Introduction ##

`v2ex.py` is a simple python scrpit that you can use it to automatically sign up v2ex daily.

Inspired by [v2ex\_daily\_mission](https://github.com/yxjxx/v2ex_daily_mission) project and create this project for `Python2` users and easier employment in `vps`.



## Package Requirements ##


* `re`
* `requests`

`re` is already contained in default python program so you don't need to install it, while you should install `requests` library by youself before you use this script.

	sudo pip install requests
	
## Version

**Python2**

## Usage ##

	python v2ex.py
	
Or in the other way, suits to users of ArchLinux or  Debian 8 system
	
	python2 v2ex.py
	

## Reminder ##

* Fill your v2ex username and password in the code
* Remove all chinese comments before you use it
* `chmod u+x v2ex.py`
* Make sure `cron` processing is running. You can get a reference from this [tutorial](http://www.cyberciti.biz/faq/howto-linux-unix-start-restart-cron/)
* `corntab -e` add your setting
* Use absolute path in `crontab` setting
* Make sure the role of script owner and crontab mission creater are the same


## Crontab ##

	0 5 * * * python /root/python/v2ex.py >/dev/null 2>&1
	
Crontab setting is not unique. You need to set it according to the datetime of your `vps` which can be got by using `date` command.

## Screenshoot ##
![v2ex_sign_in](http://7o52g5.com1.z0.glb.clouddn.com/屏幕快照%202015-12-11%20下午5.13.28.jpg)

## Gratitude List ##

* yxjxx
* Puteulanus
* yuetsh
* wenketel
* DIYgod

## License ##

Apache License 2.0
