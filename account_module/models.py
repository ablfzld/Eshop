from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class State(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=100)