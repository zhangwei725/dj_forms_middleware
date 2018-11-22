# 1.10以上的版本的写法
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Midd1(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # 请求到达视图函数之前执行的方法
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("process_view")

    #  一定要配置 模板语法 当我们调用了template.render()方法才会执行
    def process_template_response(self, request, response):
        print('process_template_response')
        return response

    # 当我视图函数中 出现异常,并且没有处理的情况会触发
    def process_exception(self, request, exp):
        print('process_exception')


# 兼容1.10以下的版本 (推荐)
# 请求阶段
# process_request
# process_view
# 响应阶段
#  process_response

class Midd2(MiddlewareMixin):
    # 在请求到达 路由之前执行的方法
    def process_request(self, request):
        if not request.META['HTTP_HOST'] in ['127.0.0.1:8000']:
            return HttpResponse('没有钱你还进高级会所!!!!!!! 滚!!!')
        else:
            print('process_request2')

    # 请求到达视图函数之前执行的方法
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("process_view2")

    #  一定要配置 模板语法 当我们调用了template.render()方法才会执行
    def process_template_response(self, request, response):
        print('process_template_response2')
        return response

    # 当我视图函数中 出现异常,并且没有处理的情况会触发
    def process_exception(self, request, exp):
        print('process_exception')

        # 当我视图函数中 出现异常,并且没有处理的情况会触发

    # 在视图函数响应之后的执行的方法
    def process_response(self, request, response):
        print('process_response2')
        return response


class Midd3(MiddlewareMixin):
    # 在请求到达 路由之前执行的方法
    def process_request(self, request):
        if not request.META['HTTP_HOST'] in ['127.0.0.1:8000']:
            return HttpResponse('没有钱你还进高级会所!!!!!!! 滚!!!')
        else:
            print('process_request3')

    # 请求到达视图函数之前执行的方法
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("process_view3")

    #  一定要配置 模板语法 当我们调用了template.render()方法才会执行
    def process_template_response(self, request, response):
        print('process_template_response')
        return response

    # 当我视图函数中 出现异常,并且没有处理的情况会触发
    def process_exception(self, request, exp):
        print('process_exception3')
        # 当我视图函数中 出现异常,并且没有处理的情况会触发

    # 在视图函数响应之后的执行的方法
    def process_response(self, request, response):
        response = HttpResponse('队友被抓,边笑边刷')
        return response

# 肉搏
