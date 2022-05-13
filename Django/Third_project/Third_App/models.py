
from django.db import models

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=225,blank=False)
    address=models.CharField(max_length=250,blank=False)
    email=models.CharField(max_length=250,blank=False)
    phone_number=models.CharField(max_length=250,blank=False)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=225,blank=False)
    age=models.CharField(max_length=3,blank=False)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

