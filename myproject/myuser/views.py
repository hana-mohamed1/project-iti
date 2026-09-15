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
    return HttpResponse("<h1>Login Page</h1>")

def signup(request):
    return HttpResponse("<h1>Signup Page</h1>")

def logout(request):
    return HttpResponse("<h1>Logout Page</h1>")
