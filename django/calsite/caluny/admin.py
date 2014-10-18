"""Admin site registration models for Caluma"""
from django.contrib import admin
from caluny.models import Subject, Teacher, TeachingSubject, School, University
from caluny.models import Student, Course, Level, Exam, Timetable, CourseLabel, Degree
from caluny.models import SemesterDate

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'degree')
    search_fields = ('code', 'title')
    list_filter = ('degree', 'degree__school',)
    ordering = ('degree', 'code',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ('user',)
    #list_display = ('code', 'title', 'degree')
    #list_filter = ('teachingsubject_set',)
    #ordering = ('degree', 'code',)

@admin.register(TeachingSubject)
class TeachingSubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ('language', 'level', 'label')
    list_filter = ('language', 'level','degree')
    ordering = ('level', 'label',)

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

@admin.register(CourseLabel)
class CourseLabelAdmin(admin.ModelAdmin):
    pass

@admin.register(SemesterDate)
class SemesterDateAdmin(admin.ModelAdmin):
    pass

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass

