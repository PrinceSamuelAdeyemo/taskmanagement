from django.contrib import admin
from .models import Profile, BusinessProfile, Project, Board, Task

# Register your models here.
admin.site.register(Profile)
admin.site.register(BusinessProfile)
admin.site.register(Task)
admin.site.register(Board)
admin.site.register(Project)