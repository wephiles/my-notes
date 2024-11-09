[TOC]



# 函数进阶-`day6`

-   今日概要: 

    -   函数名就是一个变量(扩展)

    -   匿名函数(`lambda`表达式)

    -   **重点**内置函数——`python`内置函数

    -   推导式(一行代码生成数据)

## 1. 函数名就是变量

```python
def func():
    pass

v1 = func

v1()
func()
```

```python
def register():
    ...
    
def login():
    ...
    
def show_users():
    ...

print("welcome to xxx system!")
print("1. Register | 2. Login | 3. Show all members")

choice = input("please choose a number")
choice = int(choice)

func_list = [register, login, show_users]
func_list[choice - 1]()
```

让函数当做字典的值。

```python
def func():
    print(123)
    return 123

func_dict = {
    "1": func,
    "2": func,
    "3": func
}

# 获取函数并执行
func_dict["2"]()

# 
func_object = func_dict.get("1")
if func_object == None:
    print("函数不存在。")
else:
    func_object()
```

## 案例1: 用户管理系统(`VVIP`版本)

用户登录系统显示： `1. login 2. register 3. search`

```python
def register():
    print("register")


def login():
    print("login")


def show_users():
    print("show_users")


print("welcome to xxx system!")
print("1. Register | 2. Login | 3. Show all members")

choice = input("please choose a number \n>>> ")

func_dict = {
    "1": register,
    "2": login,
    "3": show_users
}

func_object = func_dict.get(choice)
if func_object is None:
    print("function is not exist!")
else:
    func_object()
```

![image-20240224213612430](.\assets\image-20240224213612430.png)

稍微改进一下：

```python
def register():
    print("register")


def login():
    print("login")


def show_users():
    print("show_users")


print("welcome to xxx system!")
print("1. Register | 2. Login | 3. Show all members")

choice = input("please choose a number \n>>> ")

func_dict = {
    "1": register,
    "2": login,
    "3": show_users
}

func_object = func_dict.get(choice)

if not func_object:  # 修改了这一行
    print("function is not exist!")
else:
    func_object()
```

## 案例2 资源下载管理器

-   系统有三大专区，图片 `NBA` 短视频

-   每个专区定义一个函数

-   用户选择

    -   选对了，进入

    -   选错了/重复选择 错误提示

    -   `Q/q` 终止

-   图片专区

    -   罗列图片名称和序号 
    -   让用户选择序号，用户选择哪个图片，我们帮助用户下载
    -   再次提示用户输入是否继续 如果是`n/N`返回上一级(让用户重新选择专区)

```python
# ************************************* 我自己的 *************************************

# 图片专区
img_data = {
    "1": ("image1", r"https://pic.3gbizhi.com/uploadmark/20230825/979bcabfd305afce4b5b5d00e467e01f.jpg"),
    "2": ("image2", r"https://pic.3gbizhi.com/uploadmark/20220916/35c9f1a1e642ba133b0efc2b58b9ae02.png"),
    "3": ("image3", r"https://pic.3gbizhi.com/uploadmark/20190912/6d7abd46d1531635e9b187cdea724345.jpg"),
    "4": ("image4", r"https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg"),
    "5": ("image5", r"https://pic.3gbizhi.com/uploadmark/20231030/d74c8cbc8bb461cef094e6b686990fde.jpg"),
    "6": ("image6", r"https://pic.netbian.com/uploads/allimg/230405/000245-168062416593ad.jpg")
}

# NBA 专区
nba_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15/oMGs"
               r"fhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1721&bt="
               r"1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs=0&rc=OGY1Oz"
               r"VmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kLS9zcw%3D%3D&btag"
               r"=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224221658C1E7B1B597C2"
               r"A7D01ABA"
    },
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve-15"
               r"/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video_mp4&qs="
               r"0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnbGBgLS1kLT"
               r"Bzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224"
               r"221827BDAEFE7D705F16E75C4C"
    }
}

# 短视频专区
short_video_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15"
               r"/oMGsfhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"1721&bt=1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs"
               r"=0&rc=OGY1OzVmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kL"
               r"S9zcw%3D%3D&btag=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202402"
               r"24221658C1E7B1B597C2A7D01ABA"
    },
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve"
               r"-15/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv"
               r"=1&br=817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video"
               r"_mp4&qs=0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnb"
               r"GBgLS1kLTBzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed29"
               r"9&l=20240224221827BDAEFE7D705F16E75C4C"
    }
}


def image_area():
    img_num = input("choose the number of images!\n>>> ")

    print("download image ...")
    print(img_data[img_num][0], " ", img_data[img_num][1])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input(">>> ")
    if if_repeat.upper() == "Y":
        image_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def nba_area():
    img_num = input("choose the number of nba images!\n>>> ")

    print("download image ...")
    print(nba_data[img_num]["title"], " ", nba_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input(">>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def video_area():
    img_num = input("choose the number of video!\n>>> ")

    print("download image ...")
    print(short_video_data[img_num]["title"], " ", short_video_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input("please input your choice: \n>>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def main():
    function_dict = {
        "1": image_area,
        "2": nba_area,
        "3": video_area,
    }

    while True:
        print("1. image 2. nba 3. short video")
        choice = input("choose a number, input Q or q to exit.\n>>> ")
        if choice.upper() == "Q":
            break

        func_obj = function_dict.get(choice)
        if not func_obj:
            raise ValueError("input error: {}".format(choice))
        func_obj()
    print()


if __name__ == "__main__":
    main()
```

