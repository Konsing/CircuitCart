# store/urls.py
from django.urls import path
from .views import ProductList, FeaturedProductList, ComboProductList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/featured/', FeaturedProductList.as_view(), name='featured-product-list'),
    path('products/combos/', ComboProductList.as_view(), name='combo-product-list'),
]

# ecommerce/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  # API endpoints will be available under /api/
]
