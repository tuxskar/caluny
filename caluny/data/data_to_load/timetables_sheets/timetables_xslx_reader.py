# coding=utf-8
import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'caluny.settings.common'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from os.path import join, dirname, abspath
import xlrd

from core.models import SemesterDate, School, Degree, CourseLabel, Level, Subject, TeachingSubject, Course, Student, \
    Teacher, Timetable

degree_names = [
    u'Grado en Ingeniería Informática',
    u'Grado en Ingeniería del Software',
    u'Grado en Ingeniería de Computadores',
    u'Grado en Ingeniería de la Salud'
]

first_semester_start_dt = datetime.datetime.strptime('2015-09-29', '%Y-%m-%d').date()
first_semester_end_dt = datetime.datetime.strptime('2016-02-16', '%Y-%m-%d').date()
second_semester_start_dt = datetime.datetime.strptime('2016-02-22', '%Y-%m-%d').date()
second_semester_end_dt = datetime.datetime.strptime('2016-07-01', '%Y-%m-%d').date()
first_semester_start, _ = SemesterDate.objects.get_or_create(date=first_semester_start_dt)
first_semester_end, _ = SemesterDate.objects.get_or_create(date=first_semester_end_dt)
second_semester_start, _ = SemesterDate.objects.get_or_create(date=second_semester_start_dt)
second_semester_end, _ = SemesterDate.objects.get_or_create(date=second_semester_end_dt)
school, _ = School.objects.get_or_create(name=u"Escuela Técnica Superior de Ingeniería Informática")


def generate_user_model_list(Model, username_prefix, n_objects=25):
    student_list = []
    for x in range(n_objects):
        username = '{}{}'.format(username_prefix, x)
        st, created = Model.objects.get_or_create(username=username)
        if created:
            st.set_password(username)
            st.save()
        student_list.append(st)
    return student_list


students_list = generate_user_model_list(Student, 'new student', 25)
teachers_list = generate_user_model_list(Teacher, 'new teacher', 5)

for degree_name in degree_names:
    fname = join(dirname(abspath(__file__)), degree_name + '.xlsx')
    # Open the workbook
    degree, _ = Degree.objects.get_or_create(title=degree_name, school=school)

    xl_workbook = xlrd.open_workbook(fname)
    # List sheet names, and pull a sheet by name
    course_titles = xl_workbook.sheet_names()
    print('Courses for this Degree', course_titles)

    for course_title in course_titles:
        print u"Processing the course {}".format(course_title)
        xl_sheet = xl_workbook.sheet_by_name(course_title)

        # num_cols = xl_sheet.ncols  # Number of columns
        # for row_idx in range(0, xl_sheet.nrows):  # Iterate through rows
        #     print ('-' * 40)
        #     print ('Row: %s' % row_idx)  # Print row number
        #     for col_idx in range(0, num_cols):  # Iterate through columns
        #         cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
        #         print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

        level_name, course_name = course_title.split(' ')
        lvl, _ = Level.objects.get_or_create(year_name=level_name)
        course_label, _ = CourseLabel.objects.get_or_create(name=course_name)
        course, _ = Course.objects.get_or_create(label=course_label, first_semester_start=first_semester_start,
                                                 language='ES',
                                                 first_semester_end=first_semester_end,
                                                 second_semester_start=second_semester_start,
                                                 second_semester_end=second_semester_end, level=lvl)
        i = 0
        for semester_i in range(2):
            class_address = xl_sheet.cell(1 + i, 3).value  # getting the teaching class address
            for row_idx in range(2, 5):
                timetable = xl_sheet.cell(row_idx, 0).value
                separator = 'a' if timetable.count('a') > 0 else '-'
                start_time, end_time = map(lambda x: datetime.datetime.strptime(x.strip(), '%H:%M').time(),
                                           timetable.split(separator))
                for col_idx in range(1, 6):
                    # adding each subject and teaching subject for the first and second semester
                    subject_title = xl_sheet.cell(row_idx + i, col_idx).value
                    if not subject_title:
                        continue
                    subject, _ = Subject.objects.get_or_create(title=subject_title,
                                                               description=subject_title,
                                                               level=lvl, degree=degree)
                    start_date = first_semester_start_dt if i == 0 else second_semester_start_dt
                    end_date = first_semester_end_dt if i == 0 else second_semester_end_dt
                    teaching_subject, created = TeachingSubject.objects.get_or_create(address=class_address,
                                                                                      course=course,
                                                                                      subject=subject,
                                                                                      start_date=start_date,
                                                                                      end_date=end_date)
                    if created:
                        teaching_subject.students = students_list
                        teaching_subject.teachers = teachers_list
                        teaching_subject.save()
                    _, _ = Timetable.objects.get_or_create(start_time=start_time, end_time=end_time,
                                                           week_day=str(col_idx - 1),
                                                           description=' '.join([subject_title, class_address]),
                                                           period='1' if i == 0 else '2',
                                                           t_subject=teaching_subject)
                    #
