

from django.urls import path
from .views import *
app_name = 'vendeur'
urlpatterns = [
    path('categories/',categories,name='categories'),
    path('categories/<str:slug>',products,name='products'),
    path('details/<int:id>',details,name='details'),
    path('add/<int:id>',add,name='add'),
    path('poubelle/',poubelle,name='poubelle'),
    path('delete_from_poubelle/<int:id>',delete_from_poubelle,name='delete_from_poubelle'),
    path('sendCommand/',sendCommand,name='sendCommand'),

]
