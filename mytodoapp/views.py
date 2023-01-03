from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.contrib import messages
from datetime import datetime

from .models import Profile, BusinessProfile, Project, Board, Task
import json
# Create your views here.



###### Sign up view ######
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
            
            #for each_field in required_fields:
            if any(each_field == '' for each_field in required_fields):
                return redirect('/')
                    
                
            else:
                if User.objects.filter(username = username).exists():
                        messages.warning(request, "Username is taken!")
                    
                else:
                    if password == password2:
                        
                        user_model = User.objects.create_user(username = username, first_name = firstName, last_name = lastName, email = email, password = password)
                        user_model.save()
                        
                        user_profile = Profile.objects.create(personal_basicdetails = user_model, id_profile = user_model.id)
                        authenticated_user = auth.authenticate(request, username = username, password = password)
                        auth.login(request, authenticated_user)
                        return redirect('/dashboard')
                        
                        
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
            
            if any(each_field == '' for each_field in required_fields):
                return redirect('/')
            
            else:
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
                        return redirect('/dashboard')
                    
                    else:
                        messages.warning(request, "Passwords don't match!")
                
        else:
            return render(request, 'login.html')
            
        
###### Log in view ######
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
                            return redirect('/dashboard')
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
                            return redirect('/dashboard')
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
        
    
###### Log out view ######
@login_required(login_url='login')    
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

#@login_required(login_url = "login")


###### Homepage view ######
class Index(View):
    def get(self, request):
        return render(request, 'homepage.html')
    
    def post(self, request):
        pass
    
    
    
