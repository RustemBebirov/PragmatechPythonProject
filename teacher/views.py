from teacher.forms import CourseCategoryForm, CourseCurriculumForm, CourseForm, TeacherInfoForm
from teacher.models import Event,Course,Course_category,Course_Comment,Curriculum,TeacherInfo,Teacher_Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

@login_required
def dashboard(request):
    course = Course.objects.all()
    context={
        'courses':course
    }
    return render(request,'dashboard.html',context)


class TeacherInfoCreateView(CreateView):
    model = TeacherInfo
    form_class = TeacherInfoForm
    template_name = 'addteacherinfo.html'
    success_url = '/teachers/dashboard'

class TeacherInfoUpdateView(UpdateView):
    model = TeacherInfo
    form_class = TeacherInfoForm
    template_name = 'addteacherinfo.html'
    success_url = '/teachers/dashboard'
    
    queryset = TeacherInfo.objects.all()


class CourseCategoryCreateView(CreateView):
    model = Course_category
    form_class = CourseCategoryForm
    template_name = 'addcategory.html'
    success_url = '/teachers/dashboard'

class CourseCurriculumCreateView(CreateView):
    model = Curriculum
    form_class = CourseCurriculumForm
    template_name = 'addcurriculum.html'
    success_url = '/teachers/dashboard'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'addcourse.html'
    success_url = '/teachers/dashboard'

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.teacher = self.request.user
    #     obj.save()        
    #     return http.HttpResponseRedirect(self.get_success_url())

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'addcourse.html'
    success_url = '/teachers/dashboard'

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'delete.html'
    success_url = '/teachers/dashboard'






