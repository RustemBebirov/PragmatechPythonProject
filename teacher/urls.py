from django.urls import path
from teacher.views import *

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('courses/', courses, name='courses'),
    path('courses-single/<int:id>', courses_single, name='courses-single'),
    path('events/', events, name='events'),
    path('teachers/', teachers, name='teachers'),
    path('teachers-single/<int:id>', teachers_single, name='teachers-single'),
    path('events-single/<int:id>', events_single, name='events-single'),
    
    
]