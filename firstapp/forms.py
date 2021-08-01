from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=127,label='Your Name',widget=forms.TextInput(attrs={'class': 'form-input','placeholder':'Your Name'}))
    email = forms.EmailField(max_length=127,label='Your Email',widget=forms.EmailInput(attrs={'class': 'form-input','placeholder':'Your Email'}))
    subject = forms.CharField(max_length=127,label='Subject',widget=forms.TextInput(attrs={'class': 'form-input','placeholder':'Subject'}))
    phone = forms.CharField(max_length=127,label='Your Phone',widget=forms.TextInput(attrs={'class': 'form-input','placeholder':'Your Phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input','placeholder':'Your Message'}))
    
    
    def clean(self):
        full_name = self.cleaned_data.get('full_name')
        email = self.cleaned_data.get('email')
        subject = self.cleaned_data.get('subject')
        phone = self.cleaned_data.get('phone')
        message = self.cleaned_data.get('message')


        values ={
            'full_name' : full_name,
            'email' : email,
            'subject' : subject,
            'phone' : phone,
            'message' : message,
        }
        return values

    # class Meta:
    #     model = Contact
    #     fields = (
    #         'full_name',
    #         'email',
    #         'subject',
    #         'phone',
    #         'message',
    #     )
        

    #     widgets = {
    #         'full_name' : forms.TextInput(attrs={
    #             'class' : 'form-control', 'placeholder' : 'Your Name'
    #         }),
    #         'email' : forms.EmailInput(attrs={
    #             'class' : 'form-control', 'placeholder' : 'Your Email'
    #         }),
    #         'subject' : forms.TextInput(attrs={
    #             'class' : 'form-control', 'placeholder' : 'Your Subject'
    #         }),
    #         'phone' : forms.TextInput(attrs={
    #             'class' : 'form-control', 'placeholder' : 'Your Phone'
    #         }),
    #         'message' : forms.Textarea(attrs={
    #             'class' : 'form-control', 'placeholder' : 'Your Message'
    #         }),

    #     }
      
