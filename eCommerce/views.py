from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .forms import SignUpForm
from django import forms

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'section/home.html', {'products': products})

def about(request):
    return render(request, 'section/about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have just logged in!"))
            return redirect('user_home')
        else:
            messages.success(request, ("Username and Password did not match!"))
            return redirect('login')

    else:
        return render(request, 'section/login.html', {})

def login_required(request):
    return render(request, 'section/login_required.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully logged out!"))
    return redirect('home')

def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error registering, please try again!"))
            return redirect('register')
    else:
        return render(request, 'section/register.html', {'form':form})

def user_home(request):
    user = request.user
    products = Product.objects.all()
    return render(request, 'section/user_home.html', {'user': user, 'products':products})

def show_all_products(request):
    products = Product.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_all_products.html', {'products':products, 'message_data':messages_data})

def show_all_products_image(request):
    products = Product.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_all_products_image.html', {'products':products, 'message_data':messages_data})

def show_shoe_products(request):
    shoes = Shoes.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_shoe_products.html', {'shoes':shoes, 'message_data':messages_data})

def show_shoe_products_image(request):
    shoes = Shoes.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_shoe_products_image.html', {'shoes':shoes, 'message_data':messages_data})

def show_cloth_products(request):
    clothes = Clothes.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_cloth_products.html', {'clothes':clothes, 'message_data':messages_data})

def show_cloth_products_image(request):
    clothes = Clothes.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_cloth_products_image.html', {'clothes':clothes, 'message_data':messages_data})

def show_gadget_products(request):
    gadgets = Gadget.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_gadget_products.html', {'gadgets':gadgets, 'message_data':messages_data})

def show_gadget_products_image(request):
    gadgets = Gadget.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_gadget_products_image.html', {'gadgets':gadgets, 'message_data':messages_data})

def show_skincare_products(request):
    skincares = Skincare.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_skincare_products.html', {'skincares':skincares, 'message_data':messages_data})

def show_skincare_products_image(request):
    skincares = Skincare.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_skincare_products_image.html', {'skincares':skincares, 'message_data':messages_data})

def show_poultry_products(request):
    poultries = Poultry.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_poultry_products.html', {'poultries':poultries, 'message_data':messages_data})

def show_poultry_products_image(request):
    poultries = Poultry.objects.all().order_by('name')
    messages_data = messages.get_messages(request)
    return render(request, 'section/showProducts/show_poultry_products_image.html', {'poultries':poultries, 'message_data':messages_data})

def search_product(request):
    if request.method == "POST":
        search = request.POST.get('search', '')  # Get the search query or default to an empty string
        products = Product.objects.filter(
            Q(name__icontains=search)
        )
        if products:
            return render(request, 'section/search_product.html', {'search': search, 'products': products})
        else:
            no_results_message = "No products found matching your search."
            return render(request, 'section/search_product.html', {'search': search, 'no_results_message': no_results_message})
    else:
        return render(request, 'section/search_product.html', {})
    
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    thing = Product.objects.get(id=product_id)

    if hasattr(product, 'shoes'):
        products = Shoes.objects.all()
        details = product.shoes
        template = 'section/productDetails/gadget_detail.html' 
        print("This is a shoe product")
    elif hasattr(product, 'clothes'):
        products = Clothes.objects.all()
        details = product.clothes
        template = 'section/productDetails/clothes_detail.html'
    elif hasattr(product, 'gadget'):
        products = Gadget.objects.all()
        details = product.gadget
        template = 'section/productDetails/gadget_detail.html'  
    elif hasattr(product, 'skincare'):
        products = Skincare.objects.all()
        details = product.skincare
        template = 'section/productDetails/skincare_detail.html'  
    elif hasattr(product, 'poultry'):
        products = Poultry.objects.all()
        details = product.poultry
        template = 'section/productDetails/poultry_detail.html'  

    return render(request, template, {'product': product, 'details': details, 'products': products, 'thing': thing})

