import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')


import django
django.setup()
import random


from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

#create object to fakerclass"
fake = Faker()

#Defining the topics array
topics =  ['Search','Social','Marketplace','News', 'Order']


def get_create_topic():
    #Generating the Fake Topic Model data 
    T = Topic.objects.get_or_create(top_name=random.choice(topics))[0]

    #Sving/populating the topic into database
    T.save()
    return T

def populate(n):

    for i in range(n):
        # Creating and getting the Topic Model
        topic_obj=get_create_topic()
        
        # Fake Webpage Model data
        fake_name=fake.name()
        fake_url=fake.url()

        # Saving/Creating and Getting the Webpage model
        webpage_object = Webpage.objects.get_or_create(topic=topic_obj,name=fake_name,url=fake_url)[0]
        
        #Fake AccessRecord Model data
        fake_date=fake.date()
        # Saving/Creating and Getting the AccessRecord model
        accessrecord_obj = AccessRecord.objects.get_or_create(name=webpage_object,date=fake_date)[0]




if __name__=='__main__':
    populate(15)


    #HTTP - Hypertext Transfer protocol
    #GEt - request data from resource
    #POST - submit data to be processed