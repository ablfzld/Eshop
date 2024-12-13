from django.contrib import admin

from product_module.models import Category, Brand, Product, Feature, ProductImage, Comment


# Register your models here.


class ProductFeatures(admin.StackedInline):
    model = Feature

class ProductImages(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatures, ProductImages]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
