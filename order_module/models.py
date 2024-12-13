from django.contrib.auth.models import User
from django.db import models

from account_module.models import UserAddress, State
from product_module.models import Product


# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_full_name = models.CharField(max_length=150)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now_add=True)
    price = models.IntegerField(default=0)
    is_sent = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class SendPrice(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)