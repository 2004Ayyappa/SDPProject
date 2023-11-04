from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username



class Course(models.Model):
    id=models.AutoField(primary_key=True)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    academicyear_choices = (("2023-24","2023-24"), ("2022-23", "2022-23"))
    academicyear = models.CharField(max_length=20, blank=False,choices=academicyear_choices)
    sem_choices = (("ODD","ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20,blank=False)
    coursetitle = models.CharField(max_length=20,blank=False)

    class Meta:
        db_table = "course_table"

    def __str__(self):
        return self.coursecode

class Student(models.Model):
    studentId = models.BigIntegerField(blank=False,unique=True)
    fullname = models.CharField(max_length=100,blank=False)
    gender_choices=(("MALE", "MALE"), ("FEMALE", "FEMALE"),("OTHERS","OTHERS"))
    gender = models.CharField(max_length=20, blank=False,choices=gender_choices)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)
    program_choices = (("B.TECH", "B.TECH"), ("M.TECH", "M.TECH"))
    program = models.CharField(max_length=50, blank=False,choices=program_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100,blank=False,default="klu123")
    email = models.CharField(max_length=100,blank=False,unique=True)
    contact = models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table = "student_table"

    def __str__(self):
        return str(self.studentId)

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyId = models.BigIntegerField(blank=False,unique=True)
    fullname = models.CharField(max_length=100,blank=False)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))
    gender = models.CharField(max_length=20, blank=False,choices=gender_choices)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)
    qualification_choices = (("M.Tech", "M.Tech"), ("Ph.D.", "Ph.D."))
    qualification = models.CharField(max_length=50, blank=False,choices=qualification_choices)
    designation_choices = (("Prof.", "Professor"), ("Ass. Prof.", "Associate Professor"), ("Asst. Prof.", "Assistant Professor"))
    designation = models.CharField(max_length=50, blank=False,choices=designation_choices)
    password = models.CharField(max_length=100,blank=False,default="klu123")
    email = models.CharField(max_length=100,blank=False,unique=True)
    contact = models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table = "faculty_table"

    def __str__(self):
        return self.fullname



class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}+{self.faculty.fullname}"





