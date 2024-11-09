<h1 style="font-size: 50px; text-align: center; font-family: '楷体'">
    python Web 学习
</h1>
[TOC]

# `WEB`

## 注意：

如果本文件的图片不可显示时，将文件的路径改为相对路径既可。
即 `../../images/文件名.png`

## 基础

-   `ASCII`码中一个字节表示一个字符

-   `gbk`和 `gbk-2312 `

    -   `gbk-2312` 国家信息委员会制作 `1980`

    -   `gbk` 包含中日韩等文字

-   `Unicode` 万国码

    -   `utf-8` 对`unicode`压缩存储 用尽可能少的空间存储尽可能多的文字

    -   `utf-8`中 一个中文用3个字节表示

-   `python`中 `name = 'buweishi'`  在内存中使用`unicode`存储——`ucs4`

-   `name.encode('utf-8')` 将数据压缩成`utf-8`编码存储 

-   以后在`python`开发中 不能用默认编码 一般要压缩成`utf-8`编码才进行操作

-   文件编码：

    -   写文件  按照某种编码去存储文件 

    -   读文件 用同样的编码去读取内容

        ```python
        # python解释器编码 指的是打开和读取某个py文件的内容时 用的这种编码 - utf-8
        # 词法分析 & 语法分析
        name = '卜伟仕'     ->     当做字符串处理 去unicode对应关系中找 010101010101
        age = b'buweishi'   ->     字节 去utf-8对应关系中找 01010101
        ```
    
    -   还要进行词法和语法的解析 

### 数据类型

-   布尔类型   `bool`   `True/False`

    -   `0 "" [] () {} set()`  --> 都是`False`

-   整型       `int`    `15 23 100`

-   字符串     `str`    `'buweishi'`
    -   `str.upper()` 全部变大写

-   列表       `list`   `[1, 2, 3]`

-   元组       `tuple`  `(1, 2, 3)` 

-   字典       `dict`   `{'k1': 123, 'k2': 456}`
    -   `key`必须是可哈希的类型

    -   可哈希的类型 —— `int bool str tuple`

    -   不可哈希 —— 列表 字典

    -   `get`函数 参数是键值和一个其他值 返回键对应的值 如果不存在那么返回第二个值
      
        ```python
        # 举例子
        info = {
            'k1': 10,
            'k2': '123'
        }
        >>> info.get('k1', 'xxx') 
        	10
        >>> info.get('k3', 'xxx')
        	'xxx'
        ```
        
    -   `info.keys()` 获取所有键 可以循环 `python` `for item in info.keys:...`
    
-   集合

### 函数

-   面向过程
-   函数式编程
-   函数的关键字参数必须在位置参数的后面
-   装饰器
    -   特殊闭包函数

### `python`代码发邮件

*   注册邮箱 网易`126 163`邮箱

*   `设置 --> POP3/SMTP --> 开启POP3/SMTP --> 授权码为XXXXXXXXXXXXXX（我的保存在幕布中 输入密码即可获得）`

*   `SQWQBNIXGLDDTUXU 和 LFVCWRIDMGLDZNQS`

*   授权码 —— 目的是为了使用代码发邮件，防止代码丢失 不需要账号密码 只需要授权码和账号就可以发邮箱

*   保存好自己的授权码 不要泄露给别人

*   `SMTP`服务器 `smtp.126.com` 要用

*   发邮件的流程 

    *   网易平台

    *   目标邮箱

    *   代码 账户/授权码/邮件信息/目标邮箱 —— 发给网易平台

    *   代码发邮件
        ```python
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr
        
        
        def send_email():
            """发邮箱。"""
            # 构建邮件内容
            msg = MIMEText('这是一个邮件，用于测试！', 'html', 'utf-8')  # 内容
            msg['From'] = formataddr(('瑾瑜', 'jinyu20866@126.com'))  # 自己的名字和邮箱
            msg['To'] = '2086689759@qq.com'  # 要发给别人的邮箱
            msg['Subject'] = '测试'  # 主题
        
            # 发送邮件
            server = smtplib.SMTP_SSL('smtp.126.com')  # smtp
            server.login('jinyu20866@126.com', 'LFVCWRIDMGLDZNQS')  # 登录自己的邮箱
        
            # 自己的邮箱 别人的邮箱 以字符串的形式发送
            server.sendmail('jinyu20866@126.com', '2086689759@qq.com', msg.as_string())
            server.quit()
        ```

### 函数参数

-   `*args` ：    --> 表示传入的参数只能是位置参数   传入后都会被打包成元组
    -   元组
        -   `([1, 2, 3])/(1)/('a')`      分别会被识别成 列表/整数/字符串 
        -   `([1, 2, 3],)/(1,)/('a',)`   会被识别成元组
-   `**kwargs` ： --> 表示传入的参数只能是关键字参数 传入后都会被打包成字典
    -   要求：必须用关键字的形式传参
-   顺序必须是 先 `*args` 再 `**kwargs`
-   当不传参的时候 `args`和`kwargs`都是空的

### 内置函数

-   直接拿过来用 `python`内置的函数

-   第一组

    ```python
    abs             绝对值
    pow             平方
    sum             求和
    v1, v2 = divmod 取商和余数
    round           保留小数点后几位
    ```

-   第二组

    ```python
    min 最小值
    max 最大值
    all 是否所有列表元素布尔值是否都是True
    any 只要有为True的，则返回True
    ```

-   第三组

    ```python
    bin 十进制转二进制
    oct 十进制转八进制
    hex 十进制转十六进制
    ord 转换文本为二进制（ASCII码）
    chr 转换二进制位文本（ASCII码）
    
    int
    str
    bool
    list
    dict
    set
    tuple
    float
    bytes
    
    len
    print
    input
    open
    range
    hash       计算哈希值 字典的键 集合元素必须都是可哈希的
    type
    callable   是否可执行
    enumerate  循环过程中 自动提供一列 自增的一列
    sorted     排序 列表中的sort()方法只能对原列表排序
    ```

    ```python
    goods = ['飞机', '迫击炮', 'AK47', '东风41']
    for i in range(len(goods)):
        msg = '{} {}'.format(i+1, goods[i])
        print(msg)
        
    # 执行结果
    1 飞机
    2 迫击炮
    3 AK47
    4 东风41
    
    # 直接用enumerate做：
    for index, item in enumerate(goods, 1):
        msg = '{} {}'.format(index, item)
        print(msg)
    ```

    

### 函数做参数

-   一般情况下少用

```python
def do():
    print('do')

def func(a1, a2):
    print(a1)
    a2()

func(11, do)
```

```python
# 上面代码块的运行结果：
11
do
```

```python
def do():
    print('do')

def func(a1, a2):
    print(a1)
    res = a2()
    print(res)
    return 123

v1 = func(11, do)
print(v1)
```

```python
# 上面代码块代码执行结果为：
11
do
None
123
```

### 模块和包

-   模块 —— `python`中的一个`.py`文件 将某些功能按照某种维度做划分
-   包   —— 一个`.py`文件不够实现某些复杂的工程 一个文件夹包含很多`.py`文件 就是包
-   一般情况下 我们都统称为模块

#### 自定义模块和包

-   模块、包 和 运行文件不在同一个文件夹下：

    -   在`python`的安装目录下 也是可以导入成功的  但是`python`目录是不可以动的

    -   如果我想把其他位置的代码 导入到现在运行的文件中： 默认情况下是不能导入成功的 因为 `python`在寻找目录时  自动会去某些目录寻找 `sys.path()`可以打印出`python`默认寻找模块的路径 打印出的前面一个是自己当前工作目录下的路劲
        ```python
        import sys
        print(sys.path)
        
        # 显示为：
        ['d:\\VSCodeProject\\python\\PythonWeb', 
         'D:\\PythonCompiler\\python311\\python311.zip', 
         'D:\\PythonCompiler\\python311\\DLLs', 
         'D:\\PythonCompiler\\python311\\Lib', 
         'D:\\PythonCompiler\\python311', 
         'D:\\PythonCompiler', 
         'D:\\PythonCompiler\\Lib\\site-packages', 
         'D:\\PythonCompiler\\Lib\\site-packages\\win32', 
         'D:\\PythonCompiler\\Lib\\site-packages\\win32\\lib', 
         'D:\\PythonCompiler\\Lib\\site-packages\\Pythonwin', 
         'D:\\PythonCompiler\\python311\\Lib\\site-packages', 
         'D:\\PythonCompiler\\python311\\Lib\\site-packages\\win32', 
         'D:\\PythonCompiler\\python311\\Lib\\site-packages\\win32\\lib', 
         'D:\\PythonCompiler\\python311\\Lib\\site-packages\\Pythonwin']
        ```

-   `sys.path` 获取到的是一个列表 是有序的 内部在寻找模块的时候 也是有序的 前面找到了 后面就不会再找了

-   自定义模块的名字不能和内置模块的名字重名

-   导入模块和包的方式：

    -   `import xxx`   导入一个`py`文件 没办法导入某个文件中的函数（如果要使用文件里面的函数 要把导入路径写完全）
    -   `from xxx import xxxx, xxxx1, xxxx2`   从哪导入一个模块，可以直接导入函数/也可以直接导入`.py`文件 再利用文件名调用函数 —— 不需要写全部路径

-   一般情况下 要导入深层次的模块 —— 使用`from`  如果是一个单级目录则可以用`import`

#### 内置模块

-   内部提供好的功能

    ```python
    hashlib  --> 加密
    random   --> 随机值
    json     --> 一种数据格式 以字符串的形式存在 不同语言进行数据传输
    time     --> 时间模块
    datetime --> 时间模块
    os       --> 系统模块
    shutil   --> 删除 拷贝
    re       --> 正则
    ```
    
    -   `hashlib` `MD5` 加密
    
    ```python
    """hashlib MD5 加密"""
    # 在以后开发的时候 密码使用MD5 而不使用明文
    import hashlib
    
    data = 'admin'
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    res = obj.hexdigest()
    print(res)
    ```
    
    ```python
    # MD5 不能反解
    # 案例：
    user_dict = {
        'buweishi': '21232f297a57a5a743894a0e4a801fc3'
    }
    user = input('用户名')
    pwd = input('密码')
    
    my_password = user_dict.get(user)
    # 加密pwd为密文 判断和user_dict的密文是否一样
    # 撞库 —— 加盐 加密的时候 自定义一个随机字符串 
    ```
    
    ```python
    import hashlib
    
    salt = 'ncijsniuewciunew'  # 自己随便写个盐
    data = 'admin'
    obj = hashlib.md5(salt.encode('utf-8'))
    obj.update(data.encode('utf-8'))
    res = obj.hexdigest()
    print(res)
    
    # 6f9c9612974be4b40909d435e59be7f2
    ```
    
    -   序列化 ： 将数据类型包装成 `json` 反序列化 ：将`json`转化成数据类型
    -   `JSON`格式：
        -   外部整体是个字符串
        -   `JSON`字符串的内部有字符串 只能用双引号
        -   """ {"k1":123, "k2":[11, 22, 33]} """
        -   `JSON`里面 没有元组这样的格式
        -   `JSON`字符串和普通字符串的区别：`JSON`属于字符串
        -   `JSON` 关于中文 —— `dumps`的时候 会默认将中文转化为`unicode`格式要想不转换为`unicode`则 在`dumps`参数中加入 `enure_ascii=False`
        -   在`Python`中只能序列化`python`内置的数据类型 只支持最基本的数据类型
            -   `dict`
            -   `list`
            -   `tuple`
            -   `atr`
            -   `int`
            -   `float`
            -   `True`
            -   `False`
            -   `None`
    -   `json`格式可以为：
        -   整数
        -   字符串
        -   字典
        -   bool
        -   列表
    
    ``` 
    info = {'k1':123, 'k2':(11, 22, 33, 44)}
    
    json 格式：
    	' {"k1":123, "k2":[11, 22, 33, 44]} '
    
    json.dunps(info)  --> 将python数据类型转换成JSON格式的字符串
    json.loads()      --> 将JSON字符串转换成python中的数据类型
    ```
    
    -   `datatime`时间戳
      
        ```python
        import datetime
        v1 = datetime.datetime.now()  #时间戳
        print(v1)
        string_date = v1.strftime('%Y-%m-%d %H:%M:%S')  # 字符串格式的时间
        print(string_date)
        ```
        
    -   时间相关格式：
    
        -   `datatime`类型
    
        -   字符串类型
    
        -   时间戳类型 获取秒数
    
        -   另外两种都可以和`datatime`类型相互转换
    
        -   时间转换
    
            ```python
            字符串 --> datetime
            from datetime import datetime
            text = '2023-12-13'
            res = datetime.strptime(text, '%Y-%m-%d')  # 第二个参数表示text的格式
            
            datetime --> 字符串
            dt = datetime.now()
            res = dt.strftime('%Y-%m-%d %H-%M-%S')
            ```
    
        -   `datetime`可以很方便地实现时间的加减
    
            ```python
            from datetime import datetime, timedelta
            v1 = datetime.now()
            res = v1 + timedelta(days=280)  # 280天以后
            res = v1 + timedelta(seconds=100)  # 100s以后
            res = v1 + timedelta(days=100, hours=100, minutes=10)
            ```
    
    -   `os`模块
    
        -   路径拼接
    
            ```python
            windows: D:\xx\xxx\xxxx
            Mac系统:/user/xxx/xxx/xxx
            Linux系统:/user/xxxx/xxxx/xxxx
            ```
    
            ```python
            import os
            # 建议使用
            path = os.path.join('x1', 'x2', 'x3', 'x4.txt')
            print(path)
            # x1\x2\x3\x4.txt
            ```
    
        -   找上级目录
    
            ```python
            import os
            file_path = 'x1\x2\x3\x4'
            os.path.dirname(file_path)
            # x1\x2\x3
            ```
    
        -   绝对路径
    
            -   如何生成绝对路径
    
                ```python
                # 注意：肯定会获取路径 但是存在与否不在考虑之内
                import os
                res = os.path.abs.path('send_email.py')
                print(res)
                # D:\PycharmProject\Web1.0\send_email.py
                
                import os
                res = os.path.abs.path('xx')
                print(res)
                # D:\PycharmProject\Web1.0\xx
                
                # 当前文件所在目录              拼接目录
                # D:\PycharmProject\Web1.0\        xx
                ```
    
                
    
        -   判断路径是否存在
    
            ```python
            # 判断路径是否存在 os.path.exists(file_path)
            import os
            file_path = os.path.join('files', 'db.txt')
            with open(file_path, 'w', encoding='utf-8') as fp:
                data = fp.read() 
            '''报错： 因为文件路径不存在
            Traceback (most recent call last):
              File "D:\PycharmProject\Web\test1.py", line 23, in <module>
                main()
              File "D:\PycharmProject\Web\test1.py", line 17, in main
                with open(file_path, 'w', encoding='utf-8') as fp:
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            FileNotFoundError: [Errno 2] No such file or directory: 'files\\db.txt'
            '''
            ```
    
        -   创建目录
    
            ```python
            import os
            path = os.path.join('files', '2023', 'db')
            print(path)
            os.makedirs(path)
            # 如果已创建 那么不创建
            ```
    
        -   删除文件
    
            ```python
            import os
            os.remove(file_path)
            ```
    
        -   删除文件夹
    
            ```python
            # os模块删除不了文件夹
            # 删除文件夹使用shutil模块
            import shutil
            shutil.rmtree(path)
            ```
    
        -   判断是否是文件夹
    
            ```python
            import os
            os.path.isdir(path)
            ```
    
    -   补充 - 主文件
    
        -   主文件 —— 程序的入口 只有执行此程序才可以运行
    
            ```python
            def main():
                pass
            
            
            # 标志 代表这是个主文件
            # 主文件才加 if __name__ == '__main__':
            if __name__ == '__main__':
                main()
                
            # __name__ 是python内部创建的一个变量
            ```
    
        -   `shutil`模块
    
            ```python
            import shutil
            shutil.rmtree(path)  # 删除文件
            
            shutil.copytree('源文件夹', '目标文件夹路径')  # 拷贝源文件夹的内容到新文件夹
            shutil.copy('源文件夹', '目标文件路径/')  # 拷贝文件到文件夹 必须保证这个文件夹存在
            
            # 重命名
            shutil.move('x10', 'x10.txt')
            shutil.move('x10', 'x100')
            
            # 压缩和解压缩
            
            # 压缩
            # base_name 压缩文件文件名 
            # format 后缀名
            # root_dir 需要压缩的文件夹的路径
            shutil.make_archive(base_name='1116', format='zip', root_dir='ppp')
            
            # 解压
            # file_name 压缩包路径
            # extract_dir 要解压到的目录
            # format 后缀名
            shutil.unpack_archive(file_name='1116.zip', extract_dir='1117', format='zip')
            ```

#### 第三方模块

```python 
requests 
bs4
```

### `python re`模块 正则表达式

#### 正则表达式 

什么是正则表达式？—— 默认是贪婪匹配

如果需要非贪婪匹配 则在某一个能匹配多个的正则元素后面加上？，此时？不代表0个或1个 例如：**`r"d卜伟\w+"` 则会贪婪匹配** 如果写成**`r"d卜伟\w+?"`**则是非贪婪匹配

如果在`re.findall()`函数后面加上参数 `re.ASCII` 那么则匹配的时候不会匹配中文

```python 
text = '哈哈哈哈太牛了 在线想要，2086689759@qq.com 和 ciwhnciuen@163.com，手机号码15345678910'
# 手机号特征：'1[3|5|8|9]\d{9}'
# 邮箱特征  ：'\w+@\w+\.w+'
```

##### 字符相关

-   固定文本 文本内容不包含任何特殊字符

    ```python
    import re
    text = 'buweishi, 你好， 卜伟仕 计算机信息技术 1930090102阿里嘎多美羊羊桑 搜都寺内 果咩纳塞 美羊羊桑 呆就不 切 阿里嘎多美羊羊桑 阿里嘎多玛玛哈哈'
    regular = r'阿里嘎多'
    data_list = re.findall(regular, text)
    print(data_list)
    ```

