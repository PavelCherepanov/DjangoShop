from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email_confirmed = models.BooleanField(default=False)
    reset_password = models.BooleanField(default=False)
    telegram_name = models.CharField(max_length=100, default='@name')
    ip_user = models.GenericIPAddressField(default='0.0.0.0')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()