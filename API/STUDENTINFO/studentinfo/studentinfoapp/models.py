from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age=models.IntegerField()

    course=models.CharField(max_length=20)
    college=models.CharField(max_length=20)

    def __str__(self):
        return self.name