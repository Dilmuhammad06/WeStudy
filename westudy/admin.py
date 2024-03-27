from django.contrib import admin
from .models import Course,Event,Feedback

admin.site.register([Course,Event,Feedback])
