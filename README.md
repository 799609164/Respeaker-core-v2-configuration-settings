# Respeaker_Core_V2
配置respeaker core v2开发板，包括基本设定及Python库的安装
----------------------------------------------------
1.连接wifi： `sudo nmtui`

2.查看ip： `ip addr`

3.`sudo apt-get update`

4.`sudo apt-get upgrade`

5.更改系统时区： `sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`

6.更换apt清华源：<br>
  * `sudo apt install apt-transport-https`<br>
  * `cd /etc/apt`<br>
  * `sudo cp -p sources.list sources.list.old`<br>
  * `sudo vim sources.list`<br>
  * 将sources.list内容更换为:<br>
  (在清华源网站上https://mirror.tuna.tsinghua.edu.cn/help/debian/ 找到对应版本的清华源)<br>
   #默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释<br>
   deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free<br>
   #deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free<br>
   deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free<br>
   #deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free<br>
   deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free<br>
   #deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free<br>
   deb https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free<br>
   #deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free<br>
  * `sudo apt-get update`<br>

7.Python库安装
  * PyAudio: `sudo apt install python3-pyaudio`<br>
  * PyQt5: `sudo apt-get install python3-pyqt5`<br>
  * numpy: `sudo apt-get install python3-numpy`<br>
  * matplotlib: `sudo apt-get install python3-mayplotlib`<br>
  * scipy: `sudo apt-get install python3-scipy`<br>
  * sklearn: `sudo apt-get install python3-sklearn`<br>
  * hmmlearn: `sudo pip3 install hmmlearn`<br>
  * simplejson: `sudo apt-get install python3-simplejson`<br>
  * eyed3: `sudo pip3 install eyed3`<br>
  * pydub: `sudo pip3 install pydub`(需ffmpeg支持，安装：`sudo apt-get install ffmpeg`) <br>

# FAQs  
1.ssh连接出错：删除`/home/xy/.ssh/known_hosts`中的内容

2.无法显示PyQt5界面：`ssh　respeaker@192.168.xxx.xxx -X`

[PyAudioAnalysis库](https://github.com/tyiannak/pyAudioAnalysis)

![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544368789184&di=062d69406e794ae6d836b7ca387a6563&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fw%3D580%2Fsign%3D3d21336dfb039245a1b5e107b795a4a8%2F277603d3d539b600c41cca17ee50352ac45cb7fd.jpg)  
