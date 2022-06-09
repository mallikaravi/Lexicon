from django.http import JsonResponse
from studentinfoapp.models import Student
from studentinfoapp.serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



# Create your views here.

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return JsonResponse({'students':serializer.data})

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def student_detail(request,id):
    try:
        student=Student.objects.get(pk=id)

    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method== 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)