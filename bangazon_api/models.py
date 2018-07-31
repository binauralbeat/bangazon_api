from django.db import models

# Create your models here.

class Product_type(models.Model):
    type_name = models.CharField(max_length = 50, null = False, default="")

    def __str__(self):
        return "{}".format(self.type_name)

class Products(models.Model):
    product_name = models.CharField(max_length = 50, null = False, default="")
    product_price = models.CharField(max_length = 50, null = False, default="")
    product_type = models.ForeignKey(Product_type, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.product_name, self.product_price)

class Payment_type(models.Model):
    payment_type = models.CharField(max_length = 50, null = False, default="")

    def __str__(self):
        return "{}".format(self.payment_type)

class Order(models.Model):
    order_address = models.CharField(max_length = 50, null = False, default="")
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    product_type = models.ForeignKey(Product_type, on_delete = models.CASCADE)
    payment_type = models.ForeignKey(Payment_type, on_delete = models.CASCADE)

    def __str__(self):
        return "{}".format(self.order_address)

class Customers(models.Model):
    first_name = models.CharField(max_length = 50, null = False, default="")
    last_name = models.CharField(max_length = 50, null = False, default="")
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.first_name, self.last_name)




