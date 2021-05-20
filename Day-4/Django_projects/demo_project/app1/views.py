from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse # one tempalte

# Create your views here.
def demo(request):
    return HttpResponse("<h1 style=color:green;>Hello i am from Demo funtion</h1>")