from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
cart
主键
商品的图片   商品的名称   商品价格


"""
'''
验证登录
验证登录跳转的链接
1.在装饰器上使用
2.全局验证登录跳转的链接
'''
@login_required
def add_car(request):
    return HttpResponse('111')
    pass


def list_car(request):
    pass


def update_car(request):
    pass


def delete_car(request):
    pass
