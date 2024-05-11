from django.db import models
from decimal import Decimal
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banner/cartegory', blank=True, null=True)
    slug = models.SlugField(unique=True,blank=True,null=True)  # Add a SlugField for the title slug

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate slug automatically from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=256)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    
    
    
    def __str__(self):
        return self.title

