<h1 style="text-align: center;font-size: 40px; font-family: '楷体';">day03-Python CSV操作</h1>

# `CSV`格式文件

字符分隔值文件/逗号分隔值文件

小案例：下载下面`CSV`文件里面网址指向的图片，以人名命名。

```python
ID,用户名,头像
26044585,zhaolusi,https://pic.3gbizhi.com/uploadmark/20240321/e0426d1651ec542fd8b0b58bca58ac69.jpg
26044586,七十一,https://pic.3gbizhi.com/uploads/20240105/9d405b9d8437c48b063737baada1ad6d.jpg
26044125,Jennah,https://pic.3gbizhi.com/uploads/20231120/f2c9ade787517e96fbb011b6ab03a2f4.jpg
26041285,你的老杨,https://pic.3gbizhi.com/uploads/20230910/1a8a1b111038e81271bda148ce219847.jpg
26042185,尺尺寸,https://pic.3gbizhi.com/uploads/20240105/9d405b9d8437c48b063737baada1ad6d.jpg
26256885,爱起床的小灰灰,https://pic.3gbizhi.com/uploads/20231030/fb2866c603ddbb4682d6084e0f36367f.jpg
26011285,海贼玩泡泡,https://pic.3gbizhi.com/uploads/20220916/4cfc61735b9eb8b722837a128bf8dfb7.png
21589485,稀奇,https://pic.3gbizhi.com/uploads/20200914/b481135e9038d8666de7a97fa616ac87.jpeg
26041565,奥利给,https://pic.3gbizhi.com/uploads/20230423/e654a0876a471fd64c4311ef6d264d53.png
26012585,唱歌,https://pic.3gbizhi.com/uploads/20240401/faa435b9613e5f258ac7f45ba94e9404.jpg
12044585,跳舞,https://pic.3gbizhi.com/uploads/20240401/4eed148068717c4df0fbc846afd1ca2c.jpg
26124585,rap,https://pic.3gbizhi.com/uploads/20240321/8e9faa422832851ceb540310695ba2d9.jpg
21563485,篮球,https://pic.3gbizhi.com/uploads/20240401/cd5c121d80c5ea1b4427987239f33eb4.jpg
```

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/99.0.4844.84 "
                  "Safari/537.36 HBPC/12.1.3.306"
}

with open("mv.csv", "r", encoding="utf-8") as fp:
    # 表头,忽略
    fp.readline()

    # 读取每一行数据
    for line in fp:
        _, user_name, url = line.strip().split(",")

        # 下载图片
        print("Downloading images ...")
        response = requests.get(url=url, headers=headers)

        # 保存图片
        save_path = r"./assets/{}.png".format(user_name)
        with open(save_path, "wb") as file_obj:
            print("Saving image", user_name + "png", "...")
            file_obj.write(response.content)
```



