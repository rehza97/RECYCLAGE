from django.shortcuts import render
from .models import *
from .form import *
# Create your views here.
def addProd(request):
    form = addproduit()

    if  request.method == 'POST':
        form = addproduit(request.POST, request.FILES)
        if form.is_valid():
           
            sv = form.save(commit = False)
            sv.totalPrice = sv.weight * sv.price_per_kilo
            sv.save()
    
    context = {
        'form' : form
    }
    return  render(request, 'test.html',context)