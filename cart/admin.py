from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'address', 'phone')