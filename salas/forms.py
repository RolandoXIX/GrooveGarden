from django import forms
from django.forms.widgets import SelectDateWidget



class Date(forms.Form):
    date = forms.DateField(label="", widget=SelectDateWidget)