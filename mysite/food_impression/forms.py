from .models import Food, Company, Kind
from django import forms
class FoodFormAdd(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['company', 'kind', 'name','taste','value','remarks']

class CompanyFormAdd(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

class KindFormAdd(forms.ModelForm):
    class Meta:
        model = Kind
        fields = ['kind']