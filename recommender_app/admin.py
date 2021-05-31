from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Student) 
admin.site.register(Course) 
admin.site.register(Chapter) 
admin.site.register(Rating) 