from django.urls import path
from .views import *
app_name = 'collecteur'
urlpatterns = [
    path('',addProd,name='add_product'),
]
