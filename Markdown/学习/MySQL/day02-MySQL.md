<h1 style="text-align: center;font-size: 40px; font-family: '楷体';">MySQL</h1>

[TOC]

# 1 MySQL简介

![Clip_2024-06-05_10-31-35](./assets/Clip_2024-06-05_10-31-35.png)

![Clip_2024-06-05_10-32-39](./assets/Clip_2024-06-05_10-32-39.png)

![Clip_2024-06-05_10-35-08](./assets/Clip_2024-06-05_10-35-08.png)

![Clip_2024-06-05_10-35-59](./assets/Clip_2024-06-05_10-35-59.png)

# 2 `MySQL`安装和使用

这个步骤可以去查看网络上的一些帖子.

# 3 `MySQL`的卸载

![Clip_2024-06-05_10-48-15](./assets/Clip_2024-06-05_10-48-15.png)

![Clip_2024-06-05_10-51-13](./assets/Clip_2024-06-05_10-51-13.png)

# 4 图形化管理工具

![Clip_2024-06-05_10-54-26](./assets/Clip_2024-06-05_10-54-26.png)

![Clip_2024-06-05_10-55-10](./assets/Clip_2024-06-05_10-55-10.png)

![Clip_2024-06-05_10-55-25](./assets/Clip_2024-06-05_10-55-25.png)

![Clip_2024-06-05_10-55-43](./assets/Clip_2024-06-05_10-55-43.png)

![Clip_2024-06-05_10-56-14](./assets/Clip_2024-06-05_10-56-14.png)

![Clip_2024-06-05_10-56-26](./assets/Clip_2024-06-05_10-56-26.png)

## 4.1 `Navicat`安装和使用

可以去网络山找下载安装及破解教程,这里不再赘述.

![Clip_2024-06-05_10-58-10](./assets/Clip_2024-06-05_10-58-10.png)

## 4.2 `SQLYog`安装和使用

官网地址: `https://sqlyog.en.softonic.com/`

下载安装步骤可以参考:`https://blog.csdn.net/weixin_43364551/article/details/116754626`

![Clip_2024-06-05_11-02-06](./assets/Clip_2024-06-05_11-02-06.png)

点击`free download for windows`

![Clip_2024-06-05_11-08-57](./assets/Clip_2024-06-05_11-08-57.png)

## 4.3 图形化界面连接数据库

![Clip_2024-06-05_16-50-51](./assets/Clip_2024-06-05_16-50-51.png)

![Clip_2024-06-05_16-51-07](./assets/Clip_2024-06-05_16-51-07.png)

![Clip_2024-06-05_16-52-50](./assets/Clip_2024-06-05_16-52-50.png)

![Clip_2024-06-05_16-53-02](./assets/Clip_2024-06-05_16-53-02.png)

# 5 MySQL数据库基本操作 -- `DDL`

## 5.1 `DDL` -- 不涉及到数据

![Clip_2024-06-05_16-54-34](./assets/Clip_2024-06-05_16-54-34.png)

## 5.2 对数据库的常用操作

![Clip_2024-06-05_16-55-45](./assets/Clip_2024-06-05_16-55-45.png)

### 5.2.1 数据库操作

![Clip_2024-06-06_12-48-08](./assets/Clip_2024-06-06_12-48-08.png)

```sql
-- 这是注释
# 这也是注释

-- 查看所有的数据库
show databases;

# 创建数据库
create database test_db;
create database if not exists test_db;

# 选择使用哪一个数据库
use test_db;

# 删除数据库
drop database test_db;
drop database if exists test_db;

# 修改数据库编码
alter database mydb_1 charset set utf8;
```

### 5.2.2 创建表

![Clip_2024-06-06_13-02-13](./assets/Clip_2024-06-06_13-02-13.png)

### 5.2.3 数据类型

- 数值类型

  ![Clip_2024-06-06_13-09-30](./assets/Clip_2024-06-06_13-09-30.png)

- 日期和时间类型

  ![Clip_2024-06-06_13-20-21](./assets/Clip_2024-06-06_13-20-21.png)

- 字符串类型 -- 一般用单引号括起来

  ![Clip_2024-06-06_13-18-49](./assets/Clip_2024-06-06_13-18-49.png)

### 5.2.4 其他操作

![Clip_2024-06-06_13-22-49](./assets/Clip_2024-06-06_13-22-49.png)

```sql
# 查看当前数据库所有表
show tables;

# 查看指定表的创建语句
SHOW create table student;
# 所得的输出：
# CREATE TABLE `student` (
#  `sid` int DEFAULT NULL,
#  `name` varchar(20) DEFAULT NULL,
#  `gender` char(4) DEFAULT NULL,
#  `age` int DEFAULT NULL,
#  `birth` date DEFAULT NULL,
#  `address` varchar(64) DEFAULT NULL
#) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

# 查看表结构
desc student;

# 删除表
drop table student;
```

### 5.2.5 对表结构的常用操作--修改表结构格式

![Clip_2024-06-06_13-28-13](./assets/Clip_2024-06-06_13-28-13.png)

![Clip_2024-06-06_13-32-14](./assets/Clip_2024-06-06_13-32-14.png)

![Clip_2024-06-06_13-37-02](./assets/Clip_2024-06-06_13-37-02.png)

![Clip_2024-06-06_13-37-21](./assets/Clip_2024-06-06_13-37-21.png)

```sql
-- 修改表结构

-- -- 添加列
-- alter table student add dept varchar(20);

-- -- 修改列名和类型
-- alter table student change dept department varchar(30);

-- -- 删除列
-- alter table student drop department;


-- 修改表名
rename table student to stu;
```

# 6 `MySQL`数据库基本操作 - `DML`

![Clip_2024-06-06_13-40-37](./assets/Clip_2024-06-06_13-40-37.png)

## 6.1 数据插入

![Clip_2024-06-06_15-35-22](./assets/Clip_2024-06-06_15-35-22.png)

```sql
insert into 
```

















