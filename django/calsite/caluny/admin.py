"""Admin site registration models for Caluma"""
from django.contrib import admin
from caluny.models import Subject, Teacher, TeachingSubject, School, University
from caluny.models import Student, Course, Level, Exam, Timetable

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(TeachingSubject)
class TeachingSubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass
