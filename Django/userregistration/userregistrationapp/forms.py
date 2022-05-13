from socket import fromshare
from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    address =forms.CharField(widget=forms.addressarea)
    phonenumber=forms.IntegerField()