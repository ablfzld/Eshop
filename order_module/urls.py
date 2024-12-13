"""
URL configuration for Eshop project.

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

from order_module import views

urlpatterns = [
    path('cart', views.cart_view, name='cart'),
    path('add-to-cart', views.increase_product_to_cart, name='add-to-cart'),
    path('increase-cart-product/<int:cart_id>', views.increase_cart_product, name='increase-cart-product'),
    path('decrease-cart-product/<int:cart_id>', views.decrease_cart_product, name='decrease-cart-product'),
    path('remove-from-cart/<int:cart_id>', views.remove_from_cart, name='remove-from-cart'),
    path('select_address', views.select_address, name='select-address'),
    path('final_order', views.final_order, name='final_order'),

]
