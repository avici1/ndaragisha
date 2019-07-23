import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def error_view(request):
    return render(request, '500.html')


def dashboards(request):
    return render(request, 'dashboard.html')


def home_view(request):
    return render(request, 'registration/login.html')


def user_view(request):
    return render(request, 'users.html')


def signup_view(request):
    return render(request, 'signup.html')


def custom_signup(request):
    if request.method == 'POST':
        if request.POST.get('pass_1') == request.POST.get('pass_2'):
            users = ClientUsers()
            users.phone = request.POST.get('phone')
            users.first_name = request.POST.get('first_name')
            users.last_name = request.POST.get('last_name')
            users.password = hashlib.sha512(request.POST.get('pass_1').encode()).hexdigest()
            users.save()
            return redirect('/home/')
        else:
            return render(request, '500.html', {'message': 'Passwords dont match',
                                                'url': 'http://127.0.0.1:8000/api/auth/signup/',
                                                'where': 'Signup page'})

    else:
        return render(request, '500.html',
                      {'message': 'illegally Accessed', 'url': 'http://127.0.0.1:8000/home/', 'where': 'Home Page'})


def custom_login(request):
    if request.method == 'POST':
        password = hashlib.sha512(str(request.POST.get('password')).encode()).hexdigest()
        phone = request.POST.get('phone')
    else:
        return render(request, '500.html',
                      {'message': 'Illegal acess', 'url': 'http://127.0.0.1:8000/home/', 'where': 'Home Page'})

    try:
        users = ClientUsers.objects.get(phone=phone, password=password)
        return render(request, 'users.html', {'first_name': users.first_name})
    except ObjectDoesNotExist as e:
        return render(request, 'registration/login.html', {'message': 'You got that one wrong '})
