from django.conf.urls import include
from firstapp import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', include('firstapp.urls', namespace='firstapp')),
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]