# Generated by Django 3.2 on 2021-04-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProName',
            field=models.CharField(max_length=100, verbose_name='اسم المنتج كامل'),
        ),
    ]
