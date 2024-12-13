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

from account_module import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login-post', views.login_to_site, name='login-post'),
    path('register-post', views.register_to_site, name='register-post'),
    path('add-address', views.add_address_view, name='add-address'),
    path('add-address-post', views.add_address, name='add-address-post'),
    path('remove-address/<int:address_id>', views.remove_address, name='remove-address'),
    path('edit-address/<int:address_id>', views.edit_address_view, name='edit-address'),
    path('edit-address-post/<int:address_id>', views.edit_address, name='edit-address-post'),
    path('edit-name', views.edit_name_view, name='edit-name'),
    path('edit-name-post', views.edit_name, name='edit-name-post'),
    path('', views.profile, name='profile'),
]
