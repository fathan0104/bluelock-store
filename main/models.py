from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    is_featured = models.BooleanField(default=False)  
    stock = models.PositiveIntegerField(default=0, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, blank=True, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()
    
    def __str__(self):
        return self.name if self.name else "Unnamed Product"
