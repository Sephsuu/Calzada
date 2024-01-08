from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_list, name='order_list'),
    path('delete_orders/', views.delete_orders, name='delete_orders'),
]