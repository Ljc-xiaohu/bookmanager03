# 在flask中 叫钩子函数
# 在django中叫中间层

"""
Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，
修改Django的输入或输出。中间件的设计为开发者提供了一种无侵入式的开发方式，
增强了Django框架的健壮性。
我们可以使用中间件，在Django处理视图的不同阶段对输入或输出进行干预。

中间件的定义方法:
定义一个中间件工厂函数，然后返回一个可以被调用的中间件。
中间件工厂函数需要接收一个可以调用的get_response对象。
返回的中间件也是一个可以被调用的对象，
并且像视图一样需要接收一个request对象参数，返回一个response对象。
"""

def my_middleware(get_response):
    # One-time configuration and initialization.
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    #  相当于 flask 的 before_first_request
    print('before_first_request')

    def middleware(request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # 此处编写的代码会在每个请求处理视图前被调用。
        # 这里相当于 flask的 before_request
        print('before_request')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        # 此处编写的代码会在每个请求处理视图之后被调用。
        # 这里相当于 flask的 after_request
        print('after_request')

        return response

    return middleware

"""
执行结果：（其中before_first_request  2次，原因在于Debug=True）
before_first_request
before_first_request
before_request
after_request
"""

def my_middleware2(get_response):
    # One-time configuration and initialization.
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    #  相当于 flask 的 before_first_request
    print('before_first_request2222222222222')

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # 此处编写的代码会在每个请求处理视图前被调用。
        # 这里相当于 flask的 before_request
        print('before_request2222222222222')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        # 此处编写的代码会在每个请求处理视图之后被调用。
        # 这里相当于 flask的 after_request
        print('after_request222222222222')

        return response

    return middleware

"""
执行结果：
before_request
before_request2222222222222
after_request222222222222
after_request

原因：
    多个中间件的执行顺序为：
    在请求视图被处理前，中间件由上至下依次执行，按照注册的顺序来执行
    在请求视图被处理后，中间件由下至上依次执行，按照注册的顺序反过来来执行

    settings.py文件中的注册顺序为：
    'book.bookmiddleware.my_middleware',
    'book.bookmiddleware.my_middleware2',
"""