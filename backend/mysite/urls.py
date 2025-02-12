"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Global admin endpoint
    path('admin/', admin.site.urls),
    
    # Global API endpoints: versioned
    path('api/v1/auth/', include('authentication.urls', namespace='authentication')),
    path('api/v1/products/', include('products.urls', namespace='products')),
    path('api/v1/orders/', include('orders.urls', namespace='orders')),
    path('api/v1/cart/', include('cart.urls', namespace='cart')),
    path('api/v1/health/', include('health.urls', namespace='health')),
]
