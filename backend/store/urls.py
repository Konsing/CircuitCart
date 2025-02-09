# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/featured/', views.FeaturedProductList.as_view(), name='featured-product-list'),
    path('products/combos/', views.ComboProductList.as_view(), name='combo-product-list'),
]