```python
# ************************************* 沛齐老师的 *************************************
import sys

# 图片专区
img_data = {
    "1": ("image1", r"https://pic.3gbizhi.com/uploadmark/20230825/979bcabfd305afce4b5b5d00e467e01f.jpg"),
    "2": ("image2", r"https://pic.3gbizhi.com/uploadmark/20220916/35c9f1a1e642ba133b0efc2b58b9ae02.png"),
    "3": ("image3", r"https://pic.3gbizhi.com/uploadmark/20190912/6d7abd46d1531635e9b187cdea724345.jpg"),
    "4": ("image4", r"https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg"),
    "5": ("image5", r"https://pic.3gbizhi.com/uploadmark/20231030/d74c8cbc8bb461cef094e6b686990fde.jpg"),
    "6": ("image6", r"https://pic.netbian.com/uploads/allimg/230405/000245-168062416593ad.jpg")
}

# NBA 专区
nba_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15/oMGs"
        r"fhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1721&bt="
        r"1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs=0&rc=OGY1Oz"
        r"VmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kLS9zcw%3D%3D&btag"
        r"=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224221658C1E7B1B597C2"
        r"A7D01ABA"},
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve-15"
        r"/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
        r"817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video_mp4&qs="
        r"0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnbGBgLS1kLT"
        r"Bzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224"
        r"221827BDAEFE7D705F16E75C4C"}}

# 短视频专区
short_video_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15"
               r"/oMGsfhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"1721&bt=1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs"
               r"=0&rc=OGY1OzVmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kL"
               r"S9zcw%3D%3D&btag=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202402"
               r"24221658C1E7B1B597C2A7D01ABA"
    },
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve"
               r"-15/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv"
               r"=1&br=817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video"
               r"_mp4&qs=0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnb"
               r"GBgLS1kLTBzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed29"
               r"9&l=20240224221827BDAEFE7D705F16E75C4C"
    }
}


def image_area():
    print("======================== you are now in image area ========================")
    msg_list = []
    for k, item in img_data.items():
        string = "{}-{}".format(k, item[0])
        msg_list.append(string)
    msg_string = ": ".join(msg_list)
    while True:
        print(msg_string)
        img_num = input("choose the number of images!\n>>> ")
        if img_num.upper() == "N":
            return
        item_tuple = img_data.get(img_num)

        if not item_tuple:
            print("index error, please try again.", file=sys.stderr)
            continue
        print("correct index, downloading image ...")
        # print(img_data[img_num][0], " ", img_data[img_num][1])
        title, url = item_tuple
        print(title, url)
        print("download image over.")

        # print("if you want to download the image again? If you want, input n/N else input y/Y.")
        # if_repeat = input(">>> ")
        # if if_repeat.upper() == "Y":
        #     image_area()
        # elif if_repeat.upper() == "N":
        #     print()
        #     return
        # else:
        #     raise ValueError("input error: {}".format(if_repeat))
        # print()


def nba_area():
    img_num = input("choose the number of nba images!\n>>> ")

    print("download image ...")
    print(nba_data[img_num]["title"], " ", nba_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input(">>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def video_area():
    img_num = input("choose the number of video!\n>>> ")

    print("download image ...")
    print(short_video_data[img_num]["title"],
          " ", short_video_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input("please input your choice: \n>>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def run():
    function_dict = {
        "1": image_area,
        "2": nba_area,
        "3": video_area,
    }

    while True:
        print("1. image 2. nba 3. short video")
        choice = input("choose a number, input Q or q to exit.\n>>> ")
        if choice.upper() == "Q":
            break

        func_obj = function_dict.get(choice)
        if not func_obj:
            # raise ValueError("input error: {}".format(choice))
            print("input error, try again: ", file=sys.stderr)
            continue
        func_obj()
    print()


if __name__ == "__main__":
    run()

# --END--

```

