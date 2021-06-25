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

def events(request):
    return render(request, 'events.html')

def events_single(request):
    return render(request, 'events-single.html')

def teachers(request):
    return render(request, 'teachers.html')

def teachers_single(request):
    return render(request, 'teachers-single.html')

def courses(request):
    return render(request, 'courses.html')

def courses_single(request):
    return render(request, 'courses-single.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def policy(request):
    return render(request, 'policy.html')

def faq(request):
    return render(request, 'faq.html')



#homework 
def homework(request):
    return render(request, 'homework.html')

