# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from apps.blog.models import Person
from django.core.paginator import Paginator

def index(request):
    dict = {}

    p = Person.objects.all()
    paginator = Paginator(p,3)
    page = request.GET.get('page')

    if page == None:
        page = 1
    print(page)
    peoples = paginator.page(page)

    dict['peoples'] = peoples
    return render(request, "login.html", dict)


def add(request):
    username = request.POST.get('username')
    age = request.POST.get('age')

    p = Person(username=username, age=age)
    p.save()

    return render(request, "login.html")
# Create your views here.
