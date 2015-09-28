# coding=utf-8
import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'caluny.settings.common'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from os.path import join, dirname, abspath
import xlrd

from core.models import SemesterDate

degree_names = [
    u'Grado en Ingeniería Informática',
    u'Grado en Ingeniería de Computadores',
    u'Grado en Ingeniería del Software',
    u'Grado en Ingeniería de la Salud'
]

first_semester_start_date = '2015-09-29'
first_semester_end_date = '2016-02-16'
second_semester_start_date = '2016-02-22'
second_semester_end_date = '2016-07-01'

first_semester_start = SemesterDate(date=datetime.datetime.strptime(first_semester_start_date, '%Y-%m-%d').date())
first_semester_end = SemesterDate(date=datetime.datetime.strptime(first_semester_end_date, '%Y-%m-%d').date())
second_semester_start = SemesterDate(date=datetime.datetime.strptime(second_semester_start_date, '%Y-%m-%d').date())
second_semester_end = SemesterDate(date=datetime.datetime.strptime(second_semester_end_date, '%Y-%m-%d').date())
print first_semester_start
print first_semester_end

for degree_name in degree_names:
    fname = join(dirname(abspath(__file__)), degree_name + '.xlsx')
    # Open the workbook
    xl_workbook = xlrd.open_workbook(fname)
    # List sheet names, and pull a sheet by name
    courses_names = xl_workbook.sheet_names()
    print('Courses for this Degree', courses_names)

    for course_name in courses_names:
        print u"Processing the course {}".format(course_name)
        xl_sheet = xl_workbook.sheet_by_name(course_name)
        from xlrd.sheet import ctype_text

        print('(Column #) type:value')
        row = xl_sheet.row(0)  # 1st row
        for idx, cell_obj in enumerate(row):
            cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
            print('(%s) %s %s' % (idx, cell_type_str, cell_obj.value))

        # Print all values, iterating through rows and columns
        #
        num_cols = xl_sheet.ncols  # Number of columns
        for row_idx in range(0, xl_sheet.nrows):  # Iterate through rows
            print ('-' * 40)
            print ('Row: %s' % row_idx)  # Print row number
            for col_idx in range(0, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
