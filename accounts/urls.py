from django.urls import path
 
from .views import signup as signup
from .views import profile as profile
 
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
]