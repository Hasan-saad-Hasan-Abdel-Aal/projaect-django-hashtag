# Generated by Django 3.2 on 2021-04-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProName', models.CharField(max_length=100)),
                ('ProDesc', models.TextField(verbose_name='تفاصيل المنتج')),
                ('ProStock', models.BooleanField(blank=True, default=True, null=True, verbose_name='المخزون')),
                ('ProPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='السعر')),
                ('ProImg', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('ProCreated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
