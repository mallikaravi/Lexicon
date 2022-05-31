from django.shortcuts import render
import urllib.request
import json

# Create your views here.


def home(request):
    if request.method =='POST':
        city = request.POST.get('city','True')
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=imperial&appid=e2dc60e9ba365003592dbdf52cbdac40').read()
        
        #source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=7073355725546b0c7e4ebaa5aef00979').read()


    
        #list_of_data =json.loads(source)
        #print(list_of_data)
        list_of_data=json.loads(source.decode('utf-8'))
  
        context = {
            'city' :city,
            'country_code':str(list_of_data['sys']['country']),
            'coordinates':str (list_of_data['coord']['lon'])+ ''
            + str (list_of_data['coord']['lat']),
            'temp':str(list_of_data['main']['temp'])+ 'k',
            'pressure' :str(list_of_data['main']['pressure']),
            'humidity':str(list_of_data['main']['humidity']),
        }

    else:
        context={}   

    return render(request,'home.html',context)


