from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from order_module.models import CartItem
from product_module.models import Product, ProductImage, Feature, Category, Comment


# Create your views here.


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    if product.is_active:
        product_images = ProductImage.objects.filter(product=product_id)
        product_features = Feature.objects.filter(product=product_id)
        product_images_count = range(product_images.count())
        product_quantity = 0
        # product quantity
        if request.user.is_authenticated:
            if CartItem.objects.filter(user=request.user, product_id=product_id).exists():
                cart = CartItem.objects.get(user=request.user, product_id=product_id)
                product_quantity = cart.quantity

        return render(request, 'product_module/product_detail.html',
                      {'product': product, 'product_images': product_images, 'product_features': product_features,
                       'product_images_count': product_images_count, 'product_quantity': product_quantity})
    else:
        return HttpResponseNotFound()


def product_list(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    final_products = Product.objects.none()


    # filter category
    filter_categories_id = request.GET.getlist('selected_category')
    if filter_categories_id:
        filter_categories = []
        for category_id in filter_categories_id:
            filter_categories+=Category.objects.filter(id=category_id)
        for category in filter_categories:
            final_products|=products.filter(categorys__id=category.id)
    else:
        final_products = products

    # filter search
    search = request.GET.get('search')
    if search:
        final_products = final_products.filter(title__icontains=search)
    else:
        search = ''


    # order products
    order = request.GET.get('order')
    if order:
        if order == 'mostediscount':
            final_products = final_products.order_by('-discount')
        if order == 'mostexpensive':
            final_products = final_products.order_by('-price')
        if order == 'cheapest':
            final_products = final_products.order_by('price')
        if order == 'bestseller':
            final_products = final_products.order_by('order_counts')
        if order == 'date':
            final_products = final_products.order_by('-created_at')


    final_products = final_products.distinct()

    # paging
    current_page = request.GET.get('page')
    if current_page is None:
        current_page = '1'
    products_count_in_page = 12
    final_products_count = final_products.count()
    if final_products_count % products_count_in_page == 0:
        page_count = final_products_count // products_count_in_page
    else:
        page_count = final_products_count // products_count_in_page + 1

    skip_value = (int(current_page)-1) * products_count_in_page
    page_count = range(page_count)
    final_products = final_products[skip_value:][:products_count_in_page]



    return render(request, 'product_module/product_list.html',
                  {'products': final_products, 'categories': categories,
                   'search': search, 'order': order, 'selected_categories':filter_categories_id,
                   'current_page': current_page, 'page_count': page_count})


def product_comments(request, product_id):
    comments = Comment.objects.filter(product=product_id)
    user = request.user
    return render(request, 'product_module/partials/product_comments.html',
                  {'product_id': product_id, 'comments': comments, 'user': user})

def add_comment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            text = request.POST.get('text')
            comment = Comment()
            comment.product_id = product_id
            comment.user_id = request.user.id
            comment.text = text
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    return  HttpResponseNotFound()


def remove_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_id)
        user_id = request.user.id
        is_admin = request.user.is_superuser
        if comment.user_id == user_id or is_admin:
            comment.delete()
            return redirect(request.META.get('HTTP_REFERER'))
    return HttpResponseNotFound()
