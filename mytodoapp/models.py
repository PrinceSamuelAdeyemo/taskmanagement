from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model for a personal profile
class Profile(models.Model):
    personal_basicdetails = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.personal_basicdetails.username
    
    


# Model for a enterprise profile
class BusinessProfile(models.Model):
    business_basicdetails = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.business_basicdetails.username
    
    

class Task(models.Model):
    task_name = models.CharField(max_length = 500)
    date_assigned = models.DateField()
    '''
    User
    group_user
    
    schedule_task (week, day or month)
    recurring_task
    track_task
    reporting and visualization
    budget_task
    budget_task_expenses
    prioritize_task
    calendar
    track_task_time
    dependency, milestone and critical __path_
    integrate_other-thirdparty
    reak time data use
    '''
    
    def __str__(self):
        return self.task_name
    
