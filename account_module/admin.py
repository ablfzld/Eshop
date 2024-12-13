from django.contrib import admin
from account_module.models import State, City, UserAddress


# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    pass