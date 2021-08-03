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
    path('teacher-info/add/', TeacherInfoCreateView.as_view(), name='teacher-info-add'),
    # path('teacher/<int:pk>/', TeacherUpdateCreateView.as_view(), name='teacher-update'),
    # path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'
    path('category/add/', CourseCategoryCreateView.as_view(), name='category-add'),
    path('curriculum/add/', CourseCurriculumCreateView.as_view(), name='curriculum-add'),
    path('course/add/', CourseCreateView.as_view(), name='course-add'),
    path('course/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete')
    
]