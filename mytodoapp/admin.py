from django.contrib import admin
from .models import Profile, BusinessProfile, Task

# Register your models here.
admin.site.register(Profile)
admin.site.register(BusinessProfile)
admin.site.register(Task)