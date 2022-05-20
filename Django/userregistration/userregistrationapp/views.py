from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from userregistrationapp.forms import signUpForm
# Create your views here.


def index(request):
    return render(request,'userregistrationapp/index.html')

def  signup_view(request):
    form= signUpForm()
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request,'userregistrationapp/thankyou.html')
              
    return render(request,'userregistrationapp/signup.html',{'form':form})

def thankyou(request):
    return render(request,'userregistrationapp/')



    