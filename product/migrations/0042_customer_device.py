# Generated by Django 3.2 on 2021-05-23 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0041_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
