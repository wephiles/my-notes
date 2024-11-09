```python
class A:
    def __new__(cls, x):
        """从class建立一个object的过程,必须要有返回值。"""
        print('__new__')
        return super().__new__(cls)

    def __init__(self, x):
        """有了__new__建立object,有了这个object之后，给这个object初始化的过程。self是要初始化的那个对象。"""
        self.x = x
        print('__init__')


o = A(1)
# obj = __new__(A, 1)
# __init__(obj, 1)
```

```python
class A:
    def __del__(self):
        """当这个对象被释放的时候，干些什么。不太好用！！！"""
        print('__del__')


o = A()
x = o

del o  # del 个__del__方法没有关系，del o的时候，并不一定会触发__del__方法 del o只是让这个对象少一个引用
print('finish')

"""
上述运行结果:
    finish
    __del__
说明:在del o的时候并没有触发__del__方法
"""
```

```python
class A:
    def __repr__(self):
        """返回这个object的字符串表示. -- 一般要有更详细的信息。"""
        return 'class<A repr>'

    def __str__(self):
        """返回这个object的字符串表示. -- 一般来说是人类更容易理解的string -- 比较注重可读性。"""
        return 'class<A str>'


# __str__和__repr__都定义的情况下,print是会使用__str__这个函数的
print(A())  # class<A str>
print(repr(A()))  # class<A repr>
print(str(A()))  # class<A str>

# 如果没有所谓的详细版和简易版，那么只需要定义__repr__,那么在print的时候会自动调用__repr__方法
```

```python
class A:
    def __format__(self, format_spec):
        """当使用某种格式打印这个object的时候，有可能会调用到__format__方法"""
        if format_spec == 'x':
            return '0xA'
        return '<A>'


print(f'{A()}')  # <A>
print(f'{A():x}')  # 0xA

print('{}'.format(15))  # 15
print('{:b}'.format(15))  # 1111
print('{:x}'.format(15))  # f

print(f'{15}')  # 15
print(f'{15:b}')  # 1111
print(f'{15:x}')  # f
```

```python
class A:
    def __bytes__(self):
        """尝试用这个class去建立一个bytes的时候，应该返回一个什么东西。"""
        print('__bytes__ called')
        return bytes([0, 1])


print(bytes(A()))
# __bytes__ called
# b'\x00\x01'
```

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


x = Date(2024, 2, 15)
y = Date(2024, 2, 15)
print(x == y)  # False -- 等价于: print(x is y)

# ----------------------------------------
# 分割线
# ----------------------------------------
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        """等于"""
        return (
                self.year == other.year and
                self.month == other.month and
                self.day == other.day
        )

    def __ne__(self, other):
        """不等于"""
        return (self.year != other.year or
                self.month != other.month or
                self.day != other.day)


x = Date(2024, 2, 15)
y = Date(2024, 2, 15)
z = Date(2024, 3, 15)

# x.__eq__(y)
print(x == y)  # True
# x.__ne__(y)
print(x != z)  # True

# ----------------------------------------
# 分割线
# ----------------------------------------

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        """等于"""
        return (
                self.year == other.year and
                self.month == other.month and
                self.day == other.day
        )

    def __ne__(self, other):
        """不等于"""
        return (self.year != other.year or
                self.month != other.month or
                self.day != other.day)

    def __gt__(self, other):
        """大于"""
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
                return self.day > other.day


x = Date(2024, 2, 15)
y = Date(2024, 2, 15)
z = Date(2024, 3, 15)

# x.__eq__(y)
print(x == y)  # True
# x.__ne__(y)
print(x != z)  # True

# 当实现了>的时候，Python内部默认>和<是一对
print(z > x)  # True
print(x < z)  # True

