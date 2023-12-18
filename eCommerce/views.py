from django.shortcuts import render
from . models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'section/home.html', {'products': products})

def login_user(request):
    pass

def logout_user(request):
    pass