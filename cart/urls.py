from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.cartDetail, name='cartDetail'),
    path('add/<product_id>/', views.cartAdd, name='cart_add'),
    path('remove/<product_id>/', views.cartRemove, name='cart_remove'),
]