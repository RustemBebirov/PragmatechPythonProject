from django.shortcuts import render
from django.views.generic import ListView
from .models import Gallery

# Create your views here.

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.all()



