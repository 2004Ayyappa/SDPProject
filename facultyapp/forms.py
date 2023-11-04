from django import forms
from .models import StudentMarks


class AddMarksForm(forms.ModelForm):
    class Meta:
        model=StudentMarks
        fields="__all__"
        label = {"student": "Select Student", "course": "Select Course ", "marks": "Enter Marks"}







