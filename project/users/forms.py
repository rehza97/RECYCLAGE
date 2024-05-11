from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth import get_user_model
class ResisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password1','password2','first_name','last_name','age','phone','gender','address']
        
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'phone', 'gender', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If you want to customize field labels or widgets, you can do it here