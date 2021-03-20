from django import forms
from .models import *
from django.forms import fields

class studentform(forms.ModelForm):
    dob = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = student
        fields = '__all__'
        