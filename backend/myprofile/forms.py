from .models import *
from django import forms
from django.forms import TextInput


class Add_City_Form(forms.ModelForm):

    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'input your city'
            
})}
