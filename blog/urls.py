from django.urls import path
from blog.views import blog,blog_comment_reply,blog_single

app_name = 'blogs'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog-single/<slug:slug>', blog_single, name='blog-single'),
    path('blog_comment_reply/<int:id>', blog_comment_reply, name='blog_comment_reply'),  
    
    
]