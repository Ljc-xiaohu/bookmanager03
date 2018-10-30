from django.http import HttpResponse
from django.shortcuts import render, reverse


# Create your views here.
def index(request):
    # 获取路径的时候 ，就可以通过名字来获取
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

# def demo1_book(request,category_id,book_id):
def demo1_book(request, book_id, category_id):
    # print(category_id,book_id)

    ############################GET 查询字符串###############################

    # # flask中获取参数使用的是request.args，django中使用下面的方式
    # args = request.GET
    # print(args)
    # a = args.get('a')  # a=python&b=100&a=20000
    # # 如果出现一键多值 get方式会获取 最后一个值
    # b = args['b']
    # # print(a, b)
    #
    # # QueryDict 也是字典，但是 它在获取一键一值的时候使用的是get()
    # # 获取一键多值的时候使用的是 getlist()
    #
    # alist = args.getlist('a')
    # print(alist)

    ############################POST  表单 ###############################

    # form = request.POST
    # print(form)
    #
    # a = form.get('a')
    # alist = form.getlist('a')
    #
    # print(a,alist)


    ############################POST  JSON###############################

    # 1.接收json数据
    body = request.body
    # print(body)

    # 2.对body进行编码
    body_str = body.decode()
    print(body_str)

    # 3. 对json字符串进行处理 json.dumps() 将字典转换为字符串,
    # json.loads() 将字符串转换为字典
    import json
    params = json.loads(body_str)
    print(params)

    return HttpResponse('ok')
