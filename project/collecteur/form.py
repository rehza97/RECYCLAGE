from django import forms
from .models import *


class addproduit(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','image','category','type','weight','price_per_kilo','desc']

class Updateproduit(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','image','category','type','weight','price_per_kilo','desc']

class addCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','banner']

class UpdateCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','banner']