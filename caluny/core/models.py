"Caluma database models"
# !/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

LANGUAGES = (
    ('ES', _('Spanish')),
    ('EN', _('English')),
    ('DE', _('German')),
    ('FR', _('French'))
)

WEEK_DAYS = (
    ('1', _('Monday')),
    ('2', _('Tuesday')),
    ('3', _('Wednesday')),
    ('4', _('Thursday')),
    ('5', _('Friday')),
    ('6', _('Saturday')),
    ('0', _('Sunday')),
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
    year_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.year_name


class Student(User):
    """Student representation"""

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"

    def __unicode__(self):
        return "Student: {}".format(self.username)


class Teacher(User):
    """Teacher representation
    :dept: teacher's departament
    :description: teacher's information like bio, studies or degrees
    """
    dept = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = "teachers"

    def __unicode__(self):
        return "Teacher: {}".format(self.username)


class University(models.Model):
    """University representation
    :name: University name
    :address: University address
    :address: University address
    :city: University city
    """
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)

    def __unicode__(self):
        return _(u'{0} of {1}').format(self.name, self.city)


class School(models.Model):
    """School representation
    :name: School name
    :address: School address
    """
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, blank=True, null=True)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name


class Degree(models.Model):
    """Degree representation
    :title: degree title
    :first_semester_start: first semester initial day
    :first_semester_end: first semester final day
    :second_semester_start: second semester initial day
    :second_semester_end: second semester final day
    """
    title = models.CharField(max_length=254)
    school = models.ForeignKey(School, related_name='degrees')

    def __unicode__(self):
        return self.title


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
    level = models.ForeignKey(Level, null=True, blank=True)
    degree = models.ForeignKey(Degree, related_name='subjects')

    def __unicode__(self):
        return self.title


class ExtraTitle(models.Model):
    """Extra title for a subject usually in other language
    :title: title name
    :language: language of this title
    """
    title = models.CharField(max_length=254)
    language = models.CharField(max_length=5,
                                choices=LANGUAGES,
                                default='en')
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return _('{0} in {1}').format(self.title, self.language)


class CourseLabel(models.Model):
    """Course label name as A, B, Optionals"""
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class SemesterDate(models.Model):
    """Semester date to start or finish a semester"""
    date = models.DateField()

    def __unicode__(self):
        return self.date.strftime('%Y-%m-%d')


class Course(models.Model):
    """
    Represents the group of a subject
    :label: group label like A, B, etc
    :language: course lessons language
    :level: level of this course like 1, 2, 3, etc
    """
    label = models.ForeignKey(CourseLabel)
    language = models.CharField(max_length=2,
                                choices=LANGUAGES,
                                default='ES',
                                blank=True, null=True)
    first_semester_start = models.ForeignKey(SemesterDate, null=True, blank=True,
                                             related_name='first_start')
    first_semester_end = models.ForeignKey(SemesterDate, null=True, blank=True,
                                           related_name='first_end')
    second_semester_start = models.ForeignKey(SemesterDate, null=True,
                                              blank=True,
                                              related_name='second_start')
    second_semester_end = models.ForeignKey(SemesterDate, null=True, blank=True,
                                            related_name='second_end')
    level = models.ForeignKey(Level, null=True, blank=True)

    def __unicode__(self):
        return _(u'{0} {1}').format(self.level or "",
                                    self.label.name)


class TeachingSubject(models.Model):
    """Representation of a subject being teaching"""
    address = models.CharField(max_length=254, blank=True, null=True)
    students = models.ManyToManyField(Student, blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, blank=True, null=True, related_name='teachers')
    course = models.ForeignKey(Course, blank=True, null=True)
    subject = models.ForeignKey(Subject, related_name='t_subject')
    start_date = models.DateField(blank=False, null=False, default='2014-09-15')
    end_date = models.DateField(blank=False, null=False, default='2015-01-17')

    class Meta:
        unique_together = ("course", "subject")

    def title(self):
        return ' '.join([self.subject.title, unicode(self.course)])

    def __unicode__(self):
        return " ".join([unicode(self.subject), unicode(self.course)])


class Exam(models.Model):
    """Subject exam representation
    :address: site of the exam place
    :date: exam date"""
    title = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=254, blank=True, null=True)
    t_subject = models.ForeignKey(TeachingSubject, related_name='exams')

    def __unicode__(self):
        return " ".join([self.title, unicode(self.t_subject), str(self.date)])


class Timetable(models.Model):
    """Lesson/Subject timetable representation
    :start_at: lesson starting time
    :week_day: day of the lesson (see WEEK_DAYS)
    :description: period first, second or both semesters
    :t_subject: associated subject
    """
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_day = models.CharField(max_length=1,
                                choices=WEEK_DAYS,
                                default='1')
    description = models.CharField(max_length=254, blank=True, null=True)
    period = models.CharField(max_length=1,
                              choices=PERIODS,
                              default='1')
    t_subject = models.ForeignKey(TeachingSubject, related_name='timetables')

    def __unicode__(self):
        return " ".join([unicode(self.t_subject),
                         str(self.start_time),
                         WEEK_DAYS[int(self.week_day) - 1][1], ])