-   匹配字符 `[abc]`匹配`a`或者`b`或者`c`

    ```python
    import re
    text = 'buweishi, 你好， 卜伟仕 计算机信息技术 1930090102阿里嘎多美羊羊桑 搜都寺内 果咩纳塞 美羊羊桑 呆就不 切 阿里嘎多美羊羊桑 阿里嘎多玛玛哈哈 xsuhbxnsicjodncoer9uhesncpojap5566NCDOJNCIUSNCOJCScnjdsJCMKDMKOJSNJANJISJAO_-=-+++265+5+5+13@#￥%……&*（）——【】：“。，xasacefcswa！@#￥%……&*（）、||、xsxa、///\njkcnsius\\/.;,lkjiiojuihiu'
    regular = r'[abc]'
    data_list = re.findall(regular, text)
    print(data_list)  # ['b', 'b', 'c', 'c', 'c', 'a', 'c', 'a', 'a', 'c', 'c', 'a', 'a', 'c']
    
    regular = r'j[abc]'  
    data_list = re.findall(regular, text)
    print(data_list)  # ['ja']
    ```

-   字符范围 `0 - 9 a - z`

    ```python
    import re
    text = 'buweishi, 你好， 卜伟仕 计算机信息技术 1930090102阿里嘎多美羊羊桑 搜都寺内 果咩纳塞 美羊羊桑 呆就不 切 阿里嘎多美羊羊桑 阿里嘎多玛玛哈哈 xsuhbxnsicjodncoer9uhesnctpojap5566NCDOJNCIUSNCOJCScnjdsJCMKDMKOJSNJANJISJAO_-=-+++265+5+5+13@#￥%……&*（）——【】：“。，xasacefcswa！@#￥%……&*（）、||、xsxa、///\njkcnsius\\/.;,lkjiiojuihiu'
    regular = r't[a-z]'
    data_list = re.findall(regular, text)
    print(data_list)  # 找 ta tb tc ... tz
    ```

    ```python
    import re
    text = 'buweishi, 你好， 卜伟仕 计算机信息技术 1930090102阿里嘎多美羊羊桑 搜都寺内 果咩纳塞 美羊羊桑 呆就不 切 阿里嘎多美羊羊桑 阿里嘎多玛玛哈哈 xsuhbxnsicjodncoer9uhesnctpojap5566NCDOJNCIUSNCOJCScnjdsJCMKDMKOJSNJANJISJAO_-=-+++265+5+5+13@#￥%……&*（）——【】：“。，xasacefcswa！@#￥%……&*（）、||、xsxa、///\njkcnsius\\/.;,lkjiiojuihiu'
    regular = r't[0-9]'
    data_list = re.findall(regular, text)
    print(data_list)  # 找 t0 t1 t2 t3 ... t9
    ```

-   **`\d`** 代表一个数字

    ```python
    import re
    text = "root-admain1930090102-add3-admain-1023root250"
    regular = r"d\d"
    data_list = re.findall(regular, text)
    ```

    -   **`+`** 代表一个或多个 —— 只代表次数

    ```python
    import re
    text = "root-admain1930090102-add3-admain-1023root250"
    regular = r"d\d+"
    data_list = re.findall(regular, text)
    ```

    -   **`*`**代表0个或者多个  —— 只代表次数

    ```python
    import re
    text = "root-admain1930090102-add3-admain-1023root250"
    regular = r"d\d*"
    data_list = re.findall(regular, text)
    ```

    -   `?` 代表0个或者一个 —— 只代表次数

    ```python
    import re
    text = "root-admain1930090102-add3-admain-1023root250"
    regular = r"d\d?"
    data_list = re.findall(regular, text)
    ```

    -   `{n}` 代表n个 —— 只代表次数

    ```python
    import re
    text = "root-admain1930090102-add3-admain-1023root250"
    regular = r"d\d{2}}"
    data_list = re.findall(regular, text)
    ```

    -   `{n,}` ` n`个或者`n+1`, `n+2` .... 个（`n+`个） —— 只代表次数
    -   `{m, n}`  `m` 个 到 `n`个之间` m - n `    `m` <= 个数 <= `n`  —— 只代表次数

-   `\w`  数字 字母 下划线 

-   正则默认是贪婪匹配 在正则表达式中加?则可以实现非贪婪匹配`r"d卜伟\w+**?**"`

-   `.`  表示除换行符以外的任意字符（一个）

-   `.+` 表示除换行符以外的任意字符（多个） 贪婪匹配 若要变成非贪婪匹配 使用`.+？`

-   `\s` 代表任意的空白字符（一个） `\S`匹配所有非空白符

##### 数量

-   `*`       --> 代表0个或者n个 （贪婪匹配）
-   `+`       --> 代表1个或者n个 （贪婪匹配）
-   `？`      -->  代表0个或者1个（贪婪匹配）
-   `{n}`     -->  固定n个 （贪婪匹配）
-   `{n, }`   --> n+个 （贪婪匹配）
-   `{m, n}`  --> n到m个 （贪婪匹配）
-   若要非贪婪匹配 在以上元素后面加上 ？ 即可

##### 分组

-   提取数据区域 使用() —— 只要括号里面所匹配到的

    ```python
    # 若要提取后六位手机号码：
    import re
    text = r"hahhahc15345678910cqhwihuiw@cwodcd.com"
    regular = r"15345(6\d{5})"
    re.findall(regular, text)
    ```

-   还可以加上**或**的条件 以下正则匹配 `15345(6\d{5})`或`15345(r\w+太)`

    ```python
    import re
    text = r"hahhahc15345678910cqhwihuiw@cwodcd.com15345root太678910"
    regular = r"15345(6\d{5})"
    regular = r"15345(6\d{5}|r\w+太)"
    re.findall(regular, text)
    ```

-   常用正则规则

    ```python
    # QQ号
    [1-9]\d{4,}
    ```

    ```python
    # 身份证号
    \d{17}[\dX]
    ```

    ```python
    # 手机号
    1[3-9]\d{9}
    ```

    ```python
    # 邮箱  xxx@xxxx.com
    \w+@\w+\.com
    \w+@\w+\.\w+
    # 包含 - 的邮箱格式 xxx-xxx@xxxx.com
    [a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+
    ```

-   `^` \`$` 两个符号里面的文本是匹配的开始和结束

    ```python
    r"^1[3-9]\d{9}$"
    ```

#### `python` `re`模块

-   `re.findall()` 获取所有匹配的结果
-   `re.match()` 从开头匹配 开头没匹配成功那么不再向后匹配 只返回第一个对象
    -   返回值是一个对象 利用 `group()`取值
    -   应用场景 手机号格式校验
-   `re.search()` 从整个字符串去匹配 只返回第一个对象
-   `re.split()` 用匹配到的文本分割

### 面向对象

#### 面向对象

```python
# 使用 对象.方法名()调用类中的方法的时候 self会默认传入实例化的对象传进去的
# 哪个对象调用的方法 那么self就等于这个对象
# self 是Python内部传递的 会将调用此函数的对象传进去
class Message:
    def main(self, someting):
        return 0

something = 'hello'
obj = Message()
obj.main(someting)
```

```python
class Message:
    def send_emain(self, to_email):
        msg = "给{}发送一封电子邮件".format(to_email)
        return 0
    
    def send_dingding(self, to_email):
        msg = "给{}钉钉发送一封电子邮件".format(to_email)
        return 0
    
    def send_wechat(self, to_email):
        msg = "给{}微型发送一封电子邮件".format(to_email)
        return 0

msg = Message()
msg.send_email("x1")
msg.send_dingding("x2")
msg.send_wechat("x3")
```

实例化对象`(obj = Message())` —— 开辟一个内存 指向`Message`类

-   与他的类关联
-   一块内存 可以存放数据

`obj.send_email("x1")`

`obj.send_dingding('x2')`

```python
class Message:
    def main(self, someting):
        return 0

something = 'hello'
obj = Message()
obj.company()
obj.main(someting)

print(obj.company)  # 是能拿到值的
```

-   `obj.company()`的时候 在`obj = Message()`开辟的内存里面存储了 `"company='连通'"`

```python
class Message:
    def send_email(self, to_email):
        msg = "给{}的{}发送一封电子邮件".format(self.company, to_email)
        print(msg)
        return 0
    
    def send_dingding(self, to_email):
        msg = "给{}钉钉{}发送一封电子邮件".format(self.company, to_email)
        print(msg)
        return 0
    
    def send_wechat(self, to_email):
        msg = "给{}微信{}发送一封电子邮件".format(self.company, to_email)
        print(msg)
        return 0
    
obj = Message()
obj.company = '联通'
obj.numbers = 10000
obj.send_email('xxx')

new = Message()

# TODO：day 10-2 模块和面向对象53:48
```

####  面向对象三大特征

-   封装
    -   将数据打包放到对象中
    -   归类 将同一类的函数汇总到一个类中
-   继承
-   多态
    -   `python`中默认支持多态

## 前端

###  `HTML`

快速上手

```python
# 注意 这个py文件会一直运行 直到自己手动停止
# 在浏览器输入http://127.0.0.1:5000后面加上加上@app.route('/show/info')
# 中引号里面的字符串即可显示“中国联通”
from flask import Flask

app = Flask(__name__)


# 创建函数和网址的对应关系
# 到时候访问网址/show/info 的时候就会自动执行main这个函数
@app.route('/show/info')
def main() -> any:
    return '中国联通'


if __name__ == '__main__':
    app.run()  # 运行
    pass

# END
#第一次运行该文件 出现以下信息：
"""
 * Serving Flask app 'test_1'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000 # 这个http://127.0.0.1:5000即为可以在浏览器输入的东西
Press CTRL+C to quit
"""

flask框架警告：WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
```

为了能够让我们使用方便 `flask`支持将字符串写入到文件中

```python
# 注意： index.html文件存放在和.py文件同一级的Templates文件下面
from flask import Flask, render_template

app = Flask(__name__)


# 创建函数和网址的对应关系
# 到时候访问网址/show/info 的时候就会自动执行main这个函数
@app.route('/show/info')
def main() -> any:
    # return r'<h1>这是一个测试的网页</h1>中国联通'
    # flask会自动打开这个文件 读取内容并给用户返回
    # 默认：去当前文件目录的templates目录下去寻找
    return render_template(r'index.html')  # 参数是：文件路径


if __name__ == '__main__':
    app.run()  # 运行
    pass
```

1.   快速开发一个网站

     ```python
     pip install flask
     ```

2.   编码：`<meta charset="utf-8">`

3.   title

4.   标题`<h1> 到 <h6> `块级标签

5.   `div` 和 `span`

     1.   `div` 一个人占一行`<div>`内容`</div>` **块级标签**
     2.   `span` 自己多大 占多大  \<span>内容\</span> **行内标签**
     3.   这两个标签很素 可以通过写css文件使它变得很花里胡哨

6.   超链接 `a`

     ```html
     <!-- 跳转到别人的网站 -->
     <a href="https://www.baidu.com">点击跳转</a>
     
     <!-- 跳转到自己的网站 -->
     <a href="http://127.0.0.1:5000/show/info">点击跳转</a>
     <a href="/show/info">点击跳转</a>
     target = "_blank" : 在新标签页打开链接
     ```

7.   图片 `<img src="图片地址">` 自闭合标签 
     ```html
     <!-- 别人的图片 可能有防盗链 -->
     <img src="https://pic.netbian.com/uploads/allimg/221216/095854-1671155934fedf.jpg">
     
     <!-- 自己的图片 —— 自己的图片放在static目录 图片要放在static里面 -->
     <!-- 宽高设置 -->
     <img style="height: 400px" src="/static/图片01.jpg"> 
     <img style="height: 10%" src="/static/图片01.jpg">
     ```

8.   小结：
     ```html
     - 块级标签
     	- h1 到 h6
     	- div标签
     - 行内标签
     	- span 标签
     	- a 标签
     	- img 标签
     
     **标签还可以嵌套**
     ```

9.   列表 —— 块级标签

```html
<!-- 无序列表 -->
<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

```html
<!-- 有序列表 -->
<ol>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ol>
```

10.   表格

      ```html
      <table border="1">
          <thead> <tr> <th>ID</th> <th>name</th> <th>age</th> </tr> </thead>
          <tbody>
              <tr> <td>100001</td> <td>buweishi</td> <td>19</td> </tr>
              <tr> <td>100002</td> <td>buwei</td> <td>19</td> </tr>
              <tr> <td>100003</td> <td>weishi</td> <td>19</td> </tr>
              <tr> <td>100004</td> <td>bushi</td> <td>19</td> </tr>
              <tr> <td>100005</td> <td>buwbwseishi</td> <td>19</td> </tr>
          </tbody>
      </table>
      ```

11.   `input` 系列 —— 行内标签 7个

      ```html
      <input type="text" /> 文本输入框
      <input type="password" /> 密码框
      <input type="file" /> 文件选择框
      
      <input type="radio" /> 
      <input type="radio" /> 单选框 —— 可以都选
      
      # 下面为单选框 —— 只能选一个
      <input type="radio" name="n1" /> 男
      <input type="radio" name="n1" /> 女
      
      # 复选框
      <input type="checkbox" />
      <input type="checkbox" />
      <input type="checkbox" />
      <input type="checkbox" />
      <input type="checkbox" />
      <input type="checkbox" />
      
      # 按钮
      <input type="button" value="提交"/> -- 普通按钮
      <input type="submit" value="提交"/> -- 提交表单
      ```

12.   下拉框
      ```html
      <select>
          <option>北京</option>
          <option>上海</option>
          <option>广州</option>
          <option>深圳</option>
      </select>
      ```

13.   多选下拉框
      ```html
      <select multiple>
          <option>北京</option>
          <option>上海</option>
          <option>广州</option>
          <option>深圳</option>
      </select>
      -- 选中一个 按住shift键 再依次点击所需的选项
      ```

14.   多行文本
      ```html
      <textarea rows"=3">多行文本</textarea>
      rows代表默认高度 可以写更多
      ```

#### 案例：注册页面

```html
    <h1>
    用户注册
    </h1>

    <div>
        用户名: <input type="text" />
    </div>

    <div>
        密码: <input type="password" />
    </div>

    <div>
        性别: <input type="radio" name="sex"/> 男 <input type="radio" name="sex"/> 女
    </div>

    <div>
        爱好:
        <input type="checkbox" />唱
        <input type="checkbox" />跳
        <input type="checkbox" />rap
        <input type="checkbox" />篮球
    </div>

    <div>
        所在城市:
        <select name="selection_city" id="select-city">
            <option value="">北京</option>
            <option value="">上海</option>
            <option value="">广州</option>
            <option value="">深圳</option>
            <option value="">甘肃</option>
            <option value="">西安</option>
        </select>
    </div>

    <div>
        擅长领域：
        <select name="selection_good_at" id="select-good-at" multiple>
            <option value="games">打游戏</option>
            <option value="eat">吃饭</option>
            <option value="sleep">睡觉</option>
            <option value="wc">上厕所</option>
            <option value="sing">唱歌</option>
            <option value="dance">跳舞</option>
        </select>
    </div>

    <div>
        备注:
        <textarea></textarea>
    </div>

    <div>
        <input type="button" value="提交">
        <input type="submit" value="提交">
    </div>
```

#### 补充

`get`请求： `URL`方法 / 表单请求

-   `get`请求

-   跳转

-   向后台传入数据时 会拼接到`URL`上面 会在`URL`中体现
    ```python
    https://www.sogou.com/webquery=%E5%AE%89%E5%8D%93&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=636&sst0=1681999875710&lkt=0%2C0%2C0&sugsuv=1681999871894192&sugtime=1681999875710
    ```

`post`请求：表单提交

-   现象：提交数据不在`URL`中体现，体现在自己的表单中 显示在请求体中

#### 案例：用户注册

-   新创建一个项目

-   新建Flask代码
    ```html
    # 以下代码发送的是GET请求
    from flask import Flask, render_template
    app = Flask(__name__)
    @app.route('/register')
    def register():
        return render_template('register.html')
    if __name__ == '__main__':
        app.run()
    
    # 以下代码发送的是POST请求
    from flask import Flask, render_template
    app = Flask(__name__)
    @app.route('/register', methods=['GET'])
    def register():
        return render_template('register.html')
    if __name__ == '__main__':
        app.run()
    ```

    ```html
    表单提交：
    <form action="提交的地址" method="post">
        用户名: <input type="text" />
        密码: <input type="password" />
        <input type="button" value="提交">
        <input type="submit" value="提交">
    </form>
    在form标签中 只能submit提交——提交表单
    --------------------------------------------------
    <form action="/xxxx/xxx/xx" method="get">
            用户名: <input type="text" name="uu"/>
            密码: <input type="password" name="pp"/>
            <input type="submit" value="提交">
    </form>
    ```

    注意：

    1 `form`标签要包裹要提交的数据的标签

    2 在`form`标签中定义提交方式`method=“get”` 提交地址`action="提交地址"`

    3 还需要一个`submit`标签

    4 在`form`里面的标签： `input TextArea select`  **<u>一定要记得写name属性</u>**

    5 这个地址：写到自己的网址

    ```python
    # TODO：2022 Python的web开发（完整版）入门全套教程，零基础入门到项目实战 day11-2 HTML和CSS 43:38
    ```
    

```python
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/do/reg', methods=['GET'])
def do_reg():
    # return render_template('register.html')
    # 接收通过get发回的数据
    # 给用户返回结果
    print(request.args)  # 注意这一行和post方法的区别
    return '<h1>提交以后</h1>'
if __name__ == '__main__':
    app.run()
```

```html
<div>
  <form action="/do/reg" method="get">
    用户名： <input type="text" name="user">
    密码： <input type="password" name="pwd">
    <input type="submit" value="点击提交">
  </form>
</div>
```

以上两个代码块所共同作用打印出的结果为：

`ImmutableMultiDict([('user', 'qwer'), ('pwd', 'qwer')])`

以`post`请求的方式发送请求：

```python
@app.route('/post/reg', methods=['POST'])
def post_reg():
    # return render_template('register.html')

    # 接收通过post发回的数据
    # 给用户返回结果
    print(request.form)  # 注意这一行 和 get方法的区别
    return '<h1>提交以后</h1>'
```

以上结果为：

`ImmutableMultiDict([('user', 'qwer'), ('pwd', 'qwer')])`

表单提交：

```html
<form action="/post/reg" method="post">
        用户名： <input type="text" name="user">
        密码： <input type="password" name="pwd">
        性别:
          <input type="radio" name="gender" value="1"/> 男
          <input type="radio" name="gender" value="0"/> 女
        <input type="submit" value="点击提交">
      </form>
