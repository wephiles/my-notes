1. 创建虚拟环境：

- 内置
  ```python
  >>> python -m venv xxx
  ```

- 第三方工具
  ```python
  >>> pip install virtualenv
  ```

  新打开一个窗口

  ```python
  >>> virtualenv crm --python=python3.10
  ```

2. 激活虚拟环境 + 使用

- 传统方式：写全路径，直接执行
  ```python
  >>> D:/xxx/xx/x/python D:/xxxx/xxx/xx/test.py
  ```

- 激活: 进入我们新创建的虚拟环境的`Scripts`那个文件目录里面：里面有`python.exe`和一个`activate`文件
  ```python
  >>> activate
  ```

  退出激活：

  ```python
  >>> deactivate
  ```


3. 生成`requirements.txt`文件：下面命令会在当前项目根目录下面生成`requirements.txt`文件
   ```python
   >>> pip freeze > requirements.txt
   ```

4. 使用 -- 只要拿到别人的代码文件和`requirements.txt`文件即可在`pycharm`中愉快地当牛马了。

   ```python
   >>> pip install -r requirements.txt
   ```

   