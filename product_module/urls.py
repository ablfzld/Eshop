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
from tkinter.font import names

from django.contrib import admin
from django.urls import path

from product_module import views

urlpatterns = [
    path('<int:product_id>', views.product_detail, name='product-detail'),
    path('', views.product_list, name='product-list'),
    path('product_comments/<int:product_id>', views.product_comments, name='product-comments'),

    path('add_comment', views.add_comment, name='add-comment'),
    path('remove_comment/<int:comment_id>', views.remove_comment, name='remove-comment'),
]