注意: 只根据老师的代码修改了`images`这个专区的代码，其他的代码逻辑相同，不再浪费时间写了；此外，我加了一行代码`import sys`这里面有一个`sys.stderr`，可以当做参数传到`print`函数里面，这样带有`file=sys.stderr`的print语句所打印出来的语句就是红色的。

## 下载功能的实现

注意：如果没有安装`requests`第三方库，需要自己下载一下：在`pycharm`中，打开`terminal`，输入`pip install requests`，等待下载完成即可。

```python
# 安装第三方模块进行下载
import requests

# 下载图片
url_list = [
    "https://pic.3gbizhi.com/uploadmark/20230825/979bcabfd305afce4b5b5d00e467e01f.jpg",
    "https://pic.3gbizhi.com/uploadmark/20220916/35c9f1a1e642ba133b0efc2b58b9ae02.png",
    "https://pic.3gbizhi.com/uploadmark/20190912/6d7abd46d1531635e9b187cdea724345.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231030/d74c8cbc8bb461cef094e6b686990fde.jpg",
    "https://pic.netbian.com/uploads/allimg/230405/000245-168062416593ad.jpg"
]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
}
i = 0
for item in url_list:
    # 下载文件
    res = requests.get(
        url=item,
        headers=headers
    )
    # 保存文件

    with open("./images/image" + str(i) + ".jpg", "wb") as fp:
        print("downloading", i)
        fp.write(res.content)
    i += 1

# --END--
```

完成后，在自己的问价根目录下面找images文件夹，打开文件夹就能看到自己下载的图片啦。

![image-20240225173040986](.\assets\image-20240225173040986.png)

```python
# 下载视频
# 安装第三方模块进行下载
import requests

# 下载图片
url_list = [
    r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15/oMGs"
    r"fhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1721&bt="
    r"1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs=0&rc=OGY1Oz"
    r"VmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kLS9zcw%3D%3D&btag"
    r"=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224221658C1E7B1B597C2"
    r"A7D01ABA",

    "https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve-15"
    r"/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
    r"817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video_mp4&qs="
    r"0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnbGBgLS1kLT"
    r"Bzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224"
    r"221827BDAEFE7D705F16E75C4C",
]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
}
i = 0
for item in url_list:
    # 下载文件
    res = requests.get(
        url=item,
        headers=headers
    )
    # 保存文件

    with open("./videos/video" + str(i) + ".mp4", "wb") as fp:
        print("downloading", i)
        fp.write(res.content)
    i += 1
```

![image-20240225173430002](.\assets\image-20240225173430002.png)

好吧，可能是下载视频的格式问题，我的视频下载下来无法播放，下载的时候要注意，看好文件格式是什么。

接下来，把下载的相关代码拼接到相关函数就`OK`了。参考如下，我只写了下载图片的代码，其他的类似，只要模仿`images`区域的函数，将`download`函数放置到正确的地方即可。

```python
print("correct index, downloading image ...")
# print(img_data[img_num][0], " ", img_data[img_num][1])
title, url = item_tuple
download(model=".png", url=url, file_name=title)
print(title, url)
print("download image over.")
```

