from django.shortcuts import render
from rest_framework import viewsets

from .models import Customers, Products, Product_type, Order, Payment_type
from .serializers import CustomersSerializer, ProductsSerializer, ProductTypeSerializer, OrderSerializer, Payment_typeSerializer

class ListProductTypeView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Product_type.objects.all()
    serializer_class = ProductTypeSerializer

class ListProductsView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ListCustomersView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class ListOrderView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ListPaymentTypeView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Payment_type.objects.all()
    serializer_class = Payment_typeSerializer

