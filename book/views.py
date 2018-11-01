import json

from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect


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

    # # 1.接收json数据
    # body = request.body
    # # print(body)
    #
    # # 2.对body进行编码
    # body_str = body.decode()
    # print(body_str)
    #
    # # 3. 对json字符串进行处理 json.dumps() 将字典转换为字符串,
    # # json.loads() 将字符串转换为字典
    # import json
    # params = json.loads(body_str)
    # print(params)


    ############################header###############################

    # # 可以通过request.META属性获取请求头headers中的数据，request.META为字典类型
    # # print(request.META)
    # content_type = request.META.get('CONTENT_TYPE')
    # print(content_type)
    #
    # # 自定义请求头信息，需要在postman中设置请求头，例如：name 为 xxx，
    # #     系统会把name变为大写NAME，再加上HTTP_，变为HTTP_NAME，打印便可得到xxx
    # name = request.META.get('HTTP_NAME')
    # print(name)
    #
    # print(request.method)
    #
    # # user
    # # 我们请求的时候，没有用户信息，django会自动给我们分配一个 匿名用户 --》AnonymousUser
    # # 如果我登录了 会返回给我登录用户的信息
    #
    # print(request.user)


    ############################响应###############################

    # dict = {
    #     'name':'itcast'
    # }
    #
    # # import json 导入的是最后一个json
    # data = json.dumps(dict)
    #
    # return HttpResponse(data,content_type='application/json')

    return redirect('http://www.itheima.com')

    from django.http.response import JsonResponse
    dict = {
        'name': 'itheima'
    }

    list = [
        {
            'name': 'itheima'
        }, {
            'name': 'aaaa'
        }
    ]

    # safe=True
    # 　jsonresponse 可以安全的将字典转换为ｊｓｏｎ数据
    # 如果我们传递过来是一个非字典，这个时候 系统就不负责保证能够转换为json
    # safe=False 就相当于我们对这个代码负责

    return JsonResponse(list, safe=False)

    # response = HttpResponse(content=,content_type=,status=)
    # content =,  返回的内容
    # content_type
    # 值： application/json       image/jpeg      image/png   image/gif
    #       text/html   text/css    text/javascript
    # 语法形式： 大类/小类
    # MIME类型

    # status  响应状态码
    # response = HttpResponse(content=,content_type=,status=)


    return HttpResponse('ok', status=500)


def cookie(request):
    # 获取cookie,可以通过HttpResponse对象的COOKIES属性来读取本次请求携带的cookie值
    cookies = request.COOKIES
    print(cookies)

    # 设置cookie的时候 是在响应中设置
    response = HttpResponse('cookie')

    response.set_cookie('name', 'zhangsan')

    # response.delete_cookie('name')

    return response


def session(request):
    # flask中直接设置session，例如：session["is_admin"] = admin.is_admin
    # 而django中是通过HttpRequest对象的session属性进行会话的读写操作,
    #  从视图一开始便有request，方便，
    #  如果用response的话，还要接收，创建，在设置，不方便
    request.session['name'] = 'abc'

    return HttpResponse('session')


# GET 请求 展示注册页面
def get_register_template(request):
    return render()


# POST 实现注册
def register(request):
    pass


def register_func(request):
    if request.method == 'GET':
        # GET 请求 展示注册页面
        return render()
    else:
        # POST 实现注册
        pass


# 如果我们的请求方式多了，代码可读性很差
#  其实我们想做的事情就是 一个请求对应一个业务逻辑


# 类视图的好处：
# 1.代码可读性好
# 2.类视图相对于函数视图有更高的复用性 ， 如果其他地方需要用到某个类视图的某个特定逻辑，直接继承该类视图即可

# 类视图
# 定义
from django.views import View


class RegisterView(View):
    """
    类视图中的方法名 其实就是 http的请求方法名
    """

    def get(self, request):
        return HttpResponse('get')

    # http://127.0.0.1:8000/register/  最后的/必须加，不加就运行不了
    # 原因在于url(r'^register/$', views.RegisterView.as_view()),中是以/结尾的，
    # 如果url(r'^register$', views.RegisterView.as_view())，
    # 便可以访问http://127.0.0.1:8000/register，最后便不用加/
    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')

    # 没有这个方法，所以不能使用这个
    # def lalala(self,request):
    #     return HttpResponse('lalala')

    # 对象方法
    # def abc(self):
    #     pass
    #
    # @classmethod
    # def get_app(cls):
    #     pass
    #
    # @staticmethod
    # def get_demo():
    #     pass

# 个人中心

# GET方法 个人中心的显示
# POST方法 个人中心的修改

# 为类视图添加装饰器
def login_required(func):

    # 下面2行代码等价
    def wrapper(request):
    # def wrapper(request,*args,**kwargs):
        if True:
        # if False:
            # 登录返回函数
            return func(request)
            # return func(request,*args,**kwargs)
        else:
            # 没有登录 返回请登录
            return HttpResponse('请登录')

    return wrapper

# 类视图
class CenterView(View):

    def get(self,request):
        return HttpResponse('个人中心展示')

        # if True:
        #     return HttpResponse('个人中心展示')
        # else:
        #     return HttpResponse('请登录')

    def post(self,request):
        return HttpResponse('个人中心修改')

        # if True:
        #     return HttpResponse('个人中心修改')
        # else:
        #     return HttpResponse('请登录')