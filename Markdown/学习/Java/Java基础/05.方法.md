<h1 style="text-align: center; font-family: 'Menlo'">05.方法</h1>

[TOC]

# 1 什么是方法

方法是程中最小的执行单元。

![Clip_2024-07-14_16-08-56](./assets/Clip_2024-07-14_16-08-56.png)

# 2 方法的作用

![Clip_2024-07-14_16-10-18](./assets/Clip_2024-07-14_16-10-18.png)

![Clip_2024-07-14_16-11-25](./assets/Clip_2024-07-14_16-11-25.png)

![Clip_2024-07-14_16-11-52](./assets/Clip_2024-07-14_16-11-52.png)

# 3 方法的格式

![Clip_2024-07-14_16-12-27](./assets/Clip_2024-07-14_16-12-27.png)

![Clip_2024-07-14_16-12-49](./assets/Clip_2024-07-14_16-12-49.png)

```java
/*
 * @Author     : wephiles@20866
 * @CreateTime : 16:06
 * @ProjectName: base_code_1
 * @PackageName: com.jinyu.method
 * @FileName   : com.jinyu.method/MethodDemo.java
 * @ClassName  : MethodDemo
 */

package com.jinyu.method;

public class MethodDemo {
    public static void main(String[] args) {
        // 调用方法
        playGame();
    }

    // 定义方法
    public static void playGame() {
        System.out.println("打游戏...");
    }
}

```

![Clip_2024-07-14_16-17-25](./assets/Clip_2024-07-14_16-17-25.png)

![Clip_2024-07-14_16-18-20](./assets/Clip_2024-07-14_16-18-20.png)

![Clip_2024-07-14_16-24-10](./assets/Clip_2024-07-14_16-24-10.png)

![Clip_2024-07-14_16-25-25](./assets/Clip_2024-07-14_16-25-25.png)

![Clip_2024-07-14_16-30-26](./assets/Clip_2024-07-14_16-30-26.png)

![Clip_2024-07-14_16-30-51](./assets/Clip_2024-07-14_16-30-51.png)

![Clip_2024-07-14_16-31-24](./assets/Clip_2024-07-14_16-31-24.png)

![Clip_2024-07-14_16-35-40](./assets/Clip_2024-07-14_16-35-40.png)

# 4 方法小结

![Clip_2024-07-14_16-41-01](./assets/Clip_2024-07-14_16-41-01.png)

![Clip_2024-07-14_16-42-57](./assets/Clip_2024-07-14_16-42-57.png)

![Clip_2024-07-14_16-43-25](./assets/Clip_2024-07-14_16-43-25.png)

# 5 方法的重载

>   同一个类中，参数不同(参数个数、类型、顺序不同)、方法名相同 --方法重载

![Clip_2024-07-14_16-45-51](./assets/Clip_2024-07-14_16-45-51.png)

![Clip_2024-07-14_16-46-50](./assets/Clip_2024-07-14_16-46-50.png)

![Clip_2024-07-14_16-47-23](./assets/Clip_2024-07-14_16-47-23.png)

![Clip_2024-07-14_16-49-16](./assets/Clip_2024-07-14_16-49-16.png)

![Clip_2024-07-14_16-49-56](./assets/Clip_2024-07-14_16-49-56.png)

```java
/*
 * 定义函数遍历数组 -- 方法重载
 * @Author     : wephiles@20866
 * @CreateTime : 2024-07-14 16:55
 * @ProjectName: base_code_1
 * @PackageName: com.jinyu.test
 * @FileName   : com.jinyu.test/MethodTraverse.java
 * @ClassName  : MethodTraverse
 */

package com.jinyu.test;

public class MethodTraverse {
    public static void main(String[] args) {
        int[] array = {15, 5, 9, 125, 23, 25};
        traverse(array);

        double[] newArray = {10.5, 2.3, 5.2, 6.6};
        traverse(newArray);
    }

    public static void traverse(byte[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(short[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(int[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(long[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(double[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(float[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(boolean[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }

    public static void traverse(char[] array) {
        System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            if (i != array.length - 1) {
                System.out.print(STR."\{array[i]}, ");
            } else {
                System.out.println(STR."\{array[i]}]");
            }
        }
    }
}

```

# 6 方法的内存图

![Clip_2024-07-14_17-22-01](./assets/Clip_2024-07-14_17-22-01.png)

## 6.1 基本内存原理

![image-20241031200607066](./assets/image-20241031200607066.png)

![Clip_2024-07-14_17-22-28](./assets/Clip_2024-07-14_17-22-28.png)

## 6.2 方法传递基本数据类型

![Clip_2024-07-14_17-32-03](./assets/Clip_2024-07-14_17-32-03.png)

![Clip_2024-07-14_17-32-30](./assets/Clip_2024-07-14_17-32-30.png)

![Clip_2024-07-14_17-33-44](./assets/Clip_2024-07-14_17-33-44.png)

![image-20241031201219763](./assets/image-20241031201219763.png)

![Clip_2024-07-14_17-34-51](./assets/Clip_2024-07-14_17-34-51.png)

![Clip_2024-07-14_17-37-29](./assets/Clip_2024-07-14_17-37-29.png)

![image-20241031201618548](./assets/image-20241031201618548.png)

![image-20241031201648129](./assets/image-20241031201648129.png)

![Clip_2024-07-14_17-40-20](./assets/Clip_2024-07-14_17-40-20.png)

![Clip_2024-07-14_17-40-51](./assets/Clip_2024-07-14_17-40-51.png)

# 7 方法 -- 练习

## 7.1 数组遍历

题目：

![image-20241031191112706](./assets/image-20241031191112706.png)

```java
public class TraverseArray {
    public static void main(String[] args) {
        int[] array = {12, 5, 6, 7, 51, 59, 6, 2};
        traverse(array);
    }

    public static void traverse(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            if (i == arr.length - 1) {
                System.out.print(arr[i]);
            } else {
                System.out.print(arr[i] + ", ");
            }
        }
        System.out.println("]");
    }
}
```

## 7.2 求最大值

题目：

![image-20241031191813465](./assets/image-20241031191813465.png)

```java
// 求数组最大值
public static int getMax(int[] arr) {
    int max = arr[0];
    for (int i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
```

## 7.3 判断是否存在

题目：

![image-20241031192406108](./assets/image-20241031192406108.png)

```java
// 判断是否存在
public static boolean numInArray(int number, int[] arr) {
    for (int j : arr) {
        if (number == j) {
            return true;
        }
    }
    return false;
}
```

## 7.4 复制数组

题目：

![image-20241031192931702](./assets/image-20241031192931702.png)

```java
public static void main(String[] args) {
    // 复制数组
    int[] newArray = copyArray(array);
    traverse(newArray);
}

// 复制数组 -- 全部
public static int[] copyArray(int[] arr) {
    int[] newArray = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
        newArray[i] = arr[i];
    }
    return newArray;
}

// 复制数组 -- 范围
public static int[] copyOfRange(int[] arr, int from, int to) {
    if (from < 0 || to >= arr.length || to < 0 || from > to) {
        return new int[]{};
    }
    int newLength = to - from + 1;
    int[] newArray = new int[newLength];
    for (int i = from; i < to + 1; i++) {
        newArray[i - from] = arr[i];
    }
    return newArray;
}
```









































































































