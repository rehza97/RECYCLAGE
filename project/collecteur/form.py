from django import forms
from .models import *


class addproduit(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','image','category','type','weight','price_per_kilo','desc']