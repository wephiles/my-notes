<h1 style="text-align: center;font-size: 40px; font-family: '楷体';">文件和用户管理 - day08</h1>

[TOC]

# 1 文件管理

## 1.1 `Linux`目录结构简介

`windows`：以多根的方式组织文件

`Linux`：以单根的方式组织文件

## 1.2 Linux目录结构

```bash
- /                 【根目录】
	- /root         【系统超级管理员的目录】
		- /root/Desktop
		- ...
	- /bin          【Binary 最经常使用的常用命令的目录】
	- /sbin         【s:system 存放的是系统管理员使用的系统管理程序】
	- /boot         【挂载点 引导分区所挂载的地方 系统启动的时候所需的东西】
	- /dev          【devices 管理设备的文件】
	- /etc          【主要放置一些系统管理的配置文件】
	- /home         【每个用户都有一个自己的主目录 都放在HOME目录下】
	- /var          【可变的东西 一般村log】
	- /opt          【optional 可选目录 第三方软件存到这儿】
	- /lib          【库 系统和应用所需要的共享库】
	- /lib64        【64位相关的库】
	- /usr          【用户所有的应用程序和所需要的文件和数据】
		- /usr/bin
		- /usr/lib
		- ...
	- /media        【识别可移动媒体设备 比如U盘等】
	- mnt           【也是一个挂载点】
	- proc          【进程管理的相关信息】
	- run           【存放当前系统云心信息】
	- srv           【和系统服务相关】
	- sys           【系统相关的信息】
	- tmp           【临时目录 可以删除】
```

## 1.3 文件管理命令

### 1.3.1 cd

通往其他文件夹 -- 切换目录

# 2 用户管理





































