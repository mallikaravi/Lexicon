from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import User
# Create your views here.


def index(request):
    my_dict={'insert_me':"My Second App"}
    return render(request,'AppTwo\index.html',context=my_dict)


def users(request):
    user_list = User.objects.order_by('first_name','last_name','email')
    user_dict = {'user_records': user_list}
    return render(request,'AppTwo/users.html',context=user_dict)    