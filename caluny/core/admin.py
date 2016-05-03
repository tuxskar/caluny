"""Admin site registration models for Caluma"""
from django.contrib import admin

from .models import SemesterDate
from .models import Student, Course, Level, Exam, Timetable, CourseLabel, Degree
from .models import Subject, Teacher, TeachingSubject, School, University


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'degree', 'level', 'description')
    search_fields = ('code', 'title')
    list_filter = ('degree',)
    ordering = ('degree',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(TeachingSubject)
class TeachingSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'degree_info', 'course', 'start_date', 'end_date', 'address')
    search_fields = ('subject__title',)
    list_filter = ('course', 'subject__degree__title', 'address')
    ordering = ('course',)


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
    list_display = ('title', 'degree_info', 'address', 'date', 'start_time', 'end_time', 'course_info')
    search_fields = ('title',)
    list_filter = ('date', 'address', 't_subject__subject__degree__title')
    ordering = ('date',)


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('t_subject', 'degree_info', 'period', 'week_day', 'start_time', 'end_time')
    search_fields = ('t_subject__subject__title',)
    list_filter = ('week_day', 'period', 't_subject__subject__degree__title')
    ordering = ('t_subject',)


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
