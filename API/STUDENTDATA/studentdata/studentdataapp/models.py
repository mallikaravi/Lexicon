from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField( max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    grade=models.CharField( max_length=10)
    course=models.CharField(max_length=20)
    college=models.CharField(max_length=20)


def __str__(self):
     return self.firstname
