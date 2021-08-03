from django import forms
from django.forms import fields
from teacher.models import *


class TeacherInfoForm(forms.ModelForm):

    class Meta:
        model = TeacherInfo
        fields = '__all__'

class CourseCategoryForm(forms.ModelForm):

    class Meta:
        model = Course_category
        fields = '__all__'


class CourseCurriculumForm(forms.ModelForm):

    class Meta:
        model = Curriculum
        fields = '__all__'


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'