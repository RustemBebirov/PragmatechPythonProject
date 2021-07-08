from firstapp import admin
from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/<int:id>', views.blog_single, name='blog-single'),
    path('shop/', views.shop, name='shop'),
    path('shop-single/', views.shop_single, name='shop-single'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers-single/', views.teachers_single, name='teachers-single'),
    path('courses/', views.courses, name='courses'),
    path('courses-single/', views.courses_single, name='courses-single'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('ploicy/', views.policy, name='policy'),
    path('faq/', views.faq, name='faq'),
    path('events/', views.events, name='events'),
    path('events-single/', views.events_single, name='events-single'),
]
