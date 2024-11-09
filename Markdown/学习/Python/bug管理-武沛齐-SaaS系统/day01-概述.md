<h1 style="font-family: 'Menlo'; text-align: center;">SaaS平台 -- 项目概述</h1>

[TOC]

# 1、 如何学 & 如何讲

1、守规则，实事求是

2、主要任务

3、写代码

# 2、涉及知识点

- 虚拟环境

    在电脑上创建多个`Python`环境。

- `local_settings.py` 本地配置

    ```python
    你是开发:
    	链接数据库需要在Django的settings中设置，链接的数据库IP:1.1.1.1
        
    我是测试:
    	链接数据库需要在Django的settings中设置，链接的数据库IP:1.1.1.2
    ```

    在`settings.py`中，加入下面这些代码:

    ```python
    # settings.py
    try:
        from .local_settings import *
    except ImportError:
        pass
    ```

    在`local_settings.py`中写一些自己的的东西，可以覆盖`setting.py`的数据:

    ```python
    ...
    LANGUAGE_CODE = 'zh-hans'
    ...
    ```

    除了`local_settings.py`，其他的都发给测试。测试自己再写一个自己的`local_settings.py`文件，写上测试用的相关数据即可。

- 腾讯云平台（免费额度）

    - `sms` -- 云短信 -- 发送短信 -- 申请服务
    - `cos`对象存储，腾讯给了云硬盘，项目中要上传/查看/下载文件 

- `redis` 

    ```python
    MySQL:
        自己的电脑                   别人的电脑
        pymysql          ->         MySQL  -> 行为  -> 文件操作 -> 硬盘要比较大       
    Redis:
        自己的电脑                   别人的电脑  
        redis            ->         Redis软件  -> 行为  内存上操作 ->  内存要比较大
                                                set name="xxx" -> 在内存中 name="xxx"
                                                超时时间
    # 注意:
    可以将两台电脑放在同一台电脑上（本地测试）
    ```

# 3、 项目开发

- 一期：用户认证 （注册 登录 短信验证 图片验证码,`Django`的`ModelForm`组件）-   3天
- 二期：`wiki`、文件、问题管理  -   1 + 2 + 2  5 ~ 7天
- 三期：支付、部署（Linux基础视频） - 1 + 1 天 































































































































































