##Introduction

`v2ex.py` is a simple python scrpit that you can use it to automatically sign up v2ex daily.

Inspired by [v2ex\_daily\_mission](https://github.com/yxjxx/v2ex_daily_mission) project and create this project for `Python2` users and easier employment in `vps`.

You can view more details or find chinese instruction in the `README_cn.md`  and `v2ex_original.py`.


##Package Requirements 


* `re`
* `requests`

`re` is already contained in default python program so you don't need to install it, while you should install requests library by youself before you use this script.

	sudo pip install requests
	
##Version

**Python2**

##Usage##

	python v2ex.py
	
	or in the other way, suit to users of Arch or Debian
	
	python2 v2ex.py
	

##Reminder##

* Remove all chinese comments before you use it
* `chmod u+x v2ex.py`
* `corntab -e` add your setting
* use absolute direction in `crontab` setting

##Crontab

	0 5 * * * python /root/python/v2ex.py >/dev/null 2>&1
	
Crontab setting is not unique. You need to set it according to the datetime of your `vps` which can be got by using `date` command.

##Gratitude List##

* yxjxx
* Puteulanus
* yuetsh
* wenketel
* DIYgod

##License

Apache License 2.0