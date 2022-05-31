from django.shortcuts import render
import requests
import json

# Create your views here.
def users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    users = response.json()
    #print(users)

    return render(request,"users.html",{'users':users})
    
    