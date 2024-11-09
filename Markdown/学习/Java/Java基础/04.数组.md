# 04.数组



[TOC]

[![Clip_2024-07-14_12-48-58](./assets/Clip_2024-07-14_12-48-58.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-48-58.png)

# 1 数组介绍



什么是数组

[![Clip_2024-07-14_12-50-18](./assets/Clip_2024-07-14_12-50-18.png)](./assets/Clip_2024-07-14_12-50-18.png)

[![Clip_2024-07-14_12-51-23](./assets/Clip_2024-07-14_12-51-23.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-51-23.png)

# 2 数组的定义和静态初始化



## 2.1 数组的定义



[![Clip_2024-07-14_12-53-45](./assets/Clip_2024-07-14_12-53-45.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-53-45.png)

格式一比较常用。

## 2.2 数组的初始化



[![Clip_2024-07-14_12-54-47](https://github.com/wephiles/my_markdown_files/raw/master/MDFiles/my_note/%E5%AD%A6%E4%B9%A0/Java%E5%AD%A6%E4%B9%A0/Java%E5%9F%BA%E7%A1%80/assets/Clip_2024-07-14_12-54-47.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-54-47.png)

[![Clip_2024-07-14_12-55-33](./assets/Clip_2024-07-14_12-55-33.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-55-33.png)

### 2.2.1 静态初始化



[![Clip_2024-07-14_12-55-55](./assets/Clip_2024-07-14_12-55-55.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-55-55.png)

```
int[] array = new int[]{
        1, 2, 3
};  // 数组静态初始化
```



简化初始化：

[![Clip_2024-07-14_12-57-27](./assets/Clip_2024-07-14_12-57-27.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_12-57-27.png)

```
int[] newArray = {10, 20, 30};  // 数组静态初始化 -- 简化版
```



[![Clip_2024-07-14_13-03-06](./assets/Clip_2024-07-14_13-03-06.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_13-03-06.png)

```
/*
 * @Author     : 20866@20866
 * @CreateTime : 12:51
 * @ProjectName: base_code_1
 * @PackageName: com.jinyu.array_demo
 * @FileName   : com.jinyu.array_demo/DefineArray.java
 * @ClassName  : DefineArray
 */

package com.jinyu.array_demo;

import java.util.Arrays;

public class DefineArray {
    public static void main(String[] args) {
        int[] array = new int[]{
                1, 2, 3
        };  // 数组静态初始化
        double[] newArray = {10.25, 20.0, 30};  // 数组静态初始化 -- 简化版

        System.out.println(Arrays.toString(array));  // [1, 2, 3]
        System.out.println(array);  // 数组的地址值：[I@723279cf
        // 数组的地址值：[I@723279cf
        // 其中的[代表这是个数组
        // I代表这是个存储int类型数据的数组
        // @：间隔符号，没有意义 后面723279cf是十六进制，是真正的地址值
        System.out.println(newArray); // [D@10f87f48
        System.out.println(array[0]);
        System.out.println(array[1]);
        System.out.println(array[2]);
        System.out.println(newArray[0]);
        System.out.println(newArray[1]);
        System.out.println(newArray[2]);
        
        array[2] = 100;
        System.out.println(array[0]);
        System.out.println(array[1]);
        System.out.println(array[2]);
        
        // --END--
    }
}
```



### 2.2.2 动态初始化



[![Clip_2024-07-14_13-27-24](./assets/Clip_2024-07-14_13-27-24.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_13-27-24.png)

```
// 数组动态初始化
// 由我们自己指定数组长度，由虚拟机给出默认的初始化值
int[] array = new int[3];
for (int j : array) {
    System.out.println(j);
}
array[0] = 1;
for (int i = 0; i < array.length; i++) {
    System.out.println(array[i]);
}
// 数组默认初始化值
// 整数  ---  0
// 浮点  ---  0.0
// 字符  ---  '\u0000' (也就是空格)
// 布尔  ---  false
// 引用  ---  null
```



### 2.2.3 动态/静态初始化的区别



[![Clip_2024-07-14_13-34-06](./assets/Clip_2024-07-14_13-34-06.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_13-34-06.png)

# 3 数组访问



[![Clip_2024-07-14_13-07-15](./assets/Clip_2024-07-14_13-07-15.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_13-07-15.png)

[![Clip_2024-07-14_13-07-15](./assets/Clip_2024-07-14_13-07-15-1720933687554-18.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_13-07-15-1720933687554-18.png)

# 4 数组的遍历



```
/*
 * @Author     : wephiles@20866
 * @CreateTime : 13:14
 * @ProjectName: base_code_1
 * @PackageName: com.jinyu.array_demo
 * @FileName   : com.jinyu.array_demo/TraverseArray.java
 * @ClassName  : TraverseArray
 */

package com.jinyu.array_demo;

public class TraverseArray {
    public static void main(String[] args) {
        /*
        * 遍历数组。
        * */
        int [] array = {1, 5, 3, 8, 7};
        // 方式1
        for (int i = 0; i < 5; i++) {
            System.out.println(array[i]);
        }

        // 方式2 计算出长度
        // Idea：自动生成遍历数组的方式 数组名.fori, 点击回车即可快速生成遍历代码
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }

        // 方式3 增强的for循环
        for (int i : array) {
            System.out.println(i);
        }

        // --END--
    }
}
```



# 5 数组内存图



Java内存分配：

[![Clip_2024-07-14_15-28-25](./assets/Clip_2024-07-14_15-28-25.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-28-25.png)

[![Clip_2024-07-14_15-28-56](./assets/Clip_2024-07-14_15-28-56.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-28-56.png)

[![Clip_2024-07-14_15-29-45](./assets/Clip_2024-07-14_15-29-45.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-29-45.png)

[![Clip_2024-07-14_15-30-05](./assets/Clip_2024-07-14_15-30-05.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-30-05.png)

[![Clip_2024-07-14_15-31-16](./assets/Clip_2024-07-14_15-31-16.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-31-16.png)

[![Clip_2024-07-14_15-32-24](./assets/Clip_2024-07-14_15-32-24.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-32-24.png)

[![Clip_2024-07-14_15-33-10](./assets/Clip_2024-07-14_15-33-10.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-33-10.png)

[![Clip_2024-07-14_15-34-39](./assets/Clip_2024-07-14_15-34-39.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-34-39.png)

[![Clip_2024-07-14_15-35-02](./assets/Clip_2024-07-14_15-35-02.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-35-02.png)

[![Clip_2024-07-14_15-37-58](./assets/Clip_2024-07-14_15-37-58.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-37-58.png)

[![Clip_2024-07-14_15-38-09](./assets/Clip_2024-07-14_15-38-09.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-38-09.png)

# 6 数组常见问题



[![Clip_2024-07-14_13-35-05](./assets/Clip_2024-07-14_13-35-05.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_13-35-05.png)

# 7 数组常见操作



## 7.1 求最值



[![Clip_2024-07-14_15-05-01](./assets/Clip_2024-07-14_15-05-01.png)](https://github.com/wephiles/my_markdown_files/blob/master/MDFiles/my_note/学习/Java学习/Java基础/assets/Clip_2024-07-14_15-05-01.png)

## 7.2 求和



...

## 7.3 交换数据



...

## 7.4 打乱数据



```
/*
 * @Author     : wephiles@20866
 * @CreateTime : 15:21
 * @ProjectName: base_code_1
 * @PackageName: com.jinyu.test
 * @FileName   : com.jinyu.test/RandomSort.java
 * @ClassName  : RandomSort
 */


package com.jinyu.test;

import java.util.Random;

public class RandomSort {
    public static void main(String[] args) {
        /*
         * 打乱数组中的数据
         * */

        int[] array = {1, 2, 3, 4, 5};

        // 遍历
        for (int j : array) {
            System.out.print(STR."\{j} ");
        }

        System.out.println();

        Random rd = new Random();
        for (int i = 0; i < array.length; i++) {
            int newIndex = rd.nextInt(array.length);
            int temp = array[i];
            array[i] = array[newIndex];
            array[newIndex] = temp;
        }

        // 遍历
        for (int j : array) {
            System.out.print(STR."\{j} ");
        }
        // --END--
    }
}
```
