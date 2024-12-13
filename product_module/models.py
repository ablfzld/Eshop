from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    categorys = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to='static/uploads/product_imgs/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    @property
    def order_counts(self):
        return Order.objects.filter(product=self).count()

    def discount_price(self):
        return '{:,.0f}'.format(self.price - (self.price * self.discount / 100))

    def formated_price(self):
        return '{:,.0f}'.format(self.price)

    def __str__(self):
        return self.title


class Feature(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True, related_name='features')
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/uploads/product_imgs/')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    date_ordered = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)