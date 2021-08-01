from django.shortcuts import render, redirect
from user import forms 
from user.forms import LoginForm, RegistrationForm 
from django.urls import reverse_lazy 
from django.utils.encoding import force_text 
from user.tasks import send_confirmation_mail 
from user.tools.tokens import account_activation_token 
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages

from django.contrib.auth import get_user_model, authenticate, login as django_login , logout as django_logout

User = get_user_model()

# Create your views here.

def register(request): 
    form = RegistrationForm() 
    if request.method == 'POST': 
        form = RegistrationForm(data=request.POST, files=request.FILES) 
        if form.is_valid(): 
            user = form.save(commit=False) 
            user.is_active = False 
            user.save() 
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST'] 
            send_confirmation_mail(user_id=user.id, site_address=site_address) 
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('firstapp:index'))
    context = {
    'form': form,
    }
    return render(request, 'register.html', context)

def activate(request, uidb64, token): 

    try:
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid) 
    except:
        (TypeError, ValueError, OverflowError, User.DoesNotExist) 
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('firstapp:index'))

    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('user:register'))

    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('user:register'))


def login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email,password=password)
        if user:
            django_login(request,user)
            messages.success(request,'You logged in successfuly')
            return redirect(reverse_lazy('firstapp:index'))
        else:
            messages.error(request,'The information you entered is valid')

    context = {
        'form':form
    }
    return render(request,'login.html',context)    

def logout(request):
    django_logout(request)
    messages.success(request,'You logged out')
    return redirect(reverse_lazy('firstapp:index'))