# 当我们使用 > 或者 < 的时候，首先是：前面.__lt__(后面)，如果(前面)没有__lt__方法，那么去后面找有没有__gt__方法
# 此外，如果一个类同时实现了__lt__ and __gt__，那么如果前面和后面是同一个类的对象，优先前面.__lt__
# 但是如果前面对象和后面对象不是同一个类的对象(来自继承),那么优先后面.__gt__
```

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f'{self.year}/{self.month}/{self.day}'

    # def __eq__(self, other):
    #     return self.year == other.year and self.month == other.month and self.day == other.day


x = Date(2024, 8, 15)
y = Date(2024, 8, 15)
income = {x: 1000, y: 1000}
print(income)  # {2024/8/15: 1000, 2024/8/15: 1000}

# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f'{self.year}/{self.month}/{self.day}'

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day


x = Date(2024, 8, 15)
y = Date(2024, 8, 15)
income = {x: 1000, y: 1000}
print(income)  # 报错 -- 不可哈希的 Python对每一个类默认了一个__eq__和__hash__方法
# 但是，如果自定义了__eq__方法，那么内部就会删除__hash__方法，如果还想使用hash，就需要自定义一个__hash__方法
# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f'{self.year}/{self.month}/{self.day}'

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __hash__(self):
        """必须返回一个整数。对于两个相等的对象必须要有同样的hash值"""

        # 合法但愚蠢的
        # return 1

        # python建议将对象的核心属性做成一个 tuple再求hash值进行返回
        return hash((self.year, self.month, self.day))


x = Date(2024, 8, 15)
y = Date(2024, 8, 15)
income = {x: 1000, y: 1000}
print(income)  # {2024/8/15: 1000}
```

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


x = Date(1900, 1, 11)
if x:
    # 所有自定义的对象在被放进if statement的时候都会被当做True
    print('Hello')  # Hello
    
# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

    def __bool__(self):
        print('__bool__')
        return False


x = Date(2020, 1, 11)

print(bool(x))  # False
if x:
    print('hello')
```

```python
class A:
    def __init__(self, ):
        self.exist = 'ahc'

    def __getattr__(self, item):
        """当item这个属性不存在的时候，希望这个函数干嘛。传入的参数item会是以string的形式传入。

        【注意】只有在读取一个不存在属性的时候才会被调用
        """
        print(f"getting {item}")
        return None


o = A()
print(o.exist)  # ahc

print(o.test)
# getting test
# None
```

```python
class A:
    def __init__(self):
        self.data = 'abc'
        self.count = 0

    def __getattribute__(self, item):
        """只要尝试读取他的属性，都会被调用。使用的时候小心一点，注意不显眼的递归。"""
        if item == 'data':
            self.count += 1
        # 这里不能写 return getattr(self, name) -- 会导致无限递归 -- 所以应该用super()
        return super().__getattribute__(item)


o = A()
print(o.data)
print(o.data)
print(o.count)

# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------
class A:
    def __init__(self):
        self.data = 'abc'
        self.count = 0

    def __getattribute__(self, item):
        """只要尝试读取他的属性，都会被调用。使用的时候小心一点，注意不显眼的递归。"""

        # 注意这里，如果这样写会产生无限递归
        self.count += 1

        # 这里不能写 return getattr(self, name) -- 会导致无限递归 -- 所以应该用super()
        return super().__getattribute__(item)


o = A()
print(o.data)
print(o.data)
print(o.count)
```

```python
class A:
    def __init__(self):
        self.data = 'abc'
        self.count = 0

    def __setattr__(self, key, value):
        print(f'set {key}')
        object.__setattr__(self, key, value)
        # super().__setattr__(key, value)


o = A()
print(o.data)
# set data
# set count
# abc

# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------

class A:
    _attr = {}

    def __init__(self, ):
        self.data = 'abc'

    def __setattr__(self, key, value):
        self._attr[key] = value

    def __getattr__(self, item):
        if item not in self._attr:
            raise AttributeError
        return self._attr[item]


o1 = A()
o2 = A()
o1.data = 'xyz'
print(o2.data)  # xyz
```

```python
class A:
    def __init__(self):
        self.data = 'abc'

    def __delattr__(self, item):
        """尝试使用del object.attr的时候，会被调用"""
        print(f'del {item}')


o1 = A()
del o1.data
# del data

print(o1.data)  # abc

# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------
class A:
    def __init__(self):
        self.data = 'abc'

    def __delattr__(self, item):
        """尝试使用del object.attr的时候，会被调用"""
        print(f'del {item}')
        super().__delattr__(item)


o1 = A()
del o1.data
# del data

print(o1.data)  # 报错 AttributeError: 'A' object has no attribute 'data'
```

```python
class A:
    def __init__(self):
        self.data = 'ABC'

    def __dir__(self):
        lst = super().__dir__()
        return [el for el in lst if not el.startswith('__')]


