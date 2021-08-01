from teacher.models import Event,Course,Course_category,Course_Comment,Curriculum,TeacherInfo,Teacher_Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()
# Create your views here.


def events(request):
    lesson_events = Event.objects.all()
    context = {
        'events' : lesson_events,
    }
    return render(request, 'events.html', context)

def events_single(request,id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event' : event,
    }
    return render(request, 'events-single.html', context)

def teachers(request):
    teacher = User.objects.all() #filter(is_superuser=False)
    context = {
        'teachers' : teacher
    }
    return render(request, 'teachers.html', context)

def teachers_single(request,id):
    teacher = get_object_or_404(User, id=id)
    info = TeacherInfo.objects.filter(user=id).first()
    course = Course.objects.filter(user=teacher).all()
    context = {
        'teacher' : teacher,
        'info' : info,
        'courses':course
    }
    return render(request, 'teachers-single.html', context)

def courses(request):

    keyword = request.GET.get('keyword')

    if keyword:
        course = Course.objects.filter(title__icontains = keyword)
        context = {
        'courses' : course,
        }
        return render(request,'courses.html',context)

    course = Course.objects.all()
    context = {
        'courses' : course,
    }
    return render(request,'courses.html',context)
    

def courses_single(request,id):
    course = get_object_or_404(Course, id=id)
    related_courses = Course.objects.order_by('created_at')[:2]
    info = TeacherInfo.objects.filter(user=course.user.id).first()
    context = {
        'course' : course,
        'related_courses' : related_courses,
        'info' : info
    }
    return render(request, 'courses-single.html', context)


def dashboard(request):
    return render(request,'dashboard.html')




