from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Blog_category ,Blog_comment ,Order,Order_Comment, Order_category,Event,Tag,Teacher,Teacher_Comment,Course,Course_category,Course_Comment
# Create your views here.

def index(request):
    return render(request, 'index.html')


def blog(request):
    blogs = Blog.objects.all()
    blog_categories = Blog_category.objects.all()
    context = {
        'blogs' : blogs,
        'categories' : blog_categories,
    }

    return render(request, 'blog.html',context)

def blog_single(request,id):
    blog = Blog.objects.get(id=id)
    blog_categories = Blog_category.objects.all()
    blog_comments = Blog_comment.objects.get(id=id)
    context = {
        'blog' : blog,
        'categories' : blog_categories,
        'comments' : blog_comments
    }

    return render(request, 'blog-single.html', context)

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




