<h1 style="text-align: center; font-family: '仿宋';">02.C语言核心语法</h1>

[TOC]

# 1 数据类型

## 1.1 数据类型的作用：

![Clip_2024-07-04_15-25-03](./assets/Clip_2024-07-04_15-25-03.png)

![Clip_2024-07-04_15-25-13](./assets/Clip_2024-07-04_15-25-13.png)

![Clip_2024-07-04_15-26-04](./assets/Clip_2024-07-04_15-26-04.png)

![Clip_2024-07-04_15-26-19](./assets/Clip_2024-07-04_15-26-19.png)

![Clip_2024-07-04_15-26-39](./assets/Clip_2024-07-04_15-26-39.png)

## 1.2 数据类型

### 1.2.1 整数类型

![Clip_2024-07-04_15-28-00](./assets/Clip_2024-07-04_15-28-00.png)

![Clip_2024-07-04_15-28-26](./assets/Clip_2024-07-04_15-28-26.png)

![Clip_2024-07-04_15-29-15](./assets/Clip_2024-07-04_15-29-15.png)

```C
short a = 256;
int b = 153;
long c = 153564L;
long long d = 15134653LL;  // C99才有的
printf("%d \n", a);
printf("%d \n", b);
printf("%ld \n", c);
printf("%lld \n", d);

printf("%zu \n", sizeof(short));  // 2
printf("%zu \n", sizeof(int));  // 4
printf("%zu \n", sizeof(long));  // 4
printf("%zu \n", sizeof(long long));  // 8
```

```C
// 定义数据类型的完整形态
short int a = 256;
int b = 153;
long int c = 153564L;
long long int d = 15134653LL;
```

```C
// 有符号整数
unsigned int f = 1564;
printf("%u \n", f);
```

![Clip_2024-07-04_15-41-28](./assets/Clip_2024-07-04_15-41-28.png)

### 1.2.2 小数类型

![Clip_2024-07-04_15-42-31](./assets/Clip_2024-07-04_15-42-31.png)

![Clip_2024-07-04_15-43-40](./assets/Clip_2024-07-04_15-43-40.png)

```C
float a = 3.14F;
printf("%f \n", a);  // 3.140000
printf("%.2f \n", a);  // 3.14

double b = 3.1415926;  
printf("%lf \n", b);// 3.141593
printf("%.2lf \n", b);//3.14

long double c = 3.1415;
printf("%lf \n", c);//3.141500
printf("%.2lf \n", c);//3.14

printf("%zu \n", sizeof(float));//4
printf("%zu \n", sizeof(double));//8
printf("%zu \n", sizeof(long double));//8
```

```C
// unsigned和小数之间是不能组合的
```

### 1.2.3 字符

![Clip_2024-07-04_15-50-46](./assets/Clip_2024-07-04_15-50-46.png)

```C
char a = 'a';
printf("%c ------ %zu ", a, sizeof(char));//a ------ 1
```

![Clip_2024-07-04_15-55-23](./assets/Clip_2024-07-04_15-55-23.png)

# 2 标识符

![Clip_2024-07-04_15-55-43](./assets/Clip_2024-07-04_15-55-43.png)

![Clip_2024-07-04_15-57-56](./assets/Clip_2024-07-04_15-57-56.png)

![Clip_2024-07-04_15-59-31](./assets/Clip_2024-07-04_15-59-31.png)

![Clip_2024-07-04_16-01-59](./assets/Clip_2024-07-04_16-01-59.png)

# 3 键盘录入

`scanf`

![Clip_2024-07-04_16-03-38](./assets/Clip_2024-07-04_16-03-38.png)

```C
char str[10] = "aaa";
// 英文状态下，一个字符占一个字节 一个汉字占两个字节
// 字符串最后都会含有一个结束标记 \0
printf("%s", str);
```

```C
char name[100];

printf("请输入名字 >>> ");
int return_value_scanf = scanf("%s", &name);
printf("你输入的名字是：%s \n", name);
```

```C
// 键盘录入多个数据
int a, b;
scanf("%d %d", &a, &b);
printf("%d %d", a, b);
```

![Clip_2024-07-04_16-27-57](./assets/Clip_2024-07-04_16-27-57.png)











































































































