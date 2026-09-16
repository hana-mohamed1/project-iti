from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


def allusers(request):
    users = [
        [1, "Ahmed"],
        [2, "Mona"],
        [3, "Sara"]
    ]

    return render(request, 'users.html', {'users': users})
def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def logout(request):
    return render(request, 'logout.html')