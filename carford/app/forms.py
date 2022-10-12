import datetime
from dataclasses import field
from django import forms
from .models import Person, Vehicle

class DateInput(forms.DateInput):
    input_type = 'date'
    

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        exclude = ['sale_opportunity']
    
    name = forms.CharField(required=True)
    birth = forms.DateField(initial=datetime.date.today, required=True, widget=DateInput)
    document = forms.CharField(required=True)
    email = forms.EmailField(required=True, help_text='A valid e-mail address, please.')
    phone = forms.CharField(required=True)

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
    
class VehicleEditForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'plate', 'year', 'color', 'model_vehicle']
    
        