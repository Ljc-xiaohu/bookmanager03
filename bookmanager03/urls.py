"""bookmanager03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 男： 张三
    # 女： 张三
    # 在工程的url中，通过设置include的第二个参数，添加一个 namespace参数来，分割不同的name
    # namespace 一般采用子应用的名字
    # 添加了 namespace之后的url名字就升级为了： namespace:name
    #                                                 book:enenen
    url(r'^', include('book.urls',namespace='book')),
]
