from django.db import models
from users.models import User
from  collecteur.models import   *
# Create your models here.

class AllCommandes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    celletuer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='colletuer',blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True , blank=True , null=True)
    commandes = models.ManyToManyField('VendeurCommande')
    totalPrice = models.DecimalField(decimal_places=2 , max_digits=20,null=True,blank=True)
    placed = models.BooleanField(default=False)
    selected = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    def __str__(self):
        return f'command de {self.user.username}'
    
class VendeurCommande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True , null=True)
    price = models.DecimalField(decimal_places=2 , max_digits=20,null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.produit}-{self.quantity}"