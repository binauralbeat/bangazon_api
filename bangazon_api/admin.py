from django.contrib import admin
from .models import Customers, Products, Product_type

# Register your models here.

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Product_type)
