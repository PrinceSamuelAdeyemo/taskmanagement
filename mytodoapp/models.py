from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Task(models.Model):
    task_name = models.CharField(max_length = 500)
    date_assigned = models.DateField()
    
    def __str__(self):
        return self.task_name
    
