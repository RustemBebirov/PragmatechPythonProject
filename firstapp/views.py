from io import DEFAULT_BUFFER_SIZE
from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contact 
from .forms import ContactForm
from teacher.models import Course



# Create your views here.

def index(request):
    courses = Course.objects.all()[:4]
    context = {
        'courses' : courses,
        
    }
    return render(request, 'index.html', context)



def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            newContact = Contact(full_name = full_name, email = email,subject=subject, phone = phone,message = message)
            newContact.save()
            messages.success(request,'Your message sent')
            return redirect ('firstapp:index')
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)






