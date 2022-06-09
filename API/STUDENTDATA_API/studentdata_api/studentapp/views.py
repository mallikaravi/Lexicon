from django.shortcuts import render
import requests
import json

def home(request):
      response = requests.get('http://127.0.0.1:8000/students/').json()
      
      return render(request,'studentapp/home.html',{'students':response})