```python
import sys

import requests

# 图片专区
img_data = {
    "1": ("image1", r"https://pic.3gbizhi.com/uploadmark/20230825/979bcabfd305afce4b5b5d00e467e01f.jpg"),
    "2": ("image2", r"https://pic.3gbizhi.com/uploadmark/20220916/35c9f1a1e642ba133b0efc2b58b9ae02.png"),
    "3": ("image3", r"https://pic.3gbizhi.com/uploadmark/20190912/6d7abd46d1531635e9b187cdea724345.jpg"),
    "4": ("image4", r"https://pic.3gbizhi.com/uploadmark/20231120/004a59dc1b775ee4ea19cb9f350682bc.jpg"),
    "5": ("image5", r"https://pic.3gbizhi.com/uploadmark/20231030/d74c8cbc8bb461cef094e6b686990fde.jpg"),
    "6": ("image6", r"https://pic.netbian.com/uploads/allimg/230405/000245-168062416593ad.jpg")
}

# NBA 专区
nba_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15/oMGs"
               r"fhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1721&bt="
               r"1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs=0&rc=OGY1Oz"
               r"VmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kLS9zcw%3D%3D&btag"
               r"=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224221658C1E7B1B597C2"
               r"A7D01ABA"},
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve-15"
               r"/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video_mp4&qs="
               r"0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnbGBgLS1kLT"
               r"Bzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=20240224"
               r"221827BDAEFE7D705F16E75C4C"}}

# 短视频专区
short_video_data = {
    "1": {
        "title": "title1",
        "url": r"https://v3-web.douyinvod.com/5f859c5bcc8097014fe28d4aa0a51c85/65da090c/video/tos/cn/tos-cn-ve-15"
               r"/oMGsfhDALWBH8UmrCmFEAeDhBqA7L14IQBfmE6/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br="
               r"1721&bt=1721&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pikecsejKJV7TYeo0P3-I&mime_type=video_mp4&qs"
               r"=0&rc=OGY1OzVmNWQ5aTU4OWY1OEBpM2RnO205cjt3cTMzNGkzM0AzMy1iMzA1XmMxYjAxNmA1YSMtM24tMmRjY15gLS1kL"
               r"S9zcw%3D%3D&btag=e00028000&dy_q=1708784219&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202402"
               r"24221658C1E7B1B597C2A7D01ABA"
    },
    "2": {
        "title": "title2",
        "url": r"https://v3-web.douyinvod.com/f3e00fdf66b9fa32014f76739ce9a6c2/65da0964/video/tos/cn/tos-cn-ve"
               r"-15/ocw45QDzyBEJirkfhQCGnAIsAA7ZN7MgAeE5LX/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv"
               r"=1&br=817&bt=817&cs=0&ds=6&ft=bvTKJbQQqUnXfmoZmo0ORVTYA0pi9vcsejKJV7TYeo0P3-I&mime_type=video"
               r"_mp4&qs=0&rc=N2U2OGc0OGhkZWZmaGlnOUBpMzVoMzw6ZmVncTMzNGkzM0AxMjBjMzUzXzUxMDQuNi5gYSNsNjRqcjRnb"
               r"GBgLS1kLTBzcw%3D%3D&btag=e00028000&dy_q=1708784308&feature_id=f0150a16a324336cda5d6dd0b69ed29"
               r"9&l=20240224221827BDAEFE7D705F16E75C4C"
    }
}


def image_area():
    print("======================== you are now in image area ========================")
    msg_list = []
    for k, item in img_data.items():
        string = "{}-{}".format(k, item[0])
        msg_list.append(string)
    msg_string = ": ".join(msg_list)
    while True:
        print(msg_string)
        img_num = input("choose the number of images!\n>>> ")
        if img_num.upper() == "N":
            return
        item_tuple = img_data.get(img_num)

        if not item_tuple:
            print("index error, please try again.", file=sys.stderr)
            continue
        print("correct index, downloading image ...")
        # print(img_data[img_num][0], " ", img_data[img_num][1])
        title, url = item_tuple
        download(model=".png", url=url, file_name=title)
        print(title, url)
        print("download image over.")

        # print("if you want to download the image again? If you want, input n/N else input y/Y.")
        # if_repeat = input(">>> ")
        # if if_repeat.upper() == "Y":
        #     image_area()
        # elif if_repeat.upper() == "N":
        #     print()
        #     return
        # else:
        #     raise ValueError("input error: {}".format(if_repeat))
        # print()


def nba_area():
    img_num = input("choose the number of nba images!\n>>> ")

    print("download image ...")
    print(nba_data[img_num]["title"], " ", nba_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input(">>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def video_area():
    img_num = input("choose the number of video!\n>>> ")

    print("download image ...")
    print(short_video_data[img_num]["title"],
          " ", short_video_data[img_num]["url"])
    print("download image over.")

    print("if you want to download the image again? If you want, input n/N else input y/Y.")
    if_repeat = input("please input your choice: \n>>> ")
    if if_repeat.upper() == "Y":
        nba_area()
    elif if_repeat.upper() == "N":
        print()
        return
    else:
        raise ValueError("input error: {}".format(if_repeat))
    print()


def download(model=".jpg", url="", file_name=r""):
    """

    Args:
        url (): str
        model (): range from [".jpg", ".mp4"]

    Returns:

    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306"
    }
    res = requests.get(
        url=url,
        headers=headers
    )
    # 保存文件

    with open("./download_files/" + file_name + model, "wb") as fp:
        print("downloading...")
        fp.write(res.content)


def run():
    function_dict = {
        "1": image_area,
        "2": nba_area,
        "3": video_area,
    }

    while True:
        print("1. image 2. nba 3. short video")
        choice = input("choose a number, input Q or q to exit.\n>>> ")
        if choice.upper() == "Q":
            break

        func_obj = function_dict.get(choice)
        if not func_obj:
            # raise ValueError("input error: {}".format(choice))
            print("input error, try again: ", file=sys.stderr)
            continue
        func_obj()
    print()


if __name__ == "__main__":
    run()

# --END--
```

