# Generated by Django 3.2 on 2021-05-07 14:40

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20210507_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProImg_1',
            field=models.ImageField(blank=True, default='static/assets/images/no-image.jpg', max_length=150, null=True, upload_to=product.models.image_upload, verbose_name='صورة المنتج1 '),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProImg_2',
            field=models.ImageField(blank=True, default='static/assets/images/no-image.jpg', max_length=150, null=True, upload_to=product.models.image_upload, verbose_name='صورة المنتج2 '),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProName',
            field=models.CharField(max_length=150, unique=True, verbose_name='اسم المنتج كامل'),
        ),
    ]