# -*- coding: utf-8 -*-
# @CreateTime : 2023/5/15 015 19:20
# @Author : 瑾瑜@20866
# @IDE : PyCharm
# @File : PycharmProject/pagination.py
# @Description : 
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @Site : https://github.com/wephiles

import copy
from django.utils.safestring import mark_safe


class Pagination(object):
    """自定义的分页组件的实现

    使用分页组件，使用方法如下
    ---------------------

    views.py
    --------
        def pretty_number_list(request):
            # # 根据自己的情况筛选自己的数据
            query_set = models.PrettyNumber.objects.all()

            # # 实例化分页对象
            page_object = Pagination(request, query_set)

            context = {
                'queryset': page_object.page_query_set,  # 分完页的数据
                'page_string': page_object.html(),  # 页码
            }
            return render(request,
                          "pretty_number_list.html",
                          context)
    HTML页面中
    ---------
    # 展示在表中
    {% for item in queryset %}
        {{ item.xxx }}
    {% endfor %}

    # 分页
    <ul class="pagination clearfix">
        {{ page_string }}
    </ul>
    """

    def __init__(self, request, query_set, page_param="page", page_size=10, plus=5):
        """
        Parameters
        ----------
        request: 请求对象
        query_set: 查询到的符合条件的数据，需要据此进行分页处理
        page_param: 在url中通过get方法获得的分页参数 例如： /pretty/number/list/?page=1
        page_size: 每页显示多少条数据
        plus: 显示当前页面的前几页和后几页
        """

        # 为了让搜索 + 分页能够拥有正常的操作逻辑，需要使用copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True  # 为了让get_object.urlencode()能够被修改 其默认是不可修改的
        query_dict.setlist('page', [11])
        self.query_dict = query_dict
        # get_object.urlencode(): 能够显示出当前页面网址所有的参数
        self.page_param = page_param

        # page 是通过get方法传过去的当前页码数
        page = request.GET.get(page_param, "1")  # 后面参数表示默认值为1
        if page.isdecimal():
            # 如果是10进制的数
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        # 一页显示多少数据
        self.start = (page - 1) * self.page_size
        self.end = page * self.page_size

        # 从数据库中获取一页能够显示的数据
        self.page_query_set = query_set[self.start: self.end]

        # 总共有多少条数据
        total_count = query_set.count()
        self.total_count = total_count
        # 计算页码数
        total_page, div = divmod(self.total_count, self.page_size)
        # div不等于0说明 数据在上一页显示不完 只能在下一页显示 例如，倒数第二页时60页，这一页有十条数据
        # 但是第61页只有5条数据，最后的五条数据放在第61页
        if div:
            total_page += 1
        self.total_page = total_page
        self.plus = plus

    def html(self):
        """

        Returns
        -------

        """
        page_str_list = []

        # 计算出 显示当前页面的前五页 后五页
        if self.total_page <= 2 * self.plus + 1:
            # 数据库中的数据比较少，页码能在一页显示，没有达到11页
            start_page = 1
            end_page = self.total_page
        else:
            # 数据比较多
            if self.page <= self.plus:
                # 小极值，当前所在页面小于等于5，直接展示，不让显示-1 -2 -3 ...
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页面 > 5
                # 当前页面+5 > 总页面
                if (self.page + self.plus) > self.total_page:
                    start_page = self.page - self.plus
                    end_page = self.total_page
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        # 上一页 下一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            previous_page = '<li><a href="?{}" ' \
                            'aria-label="Previous"><span aria-hidden="true">' \
                            '«</span></a></li>'.format(self.query_dict.urlencode())
        else:
            previous_page = '<li class="disabled"><span href="" ' \
                            'aria-label="Previous"><span aria-hidden="true">' \
                            '«</span></span></li>'
        if self.page < self.total_page:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            next_page = '<li><a href="?{}" ' \
                        'aria-label="Next"><span aria-hidden="true">' \
                        '»</span></a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page])
            next_page = '<li class="disabled"><span href="" ' \
                        'aria-label="Next"><span aria-hidden="true">' \
                        '»</span></span></li>'
        # 页码
        self.query_dict.setlist(self.page_param, [1])
        # 首页
        first_page = '<li><a href="?{}" ' \
                     'aria-label="Previous"><span aria-hidden="true">' \
                     '首页</span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(first_page)
        page_str_list.append(previous_page)
        for i in range(start_page, end_page + 1):
            # 如果是当前样式，那么加一个样式 - 显示出这一页
            if i == self.page:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)
        page_str_list.append(next_page)
        self.query_dict.setlist(self.page_param, [self.total_page])
        the_end_page = '<li><a href="?{}" ' \
                       'aria-label="Previous"><span aria-hidden="true">' \
                       '尾页</span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(the_end_page)

        search_string = """
        <li>
            <div style="width: 110px; display: inline-block;">
                <form method="get">
                    <div class="input-group">
                        <input type="text" name="page" class="form-control" placeholder="页码">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">跳转</button>
                        </span>
                    </div>
                </form>
            </div>
        </li>"""
        page_str_list.append(search_string)
        page_string = mark_safe(''.join(page_str_list))

        return page_string

# END
