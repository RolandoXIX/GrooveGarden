from django import forms
from django.forms.widgets import SelectDateWidget
from functools import partial


DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class Date(forms.Form):
    date = forms.DateField(label="", widget=DateInput())