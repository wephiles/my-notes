<h1 style="font-size: 40px; text-align: center;">如何写优雅的Python代码</h1>



# 引论

## 建议一：理解pythonic概念

```python
import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

```text
《Python之禅》，作者:蒂姆·彼得斯

美总比丑好。
显式优于隐式。
简单总比复杂好。
复杂总比复杂好。
平的比嵌套的好。
稀疏比密集好。
可读性。
特殊情况没有特殊到违反规则的程度。
尽管实用胜过纯粹。
错误不应该无声地传递。
除非被明确噤声。
面对模棱两可，拒绝猜测的诱惑。
应该有一种——最好只有一种——明显的方法来做到这一点。
虽然这种方法一开始可能并不明显，除非你是荷兰人。
现在总比不做好。
虽然永远不要比现在更好。
如果实现很难解释，那就是一个坏主意。
如果实现很容易解释，这可能是个好主意。
名称空间是一个很棒的想法——让我们做更多这样的事情吧!
```

(1) pythonic也许可以理解为：充分体现Python自身特色的代码风格。

举例子：

1.   在Python中利用Python的packaging/unpackaging机制，pythonic的代码实现交换两个变量的值只需要一行代码：

```python
a, b = b, a
```

2.   在遍历容器的时候，Python这样写：

```python
for i in a_list:
    do_sth_with(i)
```

3.   安全地关闭文件：

```python
with open(path, 'r') as f:
    do_sth_with(f)
```

通过上述例子，可以看出，Pythonic的一个要求是：对Python语法的充分发挥。

(2) 但是，对Python语法的充分使用，不应当过分使用奇技淫巧：

比如：利用Python的slice语法：

```python
a = [1, 2, 3, 4]
b = 'abcdef'
print(a[::-1])
print(b[::-1])
```

实际上，下面代码可以充分体现Pythonic语法：

```python
print(list(reversed(a)))
print(list(reversed(b)))
```

(3) 标准库

比如：

1.   字符串格式化

```python
print("Hello %s!" % ("Tom", ))
```

但是上面语句如果`%s`太多的话，很难阅读。

在参数较多的情况下：

```python
print('Hello %(name)s' % {'name': 'Tom'})
```

还有一种格式化的方式：str.format

```python
print('{greet} from {language}.'.format(greet='Hello world', language='Python'))
```

(4) Pythonic的库或者框架

编写的程序需要团队合作，编写适合使用的接口

业内通常认为Flask框架是比较符合Pythonic的：

```python
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()
```

框架可以减少重复造轮子。

现在的库或者框架跟随以下潮流：

-   包和模块的命名采用小写、单数形式，而且短小
-   包通常作为命名空间，如只包含空的`__init__.py`文件

## 建议二：编写Pythonic代码

1. 避免劣化代码

   - 避免只用大小写区分不同的对象
   - 避免使用容易混淆的名称
   - 不要害怕过长的变量名

2. 深入认识Python

   - ![image-20230509225211769](../../images/image-20230509225211769.png)

   - ![image-20230509225257405](../../images/image-20230509225257405.png)

   - ![image-20230509225330507](../../images/image-20230509225330507.png)

   - ![image-20230509225426065](../../images/image-20230509225426065.png)
     ```python
     pip install pep8
     ```

   - ![image-20230509225530300](../../images/image-20230509225530300.png)

## 建议三：理解Python与C语言的不同之处

1. 缩进与{}
2. 单引号与双引号
3. 三元操作符 ？:
4. switch … else
   ![image-20230509225949971](../../images/image-20230509225949971.png)

## 建议四：在代码中适当添加注释

 ![image-20230510222738239](../../images/image-20230510222738239.png)

![image-20230510222819181](../../images/image-20230510222819181.png)

![image-20230510222843086](../../images/image-20230510222843086.png)

![image-20230510222917390](../../images/image-20230510222917390.png)

![image-20230510222959589](../../images/image-20230510222959589.png)

![image-20230510223207334](../../images/image-20230510223207334.png)

![image-20230510223250991](../../images/image-20230510223250991.png)

![image-20230510223321827](../../images/image-20230510223321827.png)

![image-20230510223413120](../../images/image-20230510223413120.png)

![image-20230511223530663](../../images/image-20230511223530663.png)

![image-20230511223603959](../../images/image-20230511223603959.png)

![image-20230511223732062](../../images/image-20230511223732062.png)

![image-20230512224415781](../../images/image-20230512224415781.png)

![image-20230512224539431](../../images/image-20230512224539431.png)

![image-20230512224641843](../../images/image-20230512224641843.png)

![image-20230512224707140](../../images/image-20230512224707140.png)

![image-20230512225048598](../../images/image-20230512225048598.png)

![image-20230512225106631](../../images/image-20230512225106631.png)

![image-20230512225259209](../../images/image-20230512225259209.png)

![image-20230512225349127](../../images/image-20230512225349127.png)

![image-20230512225411370](../../images/image-20230512225411370.png)

![image-20230512225425144](../../images/image-20230512225425144.png)

![image-20230512225525492](../../images/image-20230512225525492.png)

![image-20230512225556243](../../images/image-20230512225556243.png)

![image-20230512225615614](../../images/image-20230512225615614.png)

![image-20230512225733630](../../images/image-20230512225733630.png)

![image-20230512225821253](../../images/image-20230512225821253.png)

![image-20230512225909843](../../images/image-20230512225909843.png)

![image-20230512225938430](../../images/image-20230512225938430.png)

![image-20230514210807622](../../images/image-20230514210807622.png)

![image-20230514210932993](../../images/image-20230514210932993.png)

![image-20230514211043169](../../images/image-20230514211043169.png)

![image-20230514211116427](../../images/image-20230514211116427.png)

![image-20230514211137899](../../images/image-20230514211137899.png)

![image-20230514212524279](../../images/image-20230514212524279.png)

```python
['D:\\PycharmProject\\StudyProjects\\ImportPackage', 
 'D:\\PythonCompiler\\python310\\python310.zip', 
 'D:\\PythonCompiler\\python310\\DLLs', 
 'D:\\PythonCompiler\\python310\\lib', 
 'D:\\PythonCompiler\\python310', 
 'C:\\Users\\20866\\AppData\\Roaming\\Python\\Python310\\site-packages', 
 'D:\\PythonCompiler\\python310\\lib\\site-packages']
