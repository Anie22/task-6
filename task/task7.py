from itertools import Product
from home.models import Product

class Product(models.Model):
    product_name = models.CharField(max_length=220)  
    product_price = models.CharField(max_length=220)  
    product_category = models.CharField(max_length=220)  
  
    def __str__(self):
        return self.product_name
      