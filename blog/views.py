from blog.models import Blog,Blog_category,Blog_comment,Blog_comment_reply
from blog.forms import BlogCommentForm,BlogCommentFormReply
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

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
    blog_comments = Blog_comment.objects.filter(id=blog.id).all()
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