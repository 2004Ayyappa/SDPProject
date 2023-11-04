from django import forms


class ViewMarksForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=10)
    course_id = forms.CharField(label='Course ID', max_length=10)
