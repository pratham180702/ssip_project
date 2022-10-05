from django.contrib import admin
from .models import Category, Complaint,Feedback
# Register your models here.

admin.site.register(Complaint)
admin.site.register(Feedback)
admin.site.register(Category)