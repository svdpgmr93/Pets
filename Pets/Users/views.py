from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

def hello(request):
    # if request.user.is_authenticated:
    #     return HttpResponse('Hello USER' + str(request.user.username))
    # else:
    #     return HttpResponse('Hello Test')
    return render(request, 'base.html')

def logged_in(request):
    return HttpResponse('Страница пользователя')


def logged_out(request):
    logout(request)
    return render(request, 'base.html')