from django.contrib import admin
from blog.models import *
# Register your models here.

# blog model registration

admin.site.register(Blog)
admin.site.register(Blog_comment)
admin.site.register(Blog_category)
admin.site.register(Tag)
admin.site.register(Blog_comment_reply)
