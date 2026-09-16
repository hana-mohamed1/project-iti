from django.shortcuts import render, redirect
from .models import MyUser
from django.http import HttpResponse
# Create your views here.
def allusers(request):
    users = MyUser.objects.all()
    return render(request, 'users.html', {'users': users})


def insert(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        MyUser.objects.create(
            username=username,
            email=email,
            password=password
        )

        return redirect('/myuser/')

    return render(request, 'insert_user.html')
def update(request, id):
    user = MyUser.objects.get(id=id)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()

        return redirect('/myuser/')

    return render(request, 'update_user.html', {'user': user})

def delete(request, id):
    user = MyUser.objects.get(id=id)
    user.delete()

    return redirect('/myuser/')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def logout(request):
    return render(request, 'logout.html')
