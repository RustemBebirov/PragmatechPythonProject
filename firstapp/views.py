from io import DEFAULT_BUFFER_SIZE
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Blog_category ,Blog_comment, Blog_comment_reply, Contact ,Event,Tag,Teacher,Teacher_Comment,Course,Course_category,Course_Comment
from .forms import ContactForm, BlogCommentForm,BlogCommentFormReply




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






