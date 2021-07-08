from django import forms
from django.forms.fields import EmailField

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50,label='Your Name',widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(max_length=50,label='Your Email',widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    confirm = forms.CharField(max_length=20,label='Password Confirm',widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError("Password not equal")
        
        values ={
            'name' : name,
            'email' : email,
            'password' : password,
        }
        return values


