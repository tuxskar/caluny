#!/usr/bin/env python
# encoding: utf-8
import datetime
from data.school_degrees_data import schools_data
from core.models import School, Degree, Subject, University

SEMESTERS_DATES = [datetime.datetime.strptime(k, '%d-%m-%y') for k in \
                        ['29-09-14', '25-01-15', '17-02-15', '05-06-15']]
FIRST_LEVEL_SEMESTERS_DATES = [datetime.datetime.strptime(k, '%d-%m-%y') for k in \
                        ['14-09-14', '04-01-15', '17-02-15', '05-06-15']]
COURSES = {u'1º': ['A', 'B', 'C'],
           u'2º': [u'A (Español)', 'B (english)', 'C'],
           u'3º': ['A'],
           u'4º': ['A (MC)', 'A (MSI)', 'A (MTI)'],
          }


def insert_schools_data():
    university = University.objects.first()
    for school_name, degrees in schools_data.items():
        school = School(name=school_name) 
        school.university = university
        school.save()
        for degree_name, subjects in degrees.items():
            degree = Degree(title=degree_name)
            degree.school = school
            degree.save()
            for subject_code, subject_title in subjects.items():
                subject = Subject(code=subject_code, title=subject_title['title']) 
                subject.degree = degree
                subject.save()
