# Generated by Django 3.2 on 2021-05-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20210513_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ProQuantity',
            field=models.IntegerField(default=1),
        ),
    ]