# Generated by Django 5.0 on 2023-12-28 04:08

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eCommerce', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='eCommerce.product')),
            ],
        ),
    ]
