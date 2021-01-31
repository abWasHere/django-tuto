from django.contrib import admin

# Register your models here.
from .models import Product # import the Product class from the models.py that is in the same directory = relative import

admin.site.register(Product)