
from __future__ import unicode_literals
from django.db import models
class Student(models.Model):
    first_name =models.CharField(max_length=20)
    last_name  =models.CharField(max_length=30)
    contact    =models.IntegerField()
    email      =models.EmailField(max_length=50)
    age        =models.IntegerField()
    news_image=models.FileField(upload_to="news/",max_length=500,null=True,default=None)

class Meta:
    db_table="student"