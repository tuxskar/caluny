"""Admin site registration models for Caluma"""
from django.contrib import admin
from caluma.models import Subject, Teacher, TeachingSubject
from caluma.models import Student, Course, Level, Exam, Timetable

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
