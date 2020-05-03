
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('blog/<str:filtre>/<int:id>', views.blog, name="blog"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('contact', views.contact, name="contact"),
    path('register', views.register, name="register"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_page, name="logout"),
    path('product_list', views.product_list, name="product_list"),
    path('product_list/<int:limit>', views.product_list, name="product_list"),
    path('product_list/<str:filtre>/<int:idt>', views.product_list, name="product_list"),
    path('single-blog/<int:id>', views.single_blog, name="single-blog"),
    path('single-product/<int:id>', views.single_product, name="single-product"),
    path('single-product/<str:act>/<int:id>', views.single_product, name="single-product"),
]
