from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Blog

@receiver(pre_save,sender=Blog)
def save_blog(sender,instance,**kwargs):
    instance.slug = slugify(instance.title)





