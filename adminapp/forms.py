from django import forms
from .models import Faculty, Student

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"password"}
        label={"facultyid":"Enter Faculty ID","gender":"Select Gender","fullname":"Enter Full Name"}

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"



class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')

class UploadMarksForm(forms.Form):
    excel_file = forms.FileField()