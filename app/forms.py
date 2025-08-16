from django import forms
from .models import people

class peopleForm(forms.ModelForm):
    class Meta:
        model = people
        fields = '__all__'
        exclude = ['imc','state']