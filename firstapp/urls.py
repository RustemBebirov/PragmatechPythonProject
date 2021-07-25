from firstapp import admin
from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/<slug:slug>', views.blog_single, name='blog-single'),
    path('blog_comment_reply/<int:id>', views.blog_comment_reply, name='blog_comment_reply'),
    path('shop/', views.shop, name='shop'),
    path('shop-single/<int:id>', views.shop_single, name='shop-single'),
    path('like/',views.like_order,name='like_order'),
    path('add/',views.add_order,name='add_order'),
    path('liked-order/',views.like_order_page,name='like_orders'),
    path('add-order/',views.add_order_page,name='add_orders'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers-single/<int:id>', views.teachers_single, name='teachers-single'),
    path('courses/', views.courses, name='courses'),
    path('courses-single/<int:id>', views.courses_single, name='courses-single'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('ploicy/', views.policy, name='policy'),
    path('faq/', views.faq, name='faq'),
    path('events/', views.events, name='events'),
    path('events-single/<int:id>', views.events_single, name='events-single'),
]
