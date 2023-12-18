from django.contrib import admin
from .models import Customer, Product, Order, Shoes, Clothes, Gadget, Skincare, Poultry

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'image')

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(Skincare)
class SkincareAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(Poultry)
class PoultryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'address', 'phone', 'date','status')


