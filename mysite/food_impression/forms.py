from .models import Food
from django import forms
class FoodFormAdd(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['company', 'kind', 'name','taste','value','remarks']