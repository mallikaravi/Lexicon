from rest_framework import serializers
#from rest_framework import employees
from webapp.models import employees


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        #fields={"firstname","lastname"}
        fields= '__all__'