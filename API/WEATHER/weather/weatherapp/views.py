from django.shortcuts import render
import requests
import json
import geocoder
import urllib
# Create your views here.


# def weather(request):
#     g = geocoder.ip('me')
#     lat=g.latlng[0]
#     lon=g.latlng[1]
#     print(lat)
#     print(lon)
#     city=g.city
#     print(city)
#     #degree_sign = u'\N{DEGREE SIGN}'
#     source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat='+str(lat)+'&lon='+str(lon)+'&units=metric&exclude=hourly,daily&appid=e2dc60e9ba365003592dbdf52cbdac40').read()
#     #weather_info['current']['dt']
    
#     weather_data=json.loads(source.decode('utf-8'))
#     print(weather_data)
#     context={'latlng':g.latlng,
#              'city':g.city,
#             'temp':str(weather_data['current']['temp'])+'C',
#             'status':str(weather_data['current']['weather'][0]['main']) + '(' +
#                                         str(weather_data['current']['weather'][0]['description']) +')'
             
            
#     }
#     return render(request,'weather.html',context)

# def weather(request):

#     response= geocoder.ipinfo()

#     current_city=response.city


#     source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + current_city + '&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1').read()

       

#     list_of_data = json.loads(source.decode('utf-8'))


#     print(list_of_data)

        
#     context =   {

#                 'city': current_city,

#                 'temperature': list_of_data['main']['temp'],

#                 'description': list_of_data['weather'][0]['description'],

#                 'icon' : list_of_data['weather'][0]['icon']

               

               

                           

#             }

#     return render(request, 'weather.html', context)


#Another method
def new(request):
       response=requests.get("https://ipinfo.io/json?")
       #print(response.json())
       data = response.json()
       city = data['city']
       print(city)
       res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1')
       weather_data = res.json()
       print(weather_data)
       context =   {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon' : weather_data['weather'][0]['icon']
            }
       return render(request, 'weather.html', context)

   






