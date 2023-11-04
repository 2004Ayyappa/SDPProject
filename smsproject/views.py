from django.http import HttpResponse
from django.shortcuts import render

def demofunction(request):
    return HttpResponse("<font color='red'>PFSD PROJECT</font>")

def homefunction(request):
    return render(request,'index.html')

def loginfunction(request):
    return render(request,'login.html')

def contactfunction(request):
    return render(request,'contact.html')

def aboutfunction(request):
    return render(request,'about.html')

def adminhome(request):
    return render(request,'adminhome.html')


def studentlogin(request):
    return render(request,'student_login.html')

def facultylogin(request):
    return render(request,'faculty_login.html')

