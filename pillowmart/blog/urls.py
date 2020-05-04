
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<str:filtre>/<int:id>', views.blog, name="blog"),
    path('show/single/<int:id>', views.single_blog, name="single-blog"),
]
