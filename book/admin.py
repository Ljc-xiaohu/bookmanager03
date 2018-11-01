from django.contrib import admin
from .models import BookInfo, PeopleInfo

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    # list_display 列表显示
    # title 是在models中定义的方法，就是为了增加一个字段名
    list_display = ('name','id','readcount','title')

    # 使动作在下面
    actions_on_top = False
    actions_on_bottom = True

    search_fields = ['name']

    list_filter = ['name']


    ###############
    # fields = ['name']
    # fields 和 fieldsets是互斥的

    fieldsets = (
        ('基本', {'fields': ['name', 'pub_date']}),
        ('高级', {
            'fields': ['readcount', 'commentcount'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )

#注册书籍模型
# admin.site.register(BookInfo)
# 加上BookInfoAdmin，是为了关联BookInfoAdmin，在页面的显示
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'