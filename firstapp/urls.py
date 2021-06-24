from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('shop/', views.shop, name='shop'),
    path('shop-single/', views.shop_single, name='shop-single'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]