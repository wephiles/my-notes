# Python学习知识汇总

## 学习Python之前的准备工作

- 个人建议：在学习Python之前最好学习一些C/C++的知识，此外还可以学习一些**数据结构**和**操作系统**的知识。个人认为，尤其学习C/C++中的指针（C/C++）和面向对象（C++）对于理解Python中一些知识点有很大的促进作用。个人建议是如果想真正入行IT行业，做程序员，建议是**好好学一下C语言**（注意，是C语言而非C++，虽然C++完全兼容C），最主要的是学习C里面的指针等操作，对于提高编程思维有很大的帮助。诚然，在Python开发过程中很少用到C/C++，但是无疑，学习C/C++以及操作系统和数据结构能够帮助我们提高编程思维。对于提高编程思维这点来说，如果只学Python是远远不够的；

- 下载、安装Python，去[python官网](https://www.python.org/)下载python，选择一个稳定版本下载，建议不要下载最新版，最新版可能有bug，并且有些开发过程中高版本的Python会和一些低版本第三方库不兼容，建议安装3.10版本的Python即可。下载完成后安装python，傻瓜式安装即可；
- python集成开发环境：前期学习推荐使用Pycharm,等具有一定实力推荐使用Jupyter Notebook；也可以使用VSCode，看个人喜好。但是最推荐Pycharm，Pychaarm是JetBrains公司开发的一款用于Python开发的集成开发环境，拥有一整套Python开发所需要的工具，功能完备。缺点是比较臃肿，启动缓慢，占用大量内存资源，如果是小内存电脑(小于4GB的电脑)建议使用VSCode。 

## 需要学习的知识点

1. Python基础
    ！以下是我参考[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)所写出的学习步骤。可以进入https://www.runoob.com/python3/python3-tutorial.html学习。
    ![image-20240220152830497](D:\TextFiles\MDFiles\my_note\实习\2024实习\发实习生\assets\image-20240220152830497.png)

    - 第一个HelloWorld程序
        ```python
        print("Hello, World!")
        >>> Hello, World!
        ```

    - 数据类型
        - 整型
        - 布尔
        - 字符串
        - 浮点型
        - 字典
        - 列表
        - 元组
        - 集合
    - 数据类型转换
    - 交互式/脚本式编程
    - 注释
    - 运算符-算数运算符、逻辑运算符等
    - 数字
    - 字符串
        - 单引号 `‘ ’`
        - 双引号 `“ ”`
        - 三引号 `“”“ ”“”`
    - 列表
    - 元组
    - 字典
    - 集合
    - 条件控制
    - 循环
    - 推导式
        - 列表推导式
        - 字典推导式
        - 集合推导式
        - 元组推导式
    - 迭代器
    - 生成器
    - 函数
        - 函数参数
            - 位置参数
            - *args
            - **kwargs
        - 文档字符串
    - lambda
    - 数据结构
    - 模块
    - IO
    - 文件
    - OS模块
    - sys模块
    - 错误、异常
    - 面向对象
    - 命名空间、作用域
    - 标准库
    - python实例——参考 https://www.runoob.com/python3/python3-examples.html

2. 进阶
    - 正则表达式
    - CGI编程
    - 网络编程
    - 会用pip
    - math库
    - requests库
    - 数据库
        - mysql-connector
        - PyMySQL
    - 多线程
    - 内置函数
    - random库
    - json
    - 装饰器
    - **框架**
        - Python有一些很火的框架，可以看自己的喜好进行选择学习，第三点会列出当前很火的Python框架。

3. python 热门框架

    - WEB开发框架

        - **Django:** 高级全栈Web框架，适用于快速开发复杂的数据库驱动的网站。

        - **Flask:** 微型轻量级Web框架，适合小型应用和API服务。

        - **Tornado:** 异步网络库和Web服务器框架，特别适合需要处理大量并发连接的应用。

        - **Web2py:** 全功能Web框架，强调安全性和简单性。

    - 爬虫框架
        - **Scrapy**: 用于数据抓取和处理的开源框架，适用于大规模爬虫项目。

    - 机器学习、数据分析框架

        - **scikit-learn**: 提供了一系列有监督和无监督学习算法的工具集。

        - **TensorFlow**: Google开发的深度学习框架，广泛应用于机器学习领域。

        - **PyTorch**: Facebook研发的另一个深度学习框架，以其动态计算图特性受到许多开发者喜爱。

    - 其他框架

        - **Plotly/Dash**: 创建交互式网络可视化应用的框架。

        - **Keras**: 用户友好型神经网络高层API，可以运行在TensorFlow等后端上。

        - **Celery**: 分布式任务队列，常用于异步任务处理。

        * **Pyramid**: 另一个灵活且可扩展的Web框架，适合大型应用。

4. Python很好的第三方库-这些库都是开发过程中很多人用的，并不是Python自带的

    - **数据分析、科学计算**
        - NumPy: 提供高性能多维数组对象和矩阵运算。
        - Pandas: 强大的数据处理和分析工具，提供DataFrame等高效数据结构。
        - SciPy: 科学计算库，包括统计、优化、插值、积分等功能。
        - Matplotlib: 数据可视化库，用于创建高质量的静态、动态、交互式图形。
        - Scikit-learn: 机器学习库，提供了多种有监督和无监督学习算法。
    - **WEB开发框架**
        - Django: 高级全栈Web框架，适用于快速开发复杂项目。
        - Flask: 轻量级Web应用框架，适合小型或简单项目。
        - FastAPI: 近年来迅速崛起的异步Web框架，支持RESTful API和GraphQL。
    - **网络编程和请求库**
        - requests: HTTP客户端库，简化HTTP请求操作。
        - asyncio/ aiohttp: 异步I/O框架及基于此的HTTP客户端和服务器库。
    - **爬虫框架**
        - Scrapy: 功能丰富的爬虫框架，适用于构建大规模爬虫系统。
        - BeautifulSoup: HTML和XML解析库，常用于网页抓取。
    - **数据库接口**
        - SQLAlchemy: Python SQL工具包与ORM，提供全套SQL支持。
        - PyMongo: MongoDB的官方Python驱动程序。
        - psycopg2: PostgreSQL数据库的适配器。
    - **图像处理**
        - Pillow (PIL): 图像处理库，支持打开、修改和保存许多不同格式的图像文件。
        - OpenCV: 开源计算机视觉库，包含大量的图像和视频处理功能。
    - **日志记录**
        - logging: Python标准库中的日志模块，用于生成应用程序日志。
    - **测试工具**
        - unittest/unittest.mock: Python自带的单元测试框架和mock库。
        - pytest: 第三方流行的测试框架，提供更多的灵活性和便利性。
    - **部署和自动化**
        - Fabric: 远程执行命令和部署脚本的工具。
        - Ansible: IT自动化工具，可用于配置管理、应用部署等任务。
    - **数据可视化**
        - Plotly/Dash: 创建交互式网络图表和仪表盘。
        - Bokeh: 基于浏览器的数据可视化库，特别关注大型或流式数据集。

5. 一些Python学习资源

    - 不管学习什么，官方文档一定是最准确的：可以参考Python官方文档：https://docs.python.org/zh-cn/3.10/

    - 菜鸟教程：可以当做一个字典，有啥不会的去里面搜搜，个人觉得做的挺好。https://www.runoob.com/python3/python3-tutorial.html

    - 视频教程

        - 武沛齐老师的Python WEB课程：个人认为讲的比较好，有基础、前端CSS，JS，HTML的讲解，会讲解Django并且一步步实战过来，幽默风趣，如果学Django可以学习，如果只想学基础，那么也可以只学这个课程的基础部分。网址：https://www.bilibili.com/video/BV1324y1f7iJ/?spm_id_from=333.999.0.0&vd_source=3ccdc39ce9295a18b265315c9d0a3b78
            ![image-20240220160401853](D:\TextFiles\MDFiles\my_note\实习\2024实习\发实习生\assets\image-20240220160401853.png)

    
        - 学习爬虫可以进这个网址：https://www.bilibili.com/video/BV1ha4y1H7sx/?spm_id_from=333.337.search-card.all.click&vd_source=3ccdc39ce9295a18b265315c9d0a3b78
            ![image-20240220160516026](D:\TextFiles\MDFiles\my_note\实习\2024实习\发实习生\assets\image-20240220160516026.png)
    
    
    ​        
    
    - Python3.6.3中文教程：从菜鸟教程看到的，是3.6.3版本的，可以看看，https://www.runoob.com/manual/pythontutorial3/docs/html/
    
    - github上面有很多项目：作为一个程序员必须要会用github，里面有很多好的项目，适合新手练手的：
    
        - **Python算法学习**：
    
            - 地址：https://github.com/TheAlgorithms/Python
    
        - **Python-100-Days**
    
            - 地址：https://github.com/jackfrued/Python-100-Days
    
            - 简介：这是一个包含了100天Python学习计划的仓库，包含了一系列从基础到进阶的实战项目和教程，帮助初学者系统地掌握Python编程。
    
        - **python-guide**
            - 地址：https://github.com/realpython/python-guide
            - 简介：Python最佳实践指南，不仅介绍了语言特性，还提供了很多示例代码和资源链接，对于理解Python开发规范与最佳实践非常有用。
    
        - **Automate the Boring Stuff with Python**
    
            - 地址：https://github.com/BrambleXu/Automate-the-Boring-Stuff-with-Python-Solutions

    
            - 这个项目来源于同名书籍，作者Al Sweigart在GitHub上提供了大量配套代码和练习项目，通过解决实际生活中的小问题来教授Python编程。
        
        - **TheAlgorithms/Python**
        
            - 地址：https://github.com/TheAlgorithms/Python
        
            - 简介：一个包含了各种经典算法和数据结构的Python实现集合，可以帮助初学者通过阅读和实践这些算法来提高编程技巧。