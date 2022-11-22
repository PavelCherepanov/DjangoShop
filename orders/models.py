from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Order(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userOrder', null=True)
    country = models.CharField(max_length=50, default='-')
    street_address = models.CharField(max_length=250, default='-')
    city = models.CharField(max_length=100, default='-')
    zip_code = models.CharField(max_length=20, default='-')
    comment = models.CharField(max_length=100, default='-')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)