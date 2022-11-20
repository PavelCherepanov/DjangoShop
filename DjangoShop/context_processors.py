from cart.cart import Cart
from management.models import Product
from crm.form import SubscribeForm
from django.shortcuts import render

def getQuantity(request):
    c = Cart(request)
    # product = Product.objects.get(id=productId)
    # productId = str(product.id)
    quantity = 0
    print(c.cart)
    for i in c.cart:
        print(i)
        quantity += int(c.cart[i]['quantity'])
    return {'quantityAll': str(quantity)}

def subs(request):
    form = SubscribeForm()
    return {'form':form} 