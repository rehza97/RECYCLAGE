

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
# app_name = 'users'
urlpatterns = [
    # path('reg/',regFirstTypoeUser,name='reg'),
    path('add_collectuer/',add_collectuer,name='add_collectuer'),
    path('signup/',register_user,name='signup'),
    path('',login_user,name='login'),
    path('block/<int:id>',block_user,name='block'),
    path('delete/<int:id>',delete_user,name='delete'),
    path('logout/',logout_user,name='logout'),
    
    # reset password
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_done.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

