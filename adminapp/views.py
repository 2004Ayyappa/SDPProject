from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Admin, Course, Faculty, Student
from .forms import AddFacultyForm, AddStudentForm
import pandas as pd
def adminhome(request):

    return render(request, "adminhome.html")

def logout(request):
    return render(request,'index.html')
def checkadminlogin(request):
    adminuname=request.POST['uname']
    adminpwd=request.POST['pwd']
    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)
    if flag:
        request.session['auname']=adminuname
        return render(request,'adminhome.html',{"adminuname":adminuname})
    else:
        return HttpResponse("Invalid Credentials")

def viewstudents(request):

    students = Student.objects.all()
    count=Student.objects.count()
    auname = request.session["auname"]
    return render(request,'viewstudents.html',{"studentdata":students,"count":count,"adminuname":auname})

def viewcourses(request):
    courses=Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,'viewcourses.html',{"coursesdata":courses, "count":count})

def viewfaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,'viewfaculty.html',{"facultydata":faculty, "count":count,"adminuname":auname})


def adminstudent(request):
    auname=request.session["auname"]

    return render(request,'adminstudent.html',{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,'adminfaculty.html',{"adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request,'admincourse.html',{"adminuname":auname})

def addcourse(request):
    auname = request.session["auname"]

    return render(request,'addcourse.html',{"adminuname":auname})

def insertcourse(request):
    auname = request.session["auname"]
    if request.method=="POST":
        dept = request.POST["dept"]
        program = request.POST["program"]
        ay = request.POST["ay"]
        sem = request.POST["sem"]
        year = request.POST["year"]
        ccode = request.POST["ccode"]
        ctitle = request.POST["ctitle"]
        course=Course(department=dept,program=program,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle)
        Course.save(course)
        message="Course Added successfully"
        return render(request,"addcourse.html",{"msg":message,"adminuname":auname})



def addfaculty(request):
    form=AddFacultyForm()
    auname = request.session["auname"]
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="Faculty Added Successfully"
            return render(request,"addfaculty.html",{"msg":message, "form":form,"adminuname":auname})
    return render(request,'addfaculty.html',{"form":form})

def deletecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,'deletecourse.html',{"coursesdata":courses, "count":count,"adminuname":auname})

def coursedeletion(request, cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")

def deletefaculty(request):
    auname = request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,'deletefaculty.html',{"facultydata":faculty, "count":count,"adminuname":auname})

def facultydeletion(request, fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")

def addstudent(request):
    auname = request.session["auname"]
    form=AddStudentForm()
    if request.method=="POST":
        form1=AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="Student Added Successfully"
            return render(request,"addstudent.html",{"msg":message, "form":form,"adminuname":auname})
    return render(request,'addstudent.html',{"form":form})

def studentdeletion(request, sid):
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")

def deletestudent(request):
    auname=request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request,'deletestudent.html',{"studentdata":student, "count":count,"adminuname":auname})

def facultycoursemapping(request):
    auname = request.session["auname"]
    return render(request,'facultycoursemapping.html',{"adminuname":auname})

def adminchangepwd(request):
    auname=request.session["auname"]
    return render(request,'adminchangepwd.html',{"adminuname":auname})







# def upload_marks(request):
#     if request.method == 'POST':
#         form = UploadMarksForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['excel_file']
#             if excel_file.name.endswith('.xls') or excel_file.name.endswith('.xlsx'):
#                 df = pd.read_excel(excel_file)
#                 for index, row in df.iterrows():
#                     student_name = row['student_name']
#                     subject = row['subject']
#                     marks = row['marks']
#                     StudentMarks.objects.create(
#                         student_name=student_name,
#                         subject=subject,
#                         marks=marks
#                     )
#                 return redirect('success_page')  # Replace with the URL to a success page
#             else:
#                 return render(request, 'upload_marks.html', {'form': form, 'error_message': 'Please upload a valid Excel file.'})
#     else:
#         form = UploadMarksForm()
#     return render(request, 'upload_marks.html', {'form': form})
#
