# Respeaker_Core_V2
配置respeaker core v2开发板，包括基本设定及Python库的安装
----------------------------------------------------
1.Linux串口通信：<br>
 `ls /dev/ttyACM*`<br>
 `sudo minicom -s`　选择`Serial port setup`进行配置<br>
 或者`sudo screen /dev/ttyACM*  115200`

2.连接wifi：`sudo nmtui`

3.查看ip：`ip addr`

4.<br>`sudo apt-get update`<br> `sudo apt-get upgrade`

5.更改系统时区：`sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`

6.修改主机名：<br>
`sudo vim /etc/hosts`　添加　`127.0.0.1　localhsot 修改的主机名`<br>
`sudo vim /etc/hostname`　修改主机名

7.更换apt清华源(换源有风险换前需谨慎)：<br>
  * `sudo apt install apt-transport-https`<br>
  * `cd /etc/apt`<br>
  * `sudo cp -p sources.list sources.list.old`<br>
  * `sudo vim sources.list`<br>
  * 将sources.list内容更换为：<br>
  (在清华源网站上https://mirror.tuna.tsinghua.edu.cn/help/debian/ 找到对应版本的清华源)<br>
   `#默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释`<br>
   `deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free`<br>
   `#deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free`<br>
   `deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free`<br>
   `#deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free`<br>
   `deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free`<br>
   `#deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free`<br>
   `deb https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free`<br>
   `#deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free`<br>
  * `sudo apt-get update`<br>

8.Python库安装
  * PyAudio：`sudo apt install python3-pyaudio`<br>
  * PyQt5：`sudo apt-get install python3-pyqt5`<br>
  * numpy：`sudo apt-get install python3-numpy`<br>
  * matplotlib：`sudo apt-get install python3-mayplotlib`<br>
  * scipy：`sudo apt-get install python3-scipy`<br>
  * sklearn：`sudo apt-get install python3-sklearn`<br>
  * hmmlearn：`sudo pip3 install hmmlearn`<br>
  * simplejson：`sudo apt-get install python3-simplejson`<br>
  * eyed3：`sudo pip3 install eyed3`<br>
  * pydub：`sudo pip3 install pydub`(需ffmpeg支持，安装：`sudo apt-get install ffmpeg`) <br>
  * evdev：`sudp pip3 install evdev`<br>

9.系统备份：`sudo dd if=/dev/sdc of=Desktop/respeaker.img bs=4MB`<br>

10.设置python程序自启动
* 新增文件：`sudo vim /etc/systemd/system/rc-local.service`<br>
	 文件内容<br>
 `[Unit]`<br>
`Description=/etc/rc.local`<br>
`ConditionPathExists=/etc/rc.local`<br>

	`[Service]`<br>
`Type=forking`<br>
`ExecStart=/etc/rc.local start`<br>
`TimeoutSec=0`<br>
`StandardOutput=tty`<br>
`RemainAfterExit=yes`<br>
`SysVStartPriority=99`<br>
 
	`[Install]`<br>
`WantedBy=multi-user.target`<br>
* 新增文件：`sudo vim /etc/rc.local`<br>
  文件内容<br>
 `#!/bin/sh -e`<br>
  `#`<br>
  `# rc.local`<br>
  `#`<br>
  `# This script is executed at the end of each multiuser runlevel.`<br>
  `# Make sure that the script will "exit 0" on success or any other`<br>
  `# value on error.`<br>
  `#`<br>
  `# In order to enable or disable this script just change the execution`<br>
  `# bits.`<br>
  `#`<br>
  `# By default this script does nothing.`<br>

  `sudo /usr/bin/python3 /home/respeaker/recorder/*.py`<br>
  `export PYTHONPATH=$PYTHONPATH:"/home/respeaker/model/pyAudioAnalysis"`<br>
  `exit 0`<br>
  
 * 添加权限：`sudo chmod +x /etc/rc.local`
 * 设置到系统启动：`sudo systemctl enable rc-local`
 * 启动脚本：`sudo systemctl start rc-local.service`
 * 查看服务状态：`sudo systemctl status rc-local.service`
  
# FAQs
1.ssh连接失败：删除`/home/xy/.ssh/known_hosts`中的内容

2.无法显示PyQt5界面：`ssh　respeaker@192.168.xxx.xxx -X`

3.sudo python3情况下无法导入模块：<br>
  * `sudo vim /etc/sudoers`<br>
  * 注释掉`Defaults    env_reset`<br>
  * 添加<br>
  `Defaults    env_keep += "PYTHONPATH"`<br>
  `Defaults    env_keep += "/home/respeaker/model/pyAudioAnalysis"`<br>
 
[PyAudioAnalysis库](https://github.com/tyiannak/pyAudioAnalysis)

![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544368789184&di=062d69406e794ae6d836b7ca387a6563&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fw%3D580%2Fsign%3D3d21336dfb039245a1b5e107b795a4a8%2F277603d3d539b600c41cca17ee50352ac45cb7fd.jpg)  
