
from django.contrib import admin
from .models import Student

class studentdata(admin.ModelAdmin):
    list_display=["first_name","age","contact"]

admin.site.register(Student,studentdata)