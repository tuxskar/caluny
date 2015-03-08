__author__ = 'tuxskar'
from caluny.models import Student, Teacher
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['last_login', 'date_joined']

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ['last_login', 'date_joined']