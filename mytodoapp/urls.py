from django.urls import path
from . import views
from mytodoapp.views import Signup, Login

urlpatterns = [
    path('signup', Signup.as_view(), name = 'signup'),
    path('login', Login.as_view(), name = 'login'),
    path('', views.index, name="homepage"),
    path('calendar', views.calendar, name="calendar"),
    path('settings', views.settings, name="settings"),
    path('logout', views.logout, name="logout"),
]
