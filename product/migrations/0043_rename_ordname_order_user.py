# Generated by Django 3.2 on 2021-05-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0042_customer_device'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='OrdName',
            new_name='user',
        ),
    ]
