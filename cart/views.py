from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
from management.models import Product
from .cart import Cart



# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
    
    
#     cart.add(product=product,
#                 quantity=1,
#                 update_quantity=False)
#     return redirect('cart:cart_detail')



def cartDetail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})

def cartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product.id, quantity=1, update_quantity=False)
    return redirect('/cart')

def cartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('/cart')