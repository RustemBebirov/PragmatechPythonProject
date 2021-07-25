from django.forms import fields
from user import models
from user.models import User
from django import forms
from django.forms.fields import EmailField
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control','placeholder':'Password'}),
    
    )
   
    password2 = forms.CharField(label='Confirm',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control','placeholder':'Confirm Password'}),
    
    )

    class Meta:
        model = User
        fields = {
            'email',
            'fullname',
            'phone',
            'password1',
            'password2',
            'image',
            'category',

        }
        
    widgets = {
            'fullname' : forms.TextInput(attrs={
                'class' : 'form-control', 'placeholder' : 'Your Name'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control', 'placeholder' : 'Your Email'
            }),
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control', 'placeholder' : 'Your Phone'
            }),
            'category' : forms.ChoiceField(),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control', 'placeholder' : 'Your Message'
            }),

        }


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=127,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    password = forms.CharField(max_length=127,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))