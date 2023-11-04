
from django.urls import path
from .import views
urlpatterns = [
    path('adminhome/',views.adminhome,name="adminhome"),
    path('adminlogout/',views.logout,name="adminlogout"),
    path('admincourse/',views.admincourse,name="admincourse"),
    path('addcourse/',views.addcourse,name="addcourse"),
    path('deletecourse/',views.deletecourse,name="deletecourse"),
    path('deletefaculty/',views.deletefaculty,name="deletefaculty"),
    path('coursedeletion/<int:cid>',views.coursedeletion,name="coursedeletion"),
    path('facultydeletion/<int:fid>',views.facultydeletion,name="facultydeletion"),
    path('addfaculty/',views.addfaculty,name="addfaculty"),
    path('adminstudent/',views.adminstudent,name="adminstudent"),
    path('adminfaculty/',views.adminfaculty,name="adminfaculty"),
    path('insertcourse/', views.insertcourse,name="insertcourse"),
    path('viewfaculty/', views.viewfaculty,name="viewfaculty"),
    path('viewstudents/', views.viewstudents, name="viewstudents"),
    path('viewcourses/',views.viewcourses,name="viewcourses"),
    #path('upload_marks/', views.upload_marks, name='upload_marks'),
    path('checkadminlogin/', views.checkadminlogin, name="checkadminlogin"),
    path('addstudent/',views.addstudent,name="addstudent"),
    path('deletestudent/',views.deletestudent,name="deletestudent"),
    path('facultycoursemapping/', views.facultycoursemapping, name="facultycoursemapping"),
    path('studentdeletion/<int:sid>',views.studentdeletion,name="studentdeletion"),
    path('adminchangepwd/',views.adminchangepwd,name="adminchangepwd"),
    #path('upload/', views.upload_marks, name='upload_grades'),
]
