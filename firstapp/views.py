from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import forms
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request
from .models import Blog, Blog_category ,Blog_comment, Contact ,Order,Order_Comment, Order_category,Event,Tag,Teacher,Teacher_Comment,Course,Course_category,Course_Comment
from .forms import ContactForm, BlogCommentForm
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

def blog_single(request,slug):
    # blog = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, slug=slug)
    blog_categories = Blog_category.objects.all()
    blog_comments = blog.comment_blog.all()
    form = BlogCommentForm()
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            newComment = Blog_comment(full_name = full_name, email = email, content=content ,blog= blog)
            newComment.save()
            messages.success(request,'Your comment is add')
            return redirect(blog.get_absolute_url())

    context = {
        'blog' : blog,
        'categories' : blog_categories,
        'form' : form,
        'blog_comments' : blog_comments,
        
    }

    return render(request, 'blog-single.html', context)

def shop(request):
    orders = Order.objects.all()
    context = {
        'orders' : orders
    }
    return render(request, 'shop.html',context)

def shop_single(request,id):
    order = get_object_or_404(Order, id=id)
    orders = Order.objects.order_by('-created_at')[:4]
    
    context = {
        'order' : order,
        'orders' : orders
    }
    return render(request, 'shop-single.html', context)

def events(request):
    lesson_events = Event.objects.all()
    context = {
        'events' : lesson_events,
    }
    return render(request, 'events.html', context)

def events_single(request,id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event' : event,
    }
    return render(request, 'events-single.html', context)

def teachers(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher' : teacher
    }
    return render(request, 'teachers.html', context)

def teachers_single(request,id):
    teacher = get_object_or_404(Teacher, id=id)
    context = {
        'teacher' : teacher,
    }
    return render(request, 'teachers-single.html', context)

def courses(request):
    course = Course.objects.all()
    context = {
        'course' : course
    }
    return render(request, 'courses.html', context)

def courses_single(request,id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course' : course,
    }
    return render(request, 'courses-single.html', context)

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            newContact = Contact(full_name = full_name, email = email,subject=subject, phone = phone,message = message)
            newContact.save()
            messages.success(request,'Your message sent')
            return redirect ('firstapp:index')
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')

def policy(request):
    return render(request, 'policy.html')

def faq(request):
    return render(request, 'faq.html')




