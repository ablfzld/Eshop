from django.contrib import admin

from order_module.models import Order, SendPrice


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(SendPrice)
class SendPriceAdmin(admin.ModelAdmin):
    pass