## 2. `lambda`表达式 —— 匿名函数

在特定的情况下让代码更简洁。

用**一行代码**定义**一个简单的函数**。

```python
def func():
    return 123

# func是函数名(变量)
# lambda: 函数体 --- 你写一个123，内部return一个123
func = lambda: 123

res = func
print(res())  # 123
```

```python
def func(a1, a2):
    return a1 + a2

func = lambda a1, a2: a1 + a2

res = func
print(res(1, 2))  # 3
```

```python
def func(data_string):
    return data_string.upper()

func = lambda data_string: data_string.upper()
```

```python
def func(data_list):
    return data_list[0]

func = lambda data_list: data_list[0]
```

注意：`lambda`表达式在内部会自动`return`，**`return`后面生成的是什么，就返回什么。**

```python
# 注意：
data_list = [11, 22, 33]

res = data_list.append(44)
print(res)  # None
```

![image-20240225180351332](.\assets\image-20240225180351332.png)

```python
def func(data_list):
    return data_list.append(44)
res = func([11, 22, 33])
print(res)  # None
```

```python
func = lambda data_list: data_list.append(44)

value = func([11, 22, 33])
print(value)  # None
```

## 3. 函数做参数

```python
def do():
    print("do")

def func(a1, a2):
    print(a1)
    a2()
    
func(11, do)
# 11 
# do
```

```python
def do():
    print("do")

def func(a1, a2):
    print(a1)
    a2()
    return 123
    
v1 = func(11, do)
print(v1)
# 11 
# do
# None
# 123
```

注意：一般情况下少用。

## 4. 内置函数

python内部为我们写好的函数，拿来用就行。

### 4.1 数值计算(5)

**注意：自己写函数的时候，不要用这种变量名哦。**

-   `abs()` 绝对值
    
    ```python
    data = abs(-10)
    print(data)  # 10
    ```
    
-   `pow()` 次方
    
    ```python
    data = pow(2, 5)
    print(data)  # 32 (2 ** 5)
    ```
    
-   `sum()` 求和
    
    ```python
    num_list = [...]
    sum(num_list)
    ```
    
-   `divmod()` 求除法得到的商和余数
    
    ```python
    a1, a2 = divmod(92, 10)
    print(a1, a2)
    # 9 2
    ```
    
-   `round()` 保留小数点后几位 支持四舍五入
    
    ```python
    data = round(3.1415926, 2)
    print(data)  # 3.14
    ```

### 4.2 第二组(4)

-   `min()`
    
    ```python
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(min(data))
    ```
    
-   `max()`
    
    ```python
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(max(data))
    ```
    
-   `all()` 列表是否**所有**元素转换为布尔值都是`True`
    
    ```python
    data = [123, 45, 6, "com"]
    print(all(data))  # True
    ```
    
    ```python
    data = [123, 45, 6, "com", 0]
    print(all(data))  # False
    ```
    
-   `any()` 只要有转换为`True`的就为`True`

### 4.3 第三组(3)

-   `bin()` 十进制转二进制
-   `oct()` 十进制转八进制
-   `hex()` 十进制转十六进制

### 练习题

给出一个`IP`地址，将每一段转换成二进制。