这里性别 —— 单选框 如果不写value的话，传过去的参数就是“on” 但是如果写上value值的话，传过去的数据就分别是value的值
```

总结：

```html
<div>
      <form action="/register" method="post">
        <div>
            用户名： <input type="text" name="user">
        </div>

        <div>
            密码： <input type="password" name="pwd">
        </div>

      <div>
        性别:
          <input type="radio" name="gender" value="man"/> 男
          <input type="radio" name="gender" value="woman"/> 女
        </div>
    <div>
      爱好:
        <input type="checkbox" name="hobby" value="sing"/>唱
        <input type="checkbox" name="hobby" value="dance"/>跳
        <input type="checkbox" name="hobby" value="rap"/>rap
        <input type="checkbox" name="hobby" value="basketball"/>篮球
    </div>

    <div>
      所在城市:
      <select name="selection_city" id="select-city">
          <option value="beijing">北京</option>
          <option value="shanghai">上海</option>
          <option value="guangzhou">广州</option>
          <option value="shenzhen">深圳</option>
          <option value="gansu">甘肃</option>
          <option value="xian">西安</option>
      </select>
    </div>

      <div>
        擅长领域：
      <select name="selection_good_at" id="select-good-at" multiple>
          <option value="games">打游戏</option>
          <option value="eat">吃饭</option>
          <option value="sleep">睡觉</option>
          <option value="wc">上厕所</option>
          <option value="sing">唱歌</option>
          <option value="dance">跳舞</option>
      </select>
      </div>

  <div>
        备注:
        <textarea name="more"></textarea>
  </div>

      <div>
        <input type="submit" value="点击提交">
      </div>
      </form>
</div>
```

```python
@app.route('/register')
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get('user')
        password = request.form.get('pwd')
        hobbies = request.form.getlist('hobby')
        gender = request.form.get('gender')
        city = request.form.get('selection_city')
        skill = request.form.getlist('selection_good_at')
        more = request.form.get('more')
        print(user)
        print(password)
        print(hobbies)
        print(gender)
        print(city)
        print(skill)
        print(more)

        # 将用户信息写入到文件/数据库/Excel
        return '<h1>提交以后</h1>'
```

### `CSS`

`css` 美化标签 

#### 快速了解

```html
<img src="..." style="height:100px" />

<div style="color:red">
...
</div>
```

#### `CSS` 应用方式：

1.   直接在标签上应用

```html
<img src="..." style="height:100px" />

<div style="color:red">
...
</div>
```

2.   在`head`标签中写`style`标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test_page</title>
    <style>
        .c1{
            color: red;
        }
    </style>
</head>
<body>
    <h1 class = "c1">用户注册</h1>
    <h1 class = "c2">用户注册</h1>
    <h1 class = "c1">用户注册</h1>
    <h1 class = "c2">用户注册</h1>
    <div>
        用户名: <input type="text" />
    </div>

    <div>
        密码: <input type="password" />
    </div>

    <div>
        性别: <input type="radio" name="sex"/> 男 <input type="radio" name="sex"/> 女
    </div>
</body>
</html>
```

3.   将样式存到一个`CSS`文件中

     ```css
     .c1{
         height:100px;
     }
     .c2{
         color:red;
     }
     ```

     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <title>test_page</title>
         <link rel="stylesheet" href="common.css" />
     </head>
     <body>
     	<h1 class="c1">用户注册</h1>
         <div>
             用户名: <input type="text" />
         </div>
     
         <div>
             密码: <input type="password" />
         </div>
     
         <div>
             性别: <input type="radio" name="sex"/> 男 <input type="radio" name="sex"/> 女
         </div>
     </body>
     </html>
     ```

     #### 案例：在`flask`中的应用

     问题：用`Flask`框架不太方便 每次都要重启 有些文件必须放在特定的文件夹中

     函数 、 `HTML`文件

     有没有一种方式快速编写前段代码 并且查看效果  最后再将页面集成到`flask`中

     —— pycharm 提供了非常便捷的开发前端页面的工具

#### `CSS`选择器

```html
. 表示class选择器
# 表示id选择器
li li标签选择器
```

1.   `ID`选择器

2.   类选择器 —— 用的最多

3.   标签选择器

4.   属性选择器

5.   后代选择器

     ```css
     找到yy class下的所有li标签
     .yy li{
        color: pink;
     }
     只找到yy class下一级的a标签 而不会找更深层的标签
     .yy > a{
     	color: #39b362;		
     }
     ```

6.   关于选择器 用的比较多：

     -   类选择器
     -   标签选择器
     -   后代选择器

7.   注意事项：多个样式以及覆盖问题：

     -   和写的顺序无关 而和`css`样式定义的上下顺序有关系
         ```html
         .c1{
             color: yellow;
             border: 1px solid red;
         }
         .c2{
             font-size: 28px;
             color: green;
         }
         
         如果非要上面的而不要下面的 则需要按照以下的样式写：
         .c1{
             color: yellow ！important;
             border: 1px solid red;
         }
         ```

         ```python
         # todo: 2:42:17 day11-2
         ```


#### 样式

1.高度和宽度

```css
.c1{
    height: 300px;
    width: 500px;
}
```

注意事项：

第一，宽度：支持百分比

```css
.c1{
    height: 300px;
    width: 50%;
}	
```

第二，高度和宽度对行内标签是无效的，而对块级标签是有效的。

​	块级标签，是霸道的 右侧区域空白 也不给别的元素用

2.块级标签和行内标签

-   块级标签 

-   行内标签

-   `css`样式：标签 --> `display: inline-block`综合了行内标签和块级标签的特性
  
    ```html
    .c1{
        display: inline-block;
        height: 100px;
        width: 300px;
        border: 2px solid blue;
    }
    
    <span class="c1">中国</span>
    <span class="c1">联通</span>
    ```
    
-   块级标签和行内标签的设置：
    ```html
    <div style="display: inline;">中国</div>
    <div style="display: block;">联通</div>
    ```

-   注意：**块级标签 + 块级标签&行内标签** 用的比较多

3.字体和颜色

```html
颜色
字体格式
加粗
大小
```

4.文字对齐方式

```html
text-align: center; 水平居中
```

5.浮动

```html
<span>左边</span>
<span style="float: right;">右边</span>
```

`div`默认是块级标签——霸道

`div`浮动起来后 就会变得不一样

）

```html
.item{
    float: left;
    width: 280px;
    height: 170px;
    border: 3px solid blue;
}
```

但是问题是——会脱离文档流（可能将原有的数据覆盖掉）

解决方法：

```html
在父div下写： 
<div style="clear: both;"></div>
```

6.边距

-   内边距

    我自己的内部设置边距 

    ```html
    padding-top: 20px;
    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 20px;
    
    以上四行样式可以简写为：
    padding: 20px;
    
    此外，写成上右下左的格式：
    padding: 20px 10px 5px 2px;
    ```

-   外边距

-   ```python
    <div style="height: 200px; background-color: #1ba91b;"></div>
    <div style="height: 100px; background-color: #0b7d09; margin-top: 20px"></div>
    ```

    ```python
    line-height: 只针对文字 对图片不起作用
    ```

    **`a`标签是一个行内标签 行内标签默认不能设置高度和边距！！！ 有两种方法：设置块级标签 或者行内标签&块级标签**

#### 案例： 小米商城

##### 总结：

`body`标签有一个默认的边距 显示出来后 有一个白色的间隙

直接在页面上给`body`加样式 

```html
margin: 0;
```

文本居中：

```html
text-align: center;
```

区域居中：自己要有宽度 + `margin-left: auto; margin-right: auto;`

父亲如果没有高度和宽度——整体会被子`div`撑起来

如果`div`有浮动 需要加`clear: both`(需要加入到有浮动的div的同级标签的下一行)

```html
<div class="menu">  /*这个div有浮动*/
    <a>小米官网</a>
    <a>小米商城</a>
    <a>MIUI</a>
    <a>LOT</a>
    <a>云服务</a>
    <a>天星数科</a>
    <a>有品</a>
    <a>小爱开放平台</a>
    <a>企业团购</a>
    <a>资质证照</a>
    <a>协议规则</a>
    <a>下载APP</a>
    <a>SelectLocation</a>
</div>
<div class="account"> /*这个div有浮动*/
    <a>登录</a>
    <a>注册</a>
    <a>消息通知</a>
    <a>购物车</a>
</div>
/*注意看下面这一行*/
<div style="clear: both"></div>  /* 和两个浮动标签同级 */
```

想用别人的样式 可以检查别人的样式 并且应用到自己的网页上

布局 不知道如何下手

```html
text-decoration: none; —— 让超链接的下划线不显示
如果想鼠标放上去显示出不同的样式：

鼠标不放上去的样式：
.sub-header .menu-list a{
    padding: 0 10px 0 10px;
    display: inline-block;
    color: #333;
    font-size: 16px;
    text-decoration: none;
}
鼠标放上去的样式：
.sub-header .menu-list a:hover{
    color: chartreuse;
}
```

总结：

-   `a`标签 是行内标签 高度和内外边距设置是不会生效的

-   垂直居中 文本：`line-height` 图片：通过计算边距实现

-   `a`标签默认有下划线  如果要去掉：`text-decoration: none;`

-   某个标签 的 `hover` ：鼠标放上去后会应用这个样式
    ```html
    .sub-header .menu-list a:hover{
        color: chartreuse;
    }
    ```

#### 案例：推荐区域

实现案例代码如下：源码路径：`D:\PycharmProject\WebFlask\merge.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>整合</title>
	<style>
		body{
			margin: 0;
			font: 14px/1.5 Helvetica Neue,Helvetica,Arial,Microsoft Yahei,Hiragino Sans GB,Heiti SC,WenQuanYi Micro Hei,sans-serif;
		}
		img{
			width: 100%;
			height: 100%;
		}
		.header{
			/* height: 38px; */
			background-color: #333;
		}
		.header .menu{
			float: left;
			color: #b0b0b0;
			height: 38px;
			line-height: 38px;
			font-size: 12px;
		}
		.header .account{
			float: right;
			color: #b0b0b0;
			height: 38px;
			line-height: 38px;
			font-size: 12px;
		}
		.header a{
			color: #b0b0b0;
			line-height: 40px;
			display: inline-block;;
			font-size: 12px;
			margin-right: 5px;
		}
		.header .container .menu a{
			text-decoration: none;
		}
		.header .container .menu a:hover{
			color: chartreuse;
		}
		.header .container .account a{
			text-decoration: none;
		}
		.header .container .account a:hover{
			color: chartreuse;
		}
		
		.sub-header{
			height: 100px;
			/*background-color: #9b9b9b;*/
		}
		.container{
			width: 1300px;
			/*height: 38px;*/
			margin: 0 auto;
			/* 一定要设置宽度 否则居中显示不好看 */
			/*border: 2px solid  blue;*/
		}
		.sub-header .ht{
			height: 100px;
		}
		.sub-header .logo{
			width: 234px;
			/*border: 2px solid yellow;*/
			float: left;
		}
		.sub-header .logo a{
			margin-top: 22px;
			display: inline-block
		}
		.sub-header .logo a img{
			height: 56px;
			width: 56px;
		}
		.sub-header .menu-list{
			width: 650px;
			float: left;
			line-height: 100px;
			/*border: 2px solid darkcyan;*/
		}
		.sub-header .menu-list a{
			padding: 0 10px 0 10px;
			display: inline-block;
			color: #333;
			font-size: 16px;
			text-decoration: none;
		}
		.sub-header .menu-list a:hover{
			color: chartreuse;
		}
		.sub-header .search{
			width: 234px;
			float: right;
			/*border: 2px solid darkred;*/
		}
		
		.slider .container .sd-image {
			width: 1226px;
			height: 460px;
		}
		
		.left_float{
			float: left;
		}
		.news .container .channel{
			width: 228px;
			height: 164px;
			padding: 3px;
			background-color: #5f5750;
		}
		.news .container .list-item{
			width: 316px;
			height: 170px;
		}
		.news{
			margin-top: 20px;
		}
		.news .channel .item{
			height: 82px;
			width: 76px;
			text-align: center;
		}
		.news .channel .item img{
			width: 24px;
			height: 24px;
			display: block;
			margin: 0 auto 4px;
		}
		.news .channel .item a{
			font-size: 12px;
			display: inline-block;
			padding-top: 20px;
			color: #fff;
			text-decoration: none;
			opacity: 0.7;
		}
		.news .channel .item a:hover{
			opacity: 1;
		}
	</style>
</head>
<body>
	<div class="header">
		<div class="container">
			<div class="menu">
				<a href="https://i.mi.com/">小米官网</a>
				<a href="https://i.mi.com/">小米商城</a>
				<a href="https://i.mi.com/">MIUI</a>
				<a href="https://i.mi.com/">LOT</a>
				<a href="https://i.mi.com/">云服务</a>
				<a href="https://i.mi.com/">天星数科</a>
				<a href="https://i.mi.com/">有品</a>
				<a href="https://i.mi.com/">小爱开放平台</a>
				<a href="https://i.mi.com/">企业团购</a>
				<a href="https://i.mi.com/">资质证照</a>
				<a href="https://i.mi.com/">协议规则</a>
				<a href="https://i.mi.com/">下载APP</a>
				<a href="https://i.mi.com/">SelectLocation</a>
			</div>
			<div class="account">
				<a href="https://i.mi.com/">登录</a>
				<a href="https://i.mi.com/">注册</a>
				<a href="https://i.mi.com/">消息通知</a>
				<a href="https://i.mi.com/">购物车</a>
			</div>
			<div style="clear: both"></div>
		</div>
	</div>
	
	<div class="sub-header">
		<div class="container">
			<div class="ht logo">
				<a href="https://www.mi.com/">
					<img src="./images/logo-mi2.png" alt="">
				</a>
			</div>
			<div class="ht menu-list">
				<a href="https://i.mi.com/">小米手机</a>
				<a href="https://i.mi.com/">红米手机</a>
				<a href="https://i.mi.com/">电视</a>
				<a href="https://i.mi.com/">笔记本</a>
				<a href="https://i.mi.com/">平板</a>
				<a href="https://i.mi.com/">家电</a>
				<a href="https://i.mi.com/">路由器</a>
				<a href="https://i.mi.com/">服务中性</a>
				<a href="https://i.mi.com/">社区</a>
			</div>
			<div class="ht search">这是搜索框</div>
			<div style="clear: both"></div>
		</div>
	</div>

	<div class="slider">
		<div class="container">
			<div class="sd-image">
				<img src="./images/89b9804e4b794f230252bc99fb55faa5.jpg" alt="这是一张图片">
			</div>
		</div>
	</div>

	<div class="news">
		<div class="container">
			<div class="channel left_float" style="margin-right: 14px">
				<div class="item left_float">
					<a href="https://www.mi.com/">
						<img src="./images/b1.png" alt="图标">
						<span>保障服务</span>
						
					</a>
				</div>
				<div class="item left_float">
					<a href="https://www.mi.com/">
						<img src="./images/b2.png" alt="图标">
						<span>企业团购</span>
					</a>
				</div>
				<div class="item left_float">
					<a href="https://www.mi.com/">
						<img src="./images/b1.png" alt="图标">
						<span>F码通道</span>
					</a>
				</div>
				<div class="item left_float">
					<a href="https://www.mi.com/">
						<img src="./images/b2.png" alt="图标">
						<span>米粉卡</span>
					</a>
				</div>
				<div class="item left_float">
					<a href="https://www.mi.com/">
						<img src="./images/b1.png" alt="图标">
						<span>以旧换新</span>
					</a>
				</div>
				<div class="item left_float">
					<a href="https://www.mi.com/">
						<img src="./images/b2.png" alt="图标">
						<span>话费充值</span>
					</a>
				</div>
				<div style="clear: both"></div>
			</div>
			
			<div class="list-item left_float" style="margin-right: 15px">
				<img src="./images/0cf5e958bc88727b50c5c5fba7a8f47a.jpg" alt="图片1">
			</div>
			
			<div class="list-item  left_float" style="margin-right: 15px">
				<img src="./images/6dd2f3e0de4e6cbba98fd3799cfa5bf7.jpg" alt="图片2">
			</div>
			
			<div class="list-item  left_float">
				<img src="./images/d7d4be1a9e701e16de498f89b1865867.jpg" alt="图片3">
			</div>
			<div style="clear: both"></div>
		</div>
	</div>
</body>
</html>
```

用到的知识点：

```html
opacity: 0.7；/* 透明度 */
```

实现效果：![实现效果](./images/小米商城-实现效果.png)

#### `CSS`知识点

##### `hover`（伪类）

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>hover</title>
	<style>
		.c1 {
			color: black;
			font-size: 40px;
		}
		
		.c1:hover {
			color: #CC0000;
			font-size: 50px;
		}
		
		.c2 {
			height: 300px;
			width: 500px;
			border: 2px solid black;
		}
		
		.c2:hover {
			border: 5px solid blue;
		}
		
		.download{
			display: None;
		}
		.app{
			width: 310px;
		}
		.app:hover .download{
			display: block;
		}
		.app:hover .title{
			color: yellow;
		}
	</style>
</head>
<body>
	<div class="c1">联通</div>
	<div class="c2">电信</div>
	<div class="c3">移动</div>

	<div class="app">
		<div class="title">点击下载APP</div>
		<div class="download">
			<img src="./images/qrcode.png" alt="QRcode">
		</div>
	</div>
</body>
</html>
```

##### `after`（伪类）

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>after</title>
	<style>
		.c1:after{
			content: "大帅哥";
		}
	</style>
</head>
<body>
	<div class="c1">
		buweishi
	</div>
	<div class="c1">
		bujinyu
	</div>
</body>
</html>
```

展示效果：注意——这个不需要鼠标放上去 展示出来就是这个样子

![展示效果](../../images/after.png)

★★★注意：当使用`after`按照以下的样式写的时候，咋不需要写`<div style="clear: both;"></div>`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>after</title>
	<style>
		.item{
			float: left;
		}
		.clearfix:after{
			content: "" ;
			display: block;
			clear: both;
		}
	</style>
</head>
<body>
	<div class="clearfix">
		<div class="item">1</div>
		<div class="item">2</div>
		<div class="item">3</div>
		<div class="clear: both"></div>
	</div>
</body>
</html>
```

##### `position`

-   `fixed`
-   `relative`
-   `absolute`

###### `fixed`:

固定在窗口的某个位置

案例——返回顶部

```html
.back{
    position: fixed;
    width: 60px;
    height: 60px;
    border: 2px solid black;
    right: 10px;
    bottom: 10px;
}
```

