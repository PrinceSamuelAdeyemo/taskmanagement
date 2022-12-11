from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

# Create your models here.


# All Profiles
'''
class AllProfile(models.Model):
    account_name = models.CharField(max_length=200)
'''


# Model for a personal profile
class Profile(models.Model):
    personal_basicdetails = models.ForeignKey(User, on_delete = models.CASCADE)
    id_profile = models.IntegerField()
    #personalTask = models.ForeignKey(Task, on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return self.personal_basicdetails.username
    

# Model for a enterprise profile
class BusinessProfile(models.Model):
    business_basicdetails = models.ForeignKey(User, on_delete= models.CASCADE)
    businessprofile_id = models.IntegerField()
    #businessTask = models.ForeignKey(Task, on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return self.business_basicdetails.username
    

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    personalProjectowner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    businessProjectowner = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, null=True, blank=True)
    #main_taskowner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project_owner = models.CharField(max_length = 150)
    
    project_id = models.UUIDField(default = uuid.uuid4, primary_key=True)
    project_date = models.DateTimeField(auto_now_add=True)
    project_dateUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.project_name



# Task model
class Task(models.Model):
    personalTaskowner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    businessTaskowner = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, null=True, blank=True)
    task_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    
    task_owner = models.CharField(max_length = 150)
    task_name = models.CharField(max_length = 150)
    task_description = models.TextField(default=None, null=True, blank=True)
    task_file = models.FileField(default=None, upload_to='task_file_folder', null = True, blank = True)
    task_image = models.ImageField(default=None, upload_to='task_image_folder', null = True, blank = True)
    task_done = models.BooleanField(default=False, null = True, blank = True)
    in_progress = models.BooleanField(default=False, null = True, blank = True)
    #subtask = models.ForeignKey(SubTask, on_delete = models.CASCADE, null = True, blank = True)
    
    '''
    task_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    for_status = (
        ('done', 'DONE'),
        ('progress', 'IN PROGRESS'),
        ('not started', 'NOT STARTED')
    )
    task_status = models.CharField(max_length=10, choices=for_status)
    
    for_priority = (
        ('high', 'HIGH'),
        ('medium', 'MEDIUM'),
        ('low', 'LOW')
    )
    task_priority = models.CharField(max_length=10, choices=for_priority)
    '''
    '''
    for_assignee = (
        ('high', 'HIGH'),
        ('medium', 'MEDIUM'),
        ('low', 'LOW')
    )
    task_assignee = models.CharField(max_length=1, choices=for_assignee)
    '''
    
    task_id = models.UUIDField(default = uuid.uuid4, primary_key=True)
    
    task_date = models.DateTimeField(auto_now_add=True)
    task_dateUpdated = models.DateTimeField(auto_now=True)
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
    

    
class SubTask(models.Model):
    #subTask = models.CharField(max_length=200)
    #businessSubTask = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task_parent = models.ForeignKey(Task, on_delete = models.CASCADE, null=True, blank = True)
    subtask_name = models.CharField(max_length=200, null=True, blank=True)
    subtask_id = models.UUIDField(default = uuid.uuid4, primary_key=True)
    subtask_done = models.BooleanField(default=False)
    subtask_date = models.DateField()
    
    def __str__(self):
        return self.subtask_name
    

