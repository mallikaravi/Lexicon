from django.db import models

# Create your models here.

class FormModel(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=225)
    phonenumber = models.IntegerField()

    def __str__(self):
       return self.firstname    