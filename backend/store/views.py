from django.shortcuts import render

# store/views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# List all products
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# List only featured products
class FeaturedProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_featured=True)

# List combo products
class ComboProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_combo=True)