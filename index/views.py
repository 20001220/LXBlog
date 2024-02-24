from django.shortcuts import render, HttpResponse


# Create your views here.
def indextwo(request):
    return HttpResponse("hello world!")


def user_add(request):
    return HttpResponse("用户添加")


def user_del(request):
    return HttpResponse("用户删除")


# 导入render，一般django默认
from django.shortcuts import render


def user_list(request):
    # 第一个位子是视图函数的request参数，第二个参数位是html文件路径
    from index.models import UserInfo
    all_data = UserInfo.objects.all()
    return render(request, "user_list.html", {"user_list": all_data})


def temp_learn(request):
    b3 = [2, 36, 99]
    return render(request, "templates_learn.html", {"a": 2, "b": b3})


def testVue(request):
    return render(request, "testVue.html")


def index(request):
    return render(request, "index.html")
