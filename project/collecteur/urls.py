from django.urls import path
from .views import *
app_name = 'collecteur'
urlpatterns = [
    path('',home,name='home'),
    path('collecteurs/',collecteurs,name='collecteurs'),
    path('vendeurs/',vendeurs,name='vendeurs'),
    path('commandes/',commandes,name='commandes'),
    path('delivered/<int:id>',delivered,name='delivered'),
    path('cancel/<int:id>',cancel,name='cancel'),
    path('history_commandes/',history_commandes,name='history_commandes'),
    path('products/',products,name='products'),
    path('addProd/',addProd,name='addProd'),
    path('update_produit/<int:id>',update_produit,name='update_produit'),
    path('delete_product/<int:id>',delete_product,name='delete_product'),
    path('AllCategories/',AllCategories,name='AllCategories'),
    path('addcategory/',addcategory,name='addcategory'),
    path('updatecategory/<int:id>',updatecategory,name='updatecategory'),
    path('deletecategory/<int:id>',deletecategory,name='deletecategory'),
    path('pick_command/<int:id>',pick_command,name='pick_command'),
]
