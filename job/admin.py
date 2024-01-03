from django.contrib import admin

# Register your models here.
from .models import Job, Catogery

admin.site.register(Job)
admin.site.register(Catogery)