from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget = forms.PasswordInput(), label='Password', max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget = forms.PasswordInput(), label='Password', max_length=20)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='Email', max_length=20)

class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300) 
    
class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()
    thumbnail = forms.FileField() 