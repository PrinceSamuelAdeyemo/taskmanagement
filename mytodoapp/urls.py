from django.urls import path, re_path
from . import views
from mytodoapp.views import Signup, Login, Index, CreateTask, CreateSubTask
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Signup, login and other links within the page.
    path('signup', Signup.as_view(), name = 'signup'),
    path('login', Login.as_view(), name = 'login'),
    #re_path(r'^login$', Login.as_view(), name = 'login'),
    path('createtask', login_required(CreateTask.as_view()), name='createtask'),
    
    path('', login_required(Index.as_view()), name="homepage"),
    path('ab', Index.as_view(), name='ab'),
    path('getActivities', views.getActivities, name = 'bb'),
    path('calendar', views.calendar, name="calendar"),
    path('settings', views.settings, name="settings"),
    path('logout', views.logout, name="logout"),
    path('calculator', views.calculator, name="calculator"),
    
    path('add_record', views.add_record, name='add_record'),
    
    path('createsubtask', login_required(CreateSubTask.as_view()), name = 'createsubtask')
    
    
    # path to links performing some activities but not opening and page.
    #Task Creation
    
]
