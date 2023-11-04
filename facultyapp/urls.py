from django.urls import path
from .import views
urlpatterns = [
    path('facultyhome/',views.facultyhome,name="facultyhome"),
    path('facultylogout/',views.logout,name="facultylogout"),
    path('checkfacultylogin/', views.checkfacultylogin, name="checkfacultylogin"),
    path('success_page/',views.success_page,name='success_page'),
    path('viewcourses/',views.facultycourses,name='facultycourses'),
    path('addstudentmarks/',views.addstudentmarks,name="addstudentmarks")

]
