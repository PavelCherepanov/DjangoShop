from django.shortcuts import render
from crm.form import SubscribeForm
from management.models import Product
from crm.models import Crm
from telegramBot.sendmessage import sendCrmTelegram
from cart.cart import Cart

def index_page(request):
    products_list = Product.objects.all()
    dict_object = {'products_list':products_list}  
    return render(request, 'index.html', dict_object)

def product_page(request, id):
    product = Product.objects.get(id=id)
    dict_object = {'product': product}
    return render(request, 'product-details.html', dict_object)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        elemet = Crm(crm_name=name, crm_email=email)
        elemet.save()
        sendCrmTelegram(tg_name=name, tg_email=email)
        return render(request, './thanks.html', {'name':name, 'email':email})
    else:
        return render(request, './thanks.html')