from django.shortcuts import redirect, render
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from .models import *
from .form import *
from users.models import *
from vendeur.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="users:login")
def home(request):
    vendeurs = User.objects.filter(vendeur=True).count()
    collecteur = User.objects.filter(collecteur=True).count()
    commandes = AllCommandes.objects.filter(placed=True).count()
    context = {
        'commandes': commandes,
        'vendeurs': vendeurs,
        'collecteurs': collecteur
    }
    return render(request, 'collecteur/home2.html', context)

@login_required(login_url="users:login")
def collecteurs(request):
    collecteur = User.objects.filter(collecteur=True)
    context = {
        'collecteurs': collecteur
    }
    return render(request, 'collecteur/collecteurs.html', context)

@login_required(login_url="users:login")
def vendeurs(request):
    vendeur = User.objects.filter(vendeur=True)
    context = {
        'vendeur': vendeur
    }
    return render(request, 'collecteur/vendeurs.html', context)


@login_required(login_url="users:login")
def commandes(request):
    commande = AllCommandes.objects.filter(placed=True, delivered=False)

    context = {
        'commande': commande
    }
    return render(request, 'collecteur/commande.html', context)

@login_required(login_url="users:login")
def pick_command(request,id):
    commande = AllCommandes.objects.get(pk=id)
    collacter = request.user
    commande.selected = True
    commande.celletuer = collacter
    commande.save()
    # ////////////////////////////////////////////////////
    subject = 'Commande Pick Up'
    message = f'Bonjour {commande.user}, \nLa Commande N°{commande.id} a été sélectionnée par {collacter} pour être ramassé'
    email = commande.user.email
    revicer = [email]
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        revicer,
        fail_silently=False,
    )
    # ////////////////////////////////////////////////////
    return redirect('collecteur:commandes')


@login_required(login_url="users:login")
def cancel(request,id):
    commande = AllCommandes.objects.get(pk=id)
    collacter = None
    commande.selected = False
    commande.celletuer = collacter
     # ////////////////////////////////////////////////////
    subject = 'Commande annule'
    message = f'Bonjour {commande.user}, \nLa Commande N°{commande.id} a été annule par {collacter} pour être ramassé'
    email = commande.user.email
    revicer = [email]
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        revicer,
        fail_silently=False,
    )
    # ////////////////////////////////////////////////////
    commande.save()
    return redirect('collecteur:commandes')

@login_required(login_url="users:login")
def delivered(request,id):
    commande = AllCommandes.objects.get(pk=id)
    commande.delivered = True
     # ////////////////////////////////////////////////////
    subject = 'Commande Pick Up'
    message = f'Bonjour {commande.user}, \nLa Commande N°{commande.id} a été recupere par {commande.celletuer} '
    email = commande.user.email
    revicer = [email]
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        revicer,
        fail_silently=False,
    )
    # ////////////////////////////////////////////////////
    commande.save()
    return redirect('collecteur:commandes')

@login_required(login_url="users:login")
def history_commandes(request):
    commande = AllCommandes.objects.filter(delivered=True)
    context = {
        'commande': commande
    }
    return render(request, 'collecteur/old_command.html', context)

@login_required(login_url="users:login")
def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'collecteur/products.html', context)

@login_required(login_url="users:login")
def addProd(request):
    form = addproduit()

    if request.method == 'POST':
        form = addproduit(request.POST, request.FILES)
        if form.is_valid():

            sv = form.save(commit=False)
            sv.totalPrice = sv.weight * sv.price_per_kilo
            sv.save()
            return redirect('collecteur:products')

    context = {
        'form': form
    }
    return render(request, 'collecteur/add_products.html', context)

@login_required(login_url="users:login")
def update_produit(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = Updateproduit(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('collecteur:products')
    else:
        form = Updateproduit(instance=product)
    context = {
        'form': form
    }
    return render(request, 'collecteur/add_products.html', context)

@login_required(login_url="users:login")
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('collecteur:products')

@login_required(login_url="users:login")
def AllCategories(request):
    category = Category.objects.all()
    print('__________________________')
    print(category)
    context = {
        'category': category
    }
    return render(request, 'collecteur/category.html', context)

@login_required(login_url="users:login")
def addcategory(request):
    form = addCategory()
    if request.method == "POST":
        form = addCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collecteur:AllCategories')
    context = {
        'form': form
    }
    return render(request, 'collecteur/add_category.html', context)

@login_required(login_url="users:login")
def updatecategory(request, id):
    category = Category.objects.get(pk=id)

    if request.method == "POST":
        form = UpdateCategory(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('collecteur:AllCategories')
    else:
        form = UpdateCategory(instance=category)

    context = {
        'form': form
    }
    return render(request, 'collecteur/add_category.html', context)

@login_required(login_url="users:login")
def deletecategory(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('collecteur:AllCategories')
