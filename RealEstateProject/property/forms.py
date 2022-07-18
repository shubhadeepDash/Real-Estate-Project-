from importlib.abc import ExecutionLoader
from msilib.schema import Property
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Property


class PropertySellForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['longitude', 'latitude', 'created']