from cart.cart import Cart
from management.models import Product
from crm.form import SubscribeForm
from django.shortcuts import render
from decimal import Decimal

def getQuantity(request):
    c = Cart(request)
    quantity = 0
    print(c.cart)
    for i in c.cart:
        print(i)
        quantity += int(c.cart[i]['quantity'])
    return {'quantityAll': str(quantity)}

def getTotalPrice(request):
    c = Cart(request)
    totalPrice = 0
    for p in c.cart:
        totalPrice += Decimal(c.cart[p]['price'])*int(c.cart[p]['quantity'])
    return {'getTotalPrice': str(totalPrice)}

def subs(request):
    form = SubscribeForm()
    return {'form':form} 