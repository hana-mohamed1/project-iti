from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Track
# Create your views here.
def alltracks(request):
    tracks = Track.objects.all()
    return render(request, 'list.html', context={'tracks': tracks})
def insert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Track.objects.create(name=name)
        return redirect('/tracks/')

    return render(request, 'insert.html')
def update(request, id):
    track = Track.objects.get(id=id)

    if request.method == 'POST':
        track.name = request.POST.get('name')
        track.save()
        return redirect('/tracks/')

    return render(request, 'update.html', {'track': track})

def delete(request, id):
    track = Track.objects.get(id=id)
    track.delete()
    return redirect('/tracks/')