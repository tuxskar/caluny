# coding=utf-8
import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'caluny.settings.common'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from os.path import join, dirname, abspath
import xlrd

from core.models import SemesterDate, School, Degree, CourseLabel, Level, Subject, TeachingSubject, Course, Student
from core.models import Teacher, Timetable, University

GRADO_ING_INFO = u'Grado en Ingeniería Informática'
GRADO_ING_SOFT = u'Grado en Ingeniería del Software'
GRADO_ING_COMP = u'Grado en Ingeniería de Computadores'
GRADO_ING_SALU = u'Grado en Ingeniería de la Salud'

STUDENT_PER_CLASS = 5
TEACHERS_PER_CLASS = 3

FIRST_SEMESTER_START = '2015-09-29'
FIRST_SEMESTER_END = '2016-02-16'
SECOND_SEMESTER_START = '2016-02-22'
SECOND_SEMESTER_END = '2016-07-01'

DATE_FORMAT = '%Y-%m-%d'

STUDENT_USERNAME_PREFIX = 'student'
TEACHER_USERNAME_PREFIX = 'teacher'

degree_names = {
    GRADO_ING_INFO: 'ing_inf.xlsx',
    GRADO_ING_SOFT: 'ing_del_soft.xlsx',
    GRADO_ING_COMP: 'ing_de_comp.xlsx',
    GRADO_ING_SALU: 'ing_de_la_salud.xlsx'
}

# adding the data to the database
first_semester_start_dt = datetime.datetime.strptime(FIRST_SEMESTER_START, DATE_FORMAT).date()
first_semester_end_dt = datetime.datetime.strptime(FIRST_SEMESTER_END, DATE_FORMAT).date()
second_semester_start_dt = datetime.datetime.strptime(SECOND_SEMESTER_START, DATE_FORMAT).date()
second_semester_end_dt = datetime.datetime.strptime(SECOND_SEMESTER_END, DATE_FORMAT).date()
first_semester_start, _ = SemesterDate.objects.get_or_create(date=first_semester_start_dt)
first_semester_end, _ = SemesterDate.objects.get_or_create(date=first_semester_end_dt)
second_semester_start, _ = SemesterDate.objects.get_or_create(date=second_semester_start_dt)
second_semester_end, _ = SemesterDate.objects.get_or_create(date=second_semester_end_dt)
university, _ = University.objects.get_or_create(name=u'Universidad de Málaga',
                                                 address=u'Avda. Cervantes, 2, 29071',
                                                 city=u'Málaga')
school, _ = School.objects.get_or_create(name=u"Escuela Técnica Superior de Ingeniería Informática",
                                         university=university)


def generate_user_model_list(Model, username_prefix, n_objects=25):
    student_list = []
    for x in range(n_objects):
        username = '{}{}'.format(username_prefix, x + 1)
        st, m_created = Model.objects.get_or_create(username=username)
        if m_created:
            st.set_password(username)
            st.save()
        student_list.append(st)
    return student_list


NUM_DEGREES = len(degree_names)
NUM_STUDENTS = NUM_DEGREES * STUDENT_PER_CLASS
NUM_TEACHERS = NUM_DEGREES * TEACHERS_PER_CLASS

students_list = generate_user_model_list(Student, STUDENT_USERNAME_PREFIX, NUM_STUDENTS)
teachers_list = generate_user_model_list(Teacher, TEACHER_USERNAME_PREFIX, NUM_TEACHERS)

student_distribution = {
    GRADO_ING_INFO: students_list[:NUM_STUDENTS / NUM_DEGREES],
    GRADO_ING_SOFT: students_list[NUM_STUDENTS / NUM_DEGREES:NUM_STUDENTS / 2],
    GRADO_ING_COMP: students_list[NUM_STUDENTS / 2:3 * NUM_STUDENTS / NUM_DEGREES],
    GRADO_ING_SALU: students_list[3 * NUM_STUDENTS / NUM_DEGREES:],
}

teachers_distribution = {
    GRADO_ING_INFO: teachers_list[:NUM_TEACHERS / NUM_DEGREES],
    GRADO_ING_SOFT: teachers_list[NUM_TEACHERS / NUM_DEGREES:NUM_TEACHERS / 2],
    GRADO_ING_COMP: teachers_list[NUM_TEACHERS / 2:3 * NUM_TEACHERS / NUM_DEGREES],
    GRADO_ING_SALU: teachers_list[3 * NUM_TEACHERS / NUM_DEGREES:],
}

for degree_name, file_name in degree_names.iteritems():
    f_name = join(dirname(abspath(__file__)), file_name)
    # Open the workbook
    degree, _ = Degree.objects.get_or_create(title=degree_name, school=school)

    xl_workbook = xlrd.open_workbook(f_name)
    # List sheet names, and pull a sheet by name
    course_titles = xl_workbook.sheet_names()
    print('Courses for this Degree', course_titles)

    for course_title in course_titles:
        print u"Processing the course {}".format(course_title)
        xl_sheet = xl_workbook.sheet_by_name(course_title)

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
                        teaching_subject.students = student_distribution.get(degree_name)
                        teaching_subject.teachers = teachers_distribution.get(degree_name)
                        teaching_subject.save()
                    _, _ = Timetable.objects.get_or_create(start_time=start_time, end_time=end_time,
                                                           week_day=str(col_idx),
                                                           description=' '.join([subject_title, class_address]),
                                                           period='1' if i == 0 else '2',
                                                           t_subject=teaching_subject)
