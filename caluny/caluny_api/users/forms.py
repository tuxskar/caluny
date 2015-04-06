__author__ = 'tuxskar'
from django.forms import ModelForm

from core.models import Student, Teacher


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['last_login', 'date_joined']


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ['last_login', 'date_joined']
