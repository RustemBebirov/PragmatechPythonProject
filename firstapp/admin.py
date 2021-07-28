from django.contrib import admin
from .models import Blog, Tag, Blog_category, Blog_comment, Blog_comment_reply,Contact,Teacher,Teacher_Comment,Course, Course_category,Course_Comment,Event

# Register your models here.
# blog model registration
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog_comment)
admin.site.register(Blog_category)
admin.site.register(Tag)
admin.site.register(Blog_comment_reply)
admin.site.register(Teacher)
admin.site.register(Teacher_Comment)
admin.site.register(Course)
admin.site.register(Course_category)
admin.site.register(Course_Comment)
admin.site.register(Event)



#contact model
admin.site.register(Contact)