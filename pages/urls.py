from django.urls import path
from django.views.generic import TemplateView
from .views import GalleryListView

app_name = 'pages'

urlpatterns = [
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('privacy/', TemplateView.as_view(template_name='policy.html'), name='privacy'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    
    
]
