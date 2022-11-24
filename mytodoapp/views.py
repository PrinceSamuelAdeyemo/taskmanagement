from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from .models import Profile, BusinessProfile, Task
# Create your views here.


class Signup(View):
    
    global user_objects
    user_objects = User.objects.all()
    
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        if 'personalSignupSubmit' in request.POST:
            #return HttpResponse("personal")
        
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
                    if User.objects.filter(username = username).exists():
                        messages.warning(request, "Username is taken!")
                    
                    else:
                        if password == password2:
                            
                            user_model = User.objects.create_user(username = username, first_name = firstName, last_name = lastName, email = email, password = password)
                            user_model.save()
                            
                            user_profile = Profile.objects.create(personal_basicdetails = user_model)
                            authenticated_user = auth.authenticate(request, username = username, password = password)
                            auth.login(request, authenticated_user)
                            return redirect('/')
                            
                        else:
                            messages.warning(request, "Passwords don't match!")
                    
        elif 'businessSignupSubmit' in request.POST:
            username = request.POST['username'].lower()
            companyName = request.POST['companyName']
            companyNameabbr = request.POST['companyNameabbr'].lower()
            email = request.POST['businessemail'].lower()
            password = request.POST['password']
            password2 = request.POST['password2']
            
            required_fields = [username, companyName, email, password, password2]
            
            for each_field in required_fields:
                if each_field != '' or each_field != None:
                    if User.objects.filter(username = username).exists():
                        messages.warning(request, "Username is taken!")
                        
                    else:
                        if password == password2:
                            user_model = User.objects.create_user(username = username, first_name = companyName, last_name = companyNameabbr, email = email, password = password)
                            user_model.save()
                            
                            business_profile = BusinessProfile.objects.create(business_basicdetails = user_model)
                            authenticated_user = auth.authenticate(request, username = username, password = password)
                            auth.login(request, authenticated_user)
                            return redirect('/')
                        
                        else:
                            messages.warning(request, "Passwords don't match!")
                    
        else:
            return render(request, 'login.html')
            
        

class Login(View):
    
    def get(self, request):
        
        return render(request, 'login.html')
    
    
    def post(self, request):
        if "personalSignin" in request.POST:
            
            email = request.POST['email']
            password = request.POST['password']
            
            if (email == '' or email == None) and (password != '' or password != None):
                messages.info(request, "Please input username")
                return redirect('login')
            
            elif (email != '' or email != None) and (password == '' or password == None):
                messages.info(request, "Please input password")
                return redirect('login')
            
            elif (email == '' or email == None) and (password == '' or password == None):
                messages.info(request, "Please input details")
                return redirect('login')
            
            if User.objects.filter(email = email).exists():
                user_objectfilter = User.objects.filter(email = email)
                try:
                    user_object = User.objects.get(email = email)
                    user_profile = Profile.objects.get(personal_basicdetails = user_object)
                    if user_profile:
                        authenticated_user = auth.authenticate(request, username = User.objects.get(email = email), password = password)
                        if authenticated_user != None:
                            auth.login(request, authenticated_user)
                            return redirect('/')
                        else:
                            messages.info(request, "Profile does not exist!")
                            return redirect('/login')
                        
                    else:
                        messages.info(request, "Profile does not exist!")
                        return redirect('/login')
                    
                except Profile.DoesNotExist:
                    messages.info(request, "Profile does not exist!")
                    return redirect('/login')
                    
                
            
            elif User.DoesNotExist:
                messages.info(request, "User does not exist!")
                return redirect('/login')
            
        elif "businessSignin" in request.POST:
            
            email = request.POST['businessemail']
            password = request.POST['businesspassword']
            
            if (email == '' or email == None) and (password != '' or password != None):
                messages.info(request, "Please input username")
                return redirect('login')
            
            elif (email != '' or email != None) and (password == '' or password == None):
                messages.info(request, "Please input password")
                return redirect('login')
            
            elif (email == '' or email == None) and (password == '' or password == None):
                messages.info(request, "Please input details")
                return redirect('login')
            
            if User.objects.filter(email = email).exists():
                user_objectfilter = User.objects.filter(email = email)
                try:
                    user_object = User.objects.get(email = email)
                    business_profile = BusinessProfile.objects.get(business_basicdetails = user_object)
                    if business_profile:
                        authenticated_user = auth.authenticate(request, username = User.objects.get(email = email), password = password)
                        if authenticated_user != None:
                            auth.login(request, authenticated_user)
                            return redirect('/')
                        else:
                            messages.info(request, "Business Profile does not exist!")
                            return redirect('/login')
                        
                    else:
                        messages.info(request, "Business Profile does not exist!")
                        return redirect('/login')
                    
                except Profile.DoesNotExist:
                    messages.info(request, "Business Profile does not exist!")
                    return redirect('/login')
                
            
            elif User.DoesNotExist:
                messages.info(request, "User does not exist!")
                return redirect('/login')
            
        else:
                return HttpResponse('None of the personal and business login works!')
        
    
@login_required(login_url='login')    
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

@login_required(login_url = "login")
def index(request):
    return render(request, 'todoapp.html')

@login_required(login_url = "login")
def calendar(request):
    return render(request, 'calendar.html')

@login_required(login_url = "login")
def settings(request):
    return render(request, 'settings.html')

@login_required(login_url = "login")
def createTask(request):
    if request.method == "POST":
        pass
