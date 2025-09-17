from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "thumbnail", "category", "is_featured", "stock", "rating"]
