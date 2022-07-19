
from django import forms
from django.contrib.auth.models import User
from .models import Property


class PropertySellForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['longitude', 'latitude', 'created']