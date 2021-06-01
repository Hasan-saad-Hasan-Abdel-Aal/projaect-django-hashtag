# Generated by Django 3.2 on 2021-05-27 20:41

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0045_auto_20210523_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProImg_1',
            field=models.ImageField(blank=True, default='../static/assets/images/no-image.jpg', max_length=250, null=True, upload_to=product.models.image_upload, verbose_name='الصورة الرئيسية'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProImg_2',
            field=models.ImageField(blank=True, default='../static/assets/images/no-image.jpg', max_length=250, null=True, upload_to=product.models.image_upload, verbose_name='الصورة الفرعية'),
        ),
    ]