from django import forms
from app1.models import Student, Department, Faculty


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'