```html
<div class="back">
</div>
```

案例：对话框

```html
.dialog{
    position: fixed;
    height: 300px;
    width: 500px;
    background-color: white;
    left: 50%;  # 居中
    margin: -250px;
    top: 200px;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>对话框</title>
	<style>
		body{
			margin: 0;
		}
		.dialog{
			position: fixed;
			height: 300px;
			width: 500px;
			background-color: white;
			top: 200px;
			left: 0;
			right: 0;
			margin: 0 auto;
			z-index: 1000;
		}
		.mask{
			background-color: black;
			opacity: 0.7;
			position: fixed;
			left: 0;
			top: 0;
			right: 0;
			bottom: 0;
			z-index: 999;
		}
	</style>
</head>
<body>
	<div style="height: 2000px">就算是牛逼的</div>
	<div class="mask"></div>
	<div class="dialog">
	</div>
</body>
</html>
```

上面代码显示的效果：<img src="../../images\image-20230427220244654.png" alt="image-20230427220244654" style="zoom: 33%;" />

###### `relative`和`absolute`

相对显示和背景色

```html
# 边框：
border: 1px solid black; —— 上下左右边框
solid: 实线
dotted: 虚线
black: 颜色

border-left: 1px solid black; —— 左边框

也可以
border: 1px solid black; —— 上下左右边框
border-left: 1px solid black; —— 左边框
两者同时修改也行

# 特殊的一个点：
transparent: 透明度 一般和hover结合的时候用
```

```html
# 背景色
background-color
```

### `BootStrap`

别人已经写好的一些`css`样式

使用：

-   下载`BootStrap`
-   使用
    -   在页面上引用`BootStrap`
    -   变现`HTML` 按照`BootStrap`的规定编写 —— 注意无法完全实现功能 + 自定制
-   `BootStrap`网址：`https://v3.bootcss.com/`

#### 初识`BootStrap`

