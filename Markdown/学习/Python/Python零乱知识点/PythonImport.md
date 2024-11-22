<h1 style="text-align: center; font-size: 70px;">Python import</h1>



# Python import -- 官方文档

## module

-   在Python中，module算一个组织单位，他自己独立构成一个命名空间；
-   他本身是一个Python object
-   在这个object里面 还可以有很多其他的Python object
-   实际应用中，一个module**常常**对应一个.py文件
-   module是一个Python运行的时候的概念，保存在内存中是Python级别的概念
-   而文件是一个操作系统级别的概念
-   ★★★**需要通过import这个过程，从一个文件中生成一个module**

## package

-   package是一种特殊的module
-   在Python中package和module几乎有着一模一样的功能
-   package只是比module多了一个`__path__`功能
-   在OS层级，package往往对应一个文件夹
-   package里面可以有其他的sunpackage，也可以有module
-   但是module在组织结构上是一种最末端的东西了
-   一个文件夹，只有有`__init__.py`文件才算是一个package —— 这种说法在Python3中是错误的
-    不管有没有`__init__.py`文件，Python都会将一个文件夹看成一个package

## import

### import module

当前目录下有两个文件：example.py和test.py文件

在example文件里面 `import test`:将test.py里面的内容变成一个module

当做`import test`这件事的时候，发生了如下的事情：

1.   拿到test这个字符串
2.   将test作为名字寻找这个module
     1.   首先检查缓存有没有叫test的module已经被读取，如果有，就不用下面的load的过程，直接把值赋值给test
     2.   如果没有，就要寻找叫test的module
          1.   首先看这个名字是不是built-in module
          2.   如果不是，就会在几个文件夹里面寻找可以被load乘test的文件 —— 最常见的是名字叫test.py的文件
          3.   会在哪些文件夹里面寻找呢？被保存到sys.path里面
          4.   sys.path打印出的第一个，一般是我们example文件所在的文件夹
          5.   同时在运行的过程中，会放一些Python自带的package
          6.   site-packages： pip install的位置
          7.   可以手动改这个sys.path
          8.   按照sys.path的顺序寻找
3.   寻找到符合条件的文件以后，就会在一个单独的命名空间里面运行这个文件 —— 建立一个module

比如

test.py: 新建一个module，在这个module里面定义一个class A  完成这个module object后，就会更新缓存，其他文件import这个文件的时候，不需要再load一次了

```python
class A:
    pass
```

example.py: 上述完成之后，就会把module object赋值给这个叫test的变量（就是这个import test里面的test）test就可以作为一个变量使用了，不管import多少次，只会import一次

```python
import test
```

![image-20230429101447902](\image-20230429101447902.png)

![image-20230429102016770](D:\MDFiles\images\image-20230429102016770.png)

`import test as t`

![image-20230429102228584](D:\MDFiles\images\image-20230429102228584.png)

如果只想要test module里面的object A:

`from test import A`:不会把module赋值给任何一个变量，而是在这个module里面找到名字为A的variable，把这个变量A里面保存的object赋值到当前这个module下的变量 A 。

![image-20230429102618565](D:\MDFiles\images\image-20230429102618565.png)

同样也可以这样写：`from test import A as MyA`:也就是把责任切开，import的依然是test里面的class A，但是class A在example.py里面，他的变量名就变成了MyA。

### import  package

import package和import module是非常非常相似的，唯一的小区别是：会查看这个package文件夹下有没有`__init__.py`文件，如果没有的话，不会运行任何额外的代码，如果有的话，就会运行这个\__init__文件。

mypackage/\__init__.py:

```python
print('mypackage is imported')
```

![image-20230429103544447](D:\MDFiles\images\image-20230429103544447.png)

我们在import 一个 package的时候，实际上是在一个单独的命名空间里面运行init文件，然后用这个命名空间来构成一个module，这个module是一个特殊的module，也就是package。

```python
print('mypackage is imported')


class B:
    pass
```

![image-20230429103856072](D:\MDFiles\images\image-20230429103856072.png)

★★ 注意 import package和import module的区别：1 当我们import一个package的时候，只会运行这个package下面的init文件，Python是不知道这个package下面还有一个mymodule module的。

![image-20230429104144971](D:\MDFiles\images\image-20230429104144971.png)