def getActivities(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        boardOwner = request.user.username
        user_model = User.objects.get(username = boardOwner)
        activities = Board.objects.all()
        user_activities = Board.objects.filter(board_owner = boardOwner)
        user_activities_completed = Board.objects.filter(board_owner = boardOwner, board_completed = True, board_inprogress = False)
        user_activities_progress = Board.objects.filter(board_owner = boardOwner, board_completed = False, board_inprogress = True)
        user_activities_notstarted = Board.objects.filter(board_owner = boardOwner, board_completed = False, board_inprogress = False)
        try:
            profile = Profile.objects.get(personal_basicdetails = user_model)
            #activities = Board.objects.filter(task_owner = taskOwner).order_by('task_dateUpdated')
            activities = Board.objects.all()
            return HttpResponse("Return in personal")
        
        except Profile.DoesNotExist:
            profile = BusinessProfile.objects.get(business_basicdetails = user_model)
            #activities = Board.objects.filter(task_owner).order_by('task_dateUpdated')
            activities = Board.objects.all()
            return HttpResponse("Return in personal")
        
        finally:
            
                
            #context = {'profile': profile, 'activities': activities, 'user_activities': user_activities, 
            #           'user_activities_completed': user_activities_completed, 'user_activities_progress': user_activities_progress, 
            #           'user_activities_notstarted': user_activities_notstarted,}
            
            return JsonResponse({
                #'profile': profile, 
                'activities': list(activities.values()), 
                'user_activities': list(user_activities.values()), 
                'user_activities_completed': list(user_activities_completed.values()), 
                'user_activities_progress': list(user_activities_progress.values()), 
                'user_activities_notstarted': list(user_activities_notstarted.values()),
                }, 
                                safe=False)
        #return render(request, 'todoapp.html', context=context)
                
    #else:
        #return HttpResponse("Not receiving any Django request")

###### Calendar view ######
@login_required(login_url = "login")
def calendar(request):
    return render(request, 'calendar.html')

def activities(request):
    return render(request, 'boards.html')

@login_required(login_url = "login")
def settings(request):
    return render(request, 'settings.html')


    
###### Createtask view  from the create board button in the html ######
class DashBoard(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name: 'signup'
    def get(self, request):
        if request.method == 'GET':# and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            boardOwner = request.user.username
            user_model = User.objects.get(username = boardOwner)
            activities = Board.objects.all()
            user_activities = Board.objects.filter(board_owner = boardOwner)
            user_activities_completed = Board.objects.filter(board_owner = boardOwner, board_completed = True, board_inprogress = False)
            user_activities_progress = Board.objects.filter(board_owner = boardOwner, board_completed = False, board_inprogress = True)
            user_activities_notstarted = Board.objects.filter(board_owner = boardOwner, board_completed = False, board_inprogress = False)
            try:
                profile = Profile.objects.get(personal_basicdetails = user_model)
                #activities = Board.objects.filter(task_owner = taskOwner).order_by('task_dateUpdated')
                activities = Board.objects.all()
                return HttpResponse("Return in personal")
            
            except Profile.DoesNotExist:
                profile = BusinessProfile.objects.get(business_basicdetails = user_model)
                #activities = Board.objects.filter(task_owner).order_by('task_dateUpdated')
                activities = Board.objects.all()
                return HttpResponse("Return in personal")
            
            finally:
                
                    
                #context = {'profile': profile, 'activities': activities, 'user_activities': user_activities, 
                #           'user_activities_completed': user_activities_completed, 'user_activities_progress': user_activities_progress, 
                #           'user_activities_notstarted': user_activities_notstarted,}
                
                '''return JsonResponse({
                    #'profile': profile, 
                    'activities': list(activities.values()), 
                    'user_activities': list(user_activities.values()), 
                    'user_activities_completed': list(user_activities_completed.values()), 
                    'user_activities_progress': list(user_activities_progress.values()), 
                    'user_activities_notstarted': list(user_activities_notstarted.values()),
                    }, 
                                    safe=False)'''
                return render(request, 'dashboard.html')
                
        else:
            return HttpResponse("Ajax not responding")


    
    def post(self, request):
        
        #if 'createtask' in request.POST:
        if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            '''
            if 'None':
                return HttpResponse('Response is None')
            else:
                return HttpResponse('Response is Not none')
            #return HttpResponse("Sent")
            '''
            # Get the user and board details from the front end.
            user = request.user.username
            
            taskOwner = request.user.username
            taskName = request.POST['task_name']
            
            taskDescription = request.POST['task_description']
            
            task_names = request.POST.getlist("subTaskArray[]")
            #task_names = json.loads(request.)
            
            #print(alltask_names)
            #task_names = [alltask_names]
            #task_file
            #task_image
            #task_done
            #task_name = ''
            
            # Check and access the profile of the user gotten from the front end.
            personal_model = User.objects.filter(username = user).first()
            personal_profile = Profile.objects.get(personal_basicdetails = personal_model)
            #if personal_model.exists():
            #return HttpResponse(f"{personal_model}")
            
            # Check if the board name received already exists.
            # If it does not exists, create the board and save it.
            # After the save, get the board which was saved and check if if the sub board was added, if it wasn't. Don't save any task, but if the sub board was added.
            #  Check if the sub board exists for the partcular board, if not, Save the tasks also.
            
            checkpersonal_task = Board.objects.filter(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription).exists()
            if not checkpersonal_task:
                task_model = Board.objects.create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription, task_date = datetime.now())
                task_model.save()
                
                #if task_model.save() == True:
                
                #personal_task = Board.objects.get(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription)
                #personal_task = Board.objects.get_or_create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription)

                if (task_names == '' or task_names == [] or len(task_names) == 0):
                    return HttpResponse('empty')
                
                else:
                    personal_task = Board.objects.get(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription)
           
                    
                    #task_name = task_names.split(',')
                    #print(task_name)
                    for eachtask in range(len(task_names)):
                        #return HttpResponse()
                        checktask_namemodel = SubTask.objects.filter(task_parent = personal_task, task_name = task_names[eachtask]).exists()
                        if checktask_namemodel:
                            return HttpResponse("Can't save, exist")
                        else:
                            for eachtask in range(len(task_names)):
                                task_name_model = SubTask.objects.create(task_parent = personal_task, task_name=task_names[eachtask], task_date=datetime.now())
                                task_name_model.save()
                            return HttpResponse('Exists, but saved task')
                        
                """else:
                    personal_task = Board.objects.get_or_create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription)

                    checktask_namemodel = SubTask.objects.filter(task_parent = personal_task, task_name = task_name[eachtask]).exists()
                    if checktask_namemodel:
                        return HttpResponse("Can't save, no")
                    else:
                        task_name_model = SubTask.objects.create(task_parent = personal_task, task_name=task_name[eachtask], task_date=datetime.now())
                        task_name_model.save()
                        return HttpResponse('Success')"""
                
                #else:
                #    return HttpResponse('Did not save.')
            
                
            else:
                personal_task = Board.objects.get(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription)
           
                if (task_names == '' or task_names == [] or len(task_names) == 0):
                    return HttpResponse('Empty task')
                else:
                    #task_name = task_names.split(',')
                    #print(task_name)
                    for eachtask in range(len(task_names)):
                        #return HttpResponse()
                        checktask_namemodel = SubTask.objects.filter(task_parent = personal_task, task_name = task_names[eachtask]).exists()
                        if checktask_namemodel:
                            return HttpResponse("Can't save, exist")
                        else:
                            for eachtask in range(len(task_names)):
                                task_name_model = SubTask.objects.create(task_parent = personal_task, task_name=task_names[eachtask], task_date=datetime.now())
                                task_name_model.save()
                            return HttpResponse('Exists, but saved task')
                    
            
        else:
            return HttpResponse("Not create board")
         
            
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


###### Createtask view  from the create board button in the html ######
class CreateBoard(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name: 'signup'
    
    def get(self, request):
        return render(request, 'createboard.html')
    
    def post(self, request):
        
        if request.method == 'POST':
            #return HttpResponse(list(request.POST.items()))#, '+', list(request.POST.items()))
            
            if 'boardinput' in request.POST and request.headers.get('x-requested-with') == 'XMLHttpRequest':
                
                boardName = request.POST['board_name']
                if (boardName != None):
                    user = request.user.username
                
                    boardOwner = request.user.username
                    boardDescription = request.POST['board_description']
                    task_name = request.POST["taskinput"]
                    
                    personal_model = User.objects.filter(username = user).first()
                    personal_profile = Profile.objects.get(personal_basicdetails = personal_model)
                    
                    checkpersonal_board = Board.objects.filter(personalBoardowner = personal_profile, board_name = boardName, board_description = boardDescription).exists()
                    if checkpersonal_board:
                        personal_board = Board.objects.get(personalBoardowner = personal_profile, board_name = boardName, board_description = boardDescription)
                        checkpersonal_task = Task.objects.filter(task_parent = personal_task, task_name = task_name).exists()
                        if checkpersonal_task:
                            #messages.info(request, "Sub board for this board already exist!")
                            return HttpResponse("Task won't create")
                        
                        else:
                            task_name_model = Task.objects.create(task_parent = personal_task, task_name=task_name, task_date=datetime.now())
                            task_name_model.save()
                            return HttpResponse('SUB Exists, but saved')
                    else:
                        board_model = Board.objects.create(personalBoardowner = personal_profile, board_owner = user, board_name = boardName, board_description = boardDescription, board_date = datetime.now())
                        board_model.save()
                    
                        #personal_task = Board.objects.filter(personalTaskowner = personal_profile, task_name = taskName, task_description = taskDescription).first()
                        personal_task = Board.objects.get(personalBoardowner = personal_profile, board_name = boardName, board_description = boardDescription)
                        task_name_model = Task.objects.create(task_parent = personal_task, task_name=task_name, task_date=datetime.now())
                        task_name_model.save()
                        return HttpResponse('Success')
                    
                    '''
                    personal_task = Board.objects.get(personalTaskowner = personal_profile, task_name = , task_description = )
                    task_name = request.POST["taskinput"]
                    
                    
                    task_name_model = SubTask.objects.create(task_parent = personal_task, task_name=task_name, task_date=datetime.now())
                    task_name_model.save()
                    '''
                    #return HttpResponse('Saved')
                    
                else:
                    pass
                    #messages.info(request, 'Please enter a board name')
                
                
            
            else:
                return HttpResponse('It is not there')
            
        
        '''
        #task_file
        #task_image
        #task_done
        #task
        
        
        
        task_model = Board.objects.create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription, task_date = datetime.now())
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
            #task
            task_model = Board.objects.create(personalTaskowner = personal_profile, task_owner = user, task_name = taskName, task_description = taskDescription, task_date = datetime.now())
            task_model.save()
            
            return HttpResponse('Success')
            '''
            
def calculator(request):
    return render(request, 'calculator.html')

def createtask(request):
    return render(request, 'createboard.html')


def error_404_view(request, exception):
    return render(request, '404.html')