from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(blank = True , null = True)
    email = models.EmailField(unique=True)
    phone =  models.CharField(max_length=200,blank = True , null = True)
    sex = [
        ('Homme', 'Homme'),
        ('Famme', 'Famme'),
    ]
    gender = models.CharField(max_length=100, choices=sex,blank = True , null = True)
    address = models.CharField(max_length=200,blank = True , null = True)
    typeOfUser = [
        ('vendeur', 'vendeur'),
        ('collecteur', 'collecteur'),
    ]
    user_type = models.CharField(max_length=100, choices=typeOfUser,blank = True , null = True)
    vendeur = models.BooleanField(default=False) 
    collecteur = models.BooleanField(default=False) 
    
    def __str__(self) -> str:
        return self.email
    