```

![image-20230514215428236](../../images/image-20230514215428236.png)

![image-20230514215448788](../../images/image-20230514215448788.png)

![image-20230514215505930](../../images/image-20230514215505930.png)

![image-20230514215548569](../../images/image-20230514215548569.png)

模块可以包含可执行的语句以及函数定义。这些语句用于初始化模块。它们仅在模块 *第一次* 在 import 语句中被导入时才执行。 [1](https://docs.python.org/zh-cn/3.6/tutorial/modules.html#id2) (当文件被当作脚本运行时，它们也会执行。)

每个模块都有它自己的私有符号表，该表用作模块中定义的所有函数的全局符号表。因此，模块的作者可以在模块内使用全局变量，而不必担心与用户的全局变量发生意外冲突。另一方面，如果你知道自己在做什么，则可以用跟访问模块内的函数的同样标记方法，去访问一个模块的全局变量，`modname.itemname`。

模块可以导入其它模块。习惯上但不要求把所有 [`import`](https://docs.python.org/zh-cn/3.6/reference/simple_stmts.html#import) 语句放在模块（或脚本）的开头。被导入的模块名存放在调入模块的全局符号表中。

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

还有一个变体甚至可以导入模块内定义的所有名称:

```
>>> from fibo import *
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

这会调入所有非以下划线（`_`）开头的名称。 在多数情况下，Python程序员都不会使用这个功能，因为它在解释器中引入了一组未知的名称，而它们很可能会覆盖一些你已经定义过的东西。注意通常情况下从一个模块或者包内调入 `*` 的做法是不太被接受的， 因为这通常会导致代码的可读性很差。不过，在交互式编译器中为了节省打字可以这么用。

请注意，当使用 `from package import item` 时，item可以是包的子模块（或子包），也可以是包中定义的其他名称，如函数，类或变量。 `import` 语句首先测试是否在包中定义了item；如果没有，它假定它是一个模块并尝试加载它。如果找不到它，则引发 [`ImportError`](https://docs.python.org/zh-cn/3.6/library/exceptions.html#ImportError) 异常。

相反，当使用 `import item.subitem.subsubitem` 这样的语法时，除了最后一项之外的每一项都必须是一个包；最后一项可以是模块或包，但不能是前一项中定义的类或函数或变量。

如果没有定义 `__all__`，`from sound.effects import *` 语句 *不会* 从包 `sound.effects` 中导入所有子模块到当前命名空间；它只确保导入了包 `sound.effects` （可能运行任何在 `__init__.py` 中的初始化代码），然后导入包中定义的任何名称。 这包括 `__init__.py` 定义的任何名称（以及显式加载的子模块）。它还包括由之前的 [`import`](https://docs.python.org/zh-cn/3.6/reference/simple_stmts.html#import) 语句显式加载的包的任何子模块。

当包被构造成子包时（与示例中的 `sound` 包一样），你可以使用绝对导入来引用兄弟包的子模块。例如，如果模块 `sound.filters.vocoder` 需要在 `sound.effects` 包中使用 `echo` 模块，它可以使用 `from sound.effects import echo` 。

```python
整理一套可行的工程规范。在实施时尽可能参照规范建立项目：
=======================================================
项目名
	| -> 包名称(同项目名)
			| -> __init__.py
			| -> 内部包1
				| -> __init__.py
				| -> A.py
				| -> B.py
			| -> 内部包2
				| -> __init__.py
				| -> C.py
            | -> 内部包3
                | -> __init__.py
                | -> D.py
	| -> 测试文件夹
			| -> test.py
	| -> 入口运行文件（main.py）
————————————————
版权声明：本文为CSDN博主「代码狙击者」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/nuaa_llf/article/details/91431555
```





























































