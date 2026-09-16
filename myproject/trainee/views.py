from django.shortcuts import render, redirect
from .models import Trainee
from django.http import HttpResponse
# Create your views here.
def insert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        Trainee.objects.create(
            name=name,
            email=email,
            address=address
        )

        return redirect('/trainee/')

    return render(request, 'insert_trainee.html')

def update(request, id):
    trainee = Trainee.objects.get(id=id)

    if request.method == 'POST':
        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.address = request.POST.get('address')
        trainee.save()

        return redirect('/trainee/')

    return render(request, 'update_trainee.html', {'trainee': trainee})

def delete(request, id):
    trainee = Trainee.objects.get(id=id)
    trainee.delete()

    return redirect('/trainee/')

def alltrainees(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainees.html', {'trainees': trainees})