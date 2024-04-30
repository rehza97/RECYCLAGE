from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from collecteur.models import *
from .models import *
# Create your views here.
def categories(request):
    all_categories = Category.objects.all()
   
    context = {
        'all_categories': all_categories
    }
    return render(request, 'vendeur/categories.html', context)


def products(request,slug):
    category_needed = Category.objects.get(slug=slug)
    category_id = category_needed.pk
    products = Product.objects.filter(category=category_id)  
    print('____________________________')
    print(products)

    

    context = {
        'products' :products
    }
    return render(request,'vendeur/products.html',context)

def details(request, id): 
    product = Product.objects.get(pk=id)
    context = {
        'product': product
    }
    return render(request, 'vendeur/details.html', context)

def _poubelle_id(request):
    cart = request.session.session_key
    if not cart:
        request.session.create()
        cart = request.session.session_key
    return cart


def add_poubelle(request, product_id):
    product = Product.objects.get(pk=product_id)
    try:
        poubelle = Poubelle.objects.get(poubelle_id=_poubelle_id(request))
    except Poubelle.DoesNotExist :
        poubelle  = Poubelle.objects.create(
            poubelle_id = _poubelle_id(request)
        )
    poubelle.save()

    try:
            poubelleitem = PoubelleItem.objects.get(product=product, poubelle=poubelle)
            poubelleitem.quantity +=1
            poubelleitem.save()
    except PoubelleItem.DoesNotExist:
        poubelleitem = PoubelleItem.objects.create(
            product = product,
            quantity = 1,
            poubelle = poubelle
        )
        poubelleitem.save()
    print('__________________________________________________')
    print(f'categories/{product.category.slug}')
    return redirect('vendeur:products',product.category.slug)

def poubelle(request,total=0,quantity=0, poubelle_items=None):
    try:
        poubelle = Poubelle.objects.get(poubelle_id=_poubelle_id(request))
        poubelle_items = PoubelleItem.objects.filter(poubelle=poubelle)
        for item in poubelle_items:
            total +=(item.quantity * item.product.price_per_kilo)
            quantity += item.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'poubelle_items': poubelle_items
    }
    return render(request, 'vendeur/poubelle.html', context)