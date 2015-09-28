"""Admin site registration models for Caluma"""
from django.contrib import admin

from .models import Subject, Teacher, TeachingSubject, School, University
from .models import Student, Course, Level, Exam, Timetable, CourseLabel, Degree
from .models import SemesterDate


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'degree')
    search_fields = ('code', 'title')
    list_filter = ('degree', 'degree__school',)
    ordering = ('degree', 'code',)


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
    search_fields = ('language', 'level', 'label')
    list_filter = ('language', 'level')
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
    def get_queryset(self, request):
        qs = super(SchoolAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        # return qs.first()filter(owner=request.user)
        # return qs.first()
        return qs.filter(id=10)


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