如果需要import一个package下的module，我们需要这么做：

`import mypackage.mymodule`

![image-20230429104413814](D:\MDFiles\images\image-20230429104413814.png)

但是这么做的时候，Python的后台会load这个mypackage并且更新缓存，其次，当import这个mymodule的时候，还会在mypackage里面增加一个属性mymodule。

![image-20230429104742897](D:\MDFiles\images\image-20230429104742897.png)

小总结：我们只import mypackage的时候，没办法打印出来mypackage.mymodule的，但是如果我们用`import mypackage.mymodule`的话就是可以的。如果我们打印其中的属性的话，也是可以看到，mypackage里面是有mymodule这个属性的。

★★ 注意 import package和import module的区别：2 当我们import mypackage.mymodule的时候，把这个东西赋值给哪一个变量？如果像我们现在这样——`import mypackage.mymodule`的时候，会把最外层的那一个package赋值给这个package名字的变量，也就是说，当import 完成之后，会出现一个全局变量mypackage，指向mypackage。但是当我们用`import mypackage.mymodule as m`的时候，就会把最末端的这个module赋值给as后面的变量上的。

![image-20230429105639815](D:\MDFiles\images\image-20230429105639815.png)

******

以上所有的import方式被称为absolute import。就是可以根据一个确定的string，寻找module并且load进来。

## relative import

我们有时候会在一个package里面的不同module之间相互引用。而这些module之间的相互关系是更容易被发现的，或者说更稳定的。比如说package可能会改名字，或者改变路径。都会导致module的绝对路径改变。

原理：每一个relative import，都是先找到他的绝对路径，然后再import，会通过这个module的package这个变量计算绝对路径。

form .utils import f 的时候，就会变成 from mypackage.util import f ，——将relative import 转换成absolute import，正因为如此如果直接运行脚本时会报错的。因为通过Python直接运行脚本的时候，这个文件会被当做main module load 进来，它并不属于任何一个package。于是relative就无法成功转换成absolute import。

换言之，relative import 只能在package里面的module中使用，并且module被导入的时候，一定要跟着这个歌package一起被导入的，单独尝试运行一个package里面的module会导致relative import 出错

导入的时候，我们想导入的这个module不在同一个文件夹，而是在上一个文件夹，那么可以使用两个点 .. 代表往上走一个package，同样的，这段代码的使用也要求这个submodule.py跟着这个mypackage一起导入的代码中使用的。

Python在运行的时候，必须吧relative import 变成absolute import，需要知道自己输入哪个package

## 补充

---

import ... 后面所接的必须是模块，不能是包 如果是包，在\__init__.py没有导入的情况下是会报错的

首先，如果有下面的文件目录：

当前目录(package)

​	one(package)

​		\- \__init__.py

​		\- aaa.py

​		\- mo.py

其中：

```python
# mo.py
pi = 3.14
```

```python
# __init__.py

```

```python
# aaa.py
import mo
print(mo.py)
```

我们运行aaa.py,会正常显示。

但是当我们在此基础上修改一下：

当前目录(package)

​	\- \__init__.py

​	\- bbb.py

​	\- one(package)

​		\- \__init__.py

​		\- aaa.py

​		\- mo.py

其中aaa.py文件和mo文件不变，`one/__init__.py`文件和 `当前目录/__init__.py文件`都是空的

在bbb.py文件中做修改

```python
# bbb.py
import one
print(one.mo.pi)
```

这样子是不可以的，会报错`AttributeError: module 'one' has no attribute 'mo'`

我们如果修改`one/__init__.py`文件：

```python
# one/__init__.py
pi = 3.14
```

那么我们在`bbb.py`文件中这样写：

```python
# bbb.py 
import one
print(one.pi)
```

则是正常的！

此外，如果我们在``文件中这样写：

```python
# one/__init__.py
from .mo import pi
```

在bbb.py文件中这样写

```python
# bbb.py
import one
print(one.mo.pi)
```

或者这样写bbb.py文件：

```python
# bbb.py
import one
print(one.pi)
```

都是可以正常运行的。此外，还可以在`__init__.py`文件中这样写：

```python
# one/__init__.py
from .mo import pi, MoA, main
```

