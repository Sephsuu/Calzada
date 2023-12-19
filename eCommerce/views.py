from django.shortcuts import render, redirect
from . models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
            return redirect('admin:index')
        else:
            messages.success(request, ("Username and Password did not match!"))
            return redirect('login')

    else:
        return render(request, 'section/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully logged out!"))
    return redirect('home')