```
ip = "192.168.11.23"
192   0b11000000
168   0b10101000
11    0b1011
23    0b10111

# 去掉前面的0b， 补足8个bit
# 再次拼接起来
# 再转换成十进制
    num = int("10101101100011000000010000001002", base=2)
    print(num)
```

```python
# ========================== 我的代码 ==========================
def main() -> int:
    ip_address = "192.168.11.23"
    a, b, c, d = ip_address.split(".")
    data_list = [a, b, c, d]
    bin_dict = []
    for item in data_list:
        bin_dict.append(bin(int(item)))
    bin_without_0b = []
    for item in bin_dict:
        bin_without_0b.append(item.replace("0b", ""))
    final_string = []
    for item in bin_without_0b:
        if len(item) != 8:
            final_string.append("0" * (8 - len(item)) + item)
        else:
            final_string.append(item)
    string = "".join(final_string)
    number = int(string, base=2)
    print(number)
    return 0


if __name__ == "__main__":
    main()
```

![image-20240225185159464](.\assets\image-20240225185159464.png)

```python
# 老师的
ip = "192.168.11.23"
bin_str_list = []
str_list = ip.split(".")
for item in str_list:
    bin_str = bin(int(item))[2:]
    bin_fill_str = bin_str.zfill(8)
    bin_str_list.append(bin_fill_str)
num = int("".join(bin_str_list), base=2)
print(num)
```

还得是老师牛逼！！！简洁而又逻辑清晰。

![image-20240225185709003](.\assets\image-20240225185709003.png)

### 4.4 第四组(2)

编码时`unicode`编码，将文字和二进制做对应。

```python
计            10101011110100111101               987
```

-   `ord()`
    
    ```python
    v1 = ord("A")
    print(v1)  # 65
    ```
    
-   `chr()`
    
    ```python
    v2 = chr(65)
    print(v2)  # A
    ```

动态验证码：

```python
# 随机获取65-90的数字 利用chr转换成字母
import random

# 随机获取65-90的数字 利用chr转换成字母
char_list = []
for i in range(6):
    num = random.randint(65, 90)  # [65, 90]之间的随机数。
    char_list.append(chr(num))
print("".join(char_list))
```

### 4.5 第五组(9)

-   `int()`
-   `str()`
-   `bool()`
-   `list()`
-   `dict()`
-   `set()`
-   `tuple()`
-   `float()`
-   `bytes()`

### 4.6 第六组(10)

-   `len()`

-   `print()`

-   `input()`

-   `open()`

-   `range()`

-   `hash()` 字典的键，集合元素都必须是可哈希的

-   `type()` 查看数据类型
    
    ```python
    def func():
        if type(data) == str:
            ...
        if type(data) == list:
            ...
        ...
    func()
    ```
    
    ```python
    # 建议使用以下的方式:
    def func(data):
        if isinstance(data, str):
            print("string")
        elif isinstance(data, list):
            print("list")
        else:
            return
    ```
    
-   `callable()` 判断是否可执行
    
    ```python
    age = 12
    
    def func():
        return 123
    
    v1 = callable(age)
    v2 = callable(func)
    
    print(v1, v2)
    ```
    
-   `enumerate()` 在循环过程中，自动自增的一列。
    
    ```python
    goods = ["computer", "huawei", "xiaomi", "oppo"]
    # 以前
    for i in range(len(goods)):
        msg = "{} {}".format(i + 1, goods[i])
        print(msg)
        
    # 现在
    goods = ["computer", "huawei", "xiaomi", "oppo"]
    for index, item in enumerate(goods, 1):  # 那个1表示起始值
        msg = "{} {}".format(index, item)
    ```
    
-   `sorted()` 排序 --不修改源数据 会生成一个新列表
    
    ```python
    # 列表中的sort()排序(对原列表进行排序) —— 会修改原列表
    data_list = [15, 25, 0, 13, 2]
    data_list.sort()
    print(data_list)
    ```
    
    ```python
    data_list = [15, 25, 0, 13, 2]
    new_data = sorted(data_list)
    ```
    
    注意：如果元素是中文，怎么排序？
    
    `````python
    data_list = ["1", "2", "3", "10", "12"]
    new_data = sorted(data_list)
    print(new_data)  # 根据unicode编码排序 -- 因为是字符串！！！
    `````
    
    ![image-20240225210023939](.\assets\image-20240225210023939.png)
    ```python
    data_list = ["1 哈哈好", "2 嗯嗯", "3 哈哈哈", "10 嗯嗯呢", "12 哈哈好"]
    # 自定义排序规则 函数返回什么 那就按照返回的值进行排序
    def func(arg):
        return int(arg.split(" ")[0])
        
    new_data = sorted(data_list, key=func)
    print(new_data)
    ```
    
    ![image-20240225210924149](.\assets\image-20240225210924149.png)
    ```python
    data_list = ["1 哈哈好", "2 嗯嗯", "3 哈哈哈", "10 嗯嗯呢", "12 哈哈好"]
    func = lambda arg: int(arg.split(" ")[0])
    new_data = sorted(data_list, key=func)
    print(new_data)
    ```
    
    ![image-20240225211102702](.\assets\image-20240225211102702.png)

