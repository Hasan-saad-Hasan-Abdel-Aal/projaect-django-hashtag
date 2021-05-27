# Generated by Django 3.2 on 2021-05-03 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210502_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAlternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrAlName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choose_product', to='product.product', verbose_name='المنتج')),
                ('PrAlternative', models.ManyToManyField(related_name='product_with_alternative', to='product.Product', verbose_name='بدائل المنتج')),
            ],
            options={
                'verbose_name': 'المنتجات البديلة',
                'verbose_name_plural': 'ProductAlternatives',
            },
        ),
    ]
