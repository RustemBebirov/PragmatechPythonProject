from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import forms
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request, response
from .models import Blog, Blog_category ,Blog_comment, Blog_comment_reply, Contact ,Order,Order_Comment, Order_category,Event,Tag,Teacher,Teacher_Comment,Course,Course_category,Course_Comment
from .forms import ContactForm, BlogCommentForm,BlogCommentFormReply
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    courses = Course.objects.all()[:4]
    context = {
        'courses' : courses,
        
    }
    return render(request, 'index.html', context)

# blog view start
def blog(request):
    keyword = request.GET.get('keyword')

    if keyword:
        blogs = Blog.objects.filter(title__icontains = keyword)
        blog_categories = Blog_category.objects.all()
        context = {
        'blogs' : blogs,
        'categories' : blog_categories,
        }
        return render(request,'blog.html',context)
    
    blogs = Blog.objects.all()
    blog_categories = Blog_category.objects.all()
    context = {
        'blogs' : blogs,
        'categories' : blog_categories,
    }

    return render(request, 'blog.html',context)

def blog_single(request,slug):

    keyword = request.GET.get('keyword')

    if keyword:
        blogs = Blog.objects.filter(title__icontains = keyword)
        blog_categories = Blog_category.objects.all()
        context = {
        'blogs' : blogs,
        'categories' : blog_categories,
        }
        return render(request,'blog.html',context)


    # blog = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, slug=slug)
    blog_categories = Blog_category.objects.all()
    blog_comments = blog.comment_blog.all()
    form1 = BlogCommentForm()
    form2 = BlogCommentFormReply()

    if request.method == 'POST':
        form1 = BlogCommentForm(request.POST)
        if form1.is_valid():
            full_name = form1.cleaned_data.get('full_name')
            email = form1.cleaned_data.get('email')
            content = form1.cleaned_data.get('content')
            newComment = Blog_comment(author = full_name, email = email, content=content ,blog= blog)
            newComment.save()
            messages.success(request,'Your comment is add')
            return redirect(blog.get_absolute_url())

    context = {
        'blog' : blog,
        'categories' : blog_categories,
        'form1' : form1,
        'form2' : form2,
        'blog_comments' : blog_comments,
        
    }

    return render(request, 'blog-single.html', context)

def blog_comment_reply(request,id):
    comment = get_object_or_404(Blog_comment, id=id)
    form = BlogCommentFormReply()
    blog = get_object_or_404(Blog, slug=comment.blog.slug)
    if request.method == 'POST':
        form = BlogCommentFormReply(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            newComment = Blog_comment_reply(author = full_name, email = email, content=content ,comment= comment)
            newComment.save()
            messages.success(request,'Your comment is add')
            return redirect(blog.get_absolute_url())

#blog view end

#order view start
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

def like_order(request):
    if request.method == 'POST':
        liked_orders = request.COOKIES.get('liked_orders', '')
        order_id = request.POST.get('order_id')
    html = render_to_string('successfuly_added.html')
    response = HttpResponse(html)
    if order_id not in liked_orders.split(','):
        response.set_cookie("liked_orders",f'{liked_orders}{order_id},')
    return response

def like_order_page(request):
    like_orders = request.COOKIES.get('liked_orders','')
    liked_order_ids=[]
    for i in like_orders:
        try:
            j=int(i)
            liked_order_ids.append(j)
        except:
            print('None')

    orders = Order.objects.filter(id__in=liked_order_ids)
    context ={
        'orders': orders
    }
    return render(request,'liked_orders.html',context)

def add_order(request):
    if request.method == 'POST':
        add_orders = request.COOKIES.get('add_orders', '')
        order_id = request.POST.get('order_id')
    html = render_to_string('successfuly_added.html')
    response = HttpResponse(html)
    if order_id not in add_orders.split(','):
        response.set_cookie("add_orders",f'{add_orders}{order_id},')
    return response

def add_order_page(request):
    add_orders = request.COOKIES.get('add_orders','')
    add_order_ids=[]
    for i in add_orders:
        try:
            j=int(i)
            add_order_ids.append(j)
        except:
            print('None')

    orders = Order.objects.filter(id__in=add_order_ids)
    context ={
        'orders': orders
    }
    return render(request,'add_orders.html',context)
# order view end

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
    keyword = request.GET.get('keyword')

    if keyword:
        course = Course.objects.filter(title__icontains = keyword)
        context = {
        'course' : course,
        }
        return render(request,'courses.html',context)
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




