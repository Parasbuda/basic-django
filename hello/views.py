from django.shortcuts import render
from django.http import HttpResponse
from .templates import hello
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def paras(request):
    return HttpResponse("Hello! Paras")

def greet(request,name):
    return render(request,"hello/greet.html",{"name":name.capitalize()})