

from django import forms
from basicapp.models import FormModel
#from django.core import validators

class FormName(forms.ModelForm):

    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    phonenumber = forms.IntegerField()

    class Meta:
        model = FormModel
        fields = "__all__"

    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

   