# -*- coding: utf-8 -*-
# @CreateTime : 2024/4/28 028 12:57
# @Author : wephiles @20866
# @IDE : PyCharm
# @ProjectName : CSProjects
# @FileName : CSProjects/utils.py
# @Description : 这里写一些能是常用到的脚本，以后可以直接调用
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

import math
import hashlib
import heapq
import gzip
import shutil


class ListNode:
    """
    定义链表节点
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        # 查找元素 返回元素所在的根节点

        # 自己的根节点就是自己 - 自己就是根节点
        if self.parent[x] != x:
            # 路径压缩
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 合并两个元素
        root_x = self.find(x)
        root_y = self.find(y)
        # 两个元素不在一个根上面
        if root_x != root_y:
            # x所在根的树高更小
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def reverse_list(data_list: list[any]) -> list:
    """
    翻转列表，传入一个列表，将翻转后的列表return。
    eg:
        原列表: [1, 2, 3, 4, 5]
        翻转后: [5, 4, 3, 2, 1]
    Args:
        data_list (list): 需要翻转的列表

    Returns:
        list 翻转后的列表
    """
    for i in range(0, len(data_list) // 2):
        data_list[i], data_list[len(data_list) - i - 1] = data_list[
            len(data_list) - i - 1], data_list[i]
    return data_list


def reverse_list_between(data_list: list[any], begin_idx: int, end_idx: int) -> list[any]:
    """
    翻转列表中偏移(下标)在 begin_idx(包含) 和 end_idx(包含) 之间的数据
    Args:
        data_list ():
        begin_idx (): 开始的下标
        end_idx (): 结束的下标

    Returns:

    """

    if begin_idx < 0 or end_idx > len(
            data_list) or end_idx < begin_idx or begin_idx == end_idx:
        print("错误的转换范围。")
        return data_list

    length = end_idx - begin_idx + 1
    for i in range(begin_idx, begin_idx + length // 2):
        data_list[i], data_list[end_idx - i + begin_idx] = (
            data_list[end_idx - i + begin_idx], data_list[i])

    return data_list


def decompose_prime_factor(number: int) -> list[int]:
    """
    分解质因子。
    Args:
        number (int): 需要被分解的整数

    Returns:
        list[int]: 分解玩的所有质因子列表(升序排列)
    """
    if number == 1:
        print("1 没有质因子！")
        return []
    all_factor_list = []
    for i in range(2, int(math.sqrt(number)) + 1):
        # 因为当n被所有不大于根号下n的【质】因子整除后，要么余1，要么余2，
        # 要么会剩下一个且仅会剩下一个大于等于根号下n小于等于n的质数
        # （不可能出现两个不相等且同时大于根号下n的质因子a和b，这会导致a*b>n）
        while number % i == 0:
            all_factor_list.append(i)
            number //= i
    if number >= 2:
        all_factor_list.append(number)
    return all_factor_list


def binary(num: int) -> str:
    """
    将十进制转换为二进制字符串形式。

    Args:
        num (int): 需要被转换的十进制数。
    Returns:
        转换后的二进制数，以字符串形式返回
    """
    string_list = []
    decimal_divided = num
    while decimal_divided != 0:
        need_add_num = decimal_divided % 2
        string_list.append(str(need_add_num))
        decimal_divided //= 2
    return "".join(string_list[::-1])


def reverse_link_list(head: ListNode) -> ListNode:
    """
    翻转整个链表。
    Args:
        head (ListNode):

    Returns:
        ListNode :  翻转后链表的头结点。
    """
    if not head:
        return head
    p = head.next
    if not p:
        return head
    else:
        head.next = None
        while p.next:
            q = p.next
            p.next = head
            head = p
            p = q
        p.next = head
        head = p
        return head


def reverse_link_list_between(head: ListNode, m: int, n: int) -> ListNode:
    """
    题目：反转链表中指定区间的节点
    时间复杂度 O(n) ，空间复杂度 O(1)
    难度：中等
    Args:
        head ():
        m ():
        n ():

    Returns:

    """
    # write code here
    if m <= 0 or n <= 0:
        return head
    if not head or not head.next or m >= n:
        return head
    count = 1
    p = head
    begin_point = ListNode(1)
    end_point = ListNode(1)
    while p:
        if count == m:
            begin_point = p
        if count == n:
            end_point = p
            break
        p = p.next
        count += 1
    if p is None:
        print("超出范围")
        return head
    end_point_front = begin_point
    while end_point_front.next != end_point:
        end_point_front = end_point_front.next
    begin_point.val, end_point.val = end_point.val, begin_point.val

    if begin_point.next == end_point:
        return head

    p = begin_point.next
    q = end_point_front
    record_end = p

    begin_point.next = None
    q.next = None

    r = p.next
    while p != q:
        p.next = q.next
        q.next = p
        p = r
        r = p.next
    begin_point.next = p
    record_end.next = end_point
    return head


def reverse_link_list_between_slow(head: ListNode, m: int, n: int) -> ListNode:
    """
    题目：反转链表中指定区间的节点
    时间复杂度 O(n) ，空间复杂度 O(n)
    难度：中等
    Args:
        head ():
        m ():
        n ():

    Returns:

    """
    # write code here
    if not head:
        return head
    if m == n:
        return head
    p = head
    data_list = []
    while p:
        data_list.append(p.val)
        p = p.next
    reversed_list = self.reverse_list(data_list, m - 1, n - 1)
    p = head
    for item in reversed_list:
        p.val = item
        p = p.next
    return head


def md5(string: str):
    """
    md5加密
    Args:
        string (str):

    Returns:

    """
    obj = hashlib.md5(
        b"cdsnjokjseofjewDSFREFGRETRHherftHTRDHEWKJULSDgodgHFDHDFTjfhguieHHFDrhgurRTEHRTDhfughfidhHgurei")
    obj.update(string.encode("utf-8"))
    return obj.hexdigest()


def is_prime(n: int) -> bool:
    """
    判断一个数是否为质数
    Args:
        n (int): 需要判断的数

    Returns:
         flag (bool): 若为质数，返回True，否则返回False
    """
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sum_prime_between(start: int, end: int) -> int:
    """
    求两个数之间的所有质数的和
    Args:
        start (int):
        end (int):

    Returns:
        sum_prime (int): 质数的和
    """
    sum_prime = 0
    for i in range(start, end + 1):
        if is_prime(i):
            sum_prime += i
    return sum_prime


def bfs(graph, start):
    """
    广度优先遍历图，用邻接矩阵存储图
    Args:
        graph (): 图
        start (): 开始遍历的顶点

    Returns:

    """
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)

            # 访问
            print(vertex, end=" ")

        for i in range(graph[vertex]):
            # 这个判断语句是为了防止有些图 他的对角线元素全是1
            if i == vertex:
                continue
            else:
                if graph[vertex][i] == 1 and i not in visited:
                    queue.append(i)


def dfs(graph, start, visited):
    """
    深度优先遍历算法 用邻接矩阵存储
    Args:
        graph (): list[list[]]
        start (): int
        visited (): list

    Returns:

    """
    if visited is None:
        visited = set()
    visited.add(start)
    # 访问一下
    print(start, end=" ")

    for i in range(len(graph)):
        # 防止有的图会在对角线出存上1
        if i == start:
            continue
        if graph[start][i] == 1 and i not in visited:
            dfs(graph, i, visited)


def dijkstra(graph, start):
    """
    迪杰斯特拉算法。
    Args:
        graph (): 图 用邻接矩阵存储
        start (): 开始遍历的一个点

    Returns:

    """
    n = len(graph)
    distances = [float('infinity')] * n  # 从起始节点到各个节点的最短路径
    visited = [False] * n  # 标记节点是否被访问
    distances[start] = 0  # 标记自己到自己的距离为0
    for _ in range(n):
        min_distance = float('infinity')
        min_index = -1

        # 选择没有访问节点中间距离最小的节点
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i
        # 没有找到合适的顶点 跳出循环
        if min_index == -1:
            break

        visited[min_index] = True

        # 更新从选定节点出发的邻居节点的最短距离
        for i in range(n):
            if not visited[i] and graph[min_index][i] > 0:
                new_distance = distances[min_index] + graph[min_index][i]
                if new_distance < distances[i]:
                    distances[i] = new_distance
    return distances


def dijkstra_table(graph, start):
    """

    Args:
        graph (): 图，使用邻接表存储
        start (): 开始遍历的那个顶点

    Returns:

    """
    distance = {vertex: float("inf") for vertex in graph}
    distance[start] = 0

    # 优先队列 用于动态选择下一个要探索的点
    queue = [(0, start)]  # (距离, 顶点)

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        pass
    pass


def compress_data(file_path: str, output_path: str):
    """
    压缩数据
    Args:
        file_path ():
        output_path ():

    Returns:

    """
    with open(file_path, 'rb') as fp:
        with gzip.open(output_path, 'wb') as fp_out:
            shutil.copyfileobj(fp, fp_out)


def decompress_data(file_path: str, output_path):
    """
    解压缩数据
    Args:
        file_path (): 
        output_path (): 

    Returns:

    """
    with gzip.open(file_path, 'rb') as fp:
        with open(output_path, 'wb') as fp_out:
            shutil.copyfileobj(fp, fp_out)


if __name__ == "__main__":
    # print(reverse_list([1, 2, 3, 4, 5]))
    # print(reverse_list_between([1, 2, 3, 4, 5, 6, 7, 8], 6, 4))
    # print(decompose_prime_factor(16))
    # print(binary(10))
    # print(sum_prime_between(1, 100))

    # sample_graph = [
    #     [0, 5, 3, 0],
    #     [5, 0, 1, 3],
    #     [3, 1, 0, 2],
    #     [0, 3, 2, 0]
    # ]

    # sample_graph = [
    #     [0, 7, 9, 0, 0, 14],
    #     [7, 0, 10, 15, 0, 0],
    #     [9, 10, 0, 11, 0, 2],
    #     [0, 15, 11, 0, 6, 0],
    #     [0, 0, 0, 6, 0, 9],
    #     [14, 0, 2, 0, 9, 0]
    # ]
    # # 17090185547
    # shortest_distances = dijkstra(sample_graph, 1)  # 从节点0开始计算最短距离
    # print(shortest_distances)

    pass

# --END--
