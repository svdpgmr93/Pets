from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='name', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), max_length=255)
