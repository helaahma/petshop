from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class NotavailableForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields=['name','age','image', 'price']