from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email_confirmed = models.BooleanField(default=False)
    reset_password = models.BooleanField(default=False)
    telegram_name = models.CharField(max_length=100, default='@name')
    ip_user = models.GenericIPAddressField(default='0.0.0.0')


