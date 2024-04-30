

from django.urls import path
from .views import *
app_name = 'vendeur'
urlpatterns = [
    path('categories/',categories,name='categories'),
    path('categories/<str:slug>',products,name='products'),
    path('details/<int:id>',details,name='details'),
    path('add_poubelle/<int:product_id>',add_poubelle,name='add_poubelle'),
    path('poubelle/',poubelle,name='poubelle'),
]
