
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('confirmation', views.confirmation, name="confirmation"),

    path('list', views.product_list, name="product_list"),
    path('list/<int:limit>', views.product_list, name="product_list"),
    path('list/<str:filtre>/<int:idt>', views.product_list, name="product_list"),
    
    path('show/single-product/<int:id>', views.single_product, name="single-product"),
    path('show/single-product/<str:act>/<int:id>', views.single_product, name="single-product"),
]
