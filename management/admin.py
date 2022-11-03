from django.contrib import admin
from .models import Product, StatusManagement, CategoryManagement, ColorManagement, BrandManagement

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_description', 'product_img', 'product_status', 'product_category', 'product_color', 'product_brand')
admin.site.register(Product, ProductAdmin)

admin.site.register(StatusManagement)
admin.site.register(CategoryManagement)
admin.site.register(ColorManagement)
admin.site.register(BrandManagement)
