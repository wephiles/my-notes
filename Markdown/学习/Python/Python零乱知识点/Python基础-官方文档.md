<h1 style="text-align: center;">python知识点</h1>

# 一、内置函数

> 参考网址：https://docs.python.org/zh-cn/3/library/functions.html

## 1.1 `abs(x)`

返回一个数字的绝对值。 参数可以是整数、浮点数或任何实现了 [`__abs__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__abs__) 的对象。 如果参数是一个复数，则返回它的模。

```python
"""
abs(x)
  返回一个数字的绝对值。 参数可以是整数、浮点数或任何实现了 __abs__() 的对象。 如果参数是一个复数，则返回它的模。
"""

x: int = -10
abs_x: int = abs(x)
print(f'x={x}, abs_x={abs_x}')

y: float = -10.25
abs_y: float = abs(y)
print(f'y={y}, abs_y={abs_y}')

z: complex = -3 + 4j
abs_z: float = abs(z)
print(f'z={z},abs_z={abs_z}')
```

## 1.2 `aiter(async_iterable)`

返回 [asynchronous iterable](https://docs.python.org/zh-cn/3/glossary.html#term-asynchronous-iterable) 的 [asynchronous iterator](https://docs.python.org/zh-cn/3/glossary.html#term-asynchronous-iterator) 。相当于调用 `x.__aiter__()`。

注意：与 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 不同，[`aiter()`](https://docs.python.org/zh-cn/3/library/functions.html#aiter) 没有两个参数的版本。

> *Added in version 3.10.*

## 1.3 `all(iterable)`

如果 *`iterable`* 的所有元素均为真值（或可迭代对象为空）则返回 `True` 。 等价于：

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

```python
"""
all(iterable)
如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True 。 等价于：

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
"""
a_list = [1, 5, 10, 0]
x: bool = all(a_list)

print(x)

b_list = [0, 3, 10]
y: bool = any(b_list)

print(y)
```

## 1.4 **any**(*iterable*)

如果 *iterable* 的任一元素为真值则返回 `True`。 如果可迭代对象为空，返回 `False`。 等价于:

```
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

## 1.5 **ascii**(*object*)

与 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 类似，返回一个包含对象的可打印表示形式的字符串，但是使用 `\x`、`\u` 和 `\U` 对 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 返回的字符串中非 ASCII 编码的字符进行转义。生成的字符串和 Python 2 的 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr) 返回的结果相似。

## 1.6 **bin**(*x*)

将一个整数转换为带前缀 "0b" 的二进制数字符串。 结果是一个合法的 Python 表达式。 如果 *x* 不是一个 Python [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 对象，则它必须定义返回一个整数的 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__) 方法。 下面是一些例子:

```
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
```

若要控制是否显示前缀“0b”，可以采用以下两种方案：

```
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')
```

