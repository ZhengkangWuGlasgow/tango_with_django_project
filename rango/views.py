from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# 创建一个叫做index的试图
def index(request):
    return HttpResponse("Rango says hey there partner")