o = A()
print(dir(o))  # ['data']
```

```python
class D:
    def __get__(self, obj, owner=None):
        """会在我们尝试读取o.x的时候调用。self是描述对象本身（x），
        obj，有时候协程instance，对应的是这个o，也就是class A的object，
        owner是o的class
        """
        print(obj, owner)
        return 0


class A:
    x = D()


o = A()
print(o.x)
# <__main__.A object at 0x0000023C8F567AA0> <class '__main__.A'>
# 0

# --------------------------------------------------------------------------------
# 分割线
# --------------------------------------------------------------------------------

class D:
    """description这种东西是class level的"""

    def __init__(self):
        self.val = 0

    def __get__(self, obj, owner=None):
        return self.val

    def __set__(self, obj, value):
        self.val = value


class A:
    x = D()


o = A()
o2 = A()
print(o.x)  # 0

o.x = 1
print(o.x)  # 1
print(o2.x)  # 1
```

```python
class D:
    """description这种东西是class level的"""

    def __init__(self):
        self.val = 0

    def __get__(self, obj, owner=None):
        return self.val

    def __set__(self, obj, value):
        self.val = value

    def __delete__(self, obj):
        """当我们del o.x的时候，调用delete函数"""
        print('delete')


class A:
    x = D()


o = A()
del o.x
# delete
```

```python
class A:
    __slots__ = ['a', 'b']


o = A()
# o.x = 1  # 报错
o.a = 1  # 不会报错
```

```python
class Base:
    def __init_subclass__(cls, **kwargs):
        """需要定义在基类里面，以这个基类定义一个衍生类的时候就调用这个方法。"""
        print(cls)


class A(Base):
    pass
# 运行这个脚本，运行结果为：<class '__main__.A'>

# ================================================================================
# 分割线
# ================================================================================

class Base:
    def __init_subclass__(cls, **kwargs):
        """需要定义在基类里面，以这个基类定义一个衍生类的时候就调用这个方法。
        参数cls是刚刚建立的衍生类。
        """
        cls.x = {}


class A(Base):
    pass


print(A.x)  # {}

# ================================================================================
# 分割线
# ================================================================================

class Base:
    def __init_subclass__(cls, name):
        """需要定义在基类里面，以这个基类定义一个衍生类的时候就调用这个方法。
        参数cls是刚刚建立的衍生类。
        """
        cls.x = {}
        cls.name = name


class A(Base, name='Jack'):
    pass


print(A.x)  # {}
print(A.name)  # Jack
```

```python
class D:
    def __set_name__(self, owner, name):
        """更多的是定义在一个descriptor class中。
        即使这个class不是descriptor class，也依然起作用。

        这个方法相当于一个hook，当你在类定义中去构建一个这个class的instance的时候，
        这个方法就会被调用。

        owner是A，而name是它复制的这个变量的名字。
        """
        print(owner, name)


class A:
    x = D()

# 运行这个脚本，运行结果为：<class '__main__.A'> x
```

```python
class A:
    def __class_getitem__(cls, item):
        print(item)
        return 'abc'


print(A[0])
# 0
# abc

# type hint
int_arr_type = list[int]  # 这个list[int]就是使用__class_getitem__实现的

list_1: int_arr_type = []
list_2: int_arr_type = []
```

```python
class A:
    pass


class B(A()):
    pass
# 报错：TypeError: A() takes no arguments


class A:
    def __mro_entries__(self, bases):
        print(bases)
        return ()
    
# ================================================================================
# 分割线
# ================================================================================

class B(A()):
    pass
# (<__main__.A object at 0x00000204309D7B00>,)


class A:
    def __mro_entries__(self, bases):
        print(bases)
        return ()


class B(A()):
    pass


# (<__main__.A object at 0x00000204309D7B00>,)

print(issubclass(B, A))  # False

# ================================================================================
# 分割线
# ================================================================================

class A:
    def __mro_entries__(self, bases):
        print(bases)
        return (A,)


class B(A()):
    pass


# (<__main__.A object at 0x0000020F8BE27B30>,)

print(issubclass(B, A))  # True
```

```python

```

```python
```



```python

```

```python
# ================================================================================
# 分割线
# ================================================================================
```



































