## 5. 推导式

`python`提供的简单的语法，一行代码生成列表、字典等多个元素。

创建一堆数据并存储到列表中

```python
data = []
for i in range(1, 101):
    data.append(i)
```

### 5.1 列表推导式

```python
data_list = [i for i in range(100)]
# [0, 1, 2, ... , 99]
```

```python
data_list = [100 for i in range(100)]
# [100, 100, 100, ... , 100]
```

```python
data_list = [100 + i for i in range(100)]
# [100, 101, 102, ... , 199]
```

```python
data_list = [[1, 2] for i in range(100)]
# [[1, 2], [1, 2], [1, 2], ... , [1, 2]]
```

```python
data_list = [(i, i+100) for i in range(100)]
# [(0, 100), (1, 101), (2, 102), ... , (99, 199)]
```

```python
data_list = ["工号-{}".format(i) for i in range(100)]
# ['工号-0', '工号-1', '工号-2', ..., '工号-99']
```

```python
data_list = [i for i in range(10) if i > 6]
# [7, 8, 9]
```

```python
data_list = [i for i in range(100) if i > 6 and i < 10]
# [7, 8, 9]
```

### 案例

```python
data_list = [1, True, "com", "sci", [11, 22], 99, 123, (45,)]
result = [i for i in data_list if isinstance(i, int)]
```

注意下面两张图：

![image-20240225212717413](.\assets\image-20240225212717413.png)

![image-20240225212830158](.\assets\image-20240225212830158.png)

```python
data_list = [1, True, "com", "sci", [11, 22], 99, 123, (45,)]
result = [i for i in data_list if type(data_list) is int]
```

![image-20240225213457703](.\assets\image-20240225213457703.png)

### 5.2 字典推导式

```python
data = {i: 123 for i in range(10)}
"""
{
    0: 123,
    2: 123,
    ...,
    9: 123
}
"""
```

```python
data = {i: (i, 100) for i in range(10)}
"""
{
	0: (0, 100),
	1: (1, 100),
	2: (2, 100),
	3: (3, 100),
	4: (4, 100),
	5: (5, 100),
	6: (6, 100),
	7: (7, 100),
	8: (8, 100),
	9: (9, 100)
}
"""
```

```python
data = {i: (i, 100) for i in range(10) if i > 7}
"""
{
	8: (8, 100),
	9: (9, 100)
}
"""
```

练习题：

```python
text = r"https://www.sogou.com/web?query=xx&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=19&sst0=1708868657212&lkt=0%2C0%2C0&sugsuv=1708868652598249&sugtime=1708868657212"
# 将字符串转换为字典： {"query": xx, "_asf": xxxx, ...}

data_dict = {i.split("=")[0]: i.split("=")[1] for i in text.split("?")[1].split("&")}
"""
{
    '_asf': 'www.sogou.com',
    '_ast': '',
    'from': 'index-nologin',
    'ie': 'utf8',
    'lkt': '0%2C0%2C0',
    'p': '40040100',
    'query': 'xx',
    's_from': 'index',
    'sst0': '1708868657212',
    'sugsuv': '1708868652598249',
    'sugtime': '1708868657212',
    'sut': '19',
    'w': '01019900'
}
"""
```

