# coding=utf-8

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'caluny.settings.common'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import datetime
from os.path import join, dirname, abspath
import xlrd

from core.models import School, University, Subject, Exam, TeachingSubject, Degree

import locale

locale.setlocale(locale.LC_ALL, 'es_ES')
degree_names = [
    u'Grado en Ingeniería Informática',
    u'Grado en Ingeniería de Computadores',
    u'Grado en Ingeniería del Software',
    u'Grado en Ingeniería de la Salud'
]
university, _ = University.objects.get_or_create(name=u'Universidad de Málaga',
                                                 address=u'Avda. Cervantes, 2, 29071',
                                                 city=u'Málaga')
school, _ = School.objects.get_or_create(name=u"Escuela Técnica Superior de Ingeniería Informática",
                                         university=university)

for degree_name in degree_names:
    print "Analysing " + degree_name
    file_name = join(dirname(abspath(__file__)), u'Examenes ' + degree_name + u' 2015-2016.xlsx')
    # Open the workbook
    degree, _ = Degree.objects.get_or_create(title=degree_name, school=school)
    # Open the workbook
    xl_workbook = xlrd.open_workbook(file_name)
    # List sheet names, and pull a sheet by name
    dates_names = xl_workbook.sheet_names()
    for date_name in dates_names:
        xl_sheet = xl_workbook.sheet_by_name(date_name)
        base_date = datetime.datetime.strptime(date_name, '%B %Y')
        for row_idx in range(1, xl_sheet.nrows):
            subject_name, date, starting_hour, exam_address = xl_sheet.row(row_idx)
            try:
                subject = Subject.objects.get(title=subject_name.value, degree=degree)
            except Subject.DoesNotExist:
                continue
            days = int(date.value.split('-')[0])
            hours, minutes = map(int, starting_hour.value.split('.'))
            starting_date = base_date + datetime.timedelta(days=days - 1, hours=hours, minutes=minutes)
            end_date = starting_date + datetime.timedelta(hours=3)
            title = u'Examen de ' + subject.title
            description = title + u' en ' + unicode(exam_address.value)
            for t_subject in TeachingSubject.objects.filter(subject=subject):
                exam, _ = Exam.objects.get_or_create(title=title,
                                                     description=description,
                                                     address=exam_address.value,
                                                     date=starting_date.date(),
                                                     start_time=starting_date.time(),
                                                     end_time=end_date.time(),
                                                     t_subject=t_subject)
                print '    {exam}'.format(exam=exam)
