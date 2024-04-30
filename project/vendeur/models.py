from django.db import models
from users.models import User
from  collecteur.models import   *
# Create your models here.

class Poubelle(models.Model):
    poubelle_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.poubelle_id
    
class PoubelleItem(models.Model):
    product = models.ForeignKey(Product ,  on_delete=models.CASCADE)
    poubelle = models.ForeignKey(Poubelle,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.product.title} , Quantity : {self.quantity}'
    
class VendeurCommande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)