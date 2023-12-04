from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

def hello(request):
    # if request.user.is_authenticated:
    #     return HttpResponse('Hello USER' + str(request.user.username))
    # else:
    #     return HttpResponse('Hello Test')
    return render(request, 'base.html')

def logged_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user and user.is_active:
                login(request, user)
                return render(request, 'base.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logged_out(request):
    logout(request)
    return render(request, 'base.html')