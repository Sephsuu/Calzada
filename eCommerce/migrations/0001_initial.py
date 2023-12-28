# Generated by Django 5.0 on 2023-12-28 04:08

import django.db.models.deletion
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
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='', max_length=250)),
                ('image', models.ImageField(upload_to='images/product')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eCommerce.product')),
                ('model', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'clothes',
            },
            bases=('eCommerce.product',),
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eCommerce.product')),
                ('brand', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=50)),
            ],
            bases=('eCommerce.product',),
        ),
        migrations.CreateModel(
            name='Poultry',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eCommerce.product')),
                ('breed', models.CharField(max_length=250)),
                ('weight', models.IntegerField(default=0)),
                ('quality', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'poultries',
            },
            bases=('eCommerce.product',),
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eCommerce.product')),
                ('brand', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'shoes',
            },
            bases=('eCommerce.product',),
        ),
        migrations.CreateModel(
            name='Skincare',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eCommerce.product')),
                ('brand', models.CharField(max_length=250)),
                ('skincare_type', models.CharField(max_length=50)),
                ('skintype', models.CharField(max_length=50)),
            ],
            bases=('eCommerce.product',),
        ),
    ]
