# Generated by Django 4.1.3 on 2022-11-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telegram_name',
            field=models.CharField(default='@name', max_length=100),
        ),
    ]
