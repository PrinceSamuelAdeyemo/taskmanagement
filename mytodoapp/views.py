from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse

from .models import Profile, BusinessProfile, Task
# Create your views here.


class Signup(View):
    
    global user_objects
    user_objects = User.objects.all()
    
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        username = request.POST['username'].lower()
        firstName = request.POST['firstName'].lower()
        middleName = request.POST['middleName'].lower()
        lastName = request.POST['lastName'].lower()
        email = request.POST['email'].lower()
        password = request.POST['password']
        password2 = request.POST['password2']
        
        required_fields = [username, firstName, middleName, lastName, email, password, password2]
        
        for each_field in required_fields:
            if each_field != '' or each_field != None:
                if password == password2:
                    if User.objects.filter(username = username).exists():
                        return HttpResponse('Username taken!')
                        
                    else:
                        user_model = User.objects.create_user(username = username, first_name = firstName, last_name = lastName, email = email, password = password)
                        user_model.save()
                        
                        user_profile = Profile.objects.create(user = user_model)
                        authenticated_user = auth.authenticate(request, username = username, password = password)
                        auth.login(request, authenticated_user)
                        return redirect('login')
                    
                else:
                    return HttpResponse('Not logged in!')
        

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        authenticated_user = auth.authenticate(request, username = username, password = password)
        if authenticated_user != None:
            auth.login(request, authenticated_user)
            return redirect('/')
        else:
            return render(request, 'login.html')
        
    
@login_required(login_url='login')    
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

@login_required(login_url = "login")
def index(request):
    return render(request, 'todoapp.html')

def calendar(request):
    return render(request, 'calendar.html')

def settings(request):
    return render(request, 'settings.html')

def createTask(request):
    if request.method == "POST":
        pass
