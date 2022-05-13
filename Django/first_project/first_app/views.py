from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import Topic,AccessRecord, Webpage
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    #my_dict={'insert_me':"Hello i am from first_app/index.html!"}
   #return HttpResponse("Hello World!")
    date_dict = {'access_records': webpage_list}
    return render(request,'first_app/index.html',context=date_dict)