from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import employees
from webapp.serializers import employeeSerializer


class employeeList(APIView):
    def get(self, request):
        employees1=employees.objects.all()
        serializer=employeeSerializer(employees1,many=True)
        return Response(serializer.data)

    def post(self):
       pass 
    