```python
a_dict = {
    '_asf': 'www.sogou.com',
    '_ast': '',
    'from': 'index-nologin',
    'ie': 'utf8',
    'lkt': '0%2C0%2C0',
    'p': '40040100',
    'query': 'xx',
    's_from': 'index',
    'sst0': '1708868657212',
    'sugsuv': '1708868652598249',
    'sugtime': '1708868657212',
    'sut': '19',
    'w': '01019900'
}
data_list = ["{}={}".format(k, v) for k, v in a_dict.items()]
print(data_list)
"""
['_asf=www.sogou.com',
 '_ast=',
 'from=index-nologin',
 'ie=utf8',
 'lkt=0%2C0%2C0',
 'p=40040100',
 'query=xx',
 's_from=index',
 'sst0=1708868657212',
 'sugsuv=1708868652598249',
 'sugtime=1708868657212',
 'sut=19',
 'w=01019900']
"""
print("&".join(data_list))
```

### 5.3 集合推导式

...

### 5.4 元组推导式(生成器表达式)

...

上述就是学习函数必备的知识点。

-   定义
-   执行
-   参数
-   返回值
-   作用域
-   函数名就是一个变量名
-   `lambda`表达式
-   内置函数
-   推导式 —— 与函数无关 简化代码

## 6. 关于`pip.exe`

### 6.1 下载第三方包

`pip`是一个专门用于帮助我们安装第三方库的工具。

```python
- python安装目录
	- python.exe   ---   python解释器
    - Scripts
    	- pip.exe
    - Lib(内置+第三方安装的库)
    	- site-package
        	- 第三方包
```

```python
>>> pip install 包名称
```

### 6.2 `pip`常见命令

-   安装 `pip install 包名称`

-   卸载`pip uninstall 包名称`

-   罗列目前已经安装的第三方包 `pip list`

-   **将已安装的包写到文件中** `pip freeze > requirements.txt`，还可以用`pip install -r requirements.txt`进行批量安装 `requirements.txt`一般都放在项目的根目录下面。(每个项目目录下面都可以放一个。)

    ```python
    # 这个可以用于工作交接。
    # 逐一安装：
    >>> pip install absl-py==2.1.0
    >>> pip install aiosignal==1.3.1
    
    # 批量安装
    pip install -r requirements.txt
    ```

    ![image-20240226085607046](.\assets\image-20240226085607046.png)

-   在同一个`python`环境中，无法同时安装多个版本的包，只能同时有一个。即：你如果安装了`requests2.1`，那么你就无法安装另外的`requests`包。

### 6.3 配置

![image-20240226091153323](.\assets\image-20240226091153323.png)

```python
# 成为开源作者，发布包：
https://www.bilibili.com/video/BV17541187de
```

有时候下载时会比较慢，从豆瓣源下载：

```python
# 基于豆瓣源下载：
>>> pip install 包名称 -i https://pypi.douban.com/simple/
```

```python
# 永久默认配置为豆瓣源
>>> pip config set global.index-url https://pypi.douban.com/simple/
>>> pip install 包名称
```

-   一般情况下，我们在开发过程总遇到的所有第三方包都可以通过pip包管理工具来进行安装。但是有些包在pip中没有，有可能找到源码包，可以通过源码进行安装。

    -   下载 以requests为例 去`https://pypi.org/search/`搜索你想要下载的包。
        ```python
        https://files.pythonhosted.org/packages/9d/be/10918a2eac4ae9f02f6cfe6414b7a155ccd8f7f9d4380d62fd5b955065c3/requests-2.31.0.tar.gz
        ```

        ![image-20240226092926438](.\assets\image-20240226092926438.png)

    -   解压
        ![image-20240226093236374](.\assets\image-20240226093236374.png)

    -   安装【终端】

        -   进入解压的源码包

            ```python
            >>> cd C:\Users\20866\Desktop\requests-2.31.0\requests-2.31.0
            ```

        -   执行安装命令

            ```python
            >>> python setup.py build
            >>> python setup.py install
            ```

            ![image-20240226093703433](.\assets\image-20240226093703433.png)

            ![image-20240226093759216](.\assets\image-20240226093759216.png)

    -   安装 `wheel`包
        源码开发者提前将代码打包成`wheel`包，到时候不需要`build`只需要`install`即可。

        -   `pip install wheel`
        -   下载wheel包 
            `https://files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl`
            ![image-20240226094312650](.\assets\image-20240226094312650.png)

        -   进入终端进行安装
            -   打开终端 进入wheel包目录
            -   直接安装
                ![image-20240226094709543](.\assets\image-20240226094709543.png)

-   注意事项，无论通过什么方式安装的第三方包，都是安装在`site-packages`目录下面。卸载直接通过`pip uninstall 包名称`



















































































