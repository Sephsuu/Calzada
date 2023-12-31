from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('login_required/', views.login_required, name='login_required'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home, name='user_home'),
    path('show_all_products/', views.show_all_products, name='show_all_products'),
    path('show_all_products_image/', views.show_all_products_image, name='show_all_products_image'),
    path('show_shoe_products/', views.show_shoe_products, name='show_shoe_products'),
    path('show_shoe_products_image/', views.show_shoe_products_image, name='show_shoe_products_image'),
    path('show_cloth_products/', views.show_cloth_products, name='show_cloth_products'),
    path('show_cloth_products_image/', views.show_cloth_products_image, name='show_cloth_products_image'),
    path('show_gadget_products/', views.show_gadget_products, name='show_gadget_products'),
    path('show_gadget_products_image/', views.show_gadget_products_image, name='show_gadget_products_image'),
    path('show_skincare_products/', views.show_skincare_products, name='show_skincare_products'),
    path('show_skincare_products_image/', views.show_skincare_products_image, name='show_skincare_products_image'),
    path('show_poultry_products/', views.show_poultry_products, name='show_poultry_products'),
    path('show_poultry_products_image/', views.show_poultry_products_image, name='show_poultry_products_image'),
    path('search_product', views.search_product, name='search_product'),
    path('product_detail/product_id=<int:product_id>/', views.product_detail, name='product_detail'),
    path('download_act/', views.download_act, name='download_act'),
    path('download_file/', views.download_file, name='download_file'),
    path('download/', views.download, name='download'),
]

