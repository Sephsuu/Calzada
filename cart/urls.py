from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_update/', views.cart_update, name='cart_update'),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
]