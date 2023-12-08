from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label='name', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), max_length=255)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='name', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), max_length=255)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(), max_length=255)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data['password']

    def clean_email(self):
        if get_user_model().objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Такой E-mail уже существует')
        return self.cleaned_data['email']