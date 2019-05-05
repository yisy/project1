# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from apps.blog.models import Person


def index(request):
    dict = {}
    dict['err'] = "fdsafd"
    dict['myName'] = ""
    return render(request,"login.html",dict)


def add(request):
    username = request.POST.get('username')
    age = request.POST.get('age')

    p = Person(username=username, age=age)
    p.save()

    persons = Person.objects.all()
    dict = {}
    dict['persons'] = persons

    return render(request,"login.html",dict)
# Create your views here.
