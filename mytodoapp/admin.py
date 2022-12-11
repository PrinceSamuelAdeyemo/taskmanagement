from django.contrib import admin
from .models import Profile, BusinessProfile, Project, Task, SubTask

# Register your models here.
admin.site.register(Profile)
admin.site.register(BusinessProfile)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Project)