![image-20230429134400728](D:\MDFiles\images\image-20230429134400728.png)

可以导入函数、类、变量等。

此外，`one/__init__.py`还有另外一种写法：

```python
只有当 from test import * 的时候，__all__才有影响。当直接import test 时，__all__是影响不到test中子包的
```

```python
# 更多相关内容可以参考知乎：https://zhuanlan.zhihu.com/p/571294861
```

******

# python import -- 来自网络

## 模块(module)

退出 Python 解释器后，再次进入时，之前在 Python 解释器中定义的函数和变量就丢失了。

因此，编写较长程序时，最好用文本编辑器代替解释器，执行文件中的输入内容，这就是编写 *脚本* 。

随着程序越来越长，为了方便维护，最好把脚本拆分成多个文件。

编写脚本还一个好处，不同程序调用同一个函数时，不用把函数定义复制到各个程序。

## import

1. 第一种导入方式 import 模块名
    **这种方式不会直接将fibo中定义的函数名添加到当前的namespace中，只是将模块名称fibo添加到namespace里面，使用这个模块名称即可访问其中的函数**

    ```python
    # fibo.py文件
    
    def fib(n):    # write Fibonacci series up to n
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
    
    def fib2(n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result
    ```

    ```python
    import fibo
    fibo.fib(10)
    fibo.fib2(10)
    ```

2. 第二种导入方式 from 模块名 import 模块里面的名称
    **这种方式将来自某个模块的名称直接导入到<u>导入方模块</u>的命名空间(namespace)中.** **这条语句<u>不会</u>将所导入的模块的名称引入到局部命名空间中（因此在本示例中，`fibo` 将是未定义的名称）**

    ```python
    from fibo import fib, fib2
    fib(500)
    ```

3. 第三种导入方式 from 模块名 import * **导入模块内定义的所有名称** **这种方式会导入所有不以下划线（`_`）开头的名称。大多数情况下，不要用这个功能，这种方式向解释器导入了一批未知的名称，可能会覆盖已经定义的名称。**

    ```python
    from fibo import *
    fib(500)
    ```

4. 此外，模块名后使用 `as` 时，直接把 `as` 后的名称与导入模块绑定。与 `import fibo` 一样，这种方式也可以有效地导入模块，唯一的区别是，导入的名称是 `fib`。`from` 中也可以使用这种方式，效果类似：

    ```
    >>> import fibo as fib
    >>> fib.fib(500)
    ```

5. <u>**备注**</u>

    为了保证运行效率，每次解释器会话只导入一次模块。如果更改了模块内容，必须重启解释器；仅交互测试一个模块时，也可以使用 [`importlib.reload()`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.reload)，例如:

    ```python
    import importlib
    importlib.reload(modulename)
    ```

## dir()

内置函数 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 用于查找模块定义的名称。返回结果是经过排序的字符串列表；

