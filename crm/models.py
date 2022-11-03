from django.db import models

# Create your models here.
class Crm(models.Model):
    crm_dt = models.DateTimeField(auto_now=True)
    crm_name = models.CharField(max_length=200, verbose_name='Имя')
    crm_email = models.EmailField(max_length=200, verbose_name='Email')
    
    def __str__(self):
        return self.crm_name

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'