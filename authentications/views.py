from django.shortcuts import render


# Create your views here.
def error_view(request):
    return render(request, '500.html')


def home_view(request):
    return render(request, 'registration/login.html')


def user_view(request):
    return render(request, 'users.html')
