"Caluma database models"
#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
    ('de', _('German')),
    ('fr', _('French'))
    )

WEEK_DAYS = (
    ('1', _('Monday')),
    ('2', _('Tuesday')),
    ('3', _('Wednesday')),
    ('4', _('Thursday')),
    ('5', _('Friday')),
    ('6', _('Saturday')),
    ('7', _('Sunday')),
    )

PERIODS = (
    ('1', _('First semester')),
    ('2', _('Second semester')),
    ('3', _('Both semesters')),
    )

class Level(models.Model):
    """Subject level
    :year: Year of the subject teaching on the degree
    """
    year = models.CharField(max_length=20)

class Student(models.Model):
    """Student representation"""
    user = models.OneToOneField(User)

class Teacher(models.Model):
    """Teacher representation
    :user: Django teacher user
    :dept: teacher's departament
    :description: teacher's information like bio, studies or degrees
    """
    user = models.OneToOneField(User)
    dept = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #TODO: mentoring

class Course(models.Model):
    """
    Represents the group of a subject
    :label: group label like A, B, etc
    :language: course lessons language
    :level: level of this course like 1, 2, 3, etc
    """
    label = models.CharField(max_length=254, blank=True, null=True)
    language = models.CharField(max_length=5,
                                choices=LANGUAGES,
                                default='es',
                                blank=True, null=True)
    level = models.OneToOneField(Level)

class Degree(models.Model):
    """Degree representation
    :title: degree title
    :first_semester_start: first semester initial day
    :first_semester_end: first semester final day
    :second_semester_start: second semester initial day
    :second_semester_end: second semester final day
    """
    title = models.CharField(max_length=254)
    first_semester_start = models.DateField(blank=True, null=True)
    first_semester_end = models.DateField(blank=True, null=True)
    second_semester_start = models.DateField(blank=True, null=True)
    second_semester_end = models.DateField(blank=True, null=True)

class Subject(models.Model):
    """Subject/lesson of a degree
    :code: subject degree code
    :title: subject title
    :description: subject description
    :level: level where to take this subject
    :degree: degree where to study this subject
    """
    code = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    level = models.OneToOneField(Level, null=True, blank=True)
    degree = models.ForeignKey(Degree)

class TeachingSubject(models.Model):
    """Representation of a subject being teaching"""
    address = models.CharField(max_length=254, blank=True, null=True)
    student = models.ManyToManyField(Student, blank=True, null=True)
    teacher = models.ManyToManyField(Teacher, blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)
    subject = models.OneToOneField(Subject)

class Exam(models.Model):
    """Subject exam representation
    :address: site of the exam place
    :duration: exam duration in minutes
    :date: exam date"""
    title = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    duration = models.PositiveIntegerField(_("Minutes exam duration"),
                                           default=30, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    t_subject = models.ForeignKey(TeachingSubject)

class Timetable(models.Model):
    """Lesson/Subject timetable representation
    :start_at: lesson starting time
    :week_day: day of the lesson (see WEEK_DAYS)
    :description: period first, second or both semesters
    :duration: lesson duration in minutes
    :t_subject: asociated subject
    """
    start_at = models.TimeField()
    week_day = models.CharField(max_length=1,
                                choices=WEEK_DAYS,
                                default='1')
    description = models.CharField(max_length=254, blank=True, null=True)
    period = models.CharField(max_length=1,
                              choices=PERIODS,
                              default='1')
    duration = models.PositiveIntegerField(_("Minutes lesson duration"),
                                           default=30, blank=True, null=True)
    t_subject = models.ForeignKey(TeachingSubject)

