# Generated by Django 4.1.7 on 2023-02-17 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
