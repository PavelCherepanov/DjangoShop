from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from accounts import activate
from shop.views import shop_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('home/', views.index_page),
    path('product-details/<int:id>', views.product_page, name="product_page"),
    path('cart/', include('cart.urls')),
    path('checkout/', include('orders.urls')),
    path('thanks/', views.thanks_page, name='thanks_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('activate/<slug:uidb64>/<slug:token>/', activate.activate, name='activate'),
    path('shop/', shop_page),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)