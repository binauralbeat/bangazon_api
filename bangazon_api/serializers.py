
from rest_framework import serializers
from .models import Customers
from .models import Products
from .models import Product_type, Order, Payment_type


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("first_name", "last_name")

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("product_name", "product_price")

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = ("type_name",)

class Payment_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_type
        fields = ("payment_type",)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("order_address", "customer", "product", "product_type")

