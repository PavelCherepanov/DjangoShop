from django.shortcuts import render
from management.models import Product, CategoryManagement, BrandManagement, ColorManagement



def shop_page(request):
    products_list = Product.objects.all()
    CategoryManagement_list = CategoryManagement.objects.all()
    BrandManagement_list = BrandManagement.objects.all()
    ColorManagement_list = ColorManagement.objects.all()
    dict_object = {'products_list': products_list, 'CategoryManagement_list': CategoryManagement_list, 'BrandManagement_list': BrandManagement_list, 'ColorManagement_list': ColorManagement_list}
    return render(request, 'shop.html', dict_object)
