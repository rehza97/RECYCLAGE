from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from collecteur.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.
@login_required(login_url="users:login")
def categories(request):
    all_categories = Category.objects.all()
   
    context = {
        'all_categories': all_categories
    }
    return render(request, 'vendeur/categories.html', context)

@login_required(login_url="users:login")
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

@login_required(login_url="users:login")
def details(request, id): 
    product = Product.objects.get(pk=id)
    context = {
        'product': product
    }
    return render(request, 'vendeur/details.html', context)



@login_required(login_url="users:login")
def add(request, id):
    current_url = request.build_absolute_uri()
    print("Current URL:", current_url)
    
    if request.method == "POST":
        product = Product.objects.get(id=id)
        quantity = int(request.POST['quantity'])  # Convert quantity to an integer
        print(quantity)
        price = Decimal(quantity) * product.price_per_kilo  # Calculate total price
        
        # Get or create AllCommandes object for the current user
        mycommands, created = AllCommandes.objects.get_or_create(
            user=request.user
        )
        
    
        # Create or get the VendeurCommande object for the current user and product
        command, created = VendeurCommande.objects.get_or_create(
            produit=product,
            user=request.user,
            defaults={'quantity': 0}  # Default quantity is 0
        )
        
        # Update the quantity and price of the VendeurCommande object
        command.quantity += quantity
        command.price = price
        
        try:
            command.save()
        except IntegrityError:
            # Handle the case if saving the command fails due to IntegrityError
            # For example, if there's a unique constraint violation
            pass
        
        # Add the VendeurCommande object to the user's AllCommandes
        mycommands.commandes.add(command)
        
        # Update the total price of the AllCommandes object
        mycommands.totalPrice = sum(cmd.price for cmd in mycommands.commandes.all())
        mycommands.save()
    
    return redirect('vendeur:details', id=id)

@login_required(login_url="users:login")
def poubelle(request):
    poubelle = AllCommandes.objects.get(user=request.user)
    poubelle =poubelle.commandes.all()
    items = []
    for  item in poubelle:
        items.append(item)
    
    print(items)
    context = {
        'poubelle': poubelle,
        'items': items
    }
    return render(request, 'vendeur/poubelle.html', context)

@login_required(login_url="users:login")
def deletefrompoubelle(request,id):
    command = VendeurCommande.objects.filter(pk=id , user=request.user)
    command.commandes.remove(command)

@login_required(login_url="users:login")
def delete_from_poubelle(request, id):
    # Fetch the command object
    command = get_object_or_404(VendeurCommande, pk=id, user=request.user)
    
    # Remove the command from the commandes Many-to-Many field
    command.allcommandes_set.clear()  # Assuming allcommandes_set is the related name
    command.delete()
    return redirect('vendeur:poubelle')


@login_required(login_url="users:login")    
def sendCommand(resqust):
    command = AllCommandes.objects.get(user=resqust.user)
    if not command.placed:
        command.placed = True
        command.save()
    
    return redirect('vendeur:categories')