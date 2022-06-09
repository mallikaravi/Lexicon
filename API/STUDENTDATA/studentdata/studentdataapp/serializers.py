from rest_framework import serializers
from studentdataapp.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields ='__all__'
