from email.policy import default
from itertools import Product, product
from home.models import Product

# Inserting a new record into the Product Model

product2 = Product(product_name="Rice", product_type="Cereals", product_category="Grains", product_price="50,000")
product2.save()

# Get all the records in the Product table
all_entries = Product.objects.all()
all_entries

# Filtering products by their name     
x = product.objects.filter(product_name="Rice")

# Getting a single record from the product table
one_entry = product.objects.get(pk=1)


# Changing a product price
x = product_price = "100,000"
x.save()
