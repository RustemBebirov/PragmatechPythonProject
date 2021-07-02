from django.contrib import admin
from .models import Blog, Tag, Blog_category, Blog_comment, Contact, Order

# Register your models here.
# blog model registration
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Blog_comment)
admin.site.register(Blog_category)

#contact model
admin.site.register(Contact)