-   下载： 用于生产环境的 `Bootstrap`

    ![image-20230427224345735](../../images\image-20230427224345735.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>初识BootStrap</title>
	<!-- 开发版本 -->
	<link rel="stylesheet" href="plugins/bootstrap-3.4.1/css/bootstrap.css">
	
	<!-- 生产版本 -->
	<!-- <link rel="stylesheet" href="./static/plugins/bootstrap-3.4.1/css/bootstrap.min.css"> -->
	
	
</head>
<body>
	<input type="button" value="提交">
	<input type="button" value="提交" class="btn">
	<input type="button" value="提交" class="btn btn-primary">
	<input type="button" value="提交" class="btn btn-success">
	<input type="button" value="提交" class="btn btn-danger">
	<input type="button" value="提交" class="btn btn-danger btn-xs">
</body>
</html>
```

上面`HTNL`显示结果：<img src="../../images\image-20230428183645898.png" alt="image-20230428183645898" style="zoom: 50%;" />

```python
# TODO: day12-2 18:16
```

#### 导航

```css
/* 圆角 */
.navbar {
	border-radius: 10px;
}
```

显示效果：<img src="../..\images\image-20230428190652027.png" alt="image-20230428190652027" style="zoom:33%;" />

稍微修改下，可以实现下面的效果：

![image-20230428191911483](../..\images\image-20230428191911483.png)

#### 栅格系统

`https://v3.bootcss.com/css/#grid`

-   把整体划分为12个列

-   分类：

    -   响应式  根据屏幕宽度显示网页

        -   `.col-sm-  1170px`
        -   `.col-md-  970px`
        -   `.col-lg-  750px`

    -   非响应式 不随着整个页面的大小调整而调整
        ```html
        <div class="col-xs-2" style="background-color: #0ebe90; height: 10px;"></div>
        <div class="col-xs-10"></div>
        ```

#### 列偏移

```html
<div class="col-sm-offset-2 col-sm-6" style="background-color: #0ebe90; height: 50px;">
    222
</div>
```

####  `container`

-   ```html
    <div class="container-fluid">
    	<div class="col-sm-9">左边</div>
    	<div class="col-sm-3">右边</div>
    </div>
    ```

-   ```html
    <div class="container">
    	<div class="col-sm-9">左边</div>
    	<div class="col-sm-3">右边</div>
    </div>
    ```

####  面板

```html
<div class="col-sm-3">
    <div class="panel panel-default">
        <div class="panel-heading">
            默认最新推荐
        </div>
        <div class="panel-body">
            最新推荐内容
            最新推荐内容
            最新推荐内容
            最新推荐内容
        </div>
    </div>

    <div class="panel panel-primary">
        <div class="panel-heading">
            primary最新推荐
        </div>
        <div class="panel-body">
            最新推荐内容
            最新推荐内容
            最新推荐内容
            最新推荐内容
        </div>
    </div>

    <div class="panel panel-success">
        <div class="panel-heading">
            success最新推荐
        </div>
        <div class="panel-body">
            最新推荐内容
            最新推荐内容
            最新推荐内容
            最新推荐内容
        </div>
    </div>

    <div class="panel panel-info">
        <div class="panel-heading">
            info最新推荐
        </div>
        <div class="panel-body">
            最新推荐内容
            最新推荐内容
            最新推荐内容
            最新推荐内容
        </div>
    </div>

    <div class="panel panel-warning">
        <div class="panel-heading">
            warning最新推荐
        </div>
        <div class="panel-body">
            最新推荐内容
            最新推荐内容
            最新推荐内容
            最新推荐内容
        </div>
    </div>

    <div class="panel panel-danger">
        <div class="panel-heading">
            danger最新推荐
        </div>
        <div class="panel-body">
            最新推荐内容
            最新推荐内容
            最新推荐内容
            最新推荐内容
        </div>
    </div>
</div>
```

上面代码实现效果：

<img src="../..\images\image-20230428200344925.png" alt="image-20230428200344925" style="zoom:50%;" />

####  媒体对象

```html
<div class="media">
    <div class="media-left">
        <a href="#">
            <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                 src="..."
                 data-holder-rendered="true" style="width: 64px; height: 64px;">
        </a>
    </div>
    <div class="media-body">
        <h4 class="media-heading">媒体标题</h4>
        Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin commodo. Cras
        purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate
        fringilla. Donec lacinia congue felis in faucibus.
    </div>
</div>
```

<img src="../..\images\image-20230428201612692.png" alt="image-20230428201612692" style="zoom:50%;" />

#### 2.3.8 分页

```html
<ul class="pagination">
    <li class="disabled">
        <a href="#" aria-label="Previous">
            <span aria-hidden="true">
                «
            </span></a></li>
    <li class="active"><a href="#">
        1
        <span class="sr-only">
            (current)
        </span></a></li>
    <li>
        <a href="#">
            2
        </a>
    </li>
    <li>
        <a href="#">
            3
        </a>
    </li>
    <li>
        <a href="#">
            4
        </a>
    </li>
    <li>
        <a href="#">
            5
        </a>
    </li>
    <li>
        <a href="#" aria-label="Next">
            <span aria-hidden="true">
                »
            </span>
        </a>
    </li>
</ul>
```

#### 案例：

<img src="../..\images\image-20230428194447201.png" alt="image-20230428194447201" style="zoom: 50%;" />

实现效果：

<img src="../..\images\image-20230428202754835.png" alt="image-20230428202754835" style="zoom: 33%;" />

####  图标和表单

案例 —— 登录

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>form</title>
	<link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
	<style>
		.account {
			width: 300px;
			height: 350px;
			border: 1px solid dimgrey;
			margin-left: auto;
			margin-right: auto;
			margin-top: 100px;
			padding: 20px 40px;
			border-radius: 5px;
			box-shadow:-5px 5px 20px #aaa;/* 阴影： 水平 垂直 模糊距离 颜色*/
		}
		
		.account h1 {
			text-align: center;
			margin-top: 5px;
			padding-bottom: 20px;
			font-size: 30px;
		}
	</style>
</head>
<body>
<div class="account">
	<h1><strong>用户登录</strong></h1>
	<form>
		<div class="form-group">
			<label for="exampleInputEmail1">用户名</label>
			<input type="email" class="form-control" id="exampleInputEmail1" placeholder="手机号/邮箱/用户名">
		</div>
		<div class="form-group">
			<label for="exampleInputPassword1">用户密码</label>
			<input type="password" class="form-control" id="exampleInputPassword1" placeholder="密码">
		</div>
		<div class="checkbox">
			<label>
				<input type="checkbox"> Check me out
			</label>
		</div>
		<button type="submit" class="btn btn-primary">登录</button>
	</form>
</div>
</body>
</html>
```

上述实例所展示出的效果：

<img src="../..\images\image-20230428210112608.png" alt="image-20230428210112608" style="zoom: 67%;" />

#### 案例：后台管理系统

<img src="../..\images\image-20230428210838018.png" alt="image-20230428210838018" style="zoom: 50%;" />

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>后台管理系统</title>
	<link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
	<style>
		.navbar {
			border-radius: 10px;
		}
		
		.container {
			width: 1200px;
			border: 1px solid #aaaaaa;
			box-shadow: 5px 5px 20px #aaa;
		}
		
		.new {
			margin-top: 10px;
			margin-bottom: 10px;
		}
		
		.my-button {
			display: inline-block;
			margin-left: 10px;
			margin-top: 10px;
			margin-bottom: 10px;
		}
	</style>
</head>
<body>
<nav class="navbar navbar-default">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">xxx管理系统</a>
		</div>
		
		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li class="active"><a href="#">link <span class="sr-only">(current)</span></a></li>
				<li><a href="#">兰州</a></li>
				<li><a href="#">天水</a></li>
				<li><a href="#">白银</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">选择 <span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">Action</a></li>
						<li><a href="#">Another action</a></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">Separated link</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">One more separated link</a></li>
					</ul>
				</li>
			</ul>
			<form class="navbar-form navbar-left">
				<div class="form-group">
					<input type="text" class="form-control" placeholder="Search">
				</div>
				<button type="submit" class="btn btn-default">Submit</button>
			</form>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="./form.html">登录</a></li>
				<li><a href="./form.html">注册</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">Dropdown <span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">Action</a></li>
						<li><a href="#">Another action</a></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">Separated link</a></li>
					</ul>
				</li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</nav>
<div class="container">
	<div class="new">
		<div class="my-button">
			<button type="button" class="btn btn-primary">增加用户</button>
		</div>
		<div class="my-button">
			<button type="button" class="btn btn-primary">删除用户</button>
		</div>
		<div class="my-button">
			<div class="form-group">
					<input type="text" class="form-control" placeholder="搜索用户">
			</div>
		</div>
	</div>
	<div class="my-table">
		<table class="table table-hover table-bordered table-striped">
			<tbody>
			<tr>
				<th>表头1</th>
				<th>表头2</th>
				<th>表头3</th>
			</tr>
			<tr>
				<td>哈哈</td>
				<td>嘻嘻</td>
				<td>呵呵</td>
			</tr>
			<tr>
				<td>哈哈</td>
				<td>嘻嘻</td>
				<td>呵呵</td>
			</tr>
			<tr>
				<td>哈哈</td>
				<td>嘻嘻</td>
				<td>呵呵</td>
			</tr>
			<tr>
				<td>哈哈</td>
				<td>嘻嘻</td>
				<td>呵呵</td>
			</tr>
			</tbody>
		</table>
	</div>
</div>
</body>
</html>
```

上述代码展示效果为：![image-20230428215547645](../..\images\image-20230428215547645.png)

#### 案例：面板 + 后台管理系统

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>后台管理系统</title>
	<link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
	<style>
		.navbar {
			border-radius: 10px;
		}
		
		.container {
			width: 1200px;
			border: 1px solid #aaaaaa;
			box-shadow: 5px 5px 20px #aaa;
		}
		
		.new {
			margin-top: 0;
			margin-bottom: 0;
		}
		
		.my-button {
			display: inline-block;
			margin-left: 10px;
			margin-top: 10px;
			
		}
		
		.add-panel {
			margin-top: 10px;
			margin-bottom: 10px;
		}
	</style>
</head>
<body>
<nav class="navbar navbar-default">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">xxx管理系统</a>
		</div>
		
		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li class="active"><a href="#">link <span class="sr-only">(current)</span></a></li>
				<li><a href="#">兰州</a></li>
				<li><a href="#">天水</a></li>
				<li><a href="#">白银</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">选择 <span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">Action</a></li>
						<li><a href="#">Another action</a></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">Separated link</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">One more separated link</a></li>
					</ul>
				</li>
			</ul>
			<form class="navbar-form navbar-left">
				<div class="form-group">
					<input type="text" class="form-control" placeholder="Search">
				</div>
				<button type="submit" class="btn btn-default">Submit</button>
			</form>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="./form.html">登录</a></li>
				<li><a href="./form.html">注册</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">Dropdown <span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">Action</a></li>
						<li><a href="#">Another action</a></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">Separated link</a></li>
					</ul>
				</li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</nav>
<div class="container">
	<div class="panel panel-default add-panel">
		<div class="panel-heading">
			<h3 class="panel-title">提交信息</h3>
		</div>
		<div class="panel-body">
			<form class="form-inline">
				<div class="form-group">
					<label for="exampleInputName2">Name</label>
					<input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
				</div>
				<div class="form-group">
					<label for="exampleInputEmail2">Email</label>
					<input type="email" class="form-control" id="exampleInputEmail2" placeholder="jane.doe@example.com">
				</div>
				<button type="submit" class="btn btn-default">Send invitation</button>
			</form>
		</div>
	</div>
	
	<div class="panel panel-default add-panel">
		<div class="panel-heading">
			<h3 class="panel-title">用户操作</h3>
		</div>
		<div class="panel-body">
			<div class="new">
				<div class="my-button">
					<button type="button" class="btn btn-primary">增加用户</button>
				</div>
				<div class="my-button">
					<button type="button" class="btn btn-primary">删除用户</button>
				</div>
				<div class="my-button">
					<div class="form-group">
						<label>
							<input type="text" class="form-control" placeholder="搜索用户">
						</label>
					</div>
				</div>
				<!-- <h5>注意：以下是重要数据！</h5> -->
				<div class="my-table">
					<table class="table table-hover table-bordered table-striped">
						<tbody>
						<tr>
							<th>#</th>
							<th>表头1</th>
							<th>表头2</th>
							<th>操作</th>
						</tr>
						<tr>
							<td>1</td>
							<td>哈哈</td>
							<td>嘻嘻</td>
							<td>
								<a href="" class="btn btn-primary btn-xs">编辑</a>
								<a href="" class="btn btn-danger btn-xs">删除</a>
							</td>
						</tr>
						<tr>
							<td>2</td>
							<td>哈哈</td>
							<td>嘻嘻</td>
							<td>
								<a href="" class="btn btn-primary btn-xs">编辑</a>
								<a href="" class="btn btn-danger btn-xs">删除</a>
							</td>
						</tr>
						<tr>
							<td>3</td>
							<td>哈哈</td>
							<td>嘻嘻</td>
							<td>
								<a href="" class="btn btn-primary btn-xs">编辑</a>
								<a href="" class="btn btn-danger btn-xs">删除</a>
							</td>
						</tr>
						<tr>
							<td>4</td>
							<td>哈哈</td>
							<td>嘻嘻</td>
							<td>
								<a href="" class="btn btn-primary btn-xs">编辑</a>
								<a href="" class="btn btn-danger btn-xs">删除</a>
							</td>
						</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</div>
	<div>
		<ul class="pagination">
	        <li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">«</span></a></li>
	        <li class="active"><a href="#">1 <span class="sr-only">(current)</span></a></li>
	        <li><a href="#">2</a></li>
	        <li><a href="#">3</a></li>
	        <li><a href="#">4</a></li>
	        <li><a href="#">5</a></li>
	        <li><a href="#" aria-label="Next"><span aria-hidden="true">»</span></a></li>
	     </ul>
	</div>
</div>
</body>
</html>
```

上面的代码所展示的形式如下图所示：

![image-20230428222646243](../..\images\image-20230428222646243.png)

####  图标

-   `bootstrap `提供的图标不多
-   `fontawesome`组件  `https://fontawesome.dashgame.com/`

-   下载并引入

```html
<link rel="stylesheet" href="static/plugins/font-awesome/font-awesome-4.7.0/css/font-awesome.css">
```

####  依赖

`bootstrap`依赖`JavaScript`的类库，`JQuery`

-   下载`JQuery`
-   应用`JQuery`
-   在页面上应用`Bootstrap`的`JS`类库

###  `JavaScript`

-   编程语言
-   浏览器就是`JavaScript`的解释器
-   `DOM`和`BOM`
  
    ```html
    相当于js内置的模块、函数
    ```
-   类库（模块）
-   `JQuery`是`js`的一个类库，相当于是js`的`第三方模块

#### `javascript`

`javascript `是一种编程语言

意义：让网站展示动态效果

前端三大组件：

-   `html`
-   `CSS`
-   `javascript`

1.1 存放代码位置：

-   `head`标签里面，`css`标签下面
-   在`body`标签的内部，紧邻</body>之前编写 —— 推荐

1.2 `js`代码的存在形式：

写在`html`文件中

写在文件中

1.3 注释

`html`的注释：`<!-- 注释内容 -->`

`css`的注释：`/* 注释内容 */`  `<style>代码块里面`

`javascript`的注释：`/**/ 或者 //`  `<script>`代码块里面

```js
// 注释内容
/* 注释内容 */
```

##### `javascript`变量

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>变量</title>
</head>
<body>
<script type="text/javascript">
	var name = "瑾瑜"
    console.log(name)
</script>
</body>
</html>
```

通过语句`console.log(name)`在浏览器中打开抓包工具，找`console`，刷新页面既可在浏览器抓包工具中找变量的值。

#####  字符串类型

```javascript
//  声明
var name = "鲸鱼";
var name = String("金鱼");
```

```javascript
var name = "xxxx";
var v1 = name.length;
// 按照索引取字符串中的一个字符
var v2 = name[0];
var v2 = name.charAt(1)
var v3 = name.trim();  // 去除空白
var v4 = name.substring(1, 2);  // 左闭右开
```

案例：跑马灯

```html
<body>
<span id="text">欢迎光临</span>
<script type="text/javascript">
	function show() {
		// 去html中找到某个标签并且获取他的内容 DOM
		var tag = document.getElementById("text");
		var dataString = tag.innerText;
		console.log(dataString);
		// 动态起来 把文本第一个字符放到最后面
		var firstChar = dataString[0];
		var otherString = dataString.substring(1, dataString.length);
		var newText = otherString + firstChar;
		console.log(newText);
		// 在html中更新内容
		tag.innerText = newText;
	}
	// DOM 中定时器 如，每一秒执行一次show函数
	setInterval(show, 1000);
</script>
</body>
```

##### 数组

```javascript
// 定义
var v1 = [11, 22, 33, 44]
var v2 = Array([11, 22, 33])
```

```javascript
//操作
var v1 = [11, 22, 33]
v1[1] = "jinyu"
v1.push(999)  // 尾部添加元素
v1.unshift(1000)  // 头部添加元素
v1.splice(索引, 0, 元素)如：v1.splice(1, 0, "haha")  // 任意位置插入
v1.pop()  // 尾部删除
v1.shift() // 头部删除
v1.splice(索引, 1)  // 删除任意位置
```

```javascript
var v1 = [11, 22, 33, 44]
for (var index in v1) {
    // 注意：循环的是索引
    // index： 0 1 2 3
    // data = v1[index]
}
```

```javascript
for (var i=0; i < v1.length; i++) {
    // i = 0/1/2/3
}
```

注意：循环中`break`和`continue`也有

案例 - 利用`js`添加标签及文字

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>数组</title>
</head>
<body>
<ul id="city">
	<!--
	<li>北京</li>
	<li>上海</li>
	<li>深圳</li>
	<li>广州</li>
	-->
</ul>

<script type="text/javascript">
	// 发送网络请求，可以获取数据，保存在数组中
	var cityList = ["北京", "上海", "深圳", "广州"] ;
	for (var index in cityList) {
		var text = cityList[index] ;
		// 文本添加到标签里面： DOM的功能
		
		// 创建<li>标签
		var tag = document.createElement("li") ;
		// 在li标签中写入内容
		tag.innerText = text ;
		// 添加到id = "city"标签里面 DOM
		var parentTag = document.getElementById("city") ;
		parentTag.appendChild(tag) ;
	}
</script>
</body>
</html>
```

#####  对象（字典）

```javascript
info = {
    "name": "jinyu",
    "age": 18
}
info = {
    name: "jinyu",
    age: 18
}
```

```javascript
info.age ;
info.name = "qiongju"
// 或者按照下面这样
info["age"]
info["name"] = "qiongju"

delete info["age"]
```

```javascript
info = {
    name: "jinyu",
    age: 18
}

// 循环：
for (var key in info) {
    // key : name/age
    // data: info[key]
}
```

案例 - 动态表格：

```html
<body>
<table border="1">
	<thead>
	<tr>
		<th>ID</th>
		<th>name</th>
		<th>age</th>
	</tr>
	</thead>
	<tbody id="body">
	<!-- <tr>
		<td>1</td>
		<td>1</td>
		<td>1</td>
	</tr> -->
	</tbody>
</table>

<script type="text/javascript">
	var dataList = [
		{id: 100001, name: "jinyu", age: 19},
		{id: 100002, name: "qingju", age: 19},
		{id: 100003, name: "qiongjiu", age: 19},
		{id: 100004, name: "qingyao", age: 19},
		{id: 100005, name: "zhengze", age: 19}
	];
	for (index in dataList) {
		var info = dataList[index] ;
		var tr = document.createElement("tr");
		for (var key in info) {
			var text = info[key];
			var td = document.createElement("td");
			td.innerText = text;
			tr.appendChild(td);
		}
		// console.log(tr)
		var bodyTag = document.getElementById("body");
		bodyTag.appendChild(tr);
	}
</script>
</body>
```

显示结果：

<img src="../..\images\image-20230429214735273.png" alt="image-20230429214735273" style="zoom:67%;" />

#####  条件语句

```javascript
if (条件) {
    
} else {
    
}
```

```javascript
if (条件) {
    
} else if (条件) {
    
} else if (条件) {
    
} else {
    
}
```

#####  函数

```javascript
function func() {
    ...
}
    
func()
```

#### `DOM`

就是一个模块，可以对`html`中标签进行操作。

```javascript
// 根据ID获取标签
var Tag = document.getElementById("xx") ;

// 获取标签中文本
tag.innerText ;

// 设置标签中的文本
tag.innerText = "hahahahaha" ;

//创建标签 <div></div>
var tag = document.createElement("div") ;

// 标签写内容
tag.innerText = "hahahahahahaha" ;
```

```html
<ul id="city">
	<!--
	<li>北京</li>
	-->
</ul>
```

```javascript
// 在上面代码块所展示的页面中添加东西：
<script type="text/javascript">
	// 发送网络请求，可以获取数据，保存在数组中
	var cityList = ["北京", "上海", "深圳", "广州"] ;
	for (var index in cityList) {
		var text = cityList[index] ;
		// 文本添加到标签里面： DOM的功能
		
		// 创建<li>标签
		var tag = document.createElement("li") ;
		// 在li标签中写入内容
		tag.innerText = text ;
		// 添加到id = "city"标签里面 DOM
		var parentTag = document.getElementById("city") ;
		parentTag.appendChild(tag) ;
	}
</script>

// 添加新的 newTag 到 tag 中
tag.appendChild(newTag) ;
```

##### 事件的绑定

```javascript
<body>
<input type="text" placeholder="输入信息" id="getText">
<input type="button" value="点击添加" ondblclick="add_city()">
<ul id="city">
</ul>
<script type="text/javascript">
	function add_city() {
		// 找到标签
		var messageInputTag = document.getElementById("getText");
		// 获取用户输入的内容
		var textInput = messageInputTag.value;
		//判断用户输入是否为空，只有不是空才能继续
		if (textInput.length > 0) {
			// 创建一个标签 用以保存数据并且准备以后展示，中间的文本信息就是用户输入的内容
			var newTag = document.createElement("li");
			// 将文本添加进去
			newTag.innerText = textInput;
			// 定位标签并把把标签添加上去
			var parentTag = document.getElementById("city");
			parentTag.appendChild(newTag);
			// 让input框内容重新为空
			messageInputTag.value = "";
		}
		else {
			alert("输入内容为空，请重新输入！")
		}	
	}
</script>
</body>
```

注意：`onclick`是鼠标单击触发事件，`ondblclick`是鼠标双击触发事件。

此外，`DOM`可以实现很多操作，但是很繁琐，很多的工作是`JQuery`实现的。或者`VUE`实现的。

#### `JQuery`

是一个`javascript`第三方模块

-   基于`JQuery`，自己开发一些工具/功能
-   现成的工具是依赖`JQuery`，例如`BootStrap`动态效果需要使用`JQuery`。

##### 快速上手

下载``

应用

```html
<body>
<h1 id="txt">阿里嘎多</h1>
<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script type="text/javascript">
	// 利用JQuery实现我们需要的效果
	// 找到id="txt"标签
	//修改内容
	$("#txt").text("美羊羊桑")
</script>
</body>
```

##### 寻找标签(直接寻找)

-   `id`

```html
<h1 id="txt">阿里嘎多</h1>
<h1>阿里嘎多</h1>
<h1>阿里嘎多</h1>
```

```javascript
$("#txt")
```

-   样式(类)

```html
<h1 class="c1">阿里嘎多</h1>
<h1 class="c1">阿里嘎多</h1>
<h1 class="c2">阿里嘎多</h1>
```

```javascript
$(".c1")
```

-   标签

```html
<h1 class="c1">阿里嘎多</h1>
<div class="c1">阿里嘎多</div>
<h1 class="c2">阿里嘎多</h1>
```

```javascript
$("h1")
```

-   层级

```html
<h1 class="c1">阿里嘎多</h1>
<div class="c1">
    <div class="c2">
    	<span></span>
        <a></a>
    </div>
</div>
<h1 class="c2">阿里嘎多</h1>
```

```javascript
$(".c1 .c1 a")
```

-   多个选择

```html
<h1 class="c1">阿里嘎多</h1>
<div class="c1">
    <div class="c3">
    	<span></span>
        <a></a>
    </div>
</div>
<h1 class="c2">阿里嘎多</h1>
<ul>
    <li>xxx</li>
    <li>xxx</li>
</ul>
```

```javascript
$("#c3,#c2,li")
```

-   属性

```html
<input type="text" name="n1" />
<input type="text" name="n1" />
<input type="text" name="n2" />
```

```javascript
$("input[name="n1"]")
```

##### 间接寻找

-   找兄弟

```html
<div>
    <div>北京</div>
    <div id="c1">上海</div>
    <div>深圳</div>
    <div>广州</div>
</div>
```

```javascript
$("#c1").prev()         // 上一个兄弟
$("#c1")
$("#c1").next()         // 下一个兄弟
$("#c1").next().next()  // 下一个兄弟的下一个兄弟
$("#c1").siblings()     // 找到所有的兄弟
```

-   找父子

```html
<div>
    <div>
        <div id="c1">北京
            <div>朝阳区</div>
            <div class="p10">和平区</div>
            <div>八达岭</div>
        </div>
        <div>上海</div>
        <div>深圳</div>
        <div>广州</div>
    </div>
    <div>
        <div>甘肃</div>
        <div>山西</div>
        <div>陕西</div>
        <div>河南</div>
    </div>
</div>
```

```javascript
$("#c1").parent()
$("#c1").parent().parent()

$("#c1").children()  // 所有的孩子
$("#c1").children(".p10")  // 所有的孩子中符合 class="p10" 的
$("#c1").find(".p10")  // 所有的子孙里面找.p10
$("#c1").find("div")  // 所有的子孙里面找div
```

案例：菜单的切换

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>菜单的切换</title>
	<style>
		.menus {
			width: 200px;
			height: 800px;
			border: 1px solid #0a0a0a;
		}
		.menus .header {
			background-color: gold;
			padding: 10px 5px;
			border-bottom: 1px dotted #aaa;
			cursor: pointer;
		}
		
		.menus .container a {
			display: block;
			padding: 5px 5px;
			border-bottom: 1px dotted #aaa;
		}
		
		.hide {
			display: none;
		}
	</style>
</head>
<body>
<div class="menus">
	<div class="item">
		<div class="header" onclick="clickMe(this)">甘肃</div>
		<div class="container">
			<a href="">兰州</a>
			<a href="">天水</a>
			<a href="">白银</a>
		</div>
	</div>
	
	<div class="item">
		<div class="header" onclick="clickMe(this)">北京</div>
		<div class="container hide">
			<a href="">朝阳区</a>
			<a href="">海淀区</a>
			<a href="">王府井</a>
		</div>
	</div>
	
	<div class="item">
		<div class="header" onclick="clickMe(this)">甘肃2</div>
		<div class="container hide">
			<a href="">兰州</a>
			<a href="">天水</a>
			<a href="">白银</a>
		</div>
	</div>
	
	<div class="item">
		<div class="header" onclick="clickMe(this)">北京2</div>
		<div class="container hide">
			<a href="">朝阳区</a>
			<a href="">海淀区</a>
			<a href="">王府井</a>
		</div>
	</div>
</div>

<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js">

</script>

<script>
	function clickMe(self) {
		// 让自己下面的功能显示出来
		// 让其他的功能不显示
		$(self).next().removeClass("hide")
		$(self).parent().siblings().find(".container").addClass("hide")
	}
</script>
</body>
</html>
```

##### 操作样式

-   `addClass()`
-   `removeClass()`
-   `hasClass()`

##### 值的操作

```html
<div id="c1">内容</div>
```

```javascript
$("#c1").text()        // 文本内容
$("#c1").text("xx")    // 设置值
```

```html
<input type="text" id="c2" />
```

```javascript
$("#c2").val()  // 获取用户输入的值
$("#c2").val("hahaha")  // 设置值
```

案例：动态创建数据

```html
<body>

<label for="txtUser"></label><input type="text" id="txtUser" placeholder="user name"/>
<label for="txtEmail"></label><input type="text" id="txtEmail" placeholder="Email"/>
<input type="button" value="提交" onclick="getInfo()"/>
<ul id="view">
</ul>
<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>

<script>
	function getInfo() {
		// 获取用户名和邮箱
		const name = $("#txtUser").val();
		const email = $("#txtEmail").val();
		const dataString = name + " - " + email
		const newLi = $("<li>").text(dataString)
		$("#view").append(newLi)
	}
</script>
</body>
```

##### 事件绑定

```html
<ul>
    <li>百度</li>
    <li>谷歌</li>
    <li>搜狗</li>
</ul>

<script>
	$("li").click(function () {
		$(this)  // 当前点击的是哪个标签
	}) // 点击li标签的时候就执行function()函数
	
</script>
```

举例：点击某个标签就在console里面显示哪个标签里面的文本内容

```html
<body>
<ul>
	<li>百度</li>
	<li>谷歌</li>
	<li>搜狗</li>
</ul>
<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script>
	$("li").click(function () {
		const text = $(this).text()  // 当前点击的是哪个标签
		console.log(text)
	}) ; // 点击li标签的时候就执行function()函数
	
</script>
</body>
```

删除某个标签

```html
<div id="c1">内容</div>

<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script>
    $("#c1").remove() ;
</script>
```

```html
<body>
<ul>
	<li>百度</li>
	<li>谷歌</li>
	<li>搜狗</li>
</ul>
<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script>
	$("li").click(function () {
		const text = $(this).text()  // 当前点击的是哪个标签
		console.log(text)
		$(this).remove()
	}); // 点击li标签的时候就执行function()函数
</script>
</body>
```

当页面框架加载完成之后执行代码

```html
<body>
<ul>
	<li>百度</li>
	<li>谷歌</li>
    <img src="./static/images/image01.jpg" alt="图片"/>
	<li>搜狗</li>
</ul>
<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script>
    // 特殊的格式，当页面框架加载完成之后，自动执行
    $(function() {
        $("li").click(function () {
            // const text = $(this).text()  // 当前点击的是哪个标签
            // console.log(text)
            $(this).remove()
        }); // 点击li标签的时候就执行function()函数
    }) ;
	
</script>
</body>
```

案例：表格操作

```html
<body>
<table border="1">
	<thead>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>Operation</th>
	</tr>
	</thead>
	<tbody>
	<tr>
		<td>1</td>
		<td>jinyu</td>
		<td>
			<input type="button" value="编辑">
			<input type="button" value="删除" class="delete">
		</td>
	</tr>
	<tr>
		<td>1</td>
		<td>jinyu</td>
		<td>
			<input type="button" value="编辑">
			<input type="button" value="删除" class="delete">
		</td>
	</tr>
	<tr>
		<td>1</td>
		<td>jinyu</td>
		<td>
			<input type="button" value="编辑">
			<input type="button" value="删除" class="delete">
		</td>
	</tr>
	<tr>
		<td>1</td>
		<td>jinyu</td>
		<td>
			<input type="button" value="编辑">
			<input type="button" value="删除" class="delete">
		</td>
	</tr>
	</tbody>
</table>
<script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script>
	// 特殊的格式，当页面框架加载完成之后，自动执行
	$(function () {
		// 找到所有class=delete的标签 删除之
		$(".delete").click(function () {
			// 删除当前行的数据
			$(this).parent().parent().remove();
		});
	});
</script>
</body>
```

前端整合小案例：

-   `HTML`
-   `CSS`
-   `javascript`、`Jquery`
-   `BootStrap`（动态效果依赖`BootStrap`）

案例：添加数据页面

>   人员信息登录功能，需要提供用户信息
>
>   -   用户名 年龄 薪资 部门 入职时间（*）
>   -   时间的选择 `datatimepicker`
>       -   下载插件https://cdnjs.com/libraries/bootstrap-datetimepicker
>       -   或者https://www.bootcdn.cn/bootstrap-datetimepicker/
>       -   应用插件 —— 官方文档 https://bootstrap-datepicker.readthedocs.io/en/latest/ 
>       -   中文文档 https://espespcp.com/docs/bootstrap-datepicker/1/9.html

## `web`框架

### `flask`框架

...

### `Django`框架

#### 初识`Django`

-   `Python `函数 面向对象
-   前端 `css html`
-   `mysql`
-   `Python web` 框架
    -   `flask`框架 小而精 简单页面 + 第三方组件
    -   `Django `内部集成了很多的组件 大型项目+ 第三方组件 【主要】

1.   安装`django`

     ```python
     pip install Django
     ```

     ```python
     Django安装后：
     
     D:\PythonCompiler\python310
     	- bin
     	- Scripts
     		- pip.exe
     		- django-admin.exe # 工具，创建Django项目，创建其中文件和文件夹
     	- Lib
     		- 内置模块
     		- site-packages  # 第三方模块
     			- openpyxl
     			- flask
     			- django # 框架源码
     	- python.exe
     ```

     2.   创建项目

     
     ```python
     # django 中项目会有一些默认的文件夹和文件
     ```
     
     -   打开终端
     
     -   进入某个目录（项目放在哪里） 
         我的目录： `D:\PycharmProject\StudyProjects\DjangoProjects`
         
     -   执行命令： 
     
     
     ```python
     django-admin startproject 项目名称
     django-admin startproject site
     ```
     
     -   执行完上述命令后，会创建下列文件：
     
     ```text
     D:\PycharmProject\StudyProjects\DjangoProjects
     	|- mysite(项目名)
     		|- manage.py             # 非常重要 项目管理文件 启动项目 创建app 数据库管理 不动 常常用
     		|- mysite                # 和项目同名
     			|- __init__.py
     			|- setting.py       # 项目配置文件 —— 常写
     			|- urls.py          # 把全部的路径和函数的对应关系卸载这儿 —— 常写
     			|- asgi.py          # 接受网络请求 异步式 不动
     			|- wsgi.py          # 接受网络请求 同步式 不动 
     ```

#### `APP`

```python
- 项目
	- app 用户管理 【表结构 函数 HTML模板 css】
     - app 订单管理 【表结构 函数 HTML模板 css】
     - app 后台管理 【表结构 函数 HTML模板 css】
     - ...          【表结构 函数 HTML模板 css】
        
# 注意：我们开发比较简洁，用不到多APP 一般情况下，项目下创建一个APP既可。—— 用manage.py创建APP即可
```

```python
# 在终端，进入到manage所在的那一层项目文件中：
>>> python ./mysite/manage.py startapp app01
# 可以看到manage.py为我们创建了一个叫app01的文件
```

文件结构是下面这样：

![image-20230505205937091](./images/image-20230505205937091.png)

```python
D:.
├─app01
│  └─migrations
└─mysite
    └─mysite
        └─__pycache__
```

![image-20230505211923370](../../images/image-20230505211923370.png)

其中
```python
apps.py     不用动 app启动
migrations  也不用动 数据库迁移 变更记录
tests       单元测试，不用动
admin.py    不用动 默认提供admin的功能
views.py    **重要** 和urls配合使用 写函数
models.py   **重要** 专门用于操作数据库
```

##### 快速上手

-   确保`APP`已注册 
    ```python
    # 在settings.py里面的INSTALLED_APPS列表中
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "app01.apps.App01Config",
    ]
    成为
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "app01.apps.App01Config",
    ]
    其中这个App01Config指的是apps.py文件里面的类名称
    
    # apps.py
    class App01Config(AppConfig):
        default_auto_field = "django.db.models.BigAutoField"
        name = "app01"
    ```

    ![image-20230505213449687](../../images/image-20230505213449687.png)

-   编写`URL`和视图函数的对应关系：`urls.py`中编写
-   编写`views`文件里面的对应函数![image-20230505214155712](../../images/image-20230505214155712.png)

-   启动`Django`项目
    ```python
    # 命令行
    >>> python manage.py runsevere 
    # pycharm启动
    >>> 
    >>>
    >>>
    ```

-   `templates`模板

    
  
-   引入静态文件

    -   在`app`目录下创建`static`文件夹，里面存放`js css images` 和 `plugins`等文件
    -   在`HTML`最顶行加入 `{% load static %}`
    -   在引入静态文件时候，使用`"{% static '/plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}"` 方式引用

    ```python
    # 在开发过程中，一般将图片，css，插件当做静态文件处理
    {% load static %}  # 注意这一句
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<title>Title</title>
    	<link rel="stylesheet" href="{% static '/plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}">  # 注意这一句
    </head>
    <body>
    <h1>index 文件</h1>
    <img src="../static/images/image01.jpg" alt="这是个图片" style="height: 50%; width: 50%;">
    </body>
    </html>
    ```


##### 模板语法

本质上，在`HTML`中写一些占位符，由数据对这些占位符进行替换和处理。

```html
<!-- tpl.html -->
<body>
<h1>tpl 页面</h1>
<div>
	{{ n1 }}
