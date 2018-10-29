from django.http import HttpResponse
from django.shortcuts import render, reverse


# Create your views here.
def index(request):

    #获取路径的时候 ，就可以通过名字来获取
    # path = reverse('enenen')
    # 添加了namespace之后，名字就升级为了： namespace:name
    path = reverse('book:enenen')
    print(path)
    # path = 'browershistories/'
    # redirect(path)

    return HttpResponse('ok')

# http://ip:port/分类的id(category_id)/书籍id(book_id)/
# http://ip:port/1/100/

# 如果参数比较多的时候，我们的顺序很有可能写错了

def demo1_book(request,category_id,book_id):
    print(category_id,book_id)
    return HttpResponse('ok')