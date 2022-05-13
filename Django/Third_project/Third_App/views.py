from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'Third_App/index.html',{'insert_me':'Hello World!'})
    
def help(request):
    my_dict={'insert_me':'Help Page!'}
    return render(request,'Third_App/help.html',context=my_dict)


