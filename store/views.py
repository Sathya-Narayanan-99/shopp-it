from django.shortcuts import render

from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json

import datetime

from .models import *
from .utils import cookieCart, cartData

# Create your views here.
def store(request):

    data = cartData(request)

    cartItems = data['cartItems']
    
    products = Product.objects.all()
    
    context = {'products':products, 'cartItems':cartItems}
    
    return render(request,"store/store.html",context)

def cart(request):

    data = cartData(request)

    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items':items, 'order':order, 'cartItems':cartItems}

    return render(request,"store/cart.html",context)

def checkout(request):

    data = cartData(request)

    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items':items, 'order':order, 'cartItems':cartItems,}
    
    return render(request,"store/checkout.html",context)

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('store'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('store'))
            
            else:
                return HttpResponse("User account not active")
            
        else:
            return HttpResponse("Invalid credetentials")
    else:
        
        data = cartData(request)

        cartItems = data['cartItems']
        
        return render(request,'store/login.html',{'cartItems':cartItems,})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('store'))

def user_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('store'))
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = User(is_superuser=False, is_staff=False, username=username, email=email)
        user.set_password(password)
        user.save()

        print(user.id)
        customer = Customer(user=user, name=name, email=email)
        customer.save()

        return HttpResponseRedirect(reverse('store'))
    else:

        data = cartData(request)

        cartItems = data['cartItems']

        return render(request, 'store/register.html', {'cartItems':cartItems,})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(cart=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    elif action == 'delete':
        orderItem.quantity = 0
 
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['userForm']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                cart=order,
                address1=data['shippingForm']['address1'],
                address2=data['shippingForm']['address2'],
                city=data['shippingForm']['city'],
                state=data['shippingForm']['state'],
                zipcode=data['shippingForm']['zipcode'],
                country=data['shippingForm']['country']
            )
    else:
        print("User is not logged in")
    return JsonResponse('Payment complete', safe=False)