from django.shortcuts import render

from userregistrationapp import forms
# Create your views here.


def index(request):
    return render(request,'userregistrationapp/index.html')

def  signup_view(request):
    form = forms.FormName()
    return render(request,'userregistrationapp/signup.html',{'form':form})