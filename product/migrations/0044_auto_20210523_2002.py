# Generated by Django 3.2 on 2021-05-23 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_rename_ordname_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='OrdName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='device',
        ),
    ]