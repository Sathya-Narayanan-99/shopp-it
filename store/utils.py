import json
from .models import *

def cookieCart(request):
    
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}


    items = []
    order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}


    for i in cart:

        try:
            order['get_cart_items'] += cart[i]["quantity"]

            product = Product.objects.get(id=i)

            order['get_cart_total'] += (product.price * cart[i]["quantity"])

            if product.digital == False:
                order['shipping'] = True

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]["quantity"],
                'get_total':(product.price * cart[i]["quantity"])

            }

            items.append(item)

        except:
            pass

        cartItems = order['get_cart_items']


    return {'items':items, 'order':order, 'cartItems':cartItems}

def cartData(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        cartItems = order.get_cart_items


    else:

        cookieData = cookieCart(request)
        
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']

    
    return {'items':items, 'order':order, 'cartItems':cartItems}