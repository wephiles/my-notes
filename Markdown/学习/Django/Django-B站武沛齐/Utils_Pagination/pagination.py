# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/30 030 15:00
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : merge
# @FileName : merge/pagination.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

"""
自定义分页组件
"""

from django.utils.safestring import mark_safe


class Pagination(object):
    """分页组件

    如果要使用此组件，你需要这么做：
    在urls.py里面:
        写好url和视图函数的对应关系；
    在views.py中:
        def beautiful_list(request):
            # 1. 根据自己的项目筛选想要的数据
            query_set = my_md.BeautifulNumber.objects.all().order_by("-level")

            # 2. 实例化分页对象 传入你的参数
            page_obj = Pagination(request, query_set=query_set, page_size=10, plus=3)
            data = {
                'query_set': page_obj.page_query_set,  # 分页完毕的数据
                "page_string": page_obj.html(),  # 生成合适的页码
            }
            return render(request,
                          'beautiful_number_list.html',
                          data)
    在html页面中:
        <table class="table table-hover table-bordered table-striped 这是你的数据表展示区">
            <thead>
            <tr>
                <th>ID</th>
                ...
            </tr>
            </thead>

            <tbody>
            {% for item in query_set %}
                <tr>
                    <td>{{ item.id }}</td>
                    ...
                    <td>
                        <a href="/beautiful/{{ item.id }}/edit/">
                            <button type="button" class="btn btn-primary btn-xs">编辑</button>
                        </a>
                        <a href="/beautiful/{{ item.id }}/delete/">
                            <button type="button" class="btn btn-danger btn-xs">删除</button>
                        </a>
                    </td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
        ...

        -- 下面这三行会生成一个分页组件 上面的那些是展示出自己的数据 下面这三行才是真正的分页组件 下面这三行是重点
        <ul class="pagination">
            {{ page_string }}
        </ul>
    """

    def __init__(self,
                 request,
                 query_set,
                 page_param='page',
                 page_size=10,
                 plus=3):
        """初始化分页组件。

        Args:
            request (object): 传入的request对象，是django中views文件里视图函数中的
                那个request参数
            query_set (object): 查询到的所有数据的queryset对象 -- 注意，是所有数据
            page_param (str): 跳转的时候通过get方法传入的参数的值 -- 是个字符串
                比如 'page'
            page_size (int): 一页的大小
            plus (int): 分页，显示某一页的前几页后几页
        """
        # 防止点击分页的时候页面自动取消搜索结果的小bug
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.param = page_param

        # 获取当前页数
        page_str: str = request.GET.get(self.param, '1')

        # 如果获取的是可以转换成数字类型的字符串
        if page_str.isdecimal():
            page = int(page_str)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        # 找出一页显示的起止位置
        self.start = (self.page - 1) * self.page_size
        self.end = self.page * self.page_size

        # 所有数据的query_set

        self.page_query_set = query_set[self.start:self.end]

        # 数据总条数
        total_count = query_set.count()

        total_page, div = divmod(total_count, self.page_size)
        if div:
            total_page += 1
        self.total_page = total_page

        self.plus = plus

    def html(self):
        # 计算出当前页的前后plus页
        # plus = 3
        # 当时数据量比较少的时候 如果可以直接显示  直接显示所有可以显示的页数
        if self.total_page < 2 - self.plus + 1:
            start_page = 1
            stop_page = self.total_page + 1
        else:
            # 当前页面太小 为1或者2 小于3，那么就可以让第一页直接为1
            if self.page <= self.plus:
                start_page = 1
                stop_page = 2 * self.plus + 1
            else:
                # 当前页已经快接近后面的极值了
                # 当前页 + plus > 总页码
                if self.page + self.plus > self.total_page:
                    start_page = self.total_page - 2 * self.plus
                    stop_page = self.total_page + 1
                else:
                    start_page = self.page - self.plus
                    stop_page = self.page + self.plus + 1

        # 生成页码标签
        page_str_list = []
        self.query_dict.setlist(self.param, [1])

        page_str_list = [
            '<li><a href="?{}" aria-label="首页"><span aria-hidden="true">首页</span></a></li>'.format(
                self.query_dict.urlencode())]

        # 首页
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.param, [self.page - 1])
            prev_page = '<li><a href="?{}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.param, [1])
            prev_page = '<li class="disabled"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        page_str_list.append(prev_page)
        for i in range(start_page, stop_page):
            self.query_dict.setlist(self.param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page:
            self.query_dict.setlist(self.param, [self.page + 1])
            next_page = '<li><a href="?{}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                self.query_dict.urlencode())
        else:
            next_page = '<li class="disabled"><a aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        page_str_list.append(next_page)

        # 尾页
        page_str_list.append(
            '<li><a href="?page={}" aria-label="尾页"><span aria-hidden="true">尾页</span></a></li>'.format(
                self.total_page))

        # 跳转
        jump_li = """
            <li style="display: inline-block; width: 110px;">
                <form method="get">
                    <div class="input-group">
                        <input type="text" name="page" class="form-control" placeholder="跳转">
                        <span class="input-group-btn">
                        <button class="btn btn-default" type="submit">Go!</button>
                    </span>
                    </div>
                </form>
            </li>
            """
        page_str_list.append(jump_li)
        # 将生成的标签传到后端显示 注意要先 from django.utils.safestring import mark_safe
        # 然后用传到后端的数据要用mark_safe这个函数处理一下才可以传给后端 否则只会显示一堆标签字符串 浏览器并不会渲染
        page_string = mark_safe(''.join(page_str_list))
        return page_string

# --END--
