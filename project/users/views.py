from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required

# Create your views here.


# def regFirstTypoeUser(request):
#     if request.method == 'POST':
#         form = ResisterUserForm(request.POST)


#         if form.is_valid():
#             var = form.save(commit=False)
#             var.save()
#             messages.success(request, 'Account Created Successfully')
#             return redirect('users:login_user')
#         else:
#             messages.warning(request, 'something went wrong')
#             return redirect('users:reg')
#     else:
#         form = ResisterUserForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'users/register.html', context)

def register_user(request):
    User = get_user_model()

    if request.method == 'POST':
        form = ResisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username
            user.vendeur = True
            user.save()
            # ////////////////////////////////////////////////////
            subject = 'bien venue sur notre site '
            message = f'Bonjour {user.first_name} {user.last_name},  '
            email = user.email
            revicer = [email]
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                revicer,
                fail_silently=False,
            )
    # ////////////////////////////////////////////////////
            return redirect('login')
    else:
        form = ResisterUserForm()

    return render(request, 'users/register.html', {'form': form})


@login_required(login_url="login")
def add_collectuer(request):
    User = get_user_model()

    if request.method == 'POST':
        form = ResisterUserForm(request.POST)
        psrd = request.POST['password1']
        
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username
            user.collecteur = True
            user.save()
            # ////////////////////////////////////////////////////
            subject = 'bien venue sur notre site '
            message = f'Bonjour {user.first_name} {user.last_name}, voila votre \n email: {user.email} \n password : {psrd}\n bienvenu dans notre famille'
            email = user.email
            revicer = [email]
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                revicer,
                fail_silently=False,
            )
    # ////////////////////////////////////////////////////
            return redirect('login')
    else:
        form = ResisterUserForm()

    return render(request, 'users/add_collectuer.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UpdateUserForm
    template_name = 'user_update.html'  # The template where the form will be rendered
    # Redirect URL after successful update
    success_url = reverse_lazy('profile')

    # Override get_object method to get the current user's instance
    def get_object(self, queryset=None):
        return self.request.user


def login_user(request):
    if request.user.is_authenticated:
        if request.user.vendeur:
            return redirect('vendeur:categories')
        else:
            return redirect('collecteur:home')

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email)
        user = authenticate(request, username=email, password=password)

        if user and user.is_active:
            print('__________________________________')
            login(request, user)

            if request.user.vendeur:
                return redirect('vendeur:categories')
            else:
                return redirect('collecteur:home')

        else:
            messages.error(request, 'please retype your email and password carrfully')
            return redirect('login')
    return render(request, 'users/login.html')


def logout_user(request):
    user = request.user
    logout(request)
    messages.info(request, f'good bye Mr {user.first_name} {user.last_name} please revitie us soon')
    return redirect('login')


@login_required(login_url="login")
def block_user(request, id):
    user = User.objects.get(id=id)
    print(user)
    user.is_active = False
    if user.collecteur:
        user.save()
        return redirect('collecteur:collecteurs')
    else:
        user.save()
        return redirect('collecteur:vendeurs')


@login_required(login_url="login")
def delete_user(request, id):
    user = User.objects.get(id=id)
    if user.collecteur:
        user.delete()
        return redirect('collecteur:collecteurs')
    else:
        user.delete()
        return redirect('collecteur:vendeurs')
