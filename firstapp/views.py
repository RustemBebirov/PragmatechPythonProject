from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def shop(request):
    return render(request, 'shop.html')

def shop_single(request):
    return render(request, 'shop-single.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')




