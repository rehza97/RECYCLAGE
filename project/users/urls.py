

from django.urls import path
from .views import *
app_name = 'users'
urlpatterns = [
    # path('reg/',regFirstTypoeUser,name='reg'),
    path('signin/',register_user,name='signin'),
    path('',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
]
