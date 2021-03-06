from django.template import Library
from blog.models import Blog

register = Library()

@register.simple_tag
def get_blog(published=True):
    return Blog.objects.filter(is_published=published)
