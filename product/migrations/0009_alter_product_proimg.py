# Generated by Django 3.2 on 2021-05-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_probrand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProImg',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='صورة المنتج2 '),
        ),
    ]
