from django.conf.urls import url

from book.views import login_required
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

    url(r'^cookie/$', views.cookie),

    # url的第二个参数： 视图函数名
    # 配置路由时，使用类视图的as_view()方法来添加
    # views.RegisterView.as_view() 就是一个视图函数名
    url(r'^register/$', views.RegisterView.as_view()),

    # url(r'^center/$',views.CenterView.as_view()),

    # views.CenterView.as_view() 视图函数名
    # login_required(),在URL配置中装饰器
    # url(r'^center/$',login_required(views.CenterView.as_view())),

    # 使用method_decorator将其转换为适用于类视图的装饰器的url配置
    url(r'^center/$',views.CenterView.as_view()),
]
