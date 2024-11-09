[TOC]



# `Python`基础-`day1`

`Python`入门、系统性地学习`Python+HTML+Django`

## 1. 文档工具

`typora`

## 2. 环境搭建

1.   安装`Python`解释器

2.   学习`Python`语法
3.   `Python`解释器以及文件结构、文件功能

```
D:\PythonCompiler\python310
	- python.exe           Python解释器
	- Scripts              
		- pip.exe         帮助我们安装第三方包
	- Lib                  Python内置的源代码
		- 文件、文件夹    Python提供的内置功能
		- site-packages   通过pip安装的第三方包存放的地方
```

## 3. `Python`解释器

使用`Python`解释器，需要在终端操作

-   交互式
-   文件的形式

```
1. 假设在 F:\code.py 创建了一个文件
2. 在文件中写了一些代码
3. 运行代码：
	C:\python.exe F:\code.py
```

## 4. 环境变量

配置环境变量，减轻工作量

## 5. `Python`基础语法

### 5.1 编码

-   计算机 以二进制存储数据

```python
哈哈yyds666   ->    01010100 01101010 10100010
```

-   在计算机中不只有一套编码，有多套编码 比如`UTF-8`
-   文件一定要记住保存时是什么编码，打开时使用同样的编码
-   在`Python`开发过程中这种规则也要遵循
-   `Python3.x`版本会默认使用`UTF-8`编码去打开文件——以`UTF-8`编码保存文件

### 5.2 输出

让程序在内部帮我们做事，做完事之后将结果展示出来。

```python
# 展示出一个目录下面的所有文件

import os
for item in os.listdir("这里是路径名称"):
    print(item, end="|")

```

```python
# 找出所有以png为后缀的文件

import os
for item in os.listdir("这里是路径名称"):
    if item.endswith('png'):
        print(item)
```

### 5.3 数据类型

什么是数据类型？

-   字母 数字 汉字 成语 文言文
-   文本 数字 真假等等

#### 5.3.1 整型（数字） `int`

表示我们生活中的数字 19 18 520

所有整型数据都可以加减乘除

```
print(19)
```

#### 5.3.2 字符串 `str`

表示生活中的文本信息：

单行文本：
- "计算机科学与技术"
- '计算机'

多行文本：
- """计算机"""
- '''计算机'''

文本（字符串）可以进行相加 —— 拼接
字符串和数字相乘：让字符串重复多少次

#### 5.3.3 布尔类型

真/假
`True/False`

```python
print(int(True))
print(int(False))
print(bool(0))
print(bool(1))
print(bool(2))
print(bool(-10))
print(bool('计算机'))
print(bool('0'))
print(bool('1'))
print(bool(''))

# 运行结果：
# 1
# 0
# False
# True
# True
# True
# True
# True
# True
# False
```

#### 5.3.3 布尔类型

变量：给某个值取个名称

```
result = 1 == 2
print(result)
# False
```

### 5.4 变量

```
变量名规范：
1. 只能包含数字字母下划线
2. 不能以数字开头
3. 不能使用Python内置的关键字
```

#### 5.4.1 变量的内存指向

```
name = 'xxx'
a_name = 'xxx'
print(id(name))
print(id(a_name))

# 运行结果：
2405992754352
2405992754352


number = 18
print(id(number))
number = str(number)
print(id(number))
# 运行结果：
2252794888976
2252796521648
```

### 5.5 注释

单行注释

多行注释

文档字符串

### 5.6 输入

```python
str_input = input("这里面写提示信息")  # 输入的信息是字符串类型
print(str_input)
```

### 5.7 条件语句

```python
if 条件/真假:
    条件成立后执行这段代码
else:
    条件不成立后执行这段代码
```

```c
if (条件) {
	条件成立执行这条指令
} else {
	条件不成立执行这条指令
}
```



















































































