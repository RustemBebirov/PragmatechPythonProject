from firstapp import admin
from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/<slug:slug>', views.blog_single, name='blog-single'),
    path('blog_comment_reply/<int:id>', views.blog_comment_reply, name='blog_comment_reply'),   
    path('teachers/', views.teachers, name='teachers'),
    path('teachers-single/<int:id>', views.teachers_single, name='teachers-single'),
    path('courses/', views.courses, name='courses'),
    path('courses-single/<int:id>', views.courses_single, name='courses-single'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('events-single/<int:id>', views.events_single, name='events-single'),
]
