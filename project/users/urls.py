

from django.urls import path
from .views import *
app_name = 'users'
urlpatterns = [
    # path('reg/',regFirstTypoeUser,name='reg'),
    path('add_collectuer/',add_collectuer,name='add_collectuer'),
    path('signup/',register_user,name='signup'),
    path('',login_user,name='login'),
    path('block/<int:id>',block_user,name='block'),
    path('delete/<int:id>',delete_user,name='delete'),
    path('logout/',logout_user,name='logout'),
]
