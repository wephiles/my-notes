<h1 style="text-align: center; font-family: '仿宋';">05.函数</h1>

[TOC]



![Clip_2024-07-05_16-18-31](./assets/Clip_2024-07-05_16-18-31.png)

# 1 函数

![Clip_2024-07-05_16-27-16](./assets/Clip_2024-07-05_16-27-16.png)

```c
#include <stdio.h>

// 函数的声明
int function(int num1, int num2);

int function_add(int num1, int num2, int num3);


int main(void) {
    int x = function_add(12, 23, 40);
    printf("%d\n", x);
    return 0;
}

int function(int num1, int num2) {
    return num1 + num2;
}

int function_add(int num1, int num2, int num3) {
    return num3 + function(num1, num3);
}
```

# 2 `C`语言中的常见函数

![Clip_2024-07-05_16-32-44](./assets/Clip_2024-07-05_16-32-44.png)

```c
// 函数参考
https://zh.cppreference.com/w/%E9%A6%96%E9%A1%B5
```

![Clip_2024-07-05_16-35-46](./assets/Clip_2024-07-05_16-35-46.png)

![Clip_2024-07-05_16-36-18](./assets/Clip_2024-07-05_16-36-18.png)

![Clip_2024-07-05_16-44-57](./assets/Clip_2024-07-05_16-44-57.png)



![Clip_2024-07-05_16-53-27](./assets/Clip_2024-07-05_16-53-27.png)

![Clip_2024-07-05_16-54-11](./assets/Clip_2024-07-05_16-54-11.png)

```c
srand(1);
// 获取随机数
int num;
num = rand();
printf("%d\n", num);
```

![Clip_2024-07-05_16-57-17](./assets/Clip_2024-07-05_16-57-17.png)

































