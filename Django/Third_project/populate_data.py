
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Third_project.settings')

import django
django.setup()
import random

from Third_App.models import Student,School
from faker import Faker

faker=Faker()

schools=['ABC','RET','AQW','TRY']



def add_School():
    fake_address=faker.address()
    fake_email=faker.email()
    fake_phonenumber=faker.phone_number()
    s = School.objects.get_or_create(name=random.choice(schools),address=fake_address, email=fake_email, phone_number=fake_phonenumber)[0]
    s.save()
    return s

def populate(N=10):
    for entry in range(N):
        school_name=add_School()
        fake_name=faker.name()
        fake_age=faker.phone_number()

        student=Student.objects.get_or_create(school=school_name,name=fake_name,age=fake_age)

if __name__=='__main__':
    populate(10)

