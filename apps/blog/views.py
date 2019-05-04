# coding:utf-8

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dict = {}
    dict['err'] = "fdsafd"
    dict['myName'] = ""
    return render(request,"login.html",dict)


def add(request):
    print(request.POST.get('username'))
    print(request.POST.get('password'))
    return HttpResponse("fds")
# Create your views here.
