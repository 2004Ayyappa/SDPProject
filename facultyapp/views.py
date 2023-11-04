from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect


from adminapp.models import Faculty, FacultyCourseMapping

from .forms import AddMarksForm


# Create your views here.
def checkfacultylogin(request):

    context={'message': 'Invalid Credentials......'}
    facultyId=request.POST['fid']
    facultypwd=request.POST['pwd']
    flag=Faculty.objects.filter(Q(facultyId=facultyId)&Q(password=facultypwd))
    print(flag)
    if flag:
        request.session['funame']=facultyId
        return render(request,'facultyhome.html',{"facultyId":facultyId})
    else:
        return render(request,'facultylogin.html',context)


def facultyhome(request):

    return render(request, "facultyhome.html")

def logout(request):

    return render(request,'index.html')






def success_page(request):

    return render(request,"success_page.html",{"fid":fid})

def facultycourses(request):
    fid=Faculty.post('fid')
    mappingcourses=FacultyCourseMapping.Object.all()
    fmcourses=[]
    for course in mappingcourses:
        if (course.faculty.facultyId==int(fid)):
            fmcourses.append(course)

    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fcourses":fmcourses,"count":count})


def addstudentmarks(request):
    form=AddMarksForm()
    if request.method=="POST":
        form1=AddMarksForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="Marks Added Successfully"
            return render(request,"upload_grades.html",{"msg":message, "form":form})
    return render(request,'upload_grades.html',{"form":form})
