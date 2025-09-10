from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)  
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0) 

    def __str__(self):
        return self.name
