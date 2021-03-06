# Generated by Django 3.2 on 2021-05-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0046_auto_20210527_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProDiscountPrice',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=6, null=True, verbose_name='السعر بعد الخصم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProPrice',
            field=models.DecimalField(decimal_places=0, max_digits=6, verbose_name='سعر السوق'),
        ),
    ]
