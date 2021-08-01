from django import forms

class BlogCommentForm(forms.Form):
    
    full_name = forms.CharField(max_length=127,label='Your Name',widget=forms.TextInput(attrs={'class': 'form-input','placeholder':'Your Name'}))
    email = forms.EmailField(max_length=127,label='Your Email',widget=forms.EmailInput(attrs={'class': 'form-input','placeholder':'Your Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input','placeholder':'Comment'}))


    def clean(self):
        full_name = self.cleaned_data.get('full_name')
        email = self.cleaned_data.get('email')
        content = self.cleaned_data.get('content')


        values ={
            'full_name' : full_name,
            'email' : email,
            'content' : content,
        }
        return values


class BlogCommentFormReply(forms.Form):
    full_name = forms.CharField(max_length=127,label='Your Name',widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(max_length=127,label='Your Email',widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}))

    def clean(self):
        full_name = self.cleaned_data.get('full_name')
        email = self.cleaned_data.get('email')
        content = self.cleaned_data.get('content')


        values ={
            'full_name' : full_name,
            'email' : email,
            'content' : content,
        }
        return values
