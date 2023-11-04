from django.db import models

from adminapp.models import Student, Course


class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        db_table = "studentmarks_table"
    def __str__(self):
        return f"{self.student.fullname} {self.marks} {self.course}"





