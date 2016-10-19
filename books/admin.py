#-*- coding:utf8 -*-
from django.contrib import admin

# Register your models here.
from books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    # 列表界面显示字段
    list_display = ('first_name', 'last_name', 'email')
    # 列表界面显示检索项
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    # 列表界面显示字段
    list_display = ('title', 'publisher', 'publication_date')
    # 列表界面显示检索项 右边出现按照publication_date字段的过滤器
    list_filter = ('publication_date',)
    # 列表顶端会有一个逐层深入的导航条
    date_hierarchy = 'publication_date'
    # 在publication_date字段上面使用降序
    ordering = ('-publication_date',)
    # 指定编辑界面显示可编辑的字段
    fields = ('title', 'authors', 'publisher', 'publication_date')
    # authors对应BOOK来说是多选，这里新增一个过滤器  多对多字段 使用filter_horizontal
    filter_horizontal = ('authors',)
    # 下来字段显示的内容可能会过多，加载时间长，这里使用跳转文本形式进行选择，再返回主界面
    raw_id_fields = ('publisher',)
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)