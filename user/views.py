import django
from django.forms import forms
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            newUser = User(username = name, email = email)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,'Your registration is succsess')
            
            return redirect('firstapp:index')
        else:
            context = {
            'form' : form
            }
            return render(request,'register.html',context)
    else:
        form = RegisterForm()
        context = {
        'form' : form
        }
        return render(request,'register.html',context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Username or password is wrong")
            return render(request,'login.html',context)
        messages.success(request,'Login is success')
        login(request,user)
        return redirect('firstapp:index')
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    messages.success(request,'Logout is success')
    return redirect('firstapp:index')