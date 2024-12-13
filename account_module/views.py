from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from account_module.models import UserAddress, State, City


# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        user_address = UserAddress.objects.filter(user=user).order_by('-id')
        return render(request, 'account_module/profile.html', {'user': user, 'user_address': user_address})
    return HttpResponseRedirect('/account/login')


def login_view(request):
    if not request.user.is_authenticated:
        error = request.GET.get('error')
        return render(request, 'account_module/login.html', {'error': error})
    return HttpResponseNotFound()

def login_to_site(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/account/login?error=True')

    return HttpResponseNotFound()


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    return HttpResponseNotFound()


def register_view(request):
    if not request.user.is_authenticated:
        error = request.GET.get('error')
        return render(request, 'account_module/register.html', {'error': error})
    return HttpResponseNotFound()


def register_to_site(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.filter(email=email).first()
            if user is None:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                password=password, username=email)
                user.save()
                return redirect('/account/login')
            else:
                return redirect('/account/register?error=True')

    return HttpResponseNotFound()


def add_address_view(request):
    if request.user.is_authenticated:
        states = State.objects.all()
        citys = City.objects.all()
        last_url = request.META.get('HTTP_REFERER')
        return render(request, 'account_module/add_address.html', {"states": states, "citys": citys, 'last_url': last_url})
    return HttpResponseRedirect('/account/login')

def add_address(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            postal_code = request.POST['postal_code']
            title = request.POST['title']
            user_address = UserAddress(user_id=request.user.id, state_id=state, city_id=city, address=address, title=title,postal_code=postal_code)
            user_address.save()
            last_url = request.POST.get('last_url')
            if last_url:
                return redirect(last_url)
            else:
                return redirect('/account')
        else:
            return HttpResponseNotFound()
    return HttpResponseRedirect('/account/login')

def remove_address(request,address_id):
    if request.user.is_authenticated:
        address = UserAddress.objects.get(id=address_id, user_id=request.user.id)
        if address is not None:
            address.delete()
            return redirect('/account')
        return HttpResponseNotFound()
    return HttpResponseRedirect('/account/login')


def edit_address_view(request, address_id):
    if request.user.is_authenticated:
        address = UserAddress.objects.get(id=address_id, user_id=request.user.id)
        if address is not None:
            states = State.objects.all()
            citys = City.objects.all()
            return render(request, 'account_module/edit_address.html', {'address': address, 'states': states, 'citys': citys})
        return HttpResponseNotFound()
    return HttpResponseRedirect('/account/login')

def edit_address(request, address_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_address = UserAddress.objects.get(id=address_id)
            if user_address is not None:
                state = request.POST['state']
                city = request.POST['city']
                address = request.POST['address']
                postal_code = request.POST['postal_code']
                title = request.POST['title']
                user_address.state_id = state
                user_address.city_id = city
                user_address.address = address
                user_address.title = title
                user_address.postal_code = postal_code
                user_address.save()
                return redirect('/account')
    return HttpResponseNotFound()


def edit_name_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        return render(request, 'account_module/edit_name.html', {'user': user})
    return HttpResponseRedirect('/account/login')

def edit_name(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(id=request.user.id)
            if user is not None:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return redirect('/account')
    return HttpResponseNotFound()
