from django.db.models.lookups import Range
from django.shortcuts import render

from home_module.models import Slider
from product_module.models import Product, Category


# Create your views here.


def home(request):
    latest_products= Product.objects.filter(is_active=True).order_by('-created_at')[:12]
    discount_products= Product.objects.filter(is_active=True).filter(discount__gt=0).order_by('-discount')[:12]
    sliders = Slider.objects.filter(is_active=True)
    slides_count = range(sliders.count())
    return render(request, 'home_module/index.html',{
        'latest_products':latest_products, 'discount_products':discount_products,
        'sliders':sliders, 'slides_count':slides_count})


def about_us(request):
    return render(request, 'home_module/about_us.html')


def navbar_category(request):
    top_categories = Category.objects.filter(parent_id__isnull=True)
    all_categories = Category.objects.all()
    return render(request, 'partials/navbar_category.html', {'top_categories':top_categories, 'all_categories':all_categories})