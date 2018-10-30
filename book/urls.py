from django.conf.urls import url

from . import views

urlpatterns = [

    # 参数1： 正则
    # 参数2： 视图函数名
    # url的第三个参数就是： name

    url(r'^index/$', views.index, name='enenen'),

    # 正则分组 （）
    # 位置参数： 是根据正则的分组 来进行 视图函数变量的赋值
    # url(r'^(1)/(100)/$', views.demo1_book)
    url(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', views.demo1_book),

    url(r'^cookie/$',views.cookie),
]
