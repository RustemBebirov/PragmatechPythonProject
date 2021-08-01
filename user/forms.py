from user.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
    'class':'form-control'})
    )
   
    password2 = forms.CharField(label='Confirm',widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}),
    
    
    )

    agree = forms.BooleanField(label="""I agree all statements in  <a href="/pages/privacy" class='term-service'>Terms of service</a>""")

    class Meta:
        model = User
        fields = (
            'fullname',
            'email',
            'password1',
            'password2',
            'image',
            'agree'
        )
        
    # widgets = {
    #         'fullname' : forms.TextInput(attrs={
    #             'class':'form-control', 'placeholder':'Your Name'
    #         }),
    #         'email' : forms.EmailInput(attrs={
    #             'class':'form-control', 'placeholder':'Your Email'
    #         }),
    #         'message' : forms.Textarea(attrs={
    #             'class':'form-control', 'placeholder':'Your Message'
    #         }),

    #     }


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=127,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }))
    password = forms.CharField(max_length=127,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))