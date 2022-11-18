from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'todoapp.html')

def calendar(request):
    return render(request, 'calendar.html')

def createTask(request):
    if request.method == "POST":
        pass
