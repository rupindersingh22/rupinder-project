
from django.shortcuts import render
from myapp.form import EmpForm

def index(request):
    stu=EmpForm()
    return render(request,"index.html",{'form':stu})