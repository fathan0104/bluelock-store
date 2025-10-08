from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    is_featured = models.BooleanField(default=False)  
    stock = models.PositiveIntegerField(default=0, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product_views = models.PositiveIntegerField(default=0)

    def increment_views(self):
        self.product_views += 1
        self.save()

    def is_product_hot(self):
        return self.product_views > 20

    def __str__(self):
        return self.name if self.name else "Unnamed Product"
    

    
    
    
