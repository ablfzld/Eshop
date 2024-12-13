from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

from account_module.models import UserAddress
from order_module.models import CartItem
from product_module.models import Product


# Create your views here.

def cart_view(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        cart_items_count = cart_items.aggregate(Sum('quantity'))['quantity__sum']
        cart_price_count = 0
        cart_discount_count = 0
        for cart_item in cart_items:
            cart_price_count += cart_item.product.price * cart_item.quantity
            if cart_item.product.discount >0:
                cart_discount_count +=  (
                        (cart_item.product.price * cart_item.quantity) * cart_item.product.discount / 100)

        cart_final_price = cart_price_count - cart_discount_count
        cart_price_count = '{:,.0f}'.format(cart_price_count)
        cart_discount_count = '{:,.0f}'.format(cart_discount_count)
        cart_final_price = '{:,.0f}'.format(cart_final_price)
        return render(request, 'order_module/cart.html',
                      {'cart_items': cart_items, 'cart_items_count': cart_items_count,
                       'cart_price_count': cart_price_count, 'cart_discount_count': cart_discount_count,
                       'cart_final_price': cart_final_price})
    return HttpResponseRedirect('/account/login/')

def increase_cart_product(request,product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        if product is not None:
            if CartItem.objects.filter(user=request.user, product_id=product_id).exists():
                cart = CartItem.objects.get(user=request.user, product_id=product_id)
                cart.quantity += 1
                cart.save()
            else:
                cart = CartItem()
                cart.user = request.user
                cart.product = product
                cart.save()
                cart.quantity = 1
            return redirect(request.META.get('HTTP_REFERER', '/'))
        return HttpResponseNotFound()
    return HttpResponseRedirect('/account/login')

def decrease_cart_product(request, cart_id):
    if request.user.is_authenticated:
        cart = CartItem.objects.get(user=request.user, id=cart_id)
        if cart is not None:
            if cart.quantity > 0:
                cart.quantity -= 1
                cart.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseNotFound()

def remove_from_cart(request, cart_id):
    if request.user.is_authenticated:
        cart = CartItem.objects.get(user=request.user, id=cart_id)
        if cart is not None:
            cart.delete()
            return redirect('/order/cart')
    return HttpResponseNotFound()


def select_address(request):
    if request.user.is_authenticated:
        user_address = UserAddress.objects.filter(user=request.user).order_by('-id')
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items is not None:
            return render(request, 'order_module/select_address.html', {'user_address': user_address, 'cart_items': cart_items})
    return HttpResponseRedirect('/account/login',)

def final_order(request):
    if request.user.is_authenticated:
        user_address_id = request.POST.get('user_address_id')
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items is not None and user_address_id is not None:
            address = UserAddress.objects.get(id=user_address_id)
            user = request.user
            cart_items_count = cart_items.aggregate(Sum('quantity'))['quantity__sum']
            cart_price_count = 0
            cart_discount_count = 0
            for cart_item in cart_items:
                cart_price_count += cart_item.product.price * cart_item.quantity
                if cart_item.product.discount > 0:
                    cart_discount_count += (
                            (cart_item.product.price * cart_item.quantity) * cart_item.product.discount / 100)

            cart_final_price = cart_price_count - cart_discount_count
            cart_raw_final_price = int(cart_final_price)
            cart_price_count = '{:,.0f}'.format(cart_price_count)
            cart_discount_count = '{:,.0f}'.format(cart_discount_count)
            cart_final_price = '{:,.0f}'.format(cart_final_price)
            return render(request, 'order_module/final_order.html',
                          {'cart_items': cart_items, 'cart_items_count': cart_items_count,
                           'cart_price_count': cart_price_count, 'cart_discount_count': cart_discount_count,
                           'cart_final_price': cart_final_price, 'address': address,
                           'user':user, 'cart_raw_final_price': cart_raw_final_price})
        return HttpResponseNotFound()
    return HttpResponseRedirect('/account/login')
