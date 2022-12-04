from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from datetime import datetime

from .models import Profile, BusinessProfile, Task, SubTask
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
                           
                            user_profile = Profile.objects.create(personal_basicdetails = user_model, id_profile = user_model.id)
                            authenticated_user = auth.authenticate(request, username = username, password = password)
                            auth.login(request, authenticated_user)
                            
                            
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
                            #userr = user_model.remove(task_id)
                            business_profile = BusinessProfile.objects.create(business_basicdetails = user_model, businessprofile_id = user_model.id)
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

#@login_required(login_url = "login")

class Index(View):
    def get(self, request):
        return render(request, 'todoapp.html')

@login_required(login_url = "login")
def calendar(request):
    return render(request, 'calendar.html')

@login_required(login_url = "login")
def settings(request):
    return render(request, 'settings.html')


    
class CreateTask(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name: 'signup'
    def get(self, request):
        return render(request, 'todoapp.html')
    
    def post(self, request):
        
        #if 'createtask' in request.POST:
        if request.method == 'POST':
            '''
            if 'None':
                return HttpResponse('Response is None')
            else:
                return HttpResponse('Response is Not none')
            #return HttpResponse("Sent")
            '''
            
            user = request.user.username
            
            taskOwner = request.user.username
            taskName = request.POST['task_name']
            taskDescription = request.POST['task_description']
            
            subtask_name = request.POST["subtaskinput"]
            #task_file
            #task_image
            #task_done
            #subtask
            personal_model = User.objects.filter(username = user).first()
            personal_profile = Profile.objects.get(personal_basicdetails = personal_model)
            #if personal_model.exists():
            #return HttpResponse(f"{personal_model}")
            
            checkpersonal_task = Task.objects.filter(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription).exists()
            if checkpersonal_task:
                personal_task = Task.objects.get(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription)
                subtask_name_model = SubTask.objects.create(task_parent = personal_task, subtask_name=subtask_name, subtask_date=datetime.now())
                subtask_name_model.save()
                return HttpResponse('Exists, but saved')
            else:
                task_model = Task.objects.create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription, task_date = datetime.now())
                task_model.save()
            
                #personal_task = Task.objects.filter(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription).first()
                personal_task = Task.objects.get(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription)
                subtask_name_model = SubTask.objects.create(task_parent = personal_task, subtask_name=subtask_name, subtask_date=datetime.now())
                subtask_name_model.save()
                return HttpResponse('Success')
         
        else:
            return HttpResponse("Not create task")
         
            
def add_record(request):
    data = {
        "title": request.POST.get('title', None),
        }
    serializer = self.serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def createtas(request):
    if request.method == 'POST':
        #return HttpResponse(list(request.POST.items()))#, '+', list(request.POST.items()))
        
        if 'subtaskinput' in request.POST:
            user = request.user.username
            personal_model = User.objects.filter(username = user).first()
            personal_profile = Profile.objects.get(personal_basicdetails = personal_model)
            '''
            personal_task = Task.objects.get(personalTaskowner = personal_profile, task_name = , task_description = )
            subtask_name = request.POST["subtaskinput"]
            
            
            subtask_name_model = SubTask.objects.create(task_parent = personal_task, subtask_name=subtask_name, subtask_date=datetime.now())
            subtask_name_model.save()
            '''
            return HttpResponse('Saved')
        
        else:
            return HttpResponse('It is not there')
        
        
        '''
        #name = request.POST['task_nam']
        #des = request.POST['task_descriptio']
        user = request.user.username
            
        taskOwner = request.user.username
        taskName = request.POST['task_name']
        taskDescription = request.POST['task_description']
        #task_file
        #task_image
        #task_done
        #subtask
        personal_model = User.objects.filter(username = user).first()
        personal_profile = Profile.objects.get(personal_basicdetails = personal_model)
        #if personal_model.exists():
        #return HttpResponse(f"{personal_model}")
        
        
        task_model = Task.objects.create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription, task_date = datetime.now())
        task_model.save()
        
        return HttpResponse('Success')
        '''
        
        '''
        if "None":
            return HttpResponse('It is None')
        else:
            
            #name = request.POST['task_nam']
            #des = request.POST['task_descriptio']
            user = request.user.username
                
            taskOwner = request.user.username
            taskName = request.POST['task_name']
            taskDescription = request.POST['task_description']
            #task_file
            #task_image
            #task_done
            #subtask
            personal_model = User.objects.filter(username = user).first()
            personal_profile = Profile.objects.get(personal_basicdetails = personal_model)
            #if personal_model.exists():
            #return HttpResponse(f"{personal_model}")
            
            
            task_model = Task.objects.create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription, task_date = datetime.now())
            task_model.save()
            
            return HttpResponse('Success')
            '''