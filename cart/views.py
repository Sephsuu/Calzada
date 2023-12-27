from django.shortcuts import render, get_object_or_404
from .cart import Cart
from eCommerce.models import Product
from django.http import JsonResponse

# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_product()
    quantities = cart.get_qty()

    return render(request, 'cart.html', {'cart_products': cart_products, 'quantities': quantities})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()

        response = JsonResponse({'qty: ': cart_quantity})
        return response

def cart_update(request):
    pass

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        return response