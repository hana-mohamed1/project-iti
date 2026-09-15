from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def insert(request):
    return HttpResponse("<h1>Insert Page</h1>")

def update(request):
    return HttpResponse("<h1>Update Page</h1>")

def delete(request):
    return HttpResponse("<h1>Delete Page</h1>")
