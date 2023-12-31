from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegistrationForm, ProfileForm
from .models import Owner


def hello(request):
    login_form = LoginForm()
    register_form = RegistrationForm()
    if request.method == 'POST':
        print(request.POST)
        print('Run POST req')
        if 'email' in request.POST:
            print(request.POST)
            print('Run REGISTRATION')
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                return render(request, 'index.html',  {'login_form': login_form, 'register_form': register_form})
        else:
            print(request.POST)
            print('Run LOGIN')
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user and user.is_active:
                    login(request, user)
                    return render(request, 'index.html',  {'login_form': login_form, 'register_form': register_form})
    else:
        print('Run GET req.')
        return render(request, 'index.html', {'login_form': login_form, 'register_form': register_form})


def logged_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user and user.is_active:
                login(request, user)
                return render(request, 'index.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logged_out(request):
    logout(request)
    return redirect(hello)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'Users/register_done.html')
    form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile_data(request):
    username = request.user.username
    owner = Owner.objects.get(username=username)
    context = {'owner': owner}
    return render(request,
                  'profile_page.html', context)

def show_modal(request):
    form = RegistrationForm()
    return render(request, 'show_modal.html', {'form': form})