[`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 不会列出内置函数和变量的名称。这些内容的定义在标准模块 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 中：

```python
import builtins
dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

## 包 (package)

包是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式。 例如，模块名 `A.B` 表示名为 `A` 的包中名为 `B` 的子模块。 就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用带点号模块名也可以让 NumPy 或 Pillow 等多模块包的作者也不必担心彼此的模块名冲突。

```python
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

导入包时，Python 搜索 `sys.path` 里的目录，查找包的子目录。

需要有 `__init__.py` 文件才能让 Python 将包含该文件的目录当作包来处理（除非使用 namespace package，这是一个相对高级的特性）。 这可以防止重名的目录如 `string` 在无意中屏蔽后继出现在模块搜索路径中的有效模块。 在最简单的情况下，`__init__.py` 可以只是一个空文件，但它也可以执行包的初始化代码或设置 `__all__` 变量。

还可以从包中导入单个模块，例如：

```
import sound.effects.echo
```

这将加载子模块 `sound.effects.echo`。 它必须通过其全名来引用。

```
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

另一种导入子模块的方法是 ：

```
from sound.effects import echo
```

这也会加载子模块 `echo`，并使其不必加包前缀，因此可按如下方式使用:

```
echo.echofilter(input, output, delay=0.7, atten=4)
```

Import 语句的另一种变体是直接导入所需的函数或变量：

```
from sound.effects.echo import echofilter
```

同样，这将加载子模块 `echo`，但这使其函数 `echofilter()` 直接可用:

```
echofilter(input, output, delay=0.7, atten=4)
```

！！！注意，使用 `from package import item` 时，item 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。`import` 语句首先测试包中是否定义了 item；如果未在包中定义，则假定 item 是模块，并尝试加载。如果找不到 item，则触发 [`ImportError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError) 异常。

相反，使用 `import item.subitem.subsubitem` 句法时，除最后一项外，每个 item 都必须是包；最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。

注意，使用 `from package import item` 时，item 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。`import` 语句首先测试包中是否定义了 item；如果未在包中定义，则假定 item 是模块，并尝试加载。如果找不到 item，则触发 [`ImportError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ImportError) 异常。

相反，使用 `import item.subitem.subsubitem` 句法时，除最后一项外，每个 item 都必须是包；最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。

使用 `from sound.effects import *` 时会发生什么？你可能希望它会查找并导入包的所有子模块，但事实并非如此。因为这将花费很长的时间，并且可能会产生你不想要的副作用，如果这种副作用被你设计为只有在导入某个特定的子模块时才应该发生。

唯一的解决办法是提供包的显式索引。[`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句使用如下惯例：如果包的 `__init__.py` 代码定义了列表 `__all__`，运行 `from package import *` 时，它就是被导入的模块名列表。发布包的新版本时，包的作者应更新此列表。如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列表。

例如，`sound/effects/__init__.py` 文件可以包含以下代码：

```
__all__ = ["echo", "surround", "reverse"]
```

这意味着 `from sound.effects import *` 将导入 `sound.effects` 包的三个命名子模块。

请注意子模块可能会受到本地定义名称的影响。 例如，如果你在 `sound/effects/__init__.py` 文件中添加了一个 `reverse` 函数，`from sound.effects import *` 将只导入 `echo` 和 `surround` 这两个子模块，但 **不会** 导入 `reverse` 子模块，因为它被本地定义的 `reverse` 函数所遮挡:

```
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
```

如果没有定义 `__all__`，`from sound.effects import *` 语句 *不会* 把包 `sound.effects` 中的所有子模块都导入到当前命名空间；它只是确保包 `sound.effects` 已被导入（可能还会运行 `__init__.py` 中的任何初始化代码），然后再导入包中定义的任何名称。 这包括由 `__init__.py` 定义的任何名称（以及显式加载的子模块）。 它还包括先前 [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句显式加载的包里的任何子模块。 请看以下代码:

```
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

在本例中，`echo` 和 `surround` 模块被导入到当前命名空间，因为在执行 `from...import` 语句时它们已在 `sound.effects` 包中定义了。 （当定义了 `__all__` 时也是如此）。

虽然，可以把模块设计为用 `import *` 时只导出遵循指定模式的名称，但仍不提倡在生产代码中使用这种做法。

记住，使用 `from package import specific_submodule` 没有任何问题！ 实际上，除了导入模块使用不同包的同名子模块之外，这种方式是推荐用法。

## 相对导入

当包由多个子包构成（如示例中的 `sound` 包）时，可以使用绝对导入来引用同级包的子模块。 例如，如果 `sound.filters.vocoder` 模块需要使用 `sound.effects` 包中的 `echo` 模块，它可以使用 `from sound.effects import echo`。

你还可以编写相对导入代码，即使用 `from module import name` 形式的 import 语句。 这些导入使用前导点号来表示相对导入所涉及的当前包和上级包。 例如对于 `surround` 模块，可以使用:

```
from . import echo
from .. import formats
from ..filters import equalizer
```

注意，相对导入基于当前模块名。因为主模块名永远是 `"__main__"` ，所以如果计划将一个模块用作 Python 应用程序的主模块，那么该模块内的导入语句必须始终使用绝对导入。

## 多目录中的包

包还支持一个特殊属性 [`__path__`](https://docs.python.org/zh-cn/3/reference/import.html#path__) 。在包的 `__init__.py` 中的代码被执行前，该属性被初始化为一个只含一项的列表，该项是一个字符串，是 __init__.py 所在目录的名称。可以修改此变量；这样做会改变在此包中搜索模块和子包的方式。

这个功能虽然不常用，但可用于扩展包中的模块集。























