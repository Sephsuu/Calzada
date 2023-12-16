from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, max_length=250, default='')
    image = models.ImageField(upload_to='images/product')

    def __str__(self):
        return self.name

class Shoes(Product):
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    SIZE_CHOICES = [
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)

class Clothes(Product):
    model = models.CharField(max_length=250)
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)

class Gadget(Product):
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    storage = models.CharField(max_length=10)
    size = models.CharField(max_length=50)

class Skincare(Product):
    brand = models.CharField(max_length=250)
    skincare_type = models.CharField(max_length=50)
    skintype = models.CharField(max_length=50)

class Poultry(Product):
    breed = models.CharField(max_length=250)
    weight = models.IntegerField(default=0)
    quality = models.CharField(max_length=50)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=False)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)