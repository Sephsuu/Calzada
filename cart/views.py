from django.shortcuts import render, get_object_or_404
from .cart import Cart
from eCommerce.models import Product
from cart.models import Order
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        return response
    
def order_list(request):
    cart = Cart(request)
    products = cart.get_product()
    print(products)
    product_qty = [item['quantity'] for item in products]
    product_tp = [item['total_price'] for item in products]
    print(product_qty)
    print(product_tp)
    orders = Order.objects.prefetch_related('products')
    return render(request, 'order_list.html', {'orders': orders, 'product_qty': product_qty, 'product_tp': product_tp})
    
@login_required
def checkout(request):
    cart = Cart(request)
    order = cart.checkout(request.user) 
    return render(request, 'cart.html', {'order': order})

def delete_orders(request):
    cart = Cart(request)
    cart.delete_all_orders()
    return render(request, 'order_list.html', {})