</div>
<div>
	{{ n2 }}
</div>
<div>
	{{ n2.0 }}
	{{ n2.1 }}
	{{ n2.2 }}
</div>
<div>
	{% for item in n2 %}
	<span>{{ item }}</span>
	{% endfor %}
</div>
<hr/>
{{ n3 }}
{{ n3.name }}
{{ n3.salary }}
{{ n3.roles }}
<hr/>
{% for k, v in n3.items %}
	<li>{{ k }} {{ v }}</li>
{% endfor %}
{% for k in n3.keys %}
	<li>{{ k }}</li>
{% endfor %}
{% for v in n3.values %}
	<li>{{ v }}</li>
{% endfor %}
<hr/>
{{ n4 }}
<br>
{{ n4.0 }}
{{ n4.1 }}
<br>
{{ n4.0.name }}
{{ n4.1.salary }}

<hr/>
{% for item in n4 %}
	<div>{{ item.name }}</div>
	<div>{{ item.salary }}</div>
{% endfor %}
<hr/>
{% if n1 == 'buweishi' %}
	<h1>dadadada</h1>
{% elif n1 == 'denghaoliang'%}
	<h1>biubiubiu</h1>
{% else %}
	<h1>dudududu</h1>
{% endif %}
</body>
```

```python
# views.py
def tpl(request):
    name = 'denghaoliang'
    roles = ['admin', 'CEO', 'stuff']
    user_info = {'name': 'bu', 'salary': 10000, 'roles': 'CTO'}
    data_list = [{'name': 'deng', 'salary': 10000, 'roles': 'CEO'},
                 {'name': 'zhou', 'salary': 10000, 'roles': 'CEO'},
                 {'name': 'li', 'salary': 10000, 'roles': 'CTO'}]
    return render(request,
                  'tpl.html',
                  {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})
```

```python
# urls.py
from app01 import views

urlpatterns = [
    ...
    path("tpl/", views.tpl),
]
```

##### 案例：

```html
<!-- html -->
```

```python
# views.py
def something(request):
    # request是一个对象   封装了发过来的所有请求

    # 1. 获取请求方式 get/post
    print(request.method)

    # 2. 在url上传递消息
    print(request.GET)

    # 在请求体中提交数据
    print(request.POST)

    # [响应] 内容字符串内容返回给请求者
    # return HttpResponse('返回内容')

    # 【响应】浏览器重定向
    # 发给Django后，Django向浏览器返回一个值 告诉浏览器自己去百度访问。
    # 而不是Django访问百度后向浏览器返回响应
    return redirect('https://www.baidu.com')
    # [响应] 读取HTML文档的内容 渲染+替换 ->字符串 返回给浏览器
    # return render(request, "something.html")
```

```python
# urls.py
from app01 import views

urlpatterns = [
    path("something/", views.something),
]
```

##### 用户登录

解决下图展示的错误：

![image-20230506195204614](../../images/image-20230506195204614.png)

在提交数据的`HTML`文档中的表单 `form `标签里面的`input`标签的同一层：加入`{% csrf_token %}`

#### 数据库操作- `Django`

在`Django`中，操作数据库更简单，内部提供了`ORM`框架

`ORM`：

-   翻译：翻译`models.xxx.all()` 成为 `SELECT * FROM xxx`
-   操作数据库的表 —— 不用写`sql`语句 **但是无法创建数据库**
-   创建 修改 删除 —— 不用亲自写`SQL`语句

使用：

##### 安装模块：

```python 
pip install mysqlclient
```

##### 自己创建数据库：

启动`mysql`服务、创建数据库（只能自己创建数据库）

##### `Django`链接数据库

在`settings.py`里面配置：

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "NAME": "django",
        "PASSWORD": "xxxxxx",
        "PORT": 3306,
        "USER": "root",
        "CHARSET": "utf8",
    }
}
```

##### `django`操作表 

在`models.py`文件中写

-   创建

    在`models.py`文件中写

    ```python
    # modles.py
    from django.db import models
    # Create your models here.
    class UserInfo(models.Model):
        username = models.CharField(max_length=32)
        password = models.CharField(max_length=64)
        age = models.IntegerField()
    
    """
    执行上面语句，相当于：
    create table app01_userinfo (
        id bigint auto_increment primary key,
        name varchar(32),
        password varchar(64),
        age int
    )
    """
    ```

    执行下列命令：前提是`app`已经注册

    ```text
    >>> python manage.py makemigrations
    >>> python manage.py migrate
    ```

    ![image-20230506214509943](../../images/image-20230506214509943.png)

    ![image-20230506214554381](../../images/image-20230506214554381.png)

-   删除

    如果不想要表了，那么直接把相关的类/列删除或者注释掉，然后再重新执行两条语句即可

    ```text
    >>> python manage.py makemigrations
    >>> python manage.py migrate
    ```

    ★★★ 注意 ★★★

-   修改

    但是，如果要 ★ **新加列** ★：那么就可能有问题，因为可能有以前的数据，这一新加列的数据却不知道

    运行两个命令的时候，会提示你进行选择，

    -   选1，用户提供一个值，输入哪个值，新加的数据的所有值都是你输入的哪个值
    -   选2 ，退出，在后面加入默认的值

    或者，不选择的话，可以加入参数，使值能为空，在参数中加入`null=True blank=null`

    ```python
    # models.py
    class UserInfo(models.Model):
        username = models.CharField(max_length=32)
        password = models.CharField(max_length=64)
        age = models.IntegerField(default=2)
        size = models.IntegerField(default=2)
        height = models.IntegerField(null=True, blank=True)
    ```

    **以后要操作数据可相关内容 只需要在models.py里面操作即可。 **


##### 操作表中数据

**插入**数据：

```python
# models.py:
# 新建数据 insert into app01_department （title） values（"销售部"）
Department.objects.create(title='销售部')
UserInfo.objects.create(username="buweishi", password="123456", age=19)
```

也可以这样写：

```python
# views.py
from app01.models import UserInfo, Department
def orm(request):
    # 测试ORM操作表中的数据
    return render(request, "")
    Department.objects.create(title="销售部")
    Department.objects.create(title="运营部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="人事部")

    UserInfo.objects.create(username="小明", password="m12345679", age=15)
    UserInfo.objects.create(username="小泓", password="h12345679", age=16)
    UserInfo.objects.create(username="小亮", password="l12345679", age=14)
    return HttpResponse("成功")
```

**删除**数据：

```python
# views.py
from app01.models import UserInfo, Department
def orm(request):
    # # 删除数据：
    # for i in range(1, 14):
    #     # 加筛选条件
    #     UserInfo.objects.filter(id=i).delete()
    # # 删除一张表中所有记录：
    # UserInfo.objects.all().delete()
    # Department.objects.all().delete()

    # 获取所有数据 query_set = [行对象， 行对象， 行对象]
    # query_set = UserInfo.objects.all()
    # for obj in query_set:
    #     print(obj.username, obj.age, obj.password, end=' ')
    #     print('\n')

    # # 获取符合某些条件的数据 就算只有一个对象，依旧返回query set 对象
    # query_set = UserInfo.objects.filter(id=15)
    # for obj in query_set:
    #     print(obj.username, obj.age, obj.password, end=' ')
    #     print()

    # 获取符合某些条件的数据 .first代表只去取一行数据 就算只有一个对象，依旧返回query set 对象
    obj = UserInfo.objects.filter(id=15).first()
    print(obj.username, obj.age, obj.password, end=' ')
```

**更新**数据

```python
# views.py

# 更新数据
UserInfo.objects.all().update(password=999)
```

#### 案例：用户管理

-   展示用户列表

    -   对于`UserInfo`这个表
        1.   展示列表
             -   `url`
             -   函数
             -   获取所有信息
             -   `HTML`渲染

-   添加用户：

    -   `url`
    -   函数
        -   `GET`看到页面，输入内容
        -   `POST`提交数据

-   删除用户

    -   `url`
    -   函数

    ```python
    http://localhost:8000/info/delete/?nid=1
    http://localhost:8000/info/delete/?nid=2
    http://localhost:8000/info/delete/?nid=3
    
    def function():
        request.GET.get("nid")
        UserInfo.objects.filter(id=nid).delete()
        return Httpreponse("删除成功！！！")
    ```

#### `Django`开发

主题：用户管理系统

##### 新建一个项目

```python
>>> django-admin startproject my_test
```

##### 新建APP

```python
>>> python manage.py startapp my_site
```

##### 注册APP

```python
INSTALLED_APPS = [
    # 加入下面这一行：
    # "app名称.apps.apps文件下的那个类名称"
    "my_site.apps.MySiteConfig",
]
```

##### 设计表结构 - 利用`django`

```python
# models.py

# # 部门表 
class Department(models.Model):
    """
    部门管理相关数据库。
    """
    title = models.CharField(max_length=32, verbose_name="标题")  # verbose_name 注解
    
    
# # 员工表
class UserInfo(models.Model):
    """
    员工管理相关数据库。
    """
    name = models.CharField(verbose_name="员工姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    depart = models.ForeignKey(to=Department, to_field=id, verbose_name="部门",on_delete=models.CASCADE)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
```

还需要在员工表存储员工所属部门。

可以按照`ID`或者部门名称存。—— 按照数据库范式，**存`ID`**，但是大厂存**名称**。查询数据的时候，需要和另外一张表联合，比较耗时，为了加快查找，允许有数据冗余。

对部门`ID`有没有约束？ —— 需要有约束，用户表不能随便插入部门`ID`。 —— 可以加上约束，只能是部门表中已经存在的部门`ID`。如果只写`BigIntegerField`时不会有约束的，

还有个问题：如果删掉部门，用户表中的关联的用户的怎么办？ 

​	—— 级联删除（删除关联用户）`on_delete=models.CASCADE`

​	—— 置空（前提是允许为空）   `null=True, blank=True, on_delete=models.SET_NULL`

```python
# 这些代码是Django做的相关约束
gender_choices = (
    (1, "男"),
    (2, "女"),
)
gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
```

##### 创建数据库

```python
>>> create database my_django default charset utf8 collate  utf8_general_ci;
```

修改settings.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "NAME": "django",
        "PASSWORD": "WarmDou_TS20866",
        "PORT": 3306,
        "USER": "root",
        "CHARSET": "utf8",
    }
}
```

##### 开发 —— 部门管理

本案例在`D:\PycharmProject\StudyProjects\DjangoProjects`项目管理文件中的`my_test`项目中实现。

> 本次体验最原始的方法做
>
> `Django`中提供`Form`和`ModelForm`组件实现 —— 很方便

1. 部门列表

页面效果：![image-20230509224433598](../../images/image-20230509224433598.png)

![image-20230510154713469](../../images/image-20230510154713469.png)

补充：

```python
# urls.py
urlpatterns = [
    # path("admin/", admin.sites.urls),
    path("depart/list/", views.depart_list),
    path("depart/add/", views.depart_add),
    path("depart/delete/", views.depart_delete),
    path("depart/<int:nid>/edit/", views.depart_edit),
]

# 其中最后一行path("depart/<int:nid>/edit/", views.depart_edit)的作用是，传值的时候，会把nid传进去，不用再费力进行传值。直接传# 给views.py

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# views.py
def depart_edit(request, nid: int, ):
    """
    编辑部门。

    Parameters
    ----------
    request

    Returns
    -------
    render object
    """
    # 根据nid，获取他的数据
    row_object = models.Department.objects.filter(id=nid).first()
    return render(request, 'depart_edit.html', {'rowobject': row_object})

# depart_edit.html
{% csrf_token %}
    <label style="margin-left: 4px;">标题</label>
    <input type="text" class="form-control" value="{{ rowobject.title }}" name="title">
{#					value属性：默认值 #}
```

#### 模板的继承

- 部门列表
- 添加部门
- 编辑部门

创建一个模板，让`HTML`继承这个模板

- 定义模板

```html
# layout.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	{# <title>瑾瑜-愿不枉啊，愿有往啊，这盛世每一天。</title> #}
    {% block title %} {% endblock %}
    
	<link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}">
	<link rel="stylesheet" href="{% static 'plugins/font-awesome/font-awesome-4.7.0/css/font-awesome.min.css' %}">
    {% block css %} {% endblock %}
	<style>
        .navbar {
		{#border-radius: 10px;#}
        }
        .container {
            width: 1200px;
		{#border: 1px solid #aaaaaa;#} box-shadow: 5px 5px 20px #aaa;
        }
        .container-fluid {
		{#width: 1200px;#} {#border: 1px solid #aaaaaa;#} {#box-shadow: 5px 5px 20px #aaa;#}
        }
        .new {
            margin-top: 0;
            margin-bottom: 0;
        }
        .my-button {
            display: inline-block;
            margin-left: 10px;
            margin-top: 10px;
        }
        .add-panel {
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .container-table {
            width: 1200px;
            border-radius: 6px;
		{#border: 1px solid #aaaaaa;#} margin: 20px auto;
            box-shadow: 5px 5px 20px #aaa;
        }
        td {
            text-align: center;
            width: 389px;
        }
        th {
            text-align: center;
            width: 389px;
        }
	</style>
</head>
<body>
    <h1>顶部</h1>
    <div>
        {% block content %} {% endblock %}
    </div>
	<h1>底部</h1>
<script src="{% static 'js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js' %}"></script>
<script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.min.js' %}"></script>
    {% block js %} {% endblock %}
</body>
</html>
```

- 继承

```html
{# 从layout里面继承 #}
{% extends 'layout.html' %}

{% block title %}
	<title>瑾瑜-愿不枉啊，愿勇往啊，这盛世每一天。</title>
{% endblock %}

{% block css %}
	<link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.min.css' %}">
    <style>...</style>
{% endblock %}

{% block content %}
	<h1>xxx</h1>
{% endblock %}

{% block js %}
	<script src="{% static 'js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js' %}"></script>
{% endblock %}
```

用户管理：

```python
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| id          | bigint        | NO   | PRI | NULL    | auto_increment |
| name        | varchar(16)   | NO   |     | NULL    |                |
| password    | varchar(64)   | NO   |     | NULL    |                |
| age         | int           | NO   |     | NULL    |                |
| account     | decimal(10,2) | NO   |     | NULL    |                |
| create_time | datetime(6)   | NO   |     | NULL    |                |
| gender      | smallint      | NO   |     | NULL    |                |
| depart_id   | bigint        | NO   | MUL | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
```

`insert into my_site_userinfo (name, password, age, account, create_time, gender, depart_id) values("卜伟仕", "123456", 19, 10000.50, "2023-10-10", 1, 1);`

`insert into my_site_userinfo (name, password, age, account, create_time, gender, depart_id) values("邓皓亮", "123999", 18, 10000.50, "2023-11-11", 1, 2);`

`insert into my_site_userinfo (name, password, age, account, create_time, gender, depart_id) values("李会峰", "666999", 21, 10000.50, "2023-05-05", 1, 5);`

`insert into my_site_userinfo (name, password, age, account, create_time, gender, depart_id) values("小卜", "123465789", 19, 100000.50, "2023-05-15", 1, 2);`

`insert into my_site_userinfo (name, password, age, account, create_time, gender, depart_id) values("小邓", "987654321", 15, 100000.50, "2023-12-12", 2, 2);`

#### 新建用户：

- 原始方式：不会采用（本质） —— 太复杂

```python
# 数据校验，工作量大，用户提交数据需要校验
# 用户输入后没有页面提示
# 页面上每一个字段都需要我们重新写一遍，很费劲
# 有关联的数据需要手动获取并且展示在页面上（通过传参的方式）

# # 总结来首，漏洞百出。
```

- `Django`组件
  - `form`组件 —— 小高级 + 代码 才能完全解决原始方式的问题
  - `ModelForm`组件 —— 最简便

#### 初识`form`组件

1. `views.py`

   ```python
   # views.py
   
   class MyForm(Form):
       user = forms.CharField(widget=forms.Input)
       pwd = form.CharField(widget=forms.Input)
       email = form.CharField(widget=forms.Input)
       
   def user_add(request):
       if request.method == 'GET':
           form = MyForm()  # 实例化一个对象，传到前端的页面上
           return render(request, 'user_add.html', {'form': form})
   ```

2. `user_add.html`

   ```html
   <!-- user_add.html -->
   <!-- 以下代码相当于下个代码块实现的功能 -->
   <form action="" method="post">
   	{% for field in form %}
       	{{ field }}
       {% endfor %}
   </form>
   ```

   ```html
   <!-- user_add.html -->
   <form action="" method="post">
   	{{ form.user }}
   	{{ form.pwd }}
   	{{ form.email }}
       <!-- 相当于以下代码：-->
       <!--
           <input type="text" class="form-control" placeholder="姓名" name="name">
           <input type="text" class="form-control" placeholder="密码" name="password">
           <input type="text" class="form-control" placeholder="邮箱" name="email">
   	-->
   </form>
   ```

3. `ModelForm`组件

   1. `models.py`

      ```python
      class UserInfo(models.Model):
          """
          员工管理相关数据库。
          """
          name = models.CharField(verbose_name="员工姓名", max_length=16)
          password = models.CharField(verbose_name="密码", max_length=64)
          age = models.IntegerField(verbose_name="年龄")
          account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
          create_time = models.DateTimeField(verbose_name="入职时间")
          # to：与哪张表关联 to_field: 与表中哪一个列关联
          # Django中自动做的 在底层生成数据库的列的时候 会自动生成数据列 depart_id
          depart = models.ForeignKey(to="Department", to_field="id", verbose_name="部门", on_delete=models.CASCADE)
          gender_choices = (
              (1, "男"),
              (2, "女"),
          )
          gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
      ```

   2. `views.py`

      ```python
      # views.py
      
      class MyForm(ModelForm):
          xx = form.CharField(...)
          class Meta:
              model = UserInfo
              fields = ["xx", "name", "password", "age", "account", "create_time", "depart", "gender"]
          user = forms.CharField(widget=forms.Input)
          pwd = form.CharField(widget=forms.Input)
          email = form.CharField(widget=forms.Input)
          
      def user_add(request):
          if request.method == 'GET':
              form = MyForm()  # 实例化一个对象，传到前端的页面上
              return render(request, 'user_add.html', {'form': form})
      ```

   3. `user_add.html`

      ```html
      <!-- user_add.html -->
      <!-- 以下代码相当于下个代码块实现的功能 -->
      <form action="" method="post">
      	{% for field in form %}
          	{{ field }}
          {% endfor %}
      </form>
      ```

      ```html
      <!-- user_add.html -->
      <form action="" method="post">
      	{{ form.user }}
      	{{ form.pwd }}
      	{{ form.email }}
          <!-- 相当于以下代码：-->
          <!--
              <input type="text" class="form-control" placeholder="姓名" name="name">
              <input type="text" class="form-control" placeholder="密码" name="password">
              <input type="text" class="form-control" placeholder="邮箱" name="email">
      	-->
      </form>
      ```

   `modelform`:

   ```python
   <form method="post" action="">
   	{% csrf_token %}
   	<!-- form.name.label 从关联的verbose_name里面取值 -->
   	{#	{{ form.name.label }}: {{ form.name }}#}
   	{#	{{ form.password.label }}: {{ form.password }}#}
   	{#	{{ form.age.label }}: {{ form.age }}#}
   	{% for field in form %}
   		{{ field.label }}: {{ field }}
   	{% endfor %}
   </form>
   ```

#### `ModelForm`

1. 首先，在`user_list.html`文档中：添加下列信息，点击可直达显示页面，测试`ModelForm`

   ```html
   <a href="/user/model/form/add/">
       <button type="button" class="btn btn-success">
           <i class="fa fa-plus-square-o" aria-hidden="true" style="margin-right: 3px;"></i>
           添加用户ModelForm
       </button>
   </a>
   ```

2. 在`urls.py`文件中，加入一个网址和视图函数的对应关系

   ```python
   urlpatterns = [
       path("user/model/form/add/", views.user_model_form_add),
   ]
   ```

3. 在`views.py`文件中，添加下面的一个类和一个函数

   ```python
   class UserModelForm(forms.ModelForm):
       class Meta:
           model = models.UserInfo
           fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
           exclude = []
           # 小组件， 为数据库中每个要在浏览器显示的字段设置样式，防止页面太丑，但是很繁琐。
           # widgets = {
           #     'name': forms.TextInput(attrs={'class': 'form-control'}),
           #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
           #     'age': forms.TextInput(attrs={'class': 'form-control'}),
           # }
   	
       # 为防止上面几行代码很繁琐，加入下面这些代码，用一个循环添加样式
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           # # 循环找到所有的插件 添加class样式
           for name, field in self.fields.items():
               # # 如果不想给某个数据库字段添加样式，那么用以下两行代码
               # if name == 'password':
               #     continue
               field.widget.attrs = {'class': 'form-control',
                                     'placeholder': field.label}
   # # 对应的函数        
   def user_model_form_add(request, ):
       """
       添加用户 —— 基于 ModelFormForm
   
       Parameters
       ----------
       request
   
       Returns
       -------
   
       """
       
       # 传入参数，在html文档中可以获取
       form = UserModelForm()
       return render(request, 'user_model_form_add.html', {'form': form})           
   ```

4. 在`user_model_form_add.html`

   ```html
   {% extends 'layout.html' %}
   
   {% block title %}
   	<title>瑾瑜-这世界有那么多人，人群里，敞着一扇门</title>
   {% endblock %}
   
   {% block content %}
   	<div class="container">
   		<div class="panel panel-default" style="margin-top: 10px;">
   			<div class="panel-heading">
   				<h3 class="panel-title">
   					添加用户
   				</h3>
   			</div>
   			<div class="panel-body">
   				<form action="" method="post" src="/user/list/">
   					{% for field in form %}
   						<div class="form-group">
   							{% csrf_token %}
   							<label style="margin-left: 4px;">{{ field.label }}</label>
   							{{ field }}
   							{#<input type="text" class="form-control" placeholder="姓名" name="name">#}
   						</div>
   					{% endfor %}
   					<button type="submit" class="btn btn-primary">提交</button>
   				</form>
   			</div>
   		</div>
   	</div>
   {% endblock %}
   ```

   注意下面这段代码：

   ```html
   {% for field in form %}
       <div class="form-group">
           {% csrf_token %}
           <!-- field可以直接显示出来 label是Django数据库创建文件models.py里面的参数verbose_name -->
           <label style="margin-left: 4px;">{{ field.label }}</label>
           {{ field }}
       </div>
   {% endfor %}
   ```

#### `Django`开发

-   部门管理

-   用户管理

    -   用户列表
    -   新建用户

    ```html
    ModelForm: 针对数据库中某个表
    Form： 不用数据库
    ```

##### 编辑用户

点击编辑，跳转到编辑页面，（将编辑的`ID`携带过去）

编辑页面：默认数据，根据`ID`获取并设置到页面中

提交时，做错误提示和数据校验，在数据库中更新。

案例：靓号管理

-   数据库表结构：

    | `ID` | `mobile`    | 级别（`choices`） | 状态（1 未占用 2 已占用） | 价格 |
    | ---- | ----------- | ----------------- | ------------------------- | ---- |
    | 1    | 12222222222 | 1                 | 2                         | 100  |

-   根据表结构的需求，创建`models`类，在`models.py`中创建类，由类生成数据库中的表。

    -   创建数据库

        ```sql
        >>> create database mobile_number_management default charset utf8 collate  utf8_general_ci;
        ```

    -   在models.py中：

        ```python
        # models.py
        
        from django.db import models
        class PrettyNumber(models.Model):
            """
            靓号管理
            """
        
            def __str__(self):
                pass
        
            state_choices = (
                (1, "已使用"),
                (2, "未使用"),
            )
            level_choices = (
                (1, "青铜"),
                (2, "白银"),
                (3, "黄金"),
                (4, "钻石"),
                (5, "星光"),
            )
            # CharField 必须设置长度
            # 允许为空： blank=True, null=True
            mobile = models.CharField(verbose_name="号码", max_length=20)
            prices = models.IntegerField(verbose_name="价格", default=0)
            level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=1)
            state = models.SmallIntegerField(verbose_name="状态", choices=state_choices, default=2)
        ```

    -   创建一些数据

        ```sql
        >>> insert into my_site_prettynumber (mobile, prices, level, state) values("12222222222", 99, 1, 2),("13333333333", 199, 1, 2);
        ```

        ```sql
        +----+-------------+--------+-------+-------+
        | id | mobile      | prices | level | state |
        +----+-------------+--------+-------+-------+
        |  1 | 12222222222 |     99 |     1 |     2 |
        |  2 | 13333333333 |    199 |     1 |     2 |
        |  3 | 12222222222 |     99 |     1 |     2 |
        |  4 | 13333333333 |    199 |     1 |     2 |
        |  5 | 12222222222 |     99 |     1 |     2 |
        |  6 | 13333333333 |    199 |     1 |     2 |
        |  7 | 12222222222 |     99 |     1 |     2 |
        |  8 | 13333333333 |    199 |     1 |     2 |
        |  9 | 12222222222 |     99 |     1 |     2 |
        | 10 | 13333333333 |    199 |     1 |     2 |
        | 11 | 12222222222 |     99 |     1 |     2 |
        | 12 | 13333333333 |    199 |     1 |     2 |
        +----+-------------+--------+-------+-------+
        ```

-   靓号列表（`url `函数{获取所有靓号 结合`html`和`render`将靓号罗列出来 `ID `号码 价格 级别 状态——都是中文}）

    ```python
    # urls.py
    from django.contrib import admin
    from django.urls import path
    from my_site import views
    
    urlpatterns = [
        # path("admin/", admin.sites.urls),
        ...
        path("pretty/number/list/", views.pretty_number_list),
    ]
    
    # # models.py
    # # 上面已写，不再重复
    
    # views.py
    def pretty_number_list(request):
        query_set = models.PrettyNumber.objects.all()
        return render(request, "pretty_number_list.html", {'queryset': query_set})
    ```

    ```html
    <!-- pretty_number_list.html -->
    
    <table class="table table-bordered table-hover table-striped">
        <thead>
            <tr>
                <th>ID</th>
                <th>电话号码</th>
                <th>靓号等级</th>
                <th>靓号状态</th>
                <th>靓号价格</th>
            </tr>
        </thead>
        <tbody>
            {% for item in queryset %}
            <tr>
                <th scope="row">{{ item.id }}</th>
                <td>{{ item.mobile }}</td>
                <td>{{ item.prices }}</td>
                <td>{{ item.get_level_display }}</td>
                <td>{{ item.get_state_display }}</td>
                <td>
                    <a href="#" class="btn btn-primary btn-xs">
                        <i class="fa fa-pencil" aria-hidden="true"></i>
                        编辑
                    </a>
                    <a href="#" class="btn btn-danger btn-xs">
                        <i class="fa fa-trash-o fa-lg"></i>
                        删除
                    </a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    ```

    靓号展示页面：

    ![image-20230512200138368](../../images/image-20230512200138368.png)

-   增 —— 新建靓号

    列表点击跳转：`/pretty/number/add/`

    `url`

    函数（`ModelForm`类 实例化类对象 通过`render`将对象传入到`HTML`中 通过模板的循环展示所有的字段）：

    ```python
    # views.py
    from django import forms
    
    class PrettyNumberModelForm(forms.ModelForm):
        mobile = forms.CharField(min_length=11, max_length=11, label="PhoneNumber")
    
        class Meta:
            model = models.PrettyNumber
            fields = ("mobile", "prices", "level", "state")
            # 或者写：fields = '__all__'
    
        def __init__(self, *args, **kwargs):
            super().__init__(* args, ** kwargs)
            for name, field in self.fields.items():
                field.widget.attrs = {
                    'class': 'form-control',
                    'placeholder': field.label,
                }
                
    def pretty_number_add(request, ):
        """
        添加靓号
    
        Parameters
        ----------
        request
    
        Returns
        -------
        """
        if request.method == "GET":
            form = PrettyNumberModelForm()
            return render(request, 'pretty_number_add.html', {'form': form})
        form = PrettyNumberModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pretty/number/list/')
        return render(request, 'pretty_number_add.html', {'form': form})
    ```

-   改

    添加手机号时，不能重复：

    ```python
    # views.py
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
            # if len(txt_mobile) != 11:
            #     raise ValidationError('格式错误')
            return txt_mobile
    ```

    编辑手机号时（如果可以编辑），不可以使用和添加手机号相同的校验重复值的方法——因为数据库已经存在了，如果手机号不修改，则不可以提交！——排除自己以外，看其他的手机号是否重复。

    ```python
    # views.py
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 当前编辑那一行的ID
        edit_id = self.instance.pk
        if models.PrettyNumber.objects.exclude(id=edit_id).filter(mobile=txt_mobile).exists():
            raise ValidationError("手机号已存在")
            # if len(txt_mobile) != 11:
            #     raise ValidationError('格式错误')
            return txt_mobile
    ```

    

-   删 较为简单，此处省略

-   查 —— 查询手机号

    ```python
    models.PrettyNumber.objects.filter(mbile='12222222222', id=12)
    
    data_list = {'mobile': '12222222222', 'id': 123}
    models.PrettyNumber.objects.filter(**data_list)
    ```

    ```python
    models.PrettyNumber.objects.filter(id=12)
    models.PrettyNumber.objects.filter(id_gt=12)    # 大于12
    models.PrettyNumber.objects.filter(id_gte=12)   # 大于等于12
    
    models.PrettyNumber.objects.filter(id_lt=12)    # 小于12
    models.PrettyNumber.objects.filter(id_lte=12)   # 小于等于12
    ```

    ```python
    models.PrettyNumber.objects.filter(mbile__startwith='1222', id=12)  # 以 ... 开头models.PrettyNumber.objects.filter(mbile__endswith='2222', id=12)   # 以 ... 结尾models.PrettyNumber.objects.filter(mbile__contains='2222', id=12)   # 包含 ...
    ```


-    分页

    ```pythpn
    # 第一页
    query_set = models.PrettyNumber.objects.all()[0:10]
    # 第二页
    query_set = models.PrettyNumber.objects.all()[10:20]
    
    query_set = models.PrettyNumber.objects.filter(id=1)[0:10]
    ```

    分页组件的实现：

    ```python
    # 导入分页类：
    # views.py
    from xxx import Pagination
    
    # 编写相应的视图函数：
    # 获取数据库数据列表 —— 以部门列表为例
    def depart_list(request, ):
        query_set = models.Department.objects.all()
        # 分页：
        page_object = Pagination(request, query_set)  # 默认十行数据一页，可修改参数，详细参数参考Pagination类
        context = {
            "queryset": page_object.page_query_set,
            "page_string": page_object.html(),
        }
        return render(request, 'depart_list.html', context)
    
    # 在展示列表中，加入下面这写数据，可实现分页：
    # 展示数据的HTML页面 —— 以depart_list.html为例
    <ul class="pagination clearfix">
        {{ page_string }}
    </ul>
    ```
    
    最终效果：
    
    ![image-20230515221008398](../../images/image-20230515221008398.png)
    
    完善 —— 时间插件
    
    ```html
    <link rel="stylesheet" href="./static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="./static/plugins/font-awesome/font-awesome-4.7.0/css/font-awesome.css">
    <link rel="stylesheet" href="./static/plugins/bootstrap-datepicker-1.6.4-dist/css/bootstrap-datepicker.min.css">
    
    <script src="./static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
    <script src="./static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
    <script src="./static/plugins/bootstrap-datepicker-1.6.4-dist/js/bootstrap-datepicker.min.js"></script>
    <script src="./static/plugins/bootstrap-datepicker-1.6.4-dist/locales/bootstrap-datepicker.zh-CN.min.js"></script>
    
    <script type="text/javascript">
    	$(function () {
    		$("#datetime").datepicker({
    			format : "yyyy-mm-dd",
    			startDate: "0",
    			language: "zh-CN",
    			autoclose: true,
    			clearBtn: true,
    			todayHighlight: true
    		})
    	})
    </script>
    ```
    
    `ModelForm`和`BootStrap`：
    
    `ModelForm`可以帮我们生成`HTML`标签
    
    ```python
    class UserModelForm(forms.ModelForm):
        name = forms.CharField(min_length=3, label="用户名")
        # password = forms.CharField(min_length=3, label="密码")
        class Meta:
            model = models.UserInfo
            fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
            exclude = []
                    
    form = UserModelForm(data=request.POST)
    ```
    
    ```html
    {{ form.name }}
    {{ form.password }}
    ```
    
    定义插件：
    
    ```python
    class UserModelForm(forms.ModelForm):
        name = forms.CharField(min_length=3, label="用户名")
        # password = forms.CharField(min_length=3, label="密码")
        class Meta:
            model = models.UserInfo
            fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
            exclude = []
            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                'age': forms.TextInput(attrs={'class': 'form-control'}),
            }
            
    # 或者：
    class UserModelForm(forms.ModelForm):
        name = forms.CharField(min_length=3, label="用户名", widgets=forms.TextInput(attr={'class': 'form-control'}))
        class Meta:
            model = models.UserInfo
            fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
    ```
    
    上述步骤过于繁琐：——可以重新定义初始化方法：
    
    ```python
    class UserModelForm(forms.ModelForm):
        name = forms.CharField(min_length=3, label="用户名")
    
        # password = forms.CharField(min_length=3, label="密码")
    
        class Meta:
            model = models.UserInfo
            fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]
            exclude = []
            # widgets = {
            #     'name': forms.TextInput(attrs={'class': 'form-control'}),
            #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            #     'age': forms.TextInput(attrs={'class': 'form-control'}),
            # }
    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
            # 循环找到所有的插件 添加样式
            for name, field in self.fields.items():
                # if name == 'password':
                #     continue
                if name == 'create_time':
                    field.widget.attrs = {'class': 'form-control',
                                          'placeholder': field.label,
                                          'autocomplete': 'off',
                                          }
                else:
                    field.widget.attrs = {'class': 'form-control',
                                          'placeholder': field.label}
    ```
    
    上述代码需要优化，因为我们要判断以前是不是没有属性，如果没有，可以再加入样式。如果有，保留原来的属性。
    
    自定义类：
    
    ```python
    class BootStrapModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # 循环找到所有的插件 添加样式
            for name, field in self.fields.items():
                # if name == 'password':
                #     continue
                if name == 'create_time':
                    field.widget.attrs = {'class': 'form-control',
                                          'placeholder': field.label,
                                          'autocomplete': 'off',
                                          }
                else:
                    field.widget.attrs = {'class': 'form-control',
                                          'placeholder': field.label}
    ```
    
    以后我们可以直接继承这个自定义的`BootStrapModelForm`类
    
    ```python
    class UserModelForm(BootStrapModelForm):
        ...
    ```
    
    提取公共的`BootStrap`类，拆分`views.py`
    
    ★★★ 注意：在拆分`views.py`的过程中，拆完后需要将`views.py`删除★★★
    
    ★★★ 注意：可以拆`views.py`中定义的类，但是`models.py`一般不能拆！！！★★★
    
    ![image-20230518211722552](../../images/image-20230518211722552.png)

管理员登录：

```python
# TODO: day18-1 1:40:00
```







































##  `MySQL`

##  数据库

### 直观

-   静态，写死了，页面永远一个样子
-   动态页面，页面上的数据可以实时更新、修改、展示。需要用到web框架的功能

### 初识网站

```python
# app.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    # 找到index.html的文件，读取所有的内容
    # flask会找到index.html中的特殊占位符，将数据替换
    # 将替换完成的字符串返回给用户浏览器

    # 目前写死的
    # 但是以后可以增加和删除
    users = ['buweishi', 'shuaige', 'meinv', 'goodfriends', 'niuma']
    return render_template('index.html', title='示例表格', data_list=users)

if __name__ == "__main__":
    app.run()
```

```html
<!-- /templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>index</title>
	<link rel="stylesheet" href="../static/plugins/bootstrap-3.4.1/css/bootstrap.css">
</head>
<body>
<!--<h1>用户列表</h1>-->
<nav class="navbar navbar-default">
	<div class="container-fluid">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			
			<a class="navbar-brand" href="#">
				<img alt="Brand" style="width: 20px; height: 20px;" src="../static/images/下载.png">
				<!--				Brand-->
			</a>
		</div>
		
		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
				<li><a href="#">Link</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">Dropdown <span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">Action</a></li>
						<li><a href="#">Another action</a></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">Separated link</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">One more separated link</a></li>
					</ul>
				</li>
			</ul>
			<form class="navbar-form navbar-left">
				<div class="form-group">
					<input type="text" class="form-control" placeholder="Search">
				</div>
				<button type="submit" class="btn btn-default">Submit</button>
			</form>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="#">Link</a></li>
				<li class="dropdown">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
					   aria-expanded="false">Dropdown <span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="#">Action</a></li>
						<li><a href="#">Another action</a></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a href="#">Separated link</a></li>
					</ul>
				</li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</nav>

<div class="container">
	<h3>{{title}}</h3>
	<table class="table table-hover table-bordered">
		<thead>
		<tr>
			<th>#</th>
			<th>First Name</th>
			<th>Last Name</th>
			<th>Username</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<th scope="row">1</th>
			<td>Mark</td>
			<td>Otto</td>
			<td>@mdo</td>
		</tr>
		{% for item in data_list %}
            <tr>
                <th scope="row">3</th>
                <td>{{item}}</td>
                <td>the Bird</td>
                <td>@twitter</td>
            </tr>
		{% endfor %}
		</tbody>
	</table>
</div>
<script src="../static/js/jquery-3.5.1/jquery-3.5.1/jquery-3.5.1.min.js"></script>
<script src="../static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
<script type="text/javascript">
</script>
</body>
</html>

```

上面所实现的效果：![image-20230503211111051](../../images/image-20230503211111051.png)

目前所知的存储文件方式：

-   `txt`文件
-   `Excel`文件

上述两个非常繁琐且性能不高

做存储数据的专业软件：数据库管理系统

-   `mysql `
-   `oracle`
-   `sqlserver`
-   `DB2`
-   `Access`

### `mysql`数据库

启动`mysql`：

-   临时启动，运行了`mysqld.exe` 如果在`cmd`运行了这个命令，则代表`mysql`已经启动了，知道这个`cmd`黑窗口被关闭，`mysql`会被关闭

制作服务： 执行命令
```txt
>>> mysqld.exe --install mysql
```

其中`mysqld.exe`代表制作`mysql`服务

连接测试：

mysql.exe

```txt
>>> "D:\SoftwareInstall\mysql\mysql-8.0.30-winx64\bin\mysql.exe" -h 127.0.0.1 -P 3306 -u root -p
```

设置密码：`set password = password("**************");`

查看已有的数据库（文件夹）

```sql
show databases;
```

忘记密码：

-   关闭`mysql`服务
-   修改配置，重新启动`mysql `—— 无账号模式
-   mysql -u root -p
-   重设密码
-   退出
-   再重新修改`mysql`配置文件，重新启动`mysql`
-   `mysql -u root -p` 并输入新密码

### 数据库管理（文件夹）

1.   查看已有的数据库（文件夹）
     ```sql
     show databases;
     ```

2.   创建数据库（文件夹）

     ```sql
     create database 数据库名字 default charset utf8 collate  utf8_general_ci;
     create database Test default charset utf8 collate  utf8_general_ci;
     ```

3.   删除数据库

     ```sql
     drop database 数据库名字;
     drop database Test;
     ```

4.   获取以前的命令： 按键盘上的上箭头

5.   进入文件夹：

     ```sql
     use 数据库名字;
     use mydatabase;
     ```

6.   查看数据库下的所有数据表：

     ```sql
     show 数据表名;
     show tables;
     ```

7.   创建表（文件）
     ```sql
     create table 表名称 (
         列名称 类型,
         列名称 类型,
         列名称 类型
     ) default charset=utf8;
     ```
     
     ```sql
     create table message (uid int, uname varchar(16),uage int) default charset=utf8;
     ```
     
     写直观一点：
     
     ```sql
     create table message (
         uid int, 
         uname varchar(16),
         uage int
     ) default charset=utf8;
     ```
     
     ```sql
     create table message (
         uid int not null, -- 不允许为空 
         uname varchar(16),
         uage int null，   -- 允许为空
     ) default charset=utf8;
     ```
     
     ```sql
     create table message (
         uid int, 
         uname varchar(16),
         uage int default 3;  -- 插入数据时，如果没有传值，默认为3
     ) default charset=utf8;
     ```
     
     ```sql
     create table message (
         uid int primary key,   -- 主键，不能为空，并且不能重复 一般和自增同时设置。
         uname varchar(16),
         uage int
     ) default charset=utf8;
     ```
     
     主键一般用于表示行的编号，相当于身份证号码
     
     ```sql
     create table message (
         uid int auto _increment primary key, -- 内部维护自增
         uname varchar(16),
         uage int
     ) default charset=utf8;
     ```
     
     一般情况下，创建表的时候这么写。【标准】
     
     ```sql
     create table mytable_1 (
         uid int not null auto_increment primary key,
         uname varchar(16),
         uage int
     ) default charset=utf8;
     ```
     
8.   删除表：
     ```sql
     drop table 表名称；
     ```

9.   展示表的详细信息
     ```sql 
     desc 表名称;
     desc mytable_1;
     ```

     ![image-20230504211210354](D:\MDFiles\images\image-20230504211210354.png)

### 数据库表中的数据类型

#### 整型

1.   `tinyint`

     ```sql 
     有符号，取值范围 -128 ~ 127  有正有负 【默认】
     无符号 取值范围    0  ~ 255  有正无负 
     ```

     ```sql
     create table mytable_2 (
         uid int not null auto_increment primary key,
         uname varchar(16),
         uage tinyint   -- 有符号
     ) default charset=utf8;
     ```

     ```sql
     create table mytable_3 (
         uid int not null auto_increment primary key,
         uname varchar(16),
         uage tinyint unsigned   -- 无符号
     ) default charset=utf8;
     ```

2.   `int`
     
     ```
     有符号 ...
     无符号 ...
     ```
     
3.   `bigint`（有符号 无符号）

练习

```sql
# 创建数据
create table mytable_2 (
    uid bigint not null auto_increment primary key,
    salary int,
    uage tinyint
) default charset=utf8;

# 插入数据
insert into mytable_2 (salary, uage)  values(10000, 18);
insert into mytable_2 (salary, uage)  values(20000, 20);
insert into mytable_2 (salary, uage)  values(10000, 18),(40000, 30), (50000, 40);

# 查看表中的数据
select * from mytable_2;
```

![image-20230504212750700](D:\MDFiles\images\image-20230504212750700.png)

#### 小数

1.   `float `    不精准
2.   `double`    不精准
3.   `decimal`   精准

```sql
# 准确的小数值，m是数字总个数（负号不算） d时小数点后面的位数 m的最大值是65 d的最大值是30
# 注意：表中添加decimal的时候，注意整数部分加上小数部分的位数的值不能超过m，否则插入报错
create table mytable_3 (
    id bigint not null auto_increment primary key,
    salary decimal(8, 2)
) default charset=utf8;

insert into mytable_3(salary) values(1.28), (2.2658), (5.289), (5.282);
```

![image-20230504213751723](D:\MDFiles\images\image-20230504213751723.png)

#### 字符串

1.   `char(m)` 定长字符串,固定用11个字符存储，哪怕真实没有11个字符，也会存11个字符。 超过长度会报错 —— 只可少，不可多 
     -- 查询速度快 `m`最大可容纳255个字符

     ```sql
     create table mytable_4 (
         id bigint not null auto_increment primary key,
         mobile char(11)
     ) default charset=utf8;
     
     insert into mytable_4 (mobile) values("151"), ("18415584096");
     ```

2.   `varchar(m)` 变长字符串 真实数据有多长 就存多长，节省空间
     -- `m`代表字符长度 看编码而定 最大65535个字节 `65535/3 = 存储的汉字个数`（一个汉字三个字节）

     ```sql
     create table mytable_4 (
         id bigint not null auto_increment primary key,
         mobile varchar(11)
     ) default charset=utf8;
     
     insert into mytable_4 (mobile) values("151"), ("18415584096");
     ```

3.   `text` 可容纳 `65535`个字符 新闻 文章会用这个存储

4.   `mediumtext` `2 \** 24`个字符 `16,777,215`

5.   `longtext` `4GB` `2 \** 32 - 1`

#### 时间 

1.   `datetime`
     
     ```sql
     YYYY-MM-DD HH:MM:SS (1000-01-01 00:00:00/9999-12-31 23:59:59)
     ```
     
2.   `date `
     
     ```sql
     YYYY-MM-DD (1000-01-01/9999-12-31)
     ```

创建一个用户表

```sql
create table mytable_5 (
    id bigint not null auto_increment primary key,
    name varchar(10) not null,
    password char(18) not null,
    email varchar(30) not null,
    age tinyint,
    salary decimal(10, 2),
    create_time datetime
) default charset=utf8;

insert into mytable_5(name, password, email, age, salary, create_time) values("yang", "yang123456", "12345@qq.com", 20, 100000.50, "2023-05-04 22:03:00");
insert into mytable_5(name, password, email, age, salary, create_time) values("li", "li1234561", "12356@qq.com", 19, 10000.50, "2023-05-04 22:05:00");
insert into mytable_5(name, password, email, age, salary, create_time) values("huang", "huang123456", "12367@qq.com", 19, 100000.50, "2023-05-04 22:01:00");
insert into mytable_5(name, password, email, age, salary, create_time) values("deng", "deng123456", "12378@qq.com", 19, 100000.50, "2023-05-04 22:00:00");
insert into mytable_5(name, password, email, age, salary, create_time) values("zhou", "zhou123456", "12389@qq.com", 19, 100000.50, "2023-05-04 22:10:00");
insert into mytable_5(name, password, email, age, salary, create_time) values("lin", "lin123456", "12390@qq.com", 19, 100000.50, "2023-05-04 22:20:00");
```

还有很多其他的数据类型，官网上全都有。https://dev.mysql.com/doc/refman/5.7/en/data-types.html

### 数据行操作

#### 增

```sql
insert into 表名(列名) values(每一列的值-一一对应);
insert into 表名(列名) values(每一列的值-一一对应), (每一列的值-一一对应), (每一列的值-一一对应);
insert into mytable_5(name, password, email, age, salary, create_time) values("buweishi", "123456", "123@qq.com", 18, 10000.50, "2023-05-04 22:00:00");
```

#### 删

```sql
delete form 表名;
delete from 表名 where 条件;
```

```sql
delete form mytable_1;
delete from mytable_5 where id = 1 and name = "buweishi";
delete from mytable_5 where id = 1 or name = "buweishi";
delete from mytable_5 where id = in (1, 5);
```

#### 改

```sql
update 表名称 set 列 = 值;
update 表名称 set 列 = 值, 列 = 值, 列 = 值;
update 表名称 set 列 = 值, 列 = 值, 列 = 值 where 条件;

update mytable_5 set password = "哈哈666", name = "小明", email = "12345679@qq.com" where id = 2;
```

<img src="D:\MDFiles\images\image-20230504222153099.png" alt="image-20230504222153099" style="zoom:50%;" />

```sql
update mytable_5 set password = "哈哈666", name = "小明", age = age + 10 where id = 2;
```

#### 查

```sql
select * from 表名称;
select 列名称,列名称 from 表名称;
select 列名称,列名称 from 表名称 where 条件;

select name from mytable_5 where id=1;
```

一般在项目开发时： 

-   创建数据库
-   创建表结构

都是提前通过工具 + 命令创建

但是，表中的数据一般情况下都是通过程序来实现，比如增删改查。

### 员工管理案例：

-   使用内置命令

    -   创建数据库 `unicome ` `create database unicome default charset utf8 collate  utf8_general_ci;`

    -   创建数据表 `admin`

    -   表里面创建一些列

        ```sql
        表名：admin
        列：
        	id 整型
        	username 字符串 不允许为空
        	password 字符串 不允许为空
        	mobile 字符串 不为空
        ```

    -   用`Python`代码实现：

        -   添加用户
        -   删除用户
        -   查看用户
        -   更新用户


#### 创建表结构

```sql
create database unicome default charset utf8 collate  utf8_general_ci;
```

```sql
create table admin (
    id int not null auto_increment primary key,
    username char(20),
    password char(18),
    mobile char(11)
) default charset = utf8;
```

#### `Python`操作`mysql`

#####  插入数据

```python
import pymysql
# 链接mysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='WarmDou_TS20866',
    charset='utf8',
    db='unicome'
)
# 收发指令
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 发送指令
cursor.execute('insert into admin (username, password, mobile) values ("xxx", "xxxxxx", "15555555555")')
conn.commit()  # 这个是必须的！！！
# 关闭cursor和连接
cursor.close()
conn.close()
```

```sql
import pymysql
# 链接mysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='WarmDou_TS20866',
    charset='utf8',
    db='unicome'
)
# 收发指令
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# !!!!! 发送指令 千万不要用字符串格式化 — format 去做SQL的拼接，因为容易被SQL注入。 !!!!!!
# 应该用pymysql内部提供的execute去做
# sql = 'insert into admin (username, password, mobile) values ("xxxx", "xxxxxxx", "18888888888")'
# cursor.execute(sql)

# # 下面是两种正确的做法
# # 下面是pymysql内部的sql语句格式
# another_sql = 'insert into admin (username, password, mobile) values (%s, %s, %s)'
# cursor.execute(another_sql, ("hhh", "123456", "16666666666"))
the_sql = 'insert into admin (username, password, mobile) values (%(n1)s, %(n2)s, %(n3)s)'
cursor.execute(the_sql, {"n1": "哈哈哈", "n2": "123456789", "n3": "11111111111"})
conn.commit()  # ! ! ! 这个是必须的 ! ! !
# 关闭cursor和链接
cursor.close()
conn.close()
```

##### 查询数据

```python
# 获取符合条件的所有数据 fetchall() 列表套字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from admin where id > %s'
cursor.execute(sql, (6, ))
data_list = cursor.fetchall()
for item in data_list:
    print(item)
cursor.close()
conn.close()
```

```python
# 获取符合条件的第一条数据 fetchone() 字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from admin where id > %s'
cursor.execute(sql, (6, ))
# data_list = cursor.fetchone()
# # for item in data_list:
# #     print(item)
data = cursor.fetchone()
print(data)

cursor.close()
conn.close()
```

##### 删除数据

```python
import pymysql
# 链接mysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='WarmDou_TS20866',
    charset='utf8',
    db='unicome'
)
# 收发指令
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'delete from admin where id = %s'
cursor.execute(sql, (10, ))
conn.commit()
cursor.close()
conn.close()
```

##### 修改数据

```python
import pymysql
# 链接mysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='WarmDou_TS20866',
    charset='utf8',
    db='unicome'
)
# 收发指令
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = '''update admin 
    set mobile = %s 
    where id = %s'''
cursor.execute(sql, ("修改手机号", 4, ))
conn.commit()
cursor.close()
conn.close()
```

**小提示：在我们进行 增删改的时候，需要`conn.commit()` 否则修改不会生效。**

在查询时候不需要`commit` ，但是需要执行`fetchone`或者`fetchall`

**对于`SQL`语句，切记不要用`Python`的格式化语句（format）进行拼接，会被SQL注入，一定要使用`sql = "%s"execute(sql, (传入的参数))`**

### 案例：`flask + mysql`

1.   新增用户
     ```python
     # app.py
     
     from flask import Flask, render_template, request
     import pymysql
     app = Flask(__name__)
     @app.route('/add/user', methods=['POST', 'GET'])
     def add_user():
         if request.method == 'GET':
             return render_template('add_user.html')
         username = request.form.get('user')
         password = request.form.get('pwd')
         phone_number = request.form.get('mobile')
     
         # 链接数据库
         conn = pymysql.connect(
             host='127.0.0.1',
             port=3306,
             user='root',
             password='WarmDou_TS20866',
             charset='utf8',
             db='unicome'
         )
         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
         # 执行sql
         try:
             sql = "insert into admin(username, password, mobile) values(%s, %s, %s)"
             cursor.execute(sql, (username, password, phone_number))
             conn.commit()
         except Exception as e:
             print(e)
         # 关闭链接
         cursor.close()
         conn.close()
         return '添加成功'
     if __name__ == '__main__':
         app.run()
     ```

     ```sql
     <h1>添加用户</h1>
     <form method="post" action="/add/user">
     	<label>
     		<input type="text" name="user" placeholder="用户名">
     	</label>
     	<label>
     		<input type="text" name="pwd" placeholder="密码">
     	</label>
     	<label>
     		<input type="text" name="mobile" placeholder="手机号码">
     	</label>
     	<label>
     		<input type="submit" value="提交" >
     	</label>
     ```





