from django.contrib import messages
from django.contrib.auth.models import User
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
    blog_comments = Blog_comment.objects.all().filter(id=blog.id)
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
            return redirect('/')

    context = {
        'blog' : blog,
        'categories' : blog_categories,
        'form' : form,
        'blog_comments' : blog_comments,
        
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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            newContact= Contact(form)
            newContact.save()
            messages.success(request,'Succses')
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




