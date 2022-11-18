from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('calendar', views.calendar, name="calendar")
]
