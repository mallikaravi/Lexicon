from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'demoapp/home.html',{'name':'Mallika'})


def add(request):

    val1= request.POST.get('num1')
    val2= request.POST.get('num2')
    res = val1+val2

    return render(request, 'demoapp/result.html',{'result':res})
