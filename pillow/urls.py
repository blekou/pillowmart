"""pillowmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('contact', views.contact, name="contact"),
    path('elements', views.elements, name="elements"),
    path('login', views.login, name="login"),
    path('main', views.main, name="main"),
    path('product_list', views.product_list, name="product_list"),
    path('single-blog', views.single_blog, name="single-blog"),
    path('single-product', views.single_product, name="single-product"),
]
