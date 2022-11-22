from django.shortcuts import render
from management.models import Product


# Create your views here.
# Это сделала Марина
# Павелк точка Черепан
def shop_page(request):
    products_list = Product.objects.all()
    dict_object = {'products_list': products_list}
    return render(request, 'shop.html', dict_object)
