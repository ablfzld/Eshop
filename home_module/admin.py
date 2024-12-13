# Register your models here.

from django.contrib import admin

from home_module.models import Slider


@admin.register(Slider)


class SliderAdmin(admin.ModelAdmin):
    pass
