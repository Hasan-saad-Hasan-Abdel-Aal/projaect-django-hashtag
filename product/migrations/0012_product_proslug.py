# Generated by Django 3.2 on 2021-05-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_productalternative'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='URl'),
        ),
    ]