另见 [`format()`](https://docs.python.org/zh-cn/3/library/functions.html#format) 获取更多信息。

## 1.7 *class* **bool**(*object=False*, */*)

返回布尔值，即 `True` 或 `False` 中的一个。 其参数将使用标准的 [真值测试过程](https://docs.python.org/zh-cn/3/library/stdtypes.html#truth) 来转换。 如果该参数为假值或被省略，则返回 `False`；在其他情况下，将返回 `True`。 [`bool`](https://docs.python.org/zh-cn/3/library/functions.html#bool) 类是 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 的子类 (参见 [数字类型 --- int, float, complex](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesnumeric))。 它不能被继续子类化。 它只有 `False` 和 `True` 这两个实例 (参见 [布尔类型 - bool](https://docs.python.org/zh-cn/3/library/stdtypes.html#typebool))。

*在 3.7 版本发生变更:* 该形参现在为仅限位置形参。

## 1.8 **breakpoint**(\*args, \*\*kws)

此函数会在调用点进入调试器。具体来说，它调用 [`sys.breakpointhook()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.breakpointhook) ，直接传递 `args` 和 `kws` 。默认情况下， `sys.breakpointhook()` 调用 [`pdb.set_trace()`](https://docs.python.org/zh-cn/3/library/pdb.html#pdb.set_trace) 且没有参数。在这种情况下，它纯粹是一个便利函数，因此您不必显式导入 [`pdb`](https://docs.python.org/zh-cn/3/library/pdb.html#module-pdb) 且键入尽可能少的代码即可进入调试器。但是， [`sys.breakpointhook()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.breakpointhook) 可以设置为其他一些函数并被 [`breakpoint()`](https://docs.python.org/zh-cn/3/library/functions.html#breakpoint) 自动调用，以允许进入你想用的调试器。如果 [`sys.breakpointhook()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.breakpointhook) 不可访问，这个函数将会引发 [`RuntimeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#RuntimeError)。

在默认情况下，[`breakpoint()`](https://docs.python.org/zh-cn/3/library/functions.html#breakpoint) 的行为可使用 [`PYTHONBREAKPOINT`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONBREAKPOINT) 环境变量来改变。 请参阅 [`sys.breakpointhook()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.breakpointhook) 了解详细用法。

请注意这并不保证 [`sys.breakpointhook()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.breakpointhook) 会被替换。

引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `builtins.breakpoint` 并附带参数 `breakpointhook`。

*Added in version 3.7.*

## 1.9 **callable**(*object*)

如果 *object* 参数是可调用的则返回 [`True`](https://docs.python.org/zh-cn/3/library/constants.html#True)，否则返回 [`False`](https://docs.python.org/zh-cn/3/library/constants.html#False)。 如果返回 `True`，调用仍可能失败，但如果返回 `False`，则调用 *object* 肯定不会成功。 请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 [`__call__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__call__) 方法则它就是可调用的。

*Added in version 3.2:* 这个函数一开始在 Python 3.0 被移除了，但在 Python 3.2 被重新加入。

## 1.10 **chr**(*i*)

返回 Unicode 码位为整数 *i* 的字符的字符串格式。例如，`chr(97)` 返回字符串 `'a'`，`chr(8364)` 返回字符串 `'€'`。这是 [`ord()`](https://docs.python.org/zh-cn/3/library/functions.html#ord) 的逆函数。

实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 *i* 超过这个范围，会触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 异常。

## 1.11 @**classmethod**

把一个方法封装成类方法。

类方法隐含的第一个参数就是类，就像实例方法接收实例作为参数一样。要声明一个类方法，按惯例请使用以下方案：

```
class C:
    @classmethod
    def f(cls, arg1, arg2): ...
```

`@classmethod` 这样的形式称为函数的 [decorator](https://docs.python.org/zh-cn/3/glossary.html#term-decorator) -- 详情参阅 [函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function)。

类方法的调用可以在类上进行 (例如 `C.f()`) 也可以在实例上进行 (例如 `C().f()`)。 其所属类以外的类实例会被忽略。 如果类方法在其所属类的派生类上调用，则该派生类对象会被作为隐含的第一个参数被传入。

类方法与 C++ 或 Java 中的静态方法不同。 如果你需要后者，请参阅本节中的 [`staticmethod()`](https://docs.python.org/zh-cn/3/library/functions.html#staticmethod)。 有关类方法的更多信息，请参阅 [标准类型层级结构](https://docs.python.org/zh-cn/3/reference/datamodel.html#types)。

*在 3.9 版本发生变更:* 类方法现在可以包装其他 [描述器](https://docs.python.org/zh-cn/3/glossary.html#term-descriptor) 例如 [`property()`](https://docs.python.org/zh-cn/3/library/functions.html#property)。

*在 3.10 版本发生变更:* 类方法现在继承了方法的属性（ `__module__`、 `__name__`、 `__qualname__`、 `__doc__` 和 `__annotations__`），并拥有一个新的 `__wrapped__` 属性。

*在 3.11 版本发生变更:* 类方法不再可以包装其他 [descriptors](https://docs.python.org/zh-cn/3/glossary.html#term-descriptor) 例如 [`property()`](https://docs.python.org/zh-cn/3/library/functions.html#property)。

## 1.12 **compile**(*source*, *filename*, *mode*, *flags=0*, *dont_inherit=False*, *optimize=-1*)

将 *source* 编译成代码或 AST 对象。代码对象可以被 [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) 或 [`eval()`](https://docs.python.org/zh-cn/3/library/functions.html#eval) 执行。*source* 可以是常规的字符串、字节字符串，或者 AST 对象。参见 [`ast`](https://docs.python.org/zh-cn/3/library/ast.html#module-ast) 模块的文档了解如何使用 AST 对象。

*filename* 实参需要是代码读取的文件名；如果代码不需要从文件中读取，可以传入一些可辨识的值（经常会使用 `'<string>'`）。

*mode* 实参指定了编译代码必须用的模式。如果 *source* 是语句序列，可以是 `'exec'`；如果是单一表达式，可以是 `'eval'`；如果是单个交互式语句，可以是 `'single'`。（在最后一种情况下，如果表达式执行结果不是 `None` 将会被打印出来。）

可选参数 *flags* 和 *dont_inherit* 控制应当激活哪个 [编译器选项](https://docs.python.org/zh-cn/3/library/ast.html#ast-compiler-flags) 以及应当允许哪个 [future 特性](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#future)。 如果两者都未提供 (或都为零) 则代码会应用与调用 [`compile()`](https://docs.python.org/zh-cn/3/library/functions.html#compile) 的代码相同的旗标来编译。 如果给出了 *flags* 参数而未给出 *dont_inherit* (或者为零) 则会在无论如何都将被使用的旗标之外还会额外使用 *flags* 参数所指定的编译器选项和 future 语句。 如果 *dont_inherit* 为非零整数，则只使用 *flags* 参数 -- 外围代码中的旗标 (future 特性和编译器选项) 会被忽略。

编译器选项和 future 语句是由比特位来指明的。 比特位可以通过一起按位 OR 来指明多个选项。 指明特定 future 特性所需的比特位可以在 [`__future__`](https://docs.python.org/zh-cn/3/library/__future__.html#module-__future__) 模块的 [`_Feature`](https://docs.python.org/zh-cn/3/library/__future__.html#future__._Feature) 实例的 [`compiler_flag`](https://docs.python.org/zh-cn/3/library/__future__.html#future__._Feature.compiler_flag) 属性中找到。 [编译器旗标](https://docs.python.org/zh-cn/3/library/ast.html#ast-compiler-flags) 可以在 [`ast`](https://docs.python.org/zh-cn/3/library/ast.html#module-ast) 模块中查找带有 `PyCF_` 前缀的名称。

*optimize* 实参指定编译器的优化级别；默认值 `-1` 选择与解释器的 [`-O`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-O) 选项相同的优化级别。显式级别为 `0` （没有优化；`__debug__` 为真）、`1` （断言被删除， `__debug__` 为假）或 `2` （文档字符串也被删除）。

如果编译的源码不合法，此函数会触发 [`SyntaxError`](https://docs.python.org/zh-cn/3/library/exceptions.html#SyntaxError) 异常；如果源码包含 null 字节，则会触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 异常。

如果您想分析 Python 代码的 AST 表示，请参阅 [`ast.parse()`](https://docs.python.org/zh-cn/3/library/ast.html#ast.parse)。

引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `compile` 附带参数 `source` 和 `filename`。 此事件也可通过隐式编译来引发。

备注

在 `'single'` 或 `'eval'` 模式编译多行代码字符串时，输入必须以至少一个换行符结尾。 这使 [`code`](https://docs.python.org/zh-cn/3/library/code.html#module-code) 模块更容易检测语句的完整性。

> [!Warning]
>
> 在将足够大或者足够复杂的字符串编译成 AST 对象时，Python 解释器有可能因为 Python AST 编译器的栈深度限制而崩溃。
>
> *在 3.2 版本发生变更:* Windows 和 Mac 的换行符均可使用。而且在 `'exec'` 模式下的输入不必再以换行符结尾了。另增加了 *optimize* 参数。
>
> *在 3.5 版本发生变更:* 之前 *source* 中包含 null 字节的话会触发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。
>
> *Added in version 3.8:* `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` 现在可在旗标中传入以启用对最高层级 `await`, `async for` 和 `async with` 的支持。

## 1.13 **delattr**(*object*, *name*)

这是 [`setattr()`](https://docs.python.org/zh-cn/3/library/functions.html#setattr) 的相关函数。 其参数是一个对象和一个字符串。 其中字符串必须是对象的某个属性的名称。 该函数会删除指定的属性，如果对象允许这样做的话。 例如，`delattr(x, 'foobar')` 等价于 `del x.foobar`。 *name* 不要求必须是 Python 标识符 (参见 [`setattr()`](https://docs.python.org/zh-cn/3/library/functions.html#setattr))。

## 1.14 **dir**() & **dir**(*object*)

如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。

如果对象有一个名为 [`__dir__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__dir__) 的方法，则该方法将被调用并且必须返回由属列组成的列表。 这允许实现自定义This allows objects that implement a custom [`__getattr__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getattr__) 或 [`__getattribute__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getattribute__) 函数的对象能够定制 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 报告其属性的方式。

如果对象未提供 [`__dir__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__dir__)，该函数会尽量从对象所定义的 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性和其类型对象中收集信息。 结果列表不一定是完整的，并且当对象具有自定义的 [`__getattr__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getattr__) 时还可能是不准确的。

默认的 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 机制对不同类型的对象行为不同，它会试图返回最相关而不是最全的信息：

- 如果对象是模块对象，则列表包含模块的属性名称。
- 如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。
- 否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。

返回的列表按字母表排序。例如：

```
>>> import struct
>>> dir()   # show the names in the module namespace  
['__builtins__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module 
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Shape:
...     def __dir__(self):
...         return ['area', 'perimeter', 'location']
...
>>> s = Shape()
>>> dir(s)
['area', 'location', 'perimeter']
```

> [!Note]
>
> 因为 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 主要是为了便于在交互式时使用，所以它会试图返回人们感兴趣的名字集合，而不是试图保证结果的严格性或一致性，它具体的行为也可能在不同版本之间改变。例如，当实参是一个类时，metaclass 的属性不包含在结果列表中。

## 1.15 **divmod**(*a*, *b*)

接受两个（非复数）数字作为参数并返回由当对其使用整数除法时的商和余数组成的数字对。 在混用不同的操作数类型时，则会应用二元算术运算符的规则。 对于整数来说，结果与 `(a // b, a % b)` 相同。 对于浮点数来说则结果为 `(q, a % b)`，其中 *q* 通常为 `math.floor(a / b)` 但可能会比它小 1。 在任何情况下 `q * b + a % b` 都非常接近 *a*，如果 `a % b` 为非零值则它将具有与 *b* 相同的正负号，并且 `0 <= abs(a % b) < abs(b)`。

## 1.16 **enumerate**(*iterable*, *start=0*)

返回一个枚举对象。*iterable* 必须是一个序列，或 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)，或其他支持迭代的对象。 [`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate) 返回的迭代器的 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法返回一个元组，里面包含一个计数值（从 *start* 开始，默认为 0）和通过迭代 *iterable* 获得的值。

```
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

等价于:

```
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```

> [!Caution]
>
> ```python
> x = enumerate(['adssa', 'dasde', 'rew', 'yhr'])
> print(x)
> print(list(x))
> 
> for index, value in enumerate(['adssa', 'dasde', 'rew', 'yhr']):
>     print(index, '->', value)
> 
> for index, value in x:
>     print(index, '->', value)
> ```
>
> 上面的代码执行的结果是：
>
> ![image-20240816163713817](./assets/image-20240816163713817.png)
>
> 为什么下面的这两行代码不会打印出数据呢？
>
> ```python
> for index, value in x:
>     print(index, '->', value)
> ```
>
> **原因如下：**
>
> 在Python中，`enumerate` 函数用于将一个可迭代对象（如列表、元组等）组合为一个索引序列，同时返回元素索引和元素值。通常，`enumerate` 会返回一个迭代器，这个迭代器生成包含元素索引和元素值的元组。
>
> 你的代码中，`x = enumerate(['adssa', 'dasde', 'rew', 'yhr'])` 这行代码实际上创建了一个迭代器，而不是列表。当你打印 `x` 时，你会看到迭代器对象的内存地址，而不是它的元素。当你打印 `list(x)` 时，你实际上是在将迭代器转换成列表，这时候你会看到索引和值的列表。
>
> 问题出现在你尝试直接在 `for` 循环中使用 `x` 作为迭代对象。由于 `x` 是一个迭代器，它只能被迭代一次。当你使用 `list(x)` 将迭代器转换为列表时，你已经消耗了迭代器，所以再次尝试迭代它时，它已经没有元素可以返回了。
>
> 要解决这个问题，你可以重新生成迭代器，或者在第一次使用 `enumerate` 时直接在 `for` 循环中使用它，如下所示：
>
> ```
> python# 第一个for循环，直接使用enumerate生成迭代器并迭代
> for index, value in enumerate(['adssa', 'dasde', 'rew', 'yhr']):
>     print(index, '->', value)
> 
> # 第二个for循环，重新生成迭代器
> x = enumerate(['adssa', 'dasde', 'rew', 'yhr'])
> for index, value in x:
>     print(index, '->', value)
> ```
>
> 或者，如果你想要保留 `x` 作为列表，你可以这样做：
>
> ```
> python复制# 使用enumerate生成索引和值的列表
> x = list(enumerate(['adssa', 'dasde', 'rew', 'yhr']))
> print(x)
> 
> # 直接迭代x，因为它已经是列表了
> for index, value in x:
>     print(index, '->', value)
> ```
>
> 这样，你就可以在不同的 `for` 循环中使用 `x` 了。

> [!Important]
>
> 迭代器（Iterator）是Python中的一种数据类型，它允许你遍历容器中的元素，但不允许索引访问。迭代器的主要特点是惰性求值，即元素在需要时才会生成，这有助于节省内存和提高效率。
>
> 迭代器只能被迭代一次，原因如下：
>
> 1. **惰性求值**：迭代器在每次迭代时计算下一个元素，而不是一次性生成所有元素。这使得迭代器可以用于非常大的数据集，因为不需要一次性将所有数据加载到内存中。
> 2. **一次性使用**：迭代器的设计初衷是单次使用。一旦迭代完成，迭代器就会到达终止状态，无法再次使用。这有助于避免数据重复处理或错误。
> 3. **内存效率**：由于迭代器是按需生成元素的，所以它不需要存储所有元素的副本。这可以显著减少内存使用，特别是在处理大型数据集时。
> 4. **流式处理**：在某些情况下，数据可能是以流的形式提供，如文件读取或网络数据传输。迭代器允许逐步处理这些数据流，而不是一次性加载整个数据流。
>
> 当你使用 `enumerate` 函数时，它返回的是一个迭代器，这个迭代器在每次迭代时生成一个包含索引和值的元组。一旦你完成了迭代，迭代器就会到达终止状态，无法再次生成元素。这就是为什么 `x` 只能迭代一次的原因。
>
> 如果你需要多次迭代同一个序列，你可以考虑以下几种方法：
>
> - **重新生成迭代器**：每次需要迭代时，都重新调用 `enumerate` 函数。
> - **转换为列表**：使用 `list()` 函数将迭代器转换为列表，然后可以多次迭代这个列表。
> - **使用 `itertools.tee`**：如果你需要在多个地方同时迭代同一个序列，可以使用 `itertools.tee` 函数来创建多个迭代器副本。
>
> 理解迭代器的这些特性可以帮助你更有效地使用Python进行数据迭代和处理。

## 1.17 **eval**(*expression*, *globals=None*, *locals=None*)

- 参数:

    **expression** ([`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) | [code object](https://docs.python.org/zh-cn/3/reference/datamodel.html#code-objects)) -- 一个 Python 表达式。**globals** ([`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) | `None`) -- 全局命名空间 (默认值: `None`)。**locals** ([mapping](https://docs.python.org/zh-cn/3/glossary.html#term-mapping) | `None`) -- 局部命名空间 (默认值: `None`)。

- 返回:

    被求值表达式的求值结果。

- 引发:

    语法错误将作为异常被报告。

表达式解析参数 *expression* 并作为 Python 表达式进行求值（从技术上说是一个条件列表），采用 *globals* 和 *locals* 字典作为全局和局部命名空间。 如果存在 *globals* 字典，并且不包含 `__builtins__` 键的值，则在解析 *expression* 之前会插入以该字符串为键以对内置模块 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 的字典的引用为值的项。 这样就可以在将 *globals* 传给 [`eval()`](https://docs.python.org/zh-cn/3/library/functions.html#eval) 之前通过向其传入你自己的 `__builtins__` 字典来控制可供被执行代码可以使用哪些内置模块。 如果 *locals* 字典被省略则它默认为 *globals* 字典。 如果两个字典都被省略，则将使用调用 [`eval()`](https://docs.python.org/zh-cn/3/library/functions.html#eval) 的环境中的 *globals* 和 *locals* 来执行该表达式。 注意，*eval()* 无法访问闭包环境中的 [嵌套作用域](https://docs.python.org/zh-cn/3/glossary.html#term-nested-scope) (非局部变量)。

示例:

\>>>

```
>>> x = 1
>>> eval('x+1')
2
```

该函数还可用于执行任意代码对象（比如由 [`compile()`](https://docs.python.org/zh-cn/3/library/functions.html#compile) 创建的对象）。 这时传入的是代码对象，而非一个字符串了。如果代码对象已用参数为 *mode* 的 `'exec'` 进行了编译，那么 [`eval()`](https://docs.python.org/zh-cn/3/library/functions.html#eval) 的返回值将为 `None`。

提示： [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) 函数支持语句的动态执行。 [`globals()`](https://docs.python.org/zh-cn/3/library/functions.html#globals) 和 [`locals()`](https://docs.python.org/zh-cn/3/library/functions.html#locals) 函数分别返回当前的全局和本地字典，可供传给 [`eval()`](https://docs.python.org/zh-cn/3/library/functions.html#eval) 或 [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) 使用。

如果给出的源数据是个字符串，那么其前后的空格和制表符将被剔除。

另外可以参阅 [`ast.literal_eval()`](https://docs.python.org/zh-cn/3/library/ast.html#ast.literal_eval)，该函数可以安全执行仅包含文字的表达式字符串。

引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `exec` 附带代码对象作为参数。 代码编译事件也可能被引发。

## 1.18 **exec**(*object*, *globals=None*, *locals=None*, */*, ***, *closure=None*)

This function supports dynamic execution of Python code. *object* must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). [[1\]](https://docs.python.org/zh-cn/3/library/functions.html#id2) If it is a code object, it is simply executed. In all cases, the code that's executed is expected to be valid as file input (see the section [文件输入](https://docs.python.org/zh-cn/3/reference/toplevel_components.html#file-input) in the Reference Manual). Be aware that the [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal), [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield), and [`return`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#return) statements may not be used outside of function definitions even within the context of code passed to the [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) function. The return value is `None`.

> 此函数支持动态执行 Python 代码。*object* 必须是字符串或代码对象。如果它是一个字符串，则该字符串将被解析为一组 Python 语句，然后执行该语句（除非发生语法错误）。 如果它是一个代码对象，则简单地执行它。在所有情况下，执行的代码都应作为文件输入有效（请参阅参考手册中的文件输入部分）。请注意，nonlocal、yield 和 return 语句不能在函数定义之外使用，即使在传递给 exec（） 函数的代码上下文中也是如此。返回值为“None”。
>
> 在所有情况下，如果省略了可选部分，代码将在当前作用域中执行。 如果只提供了 *globals*，则它必须是一个字典（并且不能是字典的子类），它将被同时用于全局和局部变量。 如果给出了 *globals* 和 *locals*，它们将被分别用于全局和局部变量。 如果提供了 *locals*，它可以是任何映射对象。 请记住在模块层级上，globals 和 locals 是同一个字典。

备注

Most users should just pass a *globals* argument and never *locals*. If exec gets two separate objects as *globals* and *locals*, the code will be executed as if it were embedded in a class definition.

如果 *globals* 字典不包含 `__builtins__` 键值，则将为该键插入对内建 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 模块字典的引用。因此，在将执行的代码传递给 [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) 之前，可以通过将自己的 `__builtins__` 字典插入到 *globals* 中来控制可以使用哪些内置代码。

*closure* 参数指定一个闭包 -- 即由 cellvar 组成的元组。 它仅在 *object* 是一个包含自由变量的代码对象时才可用。 该元组的长度必须与代码对象所引用的自由变量的数量完全一致。

引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `exec` 附带代码对象作为参数。 代码编译事件也可能被引发。

备注

内置 [`globals()`](https://docs.python.org/zh-cn/3/library/functions.html#globals) 和 [`locals()`](https://docs.python.org/zh-cn/3/library/functions.html#locals) 函数各自返回当前的全局和本地字典，因此可以将它们传递给 [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) 的第二个和第三个实参。

备注

The default *locals* act as described for function [`locals()`](https://docs.python.org/zh-cn/3/library/functions.html#locals) below: modifications to the default *locals* dictionary should not be attempted. Pass an explicit *locals* dictionary if you need to see effects of the code on *locals* after function [`exec()`](https://docs.python.org/zh-cn/3/library/functions.html#exec) returns.

*在 3.11 版本发生变更:* 添加了 *closure* 参数。

![image-20240816164823991](./assets/image-20240816164823991.png)

## 1.19  **filter**(*function*, *iterable*)

使用 *iterable* 中 *function* 返回真值的元素构造一个迭代器。 *iterable* 可以是一个序列，一个支持迭代的容器或者一个迭代器。 如果 *function* 为 `None`，则会使用标识号函数，也就是说，*iterable* 中所有具有假值的元素都将被移除。

请注意， `filter(function, iterable)` 相当于一个生成器表达式，当 function 不是 `None` 的时候为 `(item for item in iterable if function(item))`；function 是 `None` 的时候为 `(item for item in iterable if item)` 。

请参阅 [`itertools.filterfalse()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.filterfalse) 来了解返回 *iterable* 中 *function* 返回假值的元素的补充函数。

![image-20240816165141687](./assets/image-20240816165141687.png)

## 1.20 *class* **float**(*number=0.0*, */*) & *class* **float**(*string*, */*)

返回基于一个数字或字符串构建的浮点数。

```
>>> float('+1.23')
1.23
>>> float('   -12345\n')
-12345.0
>>> float('1e-003')
0.001
>>> float('+1E6')
1000000.0
>>> float('-Infinity')
-inf
```

如果该参数是一个字符串，则它应当包含一个十进制数字，前面可以选择带一个符号，也可以选择嵌入空格。 可选的符号有 `'+'` 或 `'-'`；`'+'` 符号对所产生的值没有影响。 该参数还可以是一个代表 NaN (not-a-number) 或者正负无穷大的字符串。 更确切地说，在移除前导和尾随的空格之后，输入必须为符合以下语法的 [`floatvalue`](https://docs.python.org/zh-cn/3/library/functions.html#grammar-token-float-floatvalue) 产生规则：

```
sign          ::=  "+" | "-"
infinity      ::=  "Infinity" | "inf"
nan           ::=  "nan"
digit         ::=  <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
digitpart     ::=  digit (["_"] digit)*
number        ::=  [digitpart] "." digitpart | digitpart ["."]
exponent      ::=  ("e" | "E") [sign] digitpart
floatnumber   ::=  number [exponent]
absfloatvalue ::=  floatnumber | infinity | nan
floatvalue    ::=  [sign] absfloatvalue
```

大小写是无影响的，因此举例来说，"inf", "Inf", "INFINITY" 和 "iNfINity" 都是正无穷可接受的拼写形式。

另一方面，如果参数是整数或浮点数，则返回一个具有相同值（在 Python 浮点精度范围内）的浮点数。 如果参数超出了 Python 浮点数的取值范围，则会引发 [`OverflowError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OverflowError)。

对于一个普通 Python 对象 `x`，`float(x)` 会委托给 `x.__float__()`。 如果 [`__float__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__float__) 未定义则将回退至 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)。

如果没有实参，则返回 `0.0` 。

[数字类型 --- int, float, complex](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesnumeric) 描述了浮点类型。

*在 3.6 版本发生变更:* 您可以使用下划线将代码文字中的数字进行分组。

*在 3.7 版本发生变更:* 该形参现在为仅限位置形参。

*在 3.8 版本发生变更:* 如果 [`__float__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__float__) 未定义则回退至 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)。

## 1.21 **format**(*value*, *format_spec=''*)    需要再了解了解\*\*

将 *value* 转换为“格式化后”的形式，格式由 *format_spec* 进行控制。*format_spec* 的解释方式取决于 *value* 参数的类型；但大多数内置类型使用一种标准的格式化语法： [格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#formatspec)。默认的 *format_spec* 是一个空字符串，它通常给出与调用 [`str(value)`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 相同的结果。对 `format(value, format_spec)` 的调用会转写为 `type(value).__format__(value, format_spec)`，这样在搜索值的 [`__format__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__format__) 方法时将绕过实例字典。 如果方法搜索到达 [`object`](https://docs.python.org/zh-cn/3/library/functions.html#object) 并且 *format_spec* 不为空，或者如果 *format_spec* 或返回值不为字符串则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。*在 3.4 版本发生变更:* 当 *format_spec* 不是空字符串时， `object().__format__(format_spec)` 会触发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。

## 1.22 *class* **frozenset**(*iterable=set()*)

返回一个新的 [`frozenset`](https://docs.python.org/zh-cn/3/library/stdtypes.html#frozenset) 对象，它包含可选参数 *iterable* 中的元素。 `frozenset` 是一个内置的类。有关此类的文档，请参阅 [`frozenset`](https://docs.python.org/zh-cn/3/library/stdtypes.html#frozenset) 和 [集合类型 --- set, frozenset](https://docs.python.org/zh-cn/3/library/stdtypes.html#types-set)。请参阅内建的 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set)、[`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)、[`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 和 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 类，以及 [`collections`](https://docs.python.org/zh-cn/3/library/collections.html#module-collections) 模块来了解其它的容器。

## 1.23  **getattr**(*object*, *name*) & **getattr**(*object*, *name*, *default*)

*object* 中指定名称的属性的值。 *name* 必须是字符串。 如果该字符串是对象的某一属性的名称，则结果将为该属性的值。 例如，`getattr(x, 'foobar')` 等同于 `x.foobar`。 如果指定名称的属性不存在，则如果提供了 *default* 则返回该值，否则将引发 [`AttributeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#AttributeError)。 *name* 不必是一个 Python 标识符 (参见 [`setattr()`](https://docs.python.org/zh-cn/3/library/functions.html#setattr))。

备注

由于 [私有名称混合](https://docs.python.org/zh-cn/3/reference/expressions.html#private-name-mangling) 发生在编译时，因此必须手动混合私有属性（以两个下划线打头的属性）名称以使用 [`getattr()`](https://docs.python.org/zh-cn/3/library/functions.html#getattr) 来提取它。

## 1.24 **globals**()

返回实现当前模块命名空间的字典。对于函数内的代码，这是在定义函数时设置的，无论函数在哪里被调用都保持不变。

![image-20240816165945027](./assets/image-20240816165945027.png)

## 1.25 **hasattr**(*object*, *name*)

该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 `True`，否则返回 `False`。（此功能是通过调用 `getattr(object, name)` 看是否有 [`AttributeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#AttributeError) 异常来实现的。）

## 1.26 **hash**(*object*)

返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。

备注

对于具有自定义 [`__hash__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__hash__) 方法的对象，请注意 [`hash()`](https://docs.python.org/zh-cn/3/library/functions.html#hash) 会根据宿主机的字长来截断返回值。

## 1.27 **help**() & **help**(*request*)

启动内置的帮助系统（此函数主要在交互式中使用）。如果没有实参，解释器控制台里会启动交互式帮助系统。如果实参是一个字符串，则在模块、函数、类、方法、关键字或文档主题中搜索该字符串，并在控制台上打印帮助信息。如果实参是其他任意对象，则会生成该对象的帮助页。

请注意，如果在调用 [`help()`](https://docs.python.org/zh-cn/3/library/functions.html#help) 时，目标函数的形参列表中存在斜杠（/），则意味着斜杠之前的参数只能是位置参数。详情请参阅 [有关仅限位置形参的 FAQ 条目](https://docs.python.org/zh-cn/3/faq/programming.html#faq-positional-only-arguments)。

该函数通过 [`site`](https://docs.python.org/zh-cn/3/library/site.html#module-site) 模块加入到内置命名空间。

*在 3.4 版本发生变更:* [`pydoc`](https://docs.python.org/zh-cn/3/library/pydoc.html#module-pydoc) 和 [`inspect`](https://docs.python.org/zh-cn/3/library/inspect.html#module-inspect) 的变更使得可调用对象的签名信息更加全面和一致。

## 1.28 **hex**(*x*)

将整数转换为带前缀 "0x" 前缀的小写十六进制数字符串。 如果 *x* 不是一个 Python [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 对象，则它必须定义返回一个整数的 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__) 方法。 下面是一些例子:

```
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```

如果要将整数转换为大写或小写的十六进制字符串，并可选择有无“0x”前缀，则可以使用如下方法：

\>>>

```
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```

另见 [`format()`](https://docs.python.org/zh-cn/3/library/functions.html#format) 获取更多信息。

另请参阅 [`int()`](https://docs.python.org/zh-cn/3/library/functions.html#int) 将十六进制字符串转换为以 16 为基数的整数。

备注

如果要获取浮点数的十六进制字符串形式，请使用 [`float.hex()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#float.hex) 方法。

## 1.29 **id**(*object*)

返回对象的“标识值”。该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。两个生命期不重叠的对象可能具有相同的 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 值。

**CPython 实现细节：** 这是对象在内存中的地址。

引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `builtins.id` 并附带参数 `id`。

## 1.30 **input**() & **input**(*prompt*)

如果存在 *prompt* 实参，则将其写入标准输出，末尾不带换行符。接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。当读取到 EOF 时，则触发 [`EOFError`](https://docs.python.org/zh-cn/3/library/exceptions.html#EOFError)。例如:

```
>>> s = input('--> ')  
--> Monty Python's Flying Circus
>>> s  
"Monty Python's Flying Circus"
```

如果加载了 [`readline`](https://docs.python.org/zh-cn/3/library/readline.html#module-readline) 模块，[`input()`](https://docs.python.org/zh-cn/3/library/functions.html#input) 将使用它来提供复杂的行编辑和历史记录功能。

在读取输入前引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `builtins.input` 附带参数 `prompt`

在成功读取输入之后引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `builtins.input/result` 附带结果。

## 1.31 *class* **int**(*number=0*, */*) & *class* **int**(*string*, */*, *base=10*)

返回从一个数字或字符串构建的整数对象，或者如果未给出参数则返回 `0`。

示例：

\>>>

```
>>> int(123.45)
123
>>> int('123')
123
>>> int('   -12_345\n')
-12345
>>> int('FACE', 16)
64206
>>> int('0xface', 0)
64206
>>> int('01110011', base=2)
115
```

如果参数定义了 [`__int__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__int__)，`int(x)` 将返回 `x.__int__()`。 如果参数定义了 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)，它将返回 `x.__index__()`。 如果参数定义了 [`__trunc__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__trunc__)，它将返回 `x.__trunc__()`。 对于浮点数，这将向零方向截断。

如果参数不是数字或者如果给定了 *base*，则它必须是表示一个以 *base* 为基数的整数的字符串、[`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 或 [`bytearray`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytearray) 实例。 字符串前面还可选择加上 `+` 或 `-` (中间没有空格)，带有前导的零，带有两侧的空格，以及带有数位之间的单个下划线。

一个以 n 为基数的整数字符串包含多个数位，每个数位代表从 0 到 n-1 范围内的值。 0--9 的值可以用任何 Unicode 十进制数码来表示。 10--35 的值可以用 `a` 到 `z` (或 `A` 到 `Z`) 来表示。 默认的 *base* 为 10。 允许的基数为 0 和 2--36。 对于基数 2, -8 和 -16 来说字符串前面还能加上可选的 `0b`/`0B`, `0o`/`0O` 或 `0x`/`0X` 前缀，就像代码中的整数字面值那样。 对于基数 0 来说，字符串会以与 [代码中的整数字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#integers) 类似的方式来解读，即实际的基数将由前缀确定为 2, 8, 10 或 16。 基数为 0 还会禁用前导的零: `int('010', 0)` 将是无效的，而 `int('010')` 和 `int('010', 8)` 则是有效的。

整数类型定义请参阅 [数字类型 --- int, float, complex](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesnumeric) 。

*在 3.4 版本发生变更:* 如果 *base* 不是 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 的实例，但 *base* 对象有 [`base.__index__`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__) 方法，则会调用该方法来获取进制数。以前的版本使用 [`base.__int__`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__int__) 而不是 [`base.__index__`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)。

*在 3.6 版本发生变更:* 您可以使用下划线将代码文字中的数字进行分组。

*在 3.7 版本发生变更:* 第一个形参现在是仅限位置形参。

*在 3.8 版本发生变更:* 如果 [`__int__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__int__) 未定义则回退至 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__)。

*在 3.11 版本发生变更:* 委托给 [`__trunc__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__trunc__) 的做法已被弃用。

*在 3.11 版本发生变更:* [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 字符串输入和字符串表示形式可受到限制以帮助避免拒绝服务攻击。当将一个字符串转换为 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 或者将一个 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 转换为字符串的操作走出限制时会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。 请参阅 [整数字符串转换长度限制](https://docs.python.org/zh-cn/3/library/stdtypes.html#int-max-str-digits) 文档。

## 1.32 **isinstance**(*object*, *classinfo*)

如果 *object* 参数是 *classinfo* 参数的实例，或者是其 (直接、间接或 [虚拟](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class)) 子类的实例则返回 `True`。 如果 *object* 不是给定类型的对象，则该函数总是返回 `False`。 如果 *classinfo* 是由类型对象结成的元组 (或是由其他此类元组递归生成) 或者是多个类型的 [union 类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#types-union)，则如果 *object* 是其中任一类型的实例时将会返回 `True`。 如果 *classinfo* 不是一个类型或类型元组及此类元组，则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。 如果之前的检查成功执行则可以不会为无效的类型引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。*在 3.10 版本发生变更:* *classinfo* 可以是一个 [union 类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#types-union)。

![image-20240816171024564](./assets/image-20240816171024564.png)

## 1.33 **issubclass**(*class*, *classinfo*)

如果 *class* 是 *classinfo* 的子类（直接、间接或 [虚的](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class) ），则返回 `True`。类将视为自己的子类。*classinfo* 可为类对象的元组（或递归地，其他这样的元组）或 [union 类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#types-union)，这时如果 *class* 是 *classinfo* 中任何条目的子类，则返回 `True` 。任何其他情况都会触发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。*在 3.10 版本发生变更:* *classinfo* 可以是一个 [union 类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#types-union)。

## 1.34 **iter**(*object*) & **iter**(*object*, *sentinel*) 还需再了解了解

返回一个 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator) 对象。 根据是否存在第二个参数，对第一个参数的解读会有很大的不同。 如果没有第二个参数，*object* 必须是一个支持 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable) 协议 (有 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法) 的多项集对象，或者必须支持序列协议 (有 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 方法并使用从 `0` 开始的整数参数)。 如果它不支持这些协议，则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。 如果给出了第二个参数 *sentinel*，则 *object* 必须是一个可调用对象。 在这种情况下创建的迭代器将针对每次调用其 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法不带参数地调用 *object*；如果返回的值等于 *sentinel*，则会引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration)，否则将返回该值。另请参阅 [迭代器类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#typeiter)。适合 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 的第二种形式的应用之一是构建块读取器。 例如，从二进制数据库文件中读取固定宽度的块，直至到达文件的末尾:`from functools import partial with open('mydata.db', 'rb') as f:    for block in iter(partial(f.read, 64), b''):        process_block(block) `

## 1.35 **len**(*s*)

返回对象的长度（元素个数）。实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。**CPython 实现细节：** `len` 对于大于 [`sys.maxsize`](https://docs.python.org/zh-cn/3/library/sys.html#sys.maxsize) 的长度如 [`range(2 ** 100)`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 会引发 [`OverflowError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OverflowError)。

## 1.36 *class* **list** & *class* **list**(*iterable*)

虽然被称为函数，[`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) 实际上是一种可变序列类型，详情请参阅 [列表](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-list) 和 [序列类型 --- list, tuple, range](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq)。

## 1.37 **locals**()

Update and return a dictionary representing the current local symbol table. Free variables are returned by [`locals()`](https://docs.python.org/zh-cn/3/library/functions.html#locals) when it is called in function blocks, but not in class blocks. Note that at the module level, [`locals()`](https://docs.python.org/zh-cn/3/library/functions.html#locals) and [`globals()`](https://docs.python.org/zh-cn/3/library/functions.html#globals) are the same dictionary.备注 The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.

> 更新并返回表示当前本地符号表的字典。当在函数块中调用自由变量时，locals（）会返回自由变量，但在类块中不会返回。请注意，在模块级别，locals（） 和 globals（） 是同一个字典。
>
> 备注 此字典的内容不应被修改;
>
> 更改可能不会影响解释器使用的局部变量和自由变量的值。

- **map**(*function*, *iterable*, **iterables*)

    返回一个将 *function* 应用于 *iterable* 的每一项，并产生其结果的迭代器。 如果传入了额外的 *iterables* 参数，则 *function* 必须接受相同个数的参数并被用于到从所有可迭代对象中并行获取的项。 当有多个可迭代对象时，当最短的可迭代对象耗尽则整个迭代将会停止。 对于函数的输入已经是参数元组的情况，请参阅 [`itertools.starmap()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.starmap)。

- **max**(*iterable*, ***, *key=None*)

- **max**(*iterable*, ***, *default*, *key=None*)

- **max**(*arg1*, *arg2*, **args*, *key=None*)

    返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。如果只提供了一个位置参数，它必须是非空 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable)，返回可迭代对象中最大的元素；如果提供了两个及以上的位置参数，则返回最大的位置参数。有两个可选只能用关键字的实参。*key* 实参指定排序函数用的参数，如传给 [`list.sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort) 的。*default* 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 *default* ，则会触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。如果有多个最大元素，则此函数将返回第一个找到的。这和其他稳定排序工具如 `sorted(iterable, key=keyfunc, reverse=True)[0]` 和 `heapq.nlargest(1, iterable, key=keyfunc)` 保持一致。*在 3.4 版本发生变更:* 增加了 *default* 仅限关键字形参。*在 3.8 版本发生变更:* *key* 可以为 `None`。

- *class* **memoryview**(*object*)

    返回由给定实参创建的“内存视图”对象。有关详细信息，请参阅 [内存视图](https://docs.python.org/zh-cn/3/library/stdtypes.html#typememoryview)。

- **min**(*iterable*, ***, *key=None*)

- **min**(*iterable*, ***, *default*, *key=None*)

- **min**(*arg1*, *arg2*, **args*, *key=None*)

    返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。如果只提供了一个位置参数，它必须是 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable)，返回可迭代对象中最小的元素；如果提供了两个及以上的位置参数，则返回最小的位置参数。有两个可选只能用关键字的实参。*key* 实参指定排序函数用的参数，如传给 [`list.sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort) 的。*default* 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 *default* ，则会触发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。如果有多个最小元素，则此函数将返回第一个找到的。这和其他稳定排序工具如 `sorted(iterable, key=keyfunc)[0]` 和 `heapq.nsmallest(1, iterable, key=keyfunc)` 保持一致。*在 3.4 版本发生变更:* 增加了 *default* 仅限关键字形参。*在 3.8 版本发生变更:* *key* 可以为 `None`。

- **next**(*iterator*)

- **next**(*iterator*, *default*)

    通过调用 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator) 的 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法获取下一个元素。如果迭代器耗尽，则返回给定的 *default*，如果没有默认值则触发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration)。

- *class* **object**

    返回一个不带特征的新对象。[`object`](https://docs.python.org/zh-cn/3/library/functions.html#object) 是所有类的基类。它带有所有 Python 类实例均通用的方法。本函数不接受任何参数。备注 由于 [`object`](https://docs.python.org/zh-cn/3/library/functions.html#object) 没有 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__)，因此无法将任意属性赋给 [`object`](https://docs.python.org/zh-cn/3/library/functions.html#object) 的实例。

- **oct**(*x*)

    将整数转换为带前缀 "0o" 的八进制数字符串。 结果是一个合法的 Python 表达式。 如果 *x* 不是一个 Python [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 对象，则它必须定义返回一个整数的 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__) 方法。 例如:>>>`>>> oct(8) '0o10' >>> oct(-56) '-0o70' `若要将整数转换为八进制字符串，并可选择是否带有“0o”前缀，可采用如下方法：>>>`>>> '%#o' % 10, '%o' % 10 ('0o12', '12') >>> format(10, '#o'), format(10, 'o') ('0o12', '12') >>> f'{10:#o}', f'{10:o}' ('0o12', '12') `另见 [`format()`](https://docs.python.org/zh-cn/3/library/functions.html#format) 获取更多信息。

- **open**(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)

    打开 *file* 并返回对应的 [file object](https://docs.python.org/zh-cn/3/glossary.html#term-file-object)。 如果该文件不能被打开，则引发 [`OSError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError)。 请参阅 [读写文件](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#tut-files) 获取此函数的更多用法示例。*file* 是一个 [path-like object](https://docs.python.org/zh-cn/3/glossary.html#term-path-like-object)，表示将要打开的文件的路径（绝对路径或者相对当前工作目录的路径），也可以是要封装文件对应的整数类型文件描述符。（如果给出的是文件描述符，则当返回的 I/O 对象关闭时它也会关闭，除非将 *closefd* 设为 `False` 。）*mode* 是一个指明文件打开模式的可选字符串。 它默认为 `'r'` 表示以文本模式读取。 其他常见模式有表示写入的 `'w'` (若文件已存在则将其清空)，表示独占创建的 `'x'`，以及表示追加写入的 `'a'` (在 *某些* Unix 系统上，这意味着无论当前查找位置在哪里 *所有* 写入操作都将追加到文件末尾)。 在文本模式下，如果未指定 *encoding* 则所使用的编码格式将依赖于具体平台: [`locale.getencoding()`](https://docs.python.org/zh-cn/3/library/locale.html#locale.getencoding) 会被调用以获取当前语言区域的编码格式。 (对于读取和写入原始字节数据请使用二进制模式并且不要指定 *encoding*。) 可用的模式有:字符含意`'r'`读取（默认）`'w'`写入，并先截断文件`'x'`排它性创建，如果文件已存在则失败`'a'`打开文件用于写入，如果文件存在则在末尾追加`'b'`二进制模式`'t'`文本模式（默认）`'+'`打开用于更新（读取与写入）默认模式为 `'r'` （打开文件用于读取文本，与 `'rt'` 同义）。`'w+'` 和 `'w+b'` 模式将打开文件并清空内容。而 `'r+'` 和 `'r+b'` 模式将打开文件但不清空内容。正如在 [概述](https://docs.python.org/zh-cn/3/library/io.html#io-overview) 中提到的，Python区分二进制和文本I/O。以二进制模式打开的文件（包括 *mode* 参数中的 `'b'` ）返回的内容为 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 对象，不进行任何解码。在文本模式下（默认情况下，或者在 *mode* 参数中包含 `'t'` ）时，文件内容返回为 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) ，首先使用指定的 *encoding* （如果给定）或者使用平台默认的的字节编码解码。备注 Python不依赖于底层操作系统的文本文件概念;所有处理都由Python本身完成，因此与平台无关。*buffering* 是一个可选的整数，用于设置缓冲策略。 传入 0 来关闭缓冲（仅在二进制模式下允许），传入 1 来选择行缓冲（仅在文本模式下写入时可用），传一个整数 > 1 来表示固定大小的块缓冲区的字节大小。 注意这样指定缓冲区的大小适用于二进制缓冲的 I/O,但 `TextIOWrapper` (即用 `mode='r+'` 打开的文件) 会有另一种缓冲。 要禁用 `TextIOWrapper` 中的缓冲，请考虑为 [`io.TextIOWrapper.reconfigure()`](https://docs.python.org/zh-cn/3/library/io.html#io.TextIOWrapper.reconfigure) 使用 `write_through` 旗标。 当没有给出 *buffering* 参数时，默认的缓冲策略规则如下:二进制文件以固定大小的块进行缓冲；缓冲区的大小是使用启发方式来尝试确定底层设备的“块大小”并会回退至 [`io.DEFAULT_BUFFER_SIZE`](https://docs.python.org/zh-cn/3/library/io.html#io.DEFAULT_BUFFER_SIZE)。 在许多系统上，缓冲区的长度通常为 4096 或 8192 字节。“交互式”文本文件（ [`isatty()`](https://docs.python.org/zh-cn/3/library/io.html#io.IOBase.isatty) 返回 `True` 的文件）使用行缓冲。其他文本文件使用上述策略用于二进制文件。*encoding* 是用于编码或编码文件的编码格式名称。 这应当只有文本模式下使用。 默认的编码格式依赖于具体平台 (即 [`locale.getencoding()`](https://docs.python.org/zh-cn/3/library/locale.html#locale.getencoding) 所返回的值)，但是任何 Python 支持的 [text encoding](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding) 都可以被使用。 请参阅 [`codecs`](https://docs.python.org/zh-cn/3/library/codecs.html#module-codecs) 模块获取受支持的编码格式列表。*errors* 是一个可选的字符串参数，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。可以使用各种标准错误处理程序（列在 [错误处理方案](https://docs.python.org/zh-cn/3/library/codecs.html#error-handlers) ），但是使用 [`codecs.register_error()`](https://docs.python.org/zh-cn/3/library/codecs.html#codecs.register_error) 注册的任何错误处理名称也是有效的。标准名称包括:如果存在编码错误，`'strict'` 会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) 异常。 默认值 `None` 具有相同的效果。`'ignore'` 忽略错误。请注意，忽略编码错误可能会导致数据丢失。`'replace'` 会将替换标记（例如 `'?'` ）插入有错误数据的地方。`'surrogateescape'` 将把任何不正确的字节表示为 U+DC80 至 U+DCFF 范围内的下方替代码位。 当在写入数据时使用 `surrogateescape` 错误处理器时这些替代码位会被转回到相同的字节。 这适用于处理具有未知编码格式的文件。`'xmlcharrefreplace'` 仅在写入文件时才受到支持。 编码格式不支持的字符将被替换为相应的 XML 字符引用 `&#*nnn*;`。`'backslashreplace'` 用Python的反向转义序列替换格式错误的数据。`'namereplace'` （也只在编写时支持）用 `\N{...}` 转义序列替换不支持的字符。*newline* 决定如何解析来自流的换行符。 它可以为 `None`, `''`, `'\n'`, `'\r'` 和 `'\r\n'`。 它的工作原理如下:从流中读取输入时，如果 *newline* 为 `None`，则启用通用换行模式。输入中的行可以以 `'\n'`，`'\r'` 或 `'\r\n'` 结尾，这些行被翻译成 `'\n'` 在返回呼叫者之前。如果它是 `''`，则启用通用换行模式，但行结尾将返回给调用者未翻译。如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。将输出写入流时，如果 *newline* 为 `None`，则写入的任何 `'\n'` 字符都将转换为系统默认行分隔符 [`os.linesep`](https://docs.python.org/zh-cn/3/library/os.html#os.linesep)。如果 *newline* 是 `''` 或 `'\n'`，则不进行翻译。如果 *newline* 是任何其他合法值，则写入的任何 `'\n'` 字符将被转换为给定的字符串。如果 *closefd* 为 `False` 且给出的不是文件名而是文件描述符，那么当文件关闭时，底层文件描述符将保持打开状态。如果给出的是文件名，则 *closefd* 必须为 `True` （默认值），否则将触发错误。可以通过传递可调用的 *opener* 来使用自定义开启器。然后通过使用参数（ *file*，*flags* ）调用 *opener* 获得文件对象的基础文件描述符。 *opener* 必须返回一个打开的文件描述符（使用 [`os.open`](https://docs.python.org/zh-cn/3/library/os.html#os.open) as *opener* 时与传递 `None` 的效果相同）。新创建的文件是 [不可继承的](https://docs.python.org/zh-cn/3/library/os.html#fd-inheritance)。下面的示例使用 [`os.open()`](https://docs.python.org/zh-cn/3/library/os.html#os.open) 函数的 [dir_fd](https://docs.python.org/zh-cn/3/library/os.html#dir-fd) 的形参，从给定的目录中用相对路径打开文件:>>>`>>> import os >>> dir_fd = os.open('somedir', os.O_RDONLY) >>> def opener(path, flags): ...     return os.open(path, flags, dir_fd=dir_fd) ... >>> with open('spamspam.txt', 'w', opener=opener) as f: ...     print('This will be written to somedir/spamspam.txt', file=f) ... >>> os.close(dir_fd)  # don't leak a file descriptor `[`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open) 函数所返回的 [file object](https://docs.python.org/zh-cn/3/glossary.html#term-file-object) 类型取决于所用模式。 当使用 [`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open) 以文本模式 (`'w'`, `'r'`, `'wt'`, `'rt'` 等) 打开文件时，它将返回 [`io.TextIOBase`](https://docs.python.org/zh-cn/3/library/io.html#io.TextIOBase) (具体为 [`io.TextIOWrapper`](https://docs.python.org/zh-cn/3/library/io.html#io.TextIOWrapper)) 的一个子类。 当使用缓冲以二进制模式打开文件时，返回的类是 [`io.BufferedIOBase`](https://docs.python.org/zh-cn/3/library/io.html#io.BufferedIOBase) 的一个子类。 具体的类会有多种：在只读的二进制模式下，它将返回 [`io.BufferedReader`](https://docs.python.org/zh-cn/3/library/io.html#io.BufferedReader)；在写入二进制和追加二进制模式下，它将返回 [`io.BufferedWriter`](https://docs.python.org/zh-cn/3/library/io.html#io.BufferedWriter)，而在读/写模式下，它将返回 [`io.BufferedRandom`](https://docs.python.org/zh-cn/3/library/io.html#io.BufferedRandom)。 当禁用缓冲时，则会返回原始流，即 [`io.RawIOBase`](https://docs.python.org/zh-cn/3/library/io.html#io.RawIOBase) 的一个子类 [`io.FileIO`](https://docs.python.org/zh-cn/3/library/io.html#io.FileIO)。另请参阅文件操作模块，如 [`fileinput`](https://docs.python.org/zh-cn/3/library/fileinput.html#module-fileinput)、[`io`](https://docs.python.org/zh-cn/3/library/io.html#module-io) （声明了 [`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open)）、[`os`](https://docs.python.org/zh-cn/3/library/os.html#module-os)、[`os.path`](https://docs.python.org/zh-cn/3/library/os.path.html#module-os.path)、[`tempfile`](https://docs.python.org/zh-cn/3/library/tempfile.html#module-tempfile) 和 [`shutil`](https://docs.python.org/zh-cn/3/library/shutil.html#module-shutil)。引发一个 [审计事件](https://docs.python.org/zh-cn/3/library/sys.html#auditing) `open` 并附带参数 `path`, `mode`, `flags`。`mode` 与 `flags` 参数可以在原始调用的基础上被修改或传递。*在 3.3 版本发生变更:*增加了 *opener* 形参。增加了 `'x'` 模式。过去触发的 [`IOError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IOError)，现在是 [`OSError`](https://docs.python.org/zh-cn/3/library/exceptions.html#OSError) 的别名。如果文件已存在但使用了排它性创建模式（ `'x'` ），现在会触发 [`FileExistsError`](https://docs.python.org/zh-cn/3/library/exceptions.html#FileExistsError)。*在 3.4 版本发生变更:*文件现在禁止继承。*在 3.5 版本发生变更:*如果系统调用被中断，但信号处理程序没有触发异常，此函数现在会重试系统调用，而不是触发 [`InterruptedError`](https://docs.python.org/zh-cn/3/library/exceptions.html#InterruptedError) 异常 (原因详见 [**PEP 475**](https://peps.python.org/pep-0475/))。增加了 `'namereplace'` 错误处理接口。*在 3.6 版本发生变更:*增加对实现了 [`os.PathLike`](https://docs.python.org/zh-cn/3/library/os.html#os.PathLike) 对象的支持。在 Windows 上，打开一个控制台缓冲区将返回 [`io.RawIOBase`](https://docs.python.org/zh-cn/3/library/io.html#io.RawIOBase) 的子类，而不是 [`io.FileIO`](https://docs.python.org/zh-cn/3/library/io.html#io.FileIO)。*在 3.11 版本发生变更:* `'U'` 模式已被移除。

- **ord**(*c*)

    对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。例如 `ord('a')` 返回整数 `97`， `ord('€')` （欧元符号）返回 `8364` 。这是 [`chr()`](https://docs.python.org/zh-cn/3/library/functions.html#chr) 的逆函数。

- **pow**(*base*, *exp*, *mod=None*)

    返回 *base* 的 *exp* 次幂；如果 *mod* 存在，则返回 *base* 的 *exp* 次幂对 *mod* 取余（比 `pow(base, exp) % mod` 更高效）。 两参数形式 `pow(base, exp)` 等价于乘方运算符: `base**exp`。这些参数必须为数字类型。 对于混用的操作数类型，将应用二元算术运算的强制转换规则。 对于 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 操作数，结果具有与操作数相同的类型（转换之后）除非第二个参数为负值；在那种情况下，所有参数将被转换为浮点数并输出浮点数的结果。 例如，`pow(10, 2)` 返回 `100`，而 `pow(10, -2)` 返回 `0.01`。 对于 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 或 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float) 类型的基数为负值而幂为非整数的情况，将产生一个复数的结果。 例如，`pow(-9, 0.5)` 将返回一个接近 `3j` 的值。 最后，对于 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 或 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float) 类型的基数为负值而幂为整数的情况，将产生一个浮点数的结果。 例如，`pow(-9, 2.0)` 将返回 `81.0`。对于 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 操作数 *base* 和 *exp*，如果给出 *mod*，则 *mod* 必须为整数类型并且 *mod* 必须不为零。 如果给出 *mod* 并且 *exp* 为负值，则 *base* 必须相对于 *mod* 不可整除。 在这种情况下，将会返回 `pow(inv_base, -exp, mod)`，其中 *inv_base* 为 *base* 的倒数对 *mod* 取余。下面的例子是 `38` 的倒数对 `97` 取余:>>>`>>> pow(38, -1, mod=97) 23 >>> 23 * 38 % 97 == 1 True `*在 3.8 版本发生变更:* 对于 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 操作数，三参数形式的 `pow` 现在允许第二个参数为负值，即可以计算倒数的余数。*在 3.8 版本发生变更:* 允许关键字参数。 之前只支持位置参数。

- **print**(**objects*, *sep=' '*, *end='\n'*, *file=None*, *flush=False*)

    将 *objects* 打印输出至 *file* 指定的文本流，以 *sep* 分隔并在末尾加上 *end*。 *sep* 、 *end* 、 *file* 和 *flush* 必须以关键字参数的形式给出。所有非关键字参数都会被转换为字符串，就像是执行了 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 一样，并会被写入到流，以 *sep* 分隔并在末尾加上 *end*。 *sep* 和 *end* 都必须为字符串；它们也可以为 `None`，这意味着使用默认值。 如果没有给出 *objects*，则 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print) 将只写入 *end*。*file* 参数必须是一个具有 `write(string)` 方法的对象；如果参数不存在或为 `None`，则将使用 [`sys.stdout`](https://docs.python.org/zh-cn/3/library/sys.html#sys.stdout)。 由于要打印的参数会被转换为文本字符串，因此 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print) 不能用于二进制模式的文件对象。 对于这些对象，应改用 `file.write(...)`。输出缓冲通常由 *file* 确定。 但是，如果 *flush* 为真值，流将被强制刷新。*在 3.3 版本发生变更:* 增加了 *flush* 关键字参数。

- *class* **property**(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)

    返回 property 属性。*fget* 是获取属性值的函数。 *fset* 是用于设置属性值的函数。 *fdel* 是用于删除属性值的函数。并且 *doc* 为属性对象创建文档字符串。一个典型的用法是定义一个托管属性 `x`:`class C:    def __init__(self):        self._x = None     def getx(self):        return self._x     def setx(self, value):        self._x = value     def delx(self):        del self._x     x = property(getx, setx, delx, "I'm the 'x' property.") `如果 *c* 为 *C* 的实例，`c.x` 将调用 getter，`c.x = value` 将调用 setter， `del c.x` 将调用 deleter。如果给出，*doc* 将成为该 property 属性的文档字符串。 否则该 property 将拷贝 *fget* 的文档字符串（如果存在）。 这令使用 [`property()`](https://docs.python.org/zh-cn/3/library/functions.html#property) 作为 [decorator](https://docs.python.org/zh-cn/3/glossary.html#term-decorator) 来创建只读的特征属性可以很容易地实现:`class Parrot:    def __init__(self):        self._voltage = 100000     @property    def voltage(self):        """Get the current voltage."""        return self._voltage ``@property` 装饰器会将 `voltage()` 方法转化为一个具有相同名称的只读属性 "getter"，并将 *voltage* 的文档字符串设为 "Get the current voltage."@**getter**@**setter**@**deleter**特征属性对象具有 `getter`, `setter` 和 `deleter` 方法，它们可用作装饰器来创建该特征属性的副本，并将相应的访问函数设为所装饰的函数。 这最好是用一个例子来说明：`class C:    def __init__(self):        self._x = None     @property    def x(self):        """I'm the 'x' property."""        return self._x     @x.setter    def x(self, value):        self._x = value     @x.deleter    def x(self):        del self._x `上述代码与第一个例子完全等价。 注意一定要给附加函数与原始的特征属性相同的名称 (在本例中为 `x`。)返回的特征属性对象同样具有与构造器参数相对应的属性 `fget`, `fset` 和 `fdel`。*在 3.5 版本发生变更:* 特征属性对象的文档字符串现在是可写的。

- *class* **range**(*stop*)

- *class* **range**(*start*, *stop*, *step=1*)

    虽然被称为函数，但 [`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 实际上是一个不可变的序列类型，参见在 [range 对象](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-range) 与 [序列类型 --- list, tuple, range](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq) 中的文档说明。

- **repr**(*object*)

    返回包含一个对象的可打印表示形式的字符串。 对于许多类型而言，此函数会尝试返回一个具有与传给 [`eval()`](https://docs.python.org/zh-cn/3/library/functions.html#eval) 时相同的值的字符串；在其他情况下，其表示形式将为一个包含对象类型名称和通常包括对象名称和地址的额外信息的用尖括号括起来的字符串。 一个类可以通过定义 [`__repr__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__repr__) 方法来控制此函数为其实例所返回的内容。 如果 [`sys.displayhook()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.displayhook) 不可访问，则此函数将会引发 [`RuntimeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#RuntimeError)。该类具有自定义的表示形式，它可被求值为:`class Person:   def __init__(self, name, age):      self.name = name      self.age = age    def __repr__(self):      return f"Person('{self.name}', {self.age})" `

- **reversed**(*seq*)

    返回一个反向的 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)。 *seq* 必须是一个具有 [`__reversed__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__reversed__) 方法或是支持序列协议（具有 [`__len__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__len__) 方法和从 `0` 开始的整数参数的 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 方法）的对象。

- **round**(*number*, *ndigits=None*)

    返回 *number* 舍入到小数点后 *ndigits* 位精度的值。 如果 *ndigits* 被省略或为 `None`，则返回最接近输入值的整数。对于支持 [`round()`](https://docs.python.org/zh-cn/3/library/functions.html#round) 方法的内置类型，结果值会舍入至最接近的 10 的负 *ndigits* 次幂的倍数；如果与两个倍数同样接近，则选用偶数。因此，`round(0.5)` 和 `round(-0.5)` 均得出 `0` 而 `round(1.5)` 则为 `2`。*ndigits* 可为任意整数值（正数、零或负数）。如果省略了 *ndigits* 或为 `None` ，则返回值将为整数。否则返回值与 *number* 的类型相同。对于一般的 Python 对象 `number`, `round` 将委托给 `number.__round__`。备注 对浮点数执行 [`round()`](https://docs.python.org/zh-cn/3/library/functions.html#round) 的行为可能会令人惊讶：例如，`round(2.675, 2)` 将给出 `2.67` 而不是期望的 `2.68`。 这不算是程序错误：这一结果是由于大多数十进制小数实际上都不能以浮点数精确地表示。 请参阅 [浮点算术：争议和限制](https://docs.python.org/zh-cn/3/tutorial/floatingpoint.html#tut-fp-issues) 了解更多信息。

- *class* **set**

- *class* **set**(*iterable*)

    返回一个新的 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 对象，可以选择带有从 *iterable* 获取的元素。 `set` 是一个内置类型。 请查看 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 和 [集合类型 --- set, frozenset](https://docs.python.org/zh-cn/3/library/stdtypes.html#types-set) 获取关于这个类的文档。有关其他容器请参看内置的 [`frozenset`](https://docs.python.org/zh-cn/3/library/stdtypes.html#frozenset), [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list), [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 和 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 类，以及 [`collections`](https://docs.python.org/zh-cn/3/library/collections.html#module-collections) 模块。

- **setattr**(*object*, *name*, *value*)

    本函数与 [`getattr()`](https://docs.python.org/zh-cn/3/library/functions.html#getattr) 相对应。其参数为一个对象、一个字符串和一个任意值。字符串可以为某现有属性的名称，或为新属性。只要对象允许，函数会将值赋给属性。如 `setattr(x, 'foobar', 123)` 等价于 `x.foobar = 123`。*name* 无需为在 [标识符和关键字](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#identifiers) 中定义的 Python 标识符除非对象选择强制这样做，例如在一个自定义的 [`__getattribute__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getattribute__) 中或是通过 [`__slots__`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__slots__)。 一个名称不为标识符的属性将不可使用点号标记来访问，但是可以通过 [`getattr()`](https://docs.python.org/zh-cn/3/library/functions.html#getattr) 等来访问。备注 由于 [私有名称混合](https://docs.python.org/zh-cn/3/reference/expressions.html#private-name-mangling) 发生在编译时，因此必须手动混合私有属性（以两个下划线打头的属性）名称以便使用 [`setattr()`](https://docs.python.org/zh-cn/3/library/functions.html#setattr) 来设置它。

- *class* **slice**(*stop*)

- *class* **slice**(*start*, *stop*, *step=None*)

    返回一个表示由 `range(start, stop, step)` 指定的索引集的 [slice](https://docs.python.org/zh-cn/3/glossary.html#term-slice) 对象。 *start* 和 *step* 参数默认为 `None`。**start****stop****step**切片对象具有只读的数据属性 `start`, `stop` 和 `step`，它们将简单地返回相应的参数值（或其默认值）。 它们没有其他显式的功能；但是，它们会被 NumPy 和其他第三方包所使用。当使用扩展索引语法时也会生成切片对象。 例如: `a[start:stop:step]` 或 `a[start:stop, i]`。 请参阅 [`itertools.islice()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.islice) 了解返回 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator) 的替代版本。*在 3.12 版本发生变更:* Slice 对象现在将为 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) (如果 [`start`](https://docs.python.org/zh-cn/3/library/functions.html#slice.start), [`stop`](https://docs.python.org/zh-cn/3/library/functions.html#slice.stop) 和 [`step`](https://docs.python.org/zh-cn/3/library/functions.html#slice.step) 均为可哈希对象)。

- **sorted**(*iterable*, */*, ***, *key=None*, *reverse=False*)

    根据 *iterable* 中的项返回一个新的已排序列表。具有两个可选参数，它们都必须指定为关键字参数。*key* 指定带有单个参数的函数，用于从 *iterable* 的每个元素中提取用于比较的键 (例如 `key=str.lower`)。 默认值为 `None` (直接比较元素)。*reverse* 为一个布尔值。 如果设为 `True`，则每个列表元素将按反向顺序比较进行排序。使用 [`functools.cmp_to_key()`](https://docs.python.org/zh-cn/3/library/functools.html#functools.cmp_to_key) 可将老式的 *cmp* 函数转换为 *key* 函数。内置的 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再按薪级排序）。排序算法只使用 `<` 在项目之间比较。 虽然定义一个 [`__lt__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__lt__) 方法就足以进行排序，但 [**PEP 8**](https://peps.python.org/pep-0008/) 建议实现所有六个 [富比较](https://docs.python.org/zh-cn/3/reference/expressions.html#comparisons) 。 这将有助于避免在与其他排序工具（如 [`max()`](https://docs.python.org/zh-cn/3/library/functions.html#max) ）使用相同的数据时出现错误，这些工具依赖于不同的底层方法。实现所有六个比较也有助于避免混合类型比较的混乱，因为混合类型比较可以调用反射到 [`__gt__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__gt__) 的方法。有关排序示例和简要排序教程，请参阅 [排序的技术](https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto) 。

- @**staticmethod**

    将方法转换为静态方法。静态方法不会接收隐式的第一个参数。要声明一个静态方法，请使用此语法`class C:    @staticmethod    def f(arg1, arg2, argN): ... ``@staticmethod` 这样的形式称为函数的 [decorator](https://docs.python.org/zh-cn/3/glossary.html#term-decorator) -- 详情参阅 [函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function)。静态方式既可以在类上调用 (如 `C.f()`)，也可以在实例上调用 (如 `C().f()`)。 此外，静态方法 [descriptor](https://docs.python.org/zh-cn/3/glossary.html#term-descriptor) 也属于可调用对象，因而它们可以在类定义中使用 (如 `f()`)。Python 的静态方法与 Java 或 C++ 类似。另请参阅 [`classmethod()`](https://docs.python.org/zh-cn/3/library/functions.html#classmethod) ，可用于创建另一种类构造函数。像所有装饰器一样，也可以像常规函数一样调用 `staticmethod` ，并对其结果执行某些操作。比如某些情况下需要从类主体引用函数并且您希望避免自动转换为实例方法。对于这些情况，请使用此语法:`def regular_function():    ... class C:    method = staticmethod(regular_function) `想了解更多有关静态方法的信息，请参阅 [标准类型层级结构](https://docs.python.org/zh-cn/3/reference/datamodel.html#types) 。*在 3.10 版本发生变更:* 静态方法继承了方法的多个属性（ `__module__`、 `__name__`、 `__qualname__`、 `__doc__` 和 `__annotations__`），还拥有一个新的 `__wrapped__` 属性，并且现在还可以作为普通函数进行调用。

- *class* **str**(*object=''*)

- *class* **str**(*object=b''*, *encoding='utf-8'*, *errors='strict'*)

    返回一个 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 版本的 *object* 。有关详细信息，请参阅 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 。`str` 是内置字符串 [class](https://docs.python.org/zh-cn/3/glossary.html#term-class) 。更多关于字符串的信息查看 [文本序列类型 --- str](https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq)。

- **sum**(*iterable*, */*, *start=0*)

    从 *start* 开始自左向右对 *iterable* 的项求和并返回总计值。 *iterable* 的项通常为数字，而 start 值则不允许为字符串。对于某些用例，存在 [`sum()`](https://docs.python.org/zh-cn/3/library/functions.html#sum) 的更好替代。 拼接字符串序列的更好、更快的方式是调用 `''.join(sequence)`。 要以扩展的精度执行浮点数值的求和，请参阅 [`math.fsum()`](https://docs.python.org/zh-cn/3/library/math.html#math.fsum)。 要拼接一系列可迭代对象，请考虑使用 [`itertools.chain()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.chain)。*在 3.8 版本发生变更:* *start* 形参可用关键字参数形式来指定。*在 3.12 版本发生变更:* Summation of floats switched to an algorithm that gives higher accuracy on most builds.

- *class* **super**

- *class* **super**(*type*, *object_or_type=None*)

    返回一个代理对象，它会将方法调用委托给 *type* 的父类或兄弟类。 这对于访问已在类中被重写的继承方法很有用。*object_or_type* 确定要用于搜索的 [method resolution order](https://docs.python.org/zh-cn/3/glossary.html#term-method-resolution-order)。 搜索会从 *type* 之后的类开始。举例来说，如果 *object_or_type* 的 [`__mro__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#class.__mro__) 为 `D -> B -> C -> A -> object` 并且 *type* 的值为 `B`，则 [`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 将会搜索 `C -> A -> object`。*object_or_type* 的 [`__mro__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#class.__mro__) 属性列出了 [`getattr()`](https://docs.python.org/zh-cn/3/library/functions.html#getattr) 和 [`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 所共同使用的方法解析搜索顺序。 该属性是动态的并可在任何继承层级结构发生更新时被改变。如果省略第二个参数，则返回的超类对象是未绑定的。 如果第二个参数为一个对象，则 `isinstance(obj, type)` 必须为真值。 如果第二个参数为一个类型，则 `issubclass(type2, type)` 必须为真值（这适用于类方法）。*super* 有两个典型用例。 在具有单继承的类层级结构中，*super* 可用来引用父类而不必显式地指定它们的名称，从而令代码更易维护。 这种用法与其他编程语言中 *super* 的用法非常相似。第二个用例是在动态执行环境中支持协作多重继承。 此用例为 Python 所独有而不存在于静态编码语言或仅支持单继承的语言当中。 这使用实现“菱形图”成为可能，即有多个基类实现相同的方法。 好的设计强制要求这样的方法在每个情况下都具有相同的调用签名（因为调用顺序是在运行时确定的，也因为这个顺序要适应类层级结构的更改，还因为这个顺序可能包括在运行时之前未知的兄弟类）。对于以上两个用例，典型的超类调用看起来是这样的:`class C(B):    def method(self, arg):        super().method(arg)    # This does the same thing as:                               # super(C, self).method(arg) `除了方法查找之外，[`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 也可用于属性查找。 一个可能的应用场合是在上级或同级类中调用 [描述器](https://docs.python.org/zh-cn/3/glossary.html#term-descriptor)。请注意 [`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 被实现为为显式的带点号属性查找的绑定过程的组成部分，例如 `super().__getitem__(name)`。 它做到这一点是通过实现自己的 [`__getattribute__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getattribute__) 方法以便能够按支持协作多重继承的可预测的顺序来搜索类。 相应地，[`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 在像 `super()[name]` 这样使用语句或运算符进行隐式查找时则是未定义的。还要注意的是，除了零个参数的形式以外，[`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 并不限于在方法内部使用。 两个参数的形式明确指定参数并进行相应的引用。 零个参数的形式仅适用于类定义内部，因为编译器需要填入必要的细节以正确地检索到被定义的类，还需要让普通方法访问当前实例。对于有关如何使用 [`super()`](https://docs.python.org/zh-cn/3/library/functions.html#super) 来如何设计协作类的实用建议，请参阅 [使用 super() 的指南](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)。

- *class* **tuple**

- *class* **tuple**(*iterable*)

    虽然被称为函数，但 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 实际上是一个不可变的序列类型，参见在 [元组](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-tuple) 与 [序列类型 --- list, tuple, range](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq) 中的文档说明。

- *class* **type**(*object*)

- *class* **type**(*name*, *bases*, *dict*, ***kwds*)

    传入一个参数时，返回 *object* 的类型。 返回值是一个 type 对象，通常与 [`object.__class__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#instance.__class__) 所返回的对象相同。推荐使用 [`isinstance()`](https://docs.python.org/zh-cn/3/library/functions.html#isinstance) 内置函数来检测对象的类型，因为它会考虑子类的情况。传入三个参数时，返回一个新的 type 对象。 这在本质上是 [`class`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#class) 语句的一种动态形式，*name* 字符串即类名并会成为 [`__name__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#definition.__name__) 属性；*bases* 元组包含基类并会成为 [`__bases__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#class.__bases__) 属性；如果为空则会添加所有类的终极基类 [`object`](https://docs.python.org/zh-cn/3/library/functions.html#object)。 *dict* 字典包含类主体的属性和方法定义；它在成为 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性之前可能会被拷贝或包装。 下面两条语句会创建相同的 [`type`](https://docs.python.org/zh-cn/3/library/functions.html#type) 对象:>>>`>>> class X: ...     a = 1 ... >>> X = type('X', (), dict(a=1)) `另请参阅 [类型对象](https://docs.python.org/zh-cn/3/library/stdtypes.html#bltin-type-objects)。提供给三参数形式的关键字参数会被传递给适当的元类机制 (通常为 [`__init_subclass__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init_subclass__))，相当于类定义中关键字 (除了 *metaclass*) 的行为方式。另请参阅 [自定义类创建](https://docs.python.org/zh-cn/3/reference/datamodel.html#class-customization)。*在 3.6 版本发生变更:* [`type`](https://docs.python.org/zh-cn/3/library/functions.html#type) 的子类如果未重载 `type.__new__`，将不再能使用一个参数的形式来获取对象的类型。

- **vars**()

- **vars**(*object*)

    返回模块、类、实例或任何其它具有 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性的对象的 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性。模块和实例这样的对象具有可更新的 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性；但是，其它对象的 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性可能会设为限制写入（例如，类会使用 [`types.MappingProxyType`](https://docs.python.org/zh-cn/3/library/types.html#types.MappingProxyType) 来防止直接更新字典）。不带参数时，[`vars()`](https://docs.python.org/zh-cn/3/library/functions.html#vars) 的行为类似 [`locals()`](https://docs.python.org/zh-cn/3/library/functions.html#locals)。 请注意，locals 字典仅对于读取起作用，因为对 locals 字典的更新会被忽略。如果指定了一个对象但它没有 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性（例如，当它所属的类定义了 [`__slots__`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__slots__) 属性时）则会引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError) 异常。

- **zip**(**iterables*, *strict=False*)

    在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。示例:>>>`>>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']): ...     print(item) ... (1, 'sugar') (2, 'spice') (3, 'everything nice') `更正式的说法： [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 返回元组的迭代器，其中第 *i* 个元组包含的是每个参数迭代器的第 *i* 个元素。不妨换一种方式认识 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) ：它会把行变成列，把列变成行。这类似于 [矩阵转置](https://en.wikipedia.org/wiki/Transpose) 。[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 是延迟执行的：直至迭代时才会对元素进行处理，比如 `for` 循环或放入 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) 中。值得考虑的是，传给 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 的可迭代对象可能长度不同；有时是有意为之，有时是因为准备这些对象的代码存在错误。Python 提供了三种不同的处理方案：默认情况下，[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 在最短的迭代完成后停止。较长可迭代对象中的剩余项将被忽略，结果会裁切至最短可迭代对象的长度：>>>`>>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum'])) [(0, 'fee'), (1, 'fi'), (2, 'fo')] `通常 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 用于可迭代对象等长的情况下。这时建议用 `strict=True` 的选项。输出与普通的 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 相同：。>>>`>>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True)) [('a', 1), ('b', 2), ('c', 3)] `与默认行为不同，如果一个可迭代对象在其他几个之前被耗尽则会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError):>>>`>>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):   ...     print(item) ... (0, 'fee') (1, 'fi') (2, 'fo') Traceback (most recent call last):  ... ValueError: zip() argument 2 is longer than argument 1 `如果未指定 `strict=True` 参数，所有导致可迭代对象长度不同的错误都会被抑制，这可能会在程序的其他地方表现为难以发现的错误。为了让所有的可迭代对象具有相同的长度，长度较短的可用常量进行填充。这可由 [`itertools.zip_longest()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.zip_longest) 来完成。极端例子是只有一个可迭代对象参数，[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 会返回一个一元组的迭代器。如果未给出参数，则返回一个空的迭代器。小技巧：可确保迭代器的求值顺序是从左到右的。这样就能用 `zip(*[iter(s)]*n, strict=True)` 将数据列表按长度 n 进行分组。这将重复 *相同* 的迭代器 `n` 次，输出的每个元组都包含 `n` 次调用迭代器的结果。这样做的效果是把输入拆分为长度为 n 的块。[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 与 `*` 运算符相结合可以用来拆解一个列表:>>>`>>> x = [1, 2, 3] >>> y = [4, 5, 6] >>> list(zip(x, y)) [(1, 4), (2, 5), (3, 6)] >>> x2, y2 = zip(*zip(x, y)) >>> x == list(x2) and y == list(y2) True `*在 3.10 版本发生变更:* 增加了 `strict` 参数。

- **__import__**(*name*, *globals=None*, *locals=None*, *fromlist=()*, *level=0*)

    备注 与 [`importlib.import_module()`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module) 不同，这是一个日常 Python 编程中不需要用到的高级函数。此函数会由 [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句发起调用。 它可以被替换 (通过导入 [`builtins`](https://docs.python.org/zh-cn/3/library/builtins.html#module-builtins) 模块并赋值给 `builtins.__import__`) 以便修改 `import` 语句的语义，但是 **强烈** 不建议这样做，因为使用导入钩子 (参见 [**PEP 302**](https://peps.python.org/pep-0302/)) 通常更容易实现同样的目标，并且不会导致代码问题，因为许多代码都会假定所用的是默认实现。 同样也不建议直接使用 [`__import__()`](https://docs.python.org/zh-cn/3/library/functions.html#import__) 而应该用 [`importlib.import_module()`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module)。本函数会导入模块 *name*，利用 *globals* 和 *locals* 来决定如何在包的上下文中解释该名称。*fromlist* 给出了应从 *name* 模块中导入的对象或子模块的名称。标准的实现代码完全不会用到 *locals* 参数，只用到了 *globals* 用于确定 [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句所在的包上下文。*level* 指定是使用绝对还是相对导入。 `0` (默认值) 意味着仅执行绝对导入。 *level* 为正数值表示相对于模块调用 [`__import__()`](https://docs.python.org/zh-cn/3/library/functions.html#import__) 的目录，将要搜索的父目录层数 (详情参见 [**PEP 328**](https://peps.python.org/pep-0328/))。当 *name* 变量的形式为 `package.module` 时，通常将会返回最高层级的包（第一个点号之前的名称），而 *不是* 以 *name* 命名的模块。 但是，当给出了非空的 *fromlist* 参数时，则将返回以 *name* 命名的模块。例如，语句 `import spam` 的结果将为与以下代码作用相同的字节码:`spam = __import__('spam', globals(), locals(), [], 0) `语句 `import spam.ham` 的结果将为以下调用:`spam = __import__('spam.ham', globals(), locals(), [], 0) `请注意在这里 [`__import__()`](https://docs.python.org/zh-cn/3/library/functions.html#import__) 是如何返回顶层模块的，因为这是通过 [`import`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#import) 语句被绑定到特定名称的对象。另一方面，语句 `from spam.ham import eggs, sausage as saus` 的结果将为`_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0) eggs = _temp.eggs saus = _temp.sausage `在这里， `spam.ham` 模块会由 [`__import__()`](https://docs.python.org/zh-cn/3/library/functions.html#import__) 返回。 要导入的对象将从此对象中提取并赋值给它们对应的名称。如果您只想按名称导入模块（可能在包中），请使用 [`importlib.import_module()`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.import_module)*在 3.3 版本发生变更:* *level* 的值不再支持负数（默认值也修改为0）。*在 3.9 版本发生变更:* 当使用了命令行参数 [`-E`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-E) 或 [`-I`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-I) 时，环境变量 [`PYTHONCASEOK`](https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONCASEOK) 现在将被忽略。













































