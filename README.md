##简介


  看到 [yxjxx](https://github.com/yxjxx/v2ex_daily_mission) 写的这个脚本受到启发，因为服务器端还使用的是Python2，所以就造了这个轮子，思路基本完全参照[v2ex_daily_mission](https://github.com/yxjxx/v2ex_daily_mission)这个项目，这么良心的README真是不可多得
  
  
##依赖

使用的模块有两个 **re** 和 **request**，前者是系统自带。后者可以用pip安装，如果是root用户登陆VPS可以直接安装

	
	sudo pip install requests
	
	或者
	
	pip install requests

##版本

Python2

##使用

	python v2ex.py
	
	或者,主要是对于Arch和新版Debian用户
	
	python2 v2ex.py
	
	建议使用时去除中文注释
	
##提醒

* 使用前删除中文注释
* chmod u+x v2ex.py 
* crontab -e 增加自己的配置
* crontab使用绝对路径

##Crontab

	0 5 * * * /root/python/v2ex.py >/dev/null 2>&1

设置不唯一，请参照自己的vps时间，可以借助date命令进行参考

##说明

还有些待完善的地方，欢迎帮忙提bug，前段时间因为你懂的原因，V站在国内只能用https访问，yxjxx用https估计也是基于此考虑

但是用我在Python2时发现，貌似requests用不了https（Python3中无压力）所以就改成了http，在本地可以正常地进行请求，所以估计国内VPS也能用（毕竟已经备案了）国外VPS本身就不存在问题

5月4日更新：

貌似因为中文注释，使用时报错了，另外在python2.6的vps环境下貌似无法使用

在python2.7的本地环境下成功完成签到

![v2ex](http://jimmy66.qiniudn.com/v2ex.PNG) 

5月6日更新：

去除中文注释后，在服务器端Python2.6环境下也已经运行良好，今天设置了Crontab，结果忘了加可执行熟悉，[捂脸]

明天再看下，如果正常应该就可以较为长期地自动化运行了


##感谢

yxjxx写的那篇介绍和探索真的是太棒了，让我这个摸不着头脑的小白获得了不少启发

当然最要感谢的还是Puteulanus童鞋的http请求方面知识的科普，不然我连照葫芦画瓢的底气都没有，也不可能继续深入理解下去

当然还有之前js脚本中给我点赞的月月，文科，DIYgod


##协议

Apache License 2.0

