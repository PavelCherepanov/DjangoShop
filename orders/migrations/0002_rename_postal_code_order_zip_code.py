# Generated by Django 4.1.3 on 2022-11-21 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='zip_code',
        ),
    ]