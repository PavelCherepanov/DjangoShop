from django.urls import path
 
from .views import signup as signup
 
urlpatterns = [
    path('signup/', signup, name='signup'),
]