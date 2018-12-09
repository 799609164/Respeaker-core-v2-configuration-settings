# Respeaker-core-v2-configuration-settings
配置respeaker core v2开发板，包括基本设置及Python库的安装
----------------------------------------------------
1.连接wifi：sudo nmtui

2.查看ip：ip addr

3.sudo apt-get update

4.sudo apt-get upgrade

5.更改系统时区：sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

6.更换apt清华源：
  a.sudo apt install apt-transport-https<br>
  b.cd /etc/apt<br>
  c.sudo cp -p sources.list sources.list.old<br>
  d.sudo vim sources.list<br>
  e.将sources.list内容更换为:<br>
  (在清华源网站上https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/ 找到对应版本的清华源，将sources.list当中的内容进行替换。)<br>
    # 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释<br>
    deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free<br>
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free<br>
    deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free<br>
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free<br>
    deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free<br>
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free<br>
    deb https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free<br>
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free<br>
  f.sudo apt-get update<br>

7.Python库安装
  * PyAudio: sudo apt install python3-pyaudio<br>
  * PyQt5: sudo apt-get install python3-pyqt5<br>
  * numpy: sudo apt-get install python3-numpy<br>
  * matplotlib: sudo apt-get install python3-mayplotlib<br>
  * scipy: sudo apt-get install python3-scipy<br>
  * sklearn: sudo apt-get install python3-sklearn<br>
  * hmmlearn: sudo pip3 install hmmlearn<br>
  * simplejson: sudo apt-get install python3-simplejson<br>
  * eyed3: sudo pip3 install eyed3<br>
  * pydub: sudo pip3 install pydub(需ffmpeg支持，安装：sudo apt-get install ffmpeg) <br>
  
8.ssh连接出错：删除　/home/xy/.ssh/known_hosts

9.无法显示界面：ssh　respeaker@192.168.xxx.xxx -X

[PyAudioAnalysis库](https://github.com/tyiannak/pyAudioAnalysis)
