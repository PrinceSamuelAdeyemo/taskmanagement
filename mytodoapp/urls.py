from django.urls import path, re_path
from . import views
from mytodoapp.views import Signup, Login, Index, DashBoard, CreateBoard
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Signup, login and other links within the page.
    path('signup', Signup.as_view(), name = 'signup'),
    path('login', Login.as_view(), name = 'login'),
    #re_path(r'^login$', Login.as_view(), name = 'login'),
    path('dashboard', login_required(DashBoard.as_view()), name='dashboard'),
    path('createtask', views.createtask, name="createtask"),
    
    path('', Index.as_view(), name="homepage"),
    path('ab', Index.as_view(), name='ab'),
    path('getActivities', views.getActivities, name = 'bb'),
    path('calendar', views.calendar, name="calendar"),
    path('activities', views.activities, name="activities"),
    path('settings', views.settings, name="settings"),
    path('logout', views.logout, name="logout"),
    path('calculator', views.calculator, name="calculator"),
    
    path('add_record', views.add_record, name='add_record'),
    
    path('createboard', login_required(CreateBoard.as_view()), name = 'createboard')
    
    
    # path to links performing some activities but not opening and page.
    #Task Creation
    
]
