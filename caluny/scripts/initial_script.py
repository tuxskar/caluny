#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript caluny
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    if str(e) == "No module named import_helper":
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from django.contrib.auth.models import User

    # Processing model: Level

    from core.models import Level

    caluny_level_1 = Level()
    caluny_level_1.year_name = u'1\xba'
    caluny_level_1 = importer.save_or_locate(caluny_level_1)

    caluny_level_2 = Level()
    caluny_level_2.year_name = u'2\xba'
    caluny_level_2 = importer.save_or_locate(caluny_level_2)

    caluny_level_3 = Level()
    caluny_level_3.year_name = u'3\xba'
    caluny_level_3 = importer.save_or_locate(caluny_level_3)

    caluny_level_4 = Level()
    caluny_level_4.year_name = u'4\xba'
    caluny_level_4 = importer.save_or_locate(caluny_level_4)

    # Processing model: Student

    from core.models import Student

    caluny_student_1 = Student()
    caluny_student_1.user =  importer.locate_object(User, "id", User, "id", 4, {'username': u'pedros', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 4, 'is_superuser': False, 'is_staff': False, 'last_login': datetime.datetime(2014, 9, 2, 21, 44, 56, 671344, tzinfo=<UTC>), '_student_cache': u'pedros', 'password': u'pbkdf2_sha256$12000$ACK5ebVC2qAc$q2MHCkh0wKFbIUHkfPsExzeKTIRdgtAwr2llZZQBaLc=', 'email': u'', 'date_joined': datetime.datetime(2014, 9, 2, 21, 44, 56, 671380, tzinfo=<UTC>)} ) 
    caluny_student_1 = importer.save_or_locate(caluny_student_1)

    caluny_student_2 = Student()
    caluny_student_2.user =  importer.locate_object(User, "id", User, "id", 1, {'username': u'tuxskar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 1, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2014, 12, 13, 17, 55, 56, 416477, tzinfo=<UTC>), '_student_cache': u'tuxskar', 'password': u'pbkdf2_sha256$12000$pE53yqs8Ryo6$b/GFYbX9G/WNcPpEc24DRqdxX/aYkDDD1zV6KcnDXoQ=', 'email': u'tux@tux.com', 'date_joined': datetime.datetime(2014, 8, 25, 18, 46, 33, 467922, tzinfo=<UTC>)} ) 
    caluny_student_2 = importer.save_or_locate(caluny_student_2)

    # Processing model: Teacher

    from core.models import Teacher

    caluny_teacher_1 = Teacher()
    caluny_teacher_1.user =  importer.locate_object(User, "id", User, "id", 2, {'username': u'pepec', 'first_name': u'', 'last_name': u'', 'is_active': True, '_teacher_cache': u'pepec', 'id': 2, 'is_superuser': False, 'is_staff': False, 'last_login': datetime.datetime(2014, 9, 2, 21, 42, 39, 646188, tzinfo=<UTC>), 'password': u'pbkdf2_sha256$12000$ucKGcZ3u93ws$1B9C/k2PwA3yzgfnOOZqs8wFgiIxtcpuf/w5txhPL8k=', 'email': u'', 'date_joined': datetime.datetime(2014, 9, 2, 21, 42, 39, 646221, tzinfo=<UTC>)} ) 
    caluny_teacher_1.dept = u'Matem\xe1tica aplicada a la computaci\xf3n'
    caluny_teacher_1.description = u'Doctor en matem\xe1tica'
    caluny_teacher_1 = importer.save_or_locate(caluny_teacher_1)

    caluny_teacher_2 = Teacher()
    caluny_teacher_2.user =  importer.locate_object(User, "id", User, "id", 3, {'username': u'juanc', 'first_name': u'', 'last_name': u'', 'is_active': True, '_teacher_cache': u'juanc', 'id': 3, 'is_superuser': False, 'is_staff': False, 'last_login': datetime.datetime(2014, 9, 2, 21, 43, 36, 195243, tzinfo=<UTC>), 'password': u'pbkdf2_sha256$12000$UCPH23gHBI2M$oJOc3q+NrUtHB3OCbx32VkvPaUpS1XuTUxA0TnDv124=', 'email': u'', 'date_joined': datetime.datetime(2014, 9, 2, 21, 43, 36, 195274, tzinfo=<UTC>)} ) 
    caluny_teacher_2.dept = u'Matem\xe1tica aplicada a la computaci\xf3n'
    caluny_teacher_2.description = u'Doctorando en Matem\xe1tica pero es un coco ya vereis'
    caluny_teacher_2 = importer.save_or_locate(caluny_teacher_2)

    # Processing model: University

    from core.models import University

    caluny_university_1 = University()
    caluny_university_1.name = u'Universidad de M\xe1laga'
    caluny_university_1.address = u'Avda. Cervantes, 2, 29071'
    caluny_university_1.city = u'M\xe1laga'
    caluny_university_1 = importer.save_or_locate(caluny_university_1)

    # Processing model: School

    from core.models import School

    caluny_school_1 = School()
    caluny_school_1.name = u'Facultad de Derecho'
    caluny_school_1.address = None
    caluny_school_1.university = caluny_university_1
    caluny_school_1 = importer.save_or_locate(caluny_school_1)

    caluny_school_2 = School()
    caluny_school_2.name = u'Escuela T\xe9cnica Superior de Ingenier\xeda Inform\xe1tica'
    caluny_school_2.address = None
    caluny_school_2.university = caluny_university_1
    caluny_school_2 = importer.save_or_locate(caluny_school_2)

    caluny_school_3 = School()
    caluny_school_3.name = u'Escuela Polit\xe9cnica Superior'
    caluny_school_3.address = None
    caluny_school_3.university = caluny_university_1
    caluny_school_3 = importer.save_or_locate(caluny_school_3)

    # Processing model: Degree

    from core.models import Degree

    caluny_degree_1 = Degree()
    caluny_degree_1.title = u'Graduado/a en Derecho'
    caluny_degree_1.school = caluny_school_1
    caluny_degree_1 = importer.save_or_locate(caluny_degree_1)

    caluny_degree_2 = Degree()
    caluny_degree_2.title = u'Graduado/a en Criminolog\xeda'
    caluny_degree_2.school = caluny_school_1
    caluny_degree_2 = importer.save_or_locate(caluny_degree_2)

    caluny_degree_3 = Degree()
    caluny_degree_3.title = u'Graduado/a en Ingenier\xeda del Software'
    caluny_degree_3.school = caluny_school_2
    caluny_degree_3 = importer.save_or_locate(caluny_degree_3)

    caluny_degree_4 = Degree()
    caluny_degree_4.title = u'Graduado/a en Ingenier\xeda Inform\xe1tica'
    caluny_degree_4.school = caluny_school_2
    caluny_degree_4 = importer.save_or_locate(caluny_degree_4)

    caluny_degree_5 = Degree()
    caluny_degree_5.title = u'Graduado/a en Ingenier\xeda de la Salud'
    caluny_degree_5.school = caluny_school_2
    caluny_degree_5 = importer.save_or_locate(caluny_degree_5)

    caluny_degree_6 = Degree()
    caluny_degree_6.title = u'Graduado/a en Ingenier\xeda de Computadores'
    caluny_degree_6.school = caluny_school_2
    caluny_degree_6 = importer.save_or_locate(caluny_degree_6)

    caluny_degree_7 = Degree()
    caluny_degree_7.title = u'Graduado/a en Ingenier\xeda Electr\xf3nica Industrial + Graduado/a en Ingenier\xeda El\xe9ctrica'
    caluny_degree_7.school = caluny_school_3
    caluny_degree_7 = importer.save_or_locate(caluny_degree_7)

    caluny_degree_8 = Degree()
    caluny_degree_8.title = u'Graduado/a en Ingenier\xeda El\xe9ctrica + Graduado/a en Ingenier\xeda Mec\xe1nica'
    caluny_degree_8.school = caluny_school_3
    caluny_degree_8 = importer.save_or_locate(caluny_degree_8)

    caluny_degree_9 = Degree()
    caluny_degree_9.title = u'Graduado/a en Ingenier\xeda en Dise\xf1o Industrial y Desarrollo del Producto'
    caluny_degree_9.school = caluny_school_3
    caluny_degree_9 = importer.save_or_locate(caluny_degree_9)

    caluny_degree_10 = Degree()
    caluny_degree_10.title = u'Graduado/a en Ingenier\xeda Electr\xf3nica Industrial'
    caluny_degree_10.school = caluny_school_3
    caluny_degree_10 = importer.save_or_locate(caluny_degree_10)

    caluny_degree_11 = Degree()
    caluny_degree_11.title = u'Graduado/a en Ingenier\xeda Mec\xe1nica + Graduado/a en Ingenier\xeda en Dise\xf1o Industrial y Desarrollo del Producto'
    caluny_degree_11.school = caluny_school_3
    caluny_degree_11 = importer.save_or_locate(caluny_degree_11)

    caluny_degree_12 = Degree()
    caluny_degree_12.title = u'Graduado/a en Ingenier\xeda Mec\xe1nica'
    caluny_degree_12.school = caluny_school_3
    caluny_degree_12 = importer.save_or_locate(caluny_degree_12)

    caluny_degree_13 = Degree()
    caluny_degree_13.title = u'Graduado/a en Ingenier\xeda El\xe9ctrica'
    caluny_degree_13.school = caluny_school_3
    caluny_degree_13 = importer.save_or_locate(caluny_degree_13)

    # Processing model: Subject

    from core.models import Subject

    caluny_subject_1 = Subject()
    caluny_subject_1.code = 212
    caluny_subject_1.title = u'Procedimientos Tributarios'
    caluny_subject_1.description = None
    caluny_subject_1.level = None
    caluny_subject_1.degree = caluny_degree_1
    caluny_subject_1 = importer.save_or_locate(caluny_subject_1)

    caluny_subject_2 = Subject()
    caluny_subject_2.code = 210
    caluny_subject_2.title = u'Derecho Pol\xedtico de las Comunidades Aut\xf3nomas'
    caluny_subject_2.description = None
    caluny_subject_2.level = None
    caluny_subject_2.degree = caluny_degree_1
    caluny_subject_2 = importer.save_or_locate(caluny_subject_2)

    caluny_subject_3 = Subject()
    caluny_subject_3.code = 211
    caluny_subject_3.title = u'Instituciones Jur\xeddicas Hist\xf3ricas'
    caluny_subject_3.description = None
    caluny_subject_3.level = None
    caluny_subject_3.degree = caluny_degree_1
    caluny_subject_3 = importer.save_or_locate(caluny_subject_3)

    caluny_subject_4 = Subject()
    caluny_subject_4.code = 407
    caluny_subject_4.title = u'Proceso Penal y Derechos Fundamentales'
    caluny_subject_4.description = None
    caluny_subject_4.level = None
    caluny_subject_4.degree = caluny_degree_1
    caluny_subject_4 = importer.save_or_locate(caluny_subject_4)

    caluny_subject_5 = Subject()
    caluny_subject_5.code = 406
    caluny_subject_5.title = u'Fiscalidad Internacional'
    caluny_subject_5.description = None
    caluny_subject_5.level = None
    caluny_subject_5.degree = caluny_degree_1
    caluny_subject_5 = importer.save_or_locate(caluny_subject_5)

    caluny_subject_6 = Subject()
    caluny_subject_6.code = 404
    caluny_subject_6.title = u'Derecho de Da\xf1os'
    caluny_subject_6.description = None
    caluny_subject_6.level = None
    caluny_subject_6.degree = caluny_degree_1
    caluny_subject_6 = importer.save_or_locate(caluny_subject_6)

    caluny_subject_7 = Subject()
    caluny_subject_7.code = 403
    caluny_subject_7.title = u'Trabajo Fin de Grado'
    caluny_subject_7.description = None
    caluny_subject_7.level = None
    caluny_subject_7.degree = caluny_degree_1
    caluny_subject_7 = importer.save_or_locate(caluny_subject_7)

    caluny_subject_8 = Subject()
    caluny_subject_8.code = 402
    caluny_subject_8.title = u'Pr\xe1cticas II'
    caluny_subject_8.description = None
    caluny_subject_8.level = None
    caluny_subject_8.degree = caluny_degree_1
    caluny_subject_8 = importer.save_or_locate(caluny_subject_8)

    caluny_subject_9 = Subject()
    caluny_subject_9.code = 401
    caluny_subject_9.title = u'Derecho Internacional Privado'
    caluny_subject_9.description = None
    caluny_subject_9.level = None
    caluny_subject_9.degree = caluny_degree_1
    caluny_subject_9 = importer.save_or_locate(caluny_subject_9)

    caluny_subject_10 = Subject()
    caluny_subject_10.code = 408
    caluny_subject_10.title = u'Relaciones Laborales en la Empresa'
    caluny_subject_10.description = None
    caluny_subject_10.level = None
    caluny_subject_10.degree = caluny_degree_1
    caluny_subject_10 = importer.save_or_locate(caluny_subject_10)

    caluny_subject_11 = Subject()
    caluny_subject_11.code = 414
    caluny_subject_11.title = u'Derecho Inmobiliario Registral'
    caluny_subject_11.description = None
    caluny_subject_11.level = None
    caluny_subject_11.degree = caluny_degree_1
    caluny_subject_11 = importer.save_or_locate(caluny_subject_11)

    caluny_subject_12 = Subject()
    caluny_subject_12.code = 415
    caluny_subject_12.title = u'Ordenaci\xf3n del Territorio, Urbanismo y Medio Ambiente'
    caluny_subject_12.description = None
    caluny_subject_12.level = None
    caluny_subject_12.degree = caluny_degree_1
    caluny_subject_12 = importer.save_or_locate(caluny_subject_12)

    caluny_subject_13 = Subject()
    caluny_subject_13.code = 416
    caluny_subject_13.title = u'Procesos Especiales y Especialidades de los Procesos Ordinarios Civiles y Penales'
    caluny_subject_13.description = None
    caluny_subject_13.level = None
    caluny_subject_13.degree = caluny_degree_1
    caluny_subject_13 = importer.save_or_locate(caluny_subject_13)

    caluny_subject_14 = Subject()
    caluny_subject_14.code = 410
    caluny_subject_14.title = u'Delitos Socioecon\xf3micos y Contra la Administraci\xf3n P\xfablica'
    caluny_subject_14.description = None
    caluny_subject_14.level = None
    caluny_subject_14.degree = caluny_degree_1
    caluny_subject_14 = importer.save_or_locate(caluny_subject_14)

    caluny_subject_15 = Subject()
    caluny_subject_15.code = 411
    caluny_subject_15.title = u'Derecho Constitucional Europeo y Comparado'
    caluny_subject_15.description = None
    caluny_subject_15.level = None
    caluny_subject_15.degree = caluny_degree_1
    caluny_subject_15 = importer.save_or_locate(caluny_subject_15)

    caluny_subject_16 = Subject()
    caluny_subject_16.code = 412
    caluny_subject_16.title = u'Derecho de los Mercados Financieros'
    caluny_subject_16.description = None
    caluny_subject_16.level = None
    caluny_subject_16.degree = caluny_degree_1
    caluny_subject_16 = importer.save_or_locate(caluny_subject_16)

    caluny_subject_17 = Subject()
    caluny_subject_17.code = 308
    caluny_subject_17.title = u'Pr\xe1cticas I'
    caluny_subject_17.description = None
    caluny_subject_17.level = None
    caluny_subject_17.degree = caluny_degree_1
    caluny_subject_17 = importer.save_or_locate(caluny_subject_17)

    caluny_subject_18 = Subject()
    caluny_subject_18.code = 310
    caluny_subject_18.title = u'Organizaciones Internacionales'
    caluny_subject_18.description = None
    caluny_subject_18.level = None
    caluny_subject_18.degree = caluny_degree_1
    caluny_subject_18 = importer.save_or_locate(caluny_subject_18)

    caluny_subject_19 = Subject()
    caluny_subject_19.code = 110
    caluny_subject_19.title = u'Filosof\xeda del Derecho'
    caluny_subject_19.description = None
    caluny_subject_19.level = None
    caluny_subject_19.degree = caluny_degree_1
    caluny_subject_19 = importer.save_or_locate(caluny_subject_19)

    caluny_subject_20 = Subject()
    caluny_subject_20.code = 301
    caluny_subject_20.title = u'Derecho Administrativo II'
    caluny_subject_20.description = None
    caluny_subject_20.level = None
    caluny_subject_20.degree = caluny_degree_1
    caluny_subject_20 = importer.save_or_locate(caluny_subject_20)

    caluny_subject_21 = Subject()
    caluny_subject_21.code = 201
    caluny_subject_21.title = u'Ciencia Pol\xedtica'
    caluny_subject_21.description = None
    caluny_subject_21.level = None
    caluny_subject_21.degree = caluny_degree_1
    caluny_subject_21 = importer.save_or_locate(caluny_subject_21)

    caluny_subject_22 = Subject()
    caluny_subject_22.code = 309
    caluny_subject_22.title = u'Derecho Administrativo Econ\xf3mico'
    caluny_subject_22.description = None
    caluny_subject_22.level = None
    caluny_subject_22.degree = caluny_degree_1
    caluny_subject_22 = importer.save_or_locate(caluny_subject_22)

    caluny_subject_23 = Subject()
    caluny_subject_23.code = 203
    caluny_subject_23.title = u'Derecho Comunitario'
    caluny_subject_23.description = None
    caluny_subject_23.level = None
    caluny_subject_23.degree = caluny_degree_1
    caluny_subject_23 = importer.save_or_locate(caluny_subject_23)

    caluny_subject_24 = Subject()
    caluny_subject_24.code = 202
    caluny_subject_24.title = u'Derecho Administrativo I'
    caluny_subject_24.description = None
    caluny_subject_24.level = None
    caluny_subject_24.degree = caluny_degree_1
    caluny_subject_24 = importer.save_or_locate(caluny_subject_24)

    caluny_subject_25 = Subject()
    caluny_subject_25.code = 205
    caluny_subject_25.title = u'Derecho Financiero I'
    caluny_subject_25.description = None
    caluny_subject_25.level = None
    caluny_subject_25.degree = caluny_degree_1
    caluny_subject_25 = importer.save_or_locate(caluny_subject_25)

    caluny_subject_26 = Subject()
    caluny_subject_26.code = 204
    caluny_subject_26.title = u'Derecho Constitucional II'
    caluny_subject_26.description = None
    caluny_subject_26.level = None
    caluny_subject_26.degree = caluny_degree_1
    caluny_subject_26 = importer.save_or_locate(caluny_subject_26)

    caluny_subject_27 = Subject()
    caluny_subject_27.code = 207
    caluny_subject_27.title = u'Derecho Mercantil I'
    caluny_subject_27.description = None
    caluny_subject_27.level = None
    caluny_subject_27.degree = caluny_degree_1
    caluny_subject_27 = importer.save_or_locate(caluny_subject_27)

    caluny_subject_28 = Subject()
    caluny_subject_28.code = 206
    caluny_subject_28.title = u'Derecho Civil II'
    caluny_subject_28.description = None
    caluny_subject_28.level = None
    caluny_subject_28.degree = caluny_degree_1
    caluny_subject_28 = importer.save_or_locate(caluny_subject_28)

    caluny_subject_29 = Subject()
    caluny_subject_29.code = 209
    caluny_subject_29.title = u'Derecho de los Consumidores y Condiciones Generales de la Contrataci\xf3n'
    caluny_subject_29.description = None
    caluny_subject_29.level = None
    caluny_subject_29.degree = caluny_degree_1
    caluny_subject_29 = importer.save_or_locate(caluny_subject_29)

    caluny_subject_30 = Subject()
    caluny_subject_30.code = 208
    caluny_subject_30.title = u'Derecho Penal I'
    caluny_subject_30.description = None
    caluny_subject_30.level = None
    caluny_subject_30.degree = caluny_degree_1
    caluny_subject_30 = importer.save_or_locate(caluny_subject_30)

    caluny_subject_31 = Subject()
    caluny_subject_31.code = 302
    caluny_subject_31.title = u'Derecho Financiero II'
    caluny_subject_31.description = None
    caluny_subject_31.level = None
    caluny_subject_31.degree = caluny_degree_1
    caluny_subject_31 = importer.save_or_locate(caluny_subject_31)

    caluny_subject_32 = Subject()
    caluny_subject_32.code = 303
    caluny_subject_32.title = u'Derecho Mercantil II'
    caluny_subject_32.description = None
    caluny_subject_32.level = None
    caluny_subject_32.degree = caluny_degree_1
    caluny_subject_32 = importer.save_or_locate(caluny_subject_32)

    caluny_subject_33 = Subject()
    caluny_subject_33.code = 304
    caluny_subject_33.title = u'Derecho Procesal Civil y Penal'
    caluny_subject_33.description = None
    caluny_subject_33.level = None
    caluny_subject_33.degree = caluny_degree_1
    caluny_subject_33 = importer.save_or_locate(caluny_subject_33)

    caluny_subject_34 = Subject()
    caluny_subject_34.code = 305
    caluny_subject_34.title = u'Derecho Civil III'
    caluny_subject_34.description = None
    caluny_subject_34.level = None
    caluny_subject_34.degree = caluny_degree_1
    caluny_subject_34 = importer.save_or_locate(caluny_subject_34)

    caluny_subject_35 = Subject()
    caluny_subject_35.code = 306
    caluny_subject_35.title = u'Derecho del Trabajo y de la Seguridad Social'
    caluny_subject_35.description = None
    caluny_subject_35.level = None
    caluny_subject_35.degree = caluny_degree_1
    caluny_subject_35 = importer.save_or_locate(caluny_subject_35)

    caluny_subject_36 = Subject()
    caluny_subject_36.code = 307
    caluny_subject_36.title = u'Derecho Penal II'
    caluny_subject_36.description = None
    caluny_subject_36.level = None
    caluny_subject_36.degree = caluny_degree_1
    caluny_subject_36 = importer.save_or_locate(caluny_subject_36)

    caluny_subject_37 = Subject()
    caluny_subject_37.code = 108
    caluny_subject_37.title = u'Derecho Procesal'
    caluny_subject_37.description = None
    caluny_subject_37.level = None
    caluny_subject_37.degree = caluny_degree_1
    caluny_subject_37 = importer.save_or_locate(caluny_subject_37)

    caluny_subject_38 = Subject()
    caluny_subject_38.code = 109
    caluny_subject_38.title = u'Econom\xeda'
    caluny_subject_38.description = None
    caluny_subject_38.level = None
    caluny_subject_38.degree = caluny_degree_1
    caluny_subject_38 = importer.save_or_locate(caluny_subject_38)

    caluny_subject_39 = Subject()
    caluny_subject_39.code = 102
    caluny_subject_39.title = u'Derecho Romano'
    caluny_subject_39.description = u''
    caluny_subject_39.level = caluny_level_1
    caluny_subject_39.degree = caluny_degree_1
    caluny_subject_39 = importer.save_or_locate(caluny_subject_39)

    caluny_subject_40 = Subject()
    caluny_subject_40.code = 103
    caluny_subject_40.title = u'Derecho y Factor Religioso'
    caluny_subject_40.description = None
    caluny_subject_40.level = None
    caluny_subject_40.degree = caluny_degree_1
    caluny_subject_40 = importer.save_or_locate(caluny_subject_40)

    caluny_subject_41 = Subject()
    caluny_subject_41.code = 101
    caluny_subject_41.title = u'Derecho Constitucional I'
    caluny_subject_41.description = None
    caluny_subject_41.level = None
    caluny_subject_41.degree = caluny_degree_1
    caluny_subject_41 = importer.save_or_locate(caluny_subject_41)

    caluny_subject_42 = Subject()
    caluny_subject_42.code = 106
    caluny_subject_42.title = u'Derecho Civil I'
    caluny_subject_42.description = None
    caluny_subject_42.level = None
    caluny_subject_42.degree = caluny_degree_1
    caluny_subject_42 = importer.save_or_locate(caluny_subject_42)

    caluny_subject_43 = Subject()
    caluny_subject_43.code = 107
    caluny_subject_43.title = u'Derecho Internacional P\xfablico'
    caluny_subject_43.description = None
    caluny_subject_43.level = None
    caluny_subject_43.degree = caluny_degree_1
    caluny_subject_43 = importer.save_or_locate(caluny_subject_43)

    caluny_subject_44 = Subject()
    caluny_subject_44.code = 104
    caluny_subject_44.title = u'Historia del Derecho'
    caluny_subject_44.description = None
    caluny_subject_44.level = None
    caluny_subject_44.degree = caluny_degree_1
    caluny_subject_44 = importer.save_or_locate(caluny_subject_44)

    caluny_subject_45 = Subject()
    caluny_subject_45.code = 105
    caluny_subject_45.title = u'Sociolog\xeda Jur\xeddica'
    caluny_subject_45.description = None
    caluny_subject_45.level = None
    caluny_subject_45.degree = caluny_degree_1
    caluny_subject_45 = importer.save_or_locate(caluny_subject_45)

    caluny_subject_46 = Subject()
    caluny_subject_46.code = 201
    caluny_subject_46.title = u'Derecho Penal. Parte General'
    caluny_subject_46.description = None
    caluny_subject_46.level = None
    caluny_subject_46.degree = caluny_degree_2
    caluny_subject_46 = importer.save_or_locate(caluny_subject_46)

    caluny_subject_47 = Subject()
    caluny_subject_47.code = 308
    caluny_subject_47.title = u'Justicia Reparadora y Mediaci\xf3n'
    caluny_subject_47.description = None
    caluny_subject_47.level = None
    caluny_subject_47.degree = caluny_degree_2
    caluny_subject_47 = importer.save_or_locate(caluny_subject_47)

    caluny_subject_48 = Subject()
    caluny_subject_48.code = 203
    caluny_subject_48.title = u'Penolog\xeda'
    caluny_subject_48.description = None
    caluny_subject_48.level = None
    caluny_subject_48.degree = caluny_degree_2
    caluny_subject_48 = importer.save_or_locate(caluny_subject_48)

    caluny_subject_49 = Subject()
    caluny_subject_49.code = 202
    caluny_subject_49.title = u'Fundamentos de Derecho P\xfablico'
    caluny_subject_49.description = None
    caluny_subject_49.level = None
    caluny_subject_49.degree = caluny_degree_2
    caluny_subject_49 = importer.save_or_locate(caluny_subject_49)

    caluny_subject_50 = Subject()
    caluny_subject_50.code = 205
    caluny_subject_50.title = u'Victimolog\xeda'
    caluny_subject_50.description = None
    caluny_subject_50.level = None
    caluny_subject_50.degree = caluny_degree_2
    caluny_subject_50 = importer.save_or_locate(caluny_subject_50)

    caluny_subject_51 = Subject()
    caluny_subject_51.code = 204
    caluny_subject_51.title = u'T\xe9cnicas de Investigaci\xf3n en Criminolog\xeda'
    caluny_subject_51.description = None
    caluny_subject_51.level = None
    caluny_subject_51.degree = caluny_degree_2
    caluny_subject_51 = importer.save_or_locate(caluny_subject_51)

    caluny_subject_52 = Subject()
    caluny_subject_52.code = 207
    caluny_subject_52.title = u'Ejecuci\xf3n de Penas y Medidas de Seguridad'
    caluny_subject_52.description = None
    caluny_subject_52.level = None
    caluny_subject_52.degree = caluny_degree_2
    caluny_subject_52 = importer.save_or_locate(caluny_subject_52)

    caluny_subject_53 = Subject()
    caluny_subject_53.code = 206
    caluny_subject_53.title = u'Derecho Penal. Parte Especial'
    caluny_subject_53.description = None
    caluny_subject_53.level = None
    caluny_subject_53.degree = caluny_degree_2
    caluny_subject_53 = importer.save_or_locate(caluny_subject_53)

    caluny_subject_54 = Subject()
    caluny_subject_54.code = 209
    caluny_subject_54.title = u'Socio-Legal English'
    caluny_subject_54.description = None
    caluny_subject_54.level = None
    caluny_subject_54.degree = caluny_degree_2
    caluny_subject_54 = importer.save_or_locate(caluny_subject_54)

    caluny_subject_55 = Subject()
    caluny_subject_55.code = 208
    caluny_subject_55.title = u'Psicopatolog\xeda del Comportamiento Delictivo'
    caluny_subject_55.description = None
    caluny_subject_55.level = None
    caluny_subject_55.degree = caluny_degree_2
    caluny_subject_55 = importer.save_or_locate(caluny_subject_55)

    caluny_subject_56 = Subject()
    caluny_subject_56.code = 302
    caluny_subject_56.title = u'Formas Espec\xedficas de la Criminalidad'
    caluny_subject_56.description = None
    caluny_subject_56.level = None
    caluny_subject_56.degree = caluny_degree_2
    caluny_subject_56 = importer.save_or_locate(caluny_subject_56)

    caluny_subject_57 = Subject()
    caluny_subject_57.code = 303
    caluny_subject_57.title = u'M\xe9todos Estad\xedsticos Avanzados en Criminolog\xeda'
    caluny_subject_57.description = None
    caluny_subject_57.level = None
    caluny_subject_57.degree = caluny_degree_2
    caluny_subject_57 = importer.save_or_locate(caluny_subject_57)

    caluny_subject_58 = Subject()
    caluny_subject_58.code = 304
    caluny_subject_58.title = u'Polic\xeda Cient\xedfica'
    caluny_subject_58.description = None
    caluny_subject_58.level = None
    caluny_subject_58.degree = caluny_degree_2
    caluny_subject_58 = importer.save_or_locate(caluny_subject_58)

    caluny_subject_59 = Subject()
    caluny_subject_59.code = 305
    caluny_subject_59.title = u'Predicci\xf3n y Prevenci\xf3n de la Delincuencia'
    caluny_subject_59.description = None
    caluny_subject_59.level = None
    caluny_subject_59.degree = caluny_degree_2
    caluny_subject_59 = importer.save_or_locate(caluny_subject_59)

    caluny_subject_60 = Subject()
    caluny_subject_60.code = 306
    caluny_subject_60.title = u'Delincuencia y Responsabilidad Penal de Menores'
    caluny_subject_60.description = None
    caluny_subject_60.level = None
    caluny_subject_60.degree = caluny_degree_2
    caluny_subject_60 = importer.save_or_locate(caluny_subject_60)

    caluny_subject_61 = Subject()
    caluny_subject_61.code = 307
    caluny_subject_61.title = u'Intervenci\xf3n Social y Educativa con Delincuentes'
    caluny_subject_61.description = None
    caluny_subject_61.level = None
    caluny_subject_61.degree = caluny_degree_2
    caluny_subject_61 = importer.save_or_locate(caluny_subject_61)

    caluny_subject_62 = Subject()
    caluny_subject_62.code = 108
    caluny_subject_62.title = u'Instituciones de Control Social y Penal'
    caluny_subject_62.description = None
    caluny_subject_62.level = None
    caluny_subject_62.degree = caluny_degree_2
    caluny_subject_62 = importer.save_or_locate(caluny_subject_62)

    caluny_subject_63 = Subject()
    caluny_subject_63.code = 109
    caluny_subject_63.title = u'Medicina Legal'
    caluny_subject_63.description = None
    caluny_subject_63.level = None
    caluny_subject_63.degree = caluny_degree_2
    caluny_subject_63 = importer.save_or_locate(caluny_subject_63)

    caluny_subject_64 = Subject()
    caluny_subject_64.code = 110
    caluny_subject_64.title = u'Teor\xedas de la Criminalidad'
    caluny_subject_64.description = None
    caluny_subject_64.level = None
    caluny_subject_64.degree = caluny_degree_2
    caluny_subject_64 = importer.save_or_locate(caluny_subject_64)

    caluny_subject_65 = Subject()
    caluny_subject_65.code = 102
    caluny_subject_65.title = u'Introducci\xf3n a la Criminolog\xeda'
    caluny_subject_65.description = None
    caluny_subject_65.level = None
    caluny_subject_65.degree = caluny_degree_2
    caluny_subject_65 = importer.save_or_locate(caluny_subject_65)

    caluny_subject_66 = Subject()
    caluny_subject_66.code = 103
    caluny_subject_66.title = u'Metodolog\xeda e Investigaci\xf3n en Ciencias Sociales'
    caluny_subject_66.description = None
    caluny_subject_66.level = None
    caluny_subject_66.degree = caluny_degree_2
    caluny_subject_66 = importer.save_or_locate(caluny_subject_66)

    caluny_subject_67 = Subject()
    caluny_subject_67.code = 309
    caluny_subject_67.title = u'Programas de Tratamiento con Delincuentes'
    caluny_subject_67.description = None
    caluny_subject_67.level = None
    caluny_subject_67.degree = caluny_degree_2
    caluny_subject_67 = importer.save_or_locate(caluny_subject_67)

    caluny_subject_68 = Subject()
    caluny_subject_68.code = 101
    caluny_subject_68.title = u'Antropolog\xeda Social'
    caluny_subject_68.description = None
    caluny_subject_68.level = None
    caluny_subject_68.degree = caluny_degree_2
    caluny_subject_68 = importer.save_or_locate(caluny_subject_68)

    caluny_subject_69 = Subject()
    caluny_subject_69.code = 106
    caluny_subject_69.title = u'Derecho Constitucional'
    caluny_subject_69.description = None
    caluny_subject_69.level = None
    caluny_subject_69.degree = caluny_degree_2
    caluny_subject_69 = importer.save_or_locate(caluny_subject_69)

    caluny_subject_70 = Subject()
    caluny_subject_70.code = 107
    caluny_subject_70.title = u'Estad\xedstica'
    caluny_subject_70.description = None
    caluny_subject_70.level = None
    caluny_subject_70.degree = caluny_degree_2
    caluny_subject_70 = importer.save_or_locate(caluny_subject_70)

    caluny_subject_71 = Subject()
    caluny_subject_71.code = 104
    caluny_subject_71.title = u'Psicolog\xeda Criminal'
    caluny_subject_71.description = None
    caluny_subject_71.level = None
    caluny_subject_71.degree = caluny_degree_2
    caluny_subject_71 = importer.save_or_locate(caluny_subject_71)

    caluny_subject_72 = Subject()
    caluny_subject_72.code = 105
    caluny_subject_72.title = u'Sociolog\xeda Criminal'
    caluny_subject_72.description = None
    caluny_subject_72.level = None
    caluny_subject_72.degree = caluny_degree_2
    caluny_subject_72 = importer.save_or_locate(caluny_subject_72)

    caluny_subject_73 = Subject()
    caluny_subject_73.code = 414
    caluny_subject_73.title = u'Trabajo Fin de Grado'
    caluny_subject_73.description = None
    caluny_subject_73.level = None
    caluny_subject_73.degree = caluny_degree_2
    caluny_subject_73 = importer.save_or_locate(caluny_subject_73)

    caluny_subject_74 = Subject()
    caluny_subject_74.code = 210
    caluny_subject_74.title = u'Tanatolog\xeda y Toxicolog\xeda Forense'
    caluny_subject_74.description = None
    caluny_subject_74.level = None
    caluny_subject_74.degree = caluny_degree_2
    caluny_subject_74 = importer.save_or_locate(caluny_subject_74)

    caluny_subject_75 = Subject()
    caluny_subject_75.code = 415
    caluny_subject_75.title = u'Practicas Externas II'
    caluny_subject_75.description = None
    caluny_subject_75.level = None
    caluny_subject_75.degree = caluny_degree_2
    caluny_subject_75 = importer.save_or_locate(caluny_subject_75)

    caluny_subject_76 = Subject()
    caluny_subject_76.code = 407
    caluny_subject_76.title = u'Psicolog\xeda de las Organizaciones Policial, Judicial y Penitenciaria'
    caluny_subject_76.description = None
    caluny_subject_76.level = None
    caluny_subject_76.degree = caluny_degree_2
    caluny_subject_76 = importer.save_or_locate(caluny_subject_76)

    caluny_subject_77 = Subject()
    caluny_subject_77.code = 406
    caluny_subject_77.title = u'Pol\xedticas de Seguridad P\xfablica y Privada'
    caluny_subject_77.description = None
    caluny_subject_77.level = None
    caluny_subject_77.degree = caluny_degree_2
    caluny_subject_77 = importer.save_or_locate(caluny_subject_77)

    caluny_subject_78 = Subject()
    caluny_subject_78.code = 405
    caluny_subject_78.title = u'Pol\xedtica Criminal'
    caluny_subject_78.description = None
    caluny_subject_78.level = None
    caluny_subject_78.degree = caluny_degree_2
    caluny_subject_78 = importer.save_or_locate(caluny_subject_78)

    caluny_subject_79 = Subject()
    caluny_subject_79.code = 404
    caluny_subject_79.title = u'G\xe9nero y Violencia'
    caluny_subject_79.description = None
    caluny_subject_79.level = None
    caluny_subject_79.degree = caluny_degree_2
    caluny_subject_79 = importer.save_or_locate(caluny_subject_79)

    caluny_subject_80 = Subject()
    caluny_subject_80.code = 310
    caluny_subject_80.title = u'Psicolog\xeda Jur\xeddica'
    caluny_subject_80.description = None
    caluny_subject_80.level = None
    caluny_subject_80.degree = caluny_degree_2
    caluny_subject_80 = importer.save_or_locate(caluny_subject_80)

    caluny_subject_81 = Subject()
    caluny_subject_81.code = 402
    caluny_subject_81.title = u'Econom\xeda del Delito y Comportamiento Criminal'
    caluny_subject_81.description = None
    caluny_subject_81.level = None
    caluny_subject_81.degree = caluny_degree_2
    caluny_subject_81 = importer.save_or_locate(caluny_subject_81)

    caluny_subject_82 = Subject()
    caluny_subject_82.code = 401
    caluny_subject_82.title = u'Drogodependencias'
    caluny_subject_82.description = None
    caluny_subject_82.level = None
    caluny_subject_82.degree = caluny_degree_2
    caluny_subject_82 = importer.save_or_locate(caluny_subject_82)

    caluny_subject_83 = Subject()
    caluny_subject_83.code = 301
    caluny_subject_83.title = u'Derecho Procesal Penal'
    caluny_subject_83.description = None
    caluny_subject_83.level = None
    caluny_subject_83.degree = caluny_degree_2
    caluny_subject_83 = importer.save_or_locate(caluny_subject_83)

    caluny_subject_84 = Subject()
    caluny_subject_84.code = 410
    caluny_subject_84.title = u'Cooperaci\xf3n Internacional contra la Delincuencia Transnacional'
    caluny_subject_84.description = None
    caluny_subject_84.level = None
    caluny_subject_84.degree = caluny_degree_2
    caluny_subject_84 = importer.save_or_locate(caluny_subject_84)

    caluny_subject_85 = Subject()
    caluny_subject_85.code = 412
    caluny_subject_85.title = u'Medios de Comunicaci\xf3n, Opini\xf3n P\xfablica y Violencia'
    caluny_subject_85.description = None
    caluny_subject_85.level = None
    caluny_subject_85.degree = caluny_degree_2
    caluny_subject_85 = importer.save_or_locate(caluny_subject_85)

    caluny_subject_86 = Subject()
    caluny_subject_86.code = 409
    caluny_subject_86.title = u'Practicas Externas I'
    caluny_subject_86.description = None
    caluny_subject_86.level = None
    caluny_subject_86.degree = caluny_degree_2
    caluny_subject_86 = importer.save_or_locate(caluny_subject_86)

    caluny_subject_87 = Subject()
    caluny_subject_87.code = 411
    caluny_subject_87.title = u'Evaluaci\xf3n de Programas y Pol\xedticas P\xfablicas'
    caluny_subject_87.description = None
    caluny_subject_87.level = None
    caluny_subject_87.degree = caluny_degree_2
    caluny_subject_87 = importer.save_or_locate(caluny_subject_87)

    caluny_subject_88 = Subject()
    caluny_subject_88.code = 210
    caluny_subject_88.title = u'Sistemas Operativos'
    caluny_subject_88.description = None
    caluny_subject_88.level = None
    caluny_subject_88.degree = caluny_degree_3
    caluny_subject_88 = importer.save_or_locate(caluny_subject_88)

    caluny_subject_89 = Subject()
    caluny_subject_89.code = 407
    caluny_subject_89.title = u'Procesamiento de Im\xe1genes y Video'
    caluny_subject_89.description = None
    caluny_subject_89.level = None
    caluny_subject_89.degree = caluny_degree_3
    caluny_subject_89 = importer.save_or_locate(caluny_subject_89)

    caluny_subject_90 = Subject()
    caluny_subject_90.code = 406
    caluny_subject_90.title = u'M\xe9todos formales para la Ingenier\xeda del Software'
    caluny_subject_90.description = None
    caluny_subject_90.level = None
    caluny_subject_90.degree = caluny_degree_3
    caluny_subject_90 = importer.save_or_locate(caluny_subject_90)

    caluny_subject_91 = Subject()
    caluny_subject_91.code = 405
    caluny_subject_91.title = u'Ingenier\xeda Web'
    caluny_subject_91.description = None
    caluny_subject_91.level = None
    caluny_subject_91.degree = caluny_degree_3
    caluny_subject_91 = importer.save_or_locate(caluny_subject_91)

    caluny_subject_92 = Subject()
    caluny_subject_92.code = 404
    caluny_subject_92.title = u'Gesti\xf3n de Proyectos Software'
    caluny_subject_92.description = None
    caluny_subject_92.level = None
    caluny_subject_92.degree = caluny_degree_3
    caluny_subject_92 = importer.save_or_locate(caluny_subject_92)

    caluny_subject_93 = Subject()
    caluny_subject_93.code = 401
    caluny_subject_93.title = u'Arquitectura Cluster'
    caluny_subject_93.description = None
    caluny_subject_93.level = None
    caluny_subject_93.degree = caluny_degree_3
    caluny_subject_93 = importer.save_or_locate(caluny_subject_93)

    caluny_subject_94 = Subject()
    caluny_subject_94.code = 408
    caluny_subject_94.title = u'Programaci\xf3n de Robots'
    caluny_subject_94.description = None
    caluny_subject_94.level = None
    caluny_subject_94.degree = caluny_degree_3
    caluny_subject_94 = importer.save_or_locate(caluny_subject_94)

    caluny_subject_95 = Subject()
    caluny_subject_95.code = 414
    caluny_subject_95.title = u'Calidad de Software'
    caluny_subject_95.description = None
    caluny_subject_95.level = None
    caluny_subject_95.degree = caluny_degree_3
    caluny_subject_95 = importer.save_or_locate(caluny_subject_95)

    caluny_subject_96 = Subject()
    caluny_subject_96.code = 415
    caluny_subject_96.title = u'Cognici\xf3n y Comunicaci\xf3n en Ingenier\xeda del Software'
    caluny_subject_96.description = None
    caluny_subject_96.level = None
    caluny_subject_96.degree = caluny_degree_3
    caluny_subject_96 = importer.save_or_locate(caluny_subject_96)

    caluny_subject_97 = Subject()
    caluny_subject_97.code = 417
    caluny_subject_97.title = u'Electr\xf3nica para Dom\xf3tica'
    caluny_subject_97.description = None
    caluny_subject_97.level = None
    caluny_subject_97.degree = caluny_degree_3
    caluny_subject_97 = importer.save_or_locate(caluny_subject_97)

    caluny_subject_98 = Subject()
    caluny_subject_98.code = 410
    caluny_subject_98.title = u'Software para sistemas empotrados y dispositivos m\xf3viles'
    caluny_subject_98.description = None
    caluny_subject_98.level = None
    caluny_subject_98.degree = caluny_degree_3
    caluny_subject_98 = importer.save_or_locate(caluny_subject_98)

    caluny_subject_99 = Subject()
    caluny_subject_99.code = 411
    caluny_subject_99.title = u'Teor\xeda de la Informaci\xf3n y la Codificaci\xf3n'
    caluny_subject_99.description = None
    caluny_subject_99.level = None
    caluny_subject_99.degree = caluny_degree_3
    caluny_subject_99 = importer.save_or_locate(caluny_subject_99)

    caluny_subject_100 = Subject()
    caluny_subject_100.code = 413
    caluny_subject_100.title = u'Arquitecturas Virtuales'
    caluny_subject_100.description = None
    caluny_subject_100.level = None
    caluny_subject_100.degree = caluny_degree_3
    caluny_subject_100 = importer.save_or_locate(caluny_subject_100)

    caluny_subject_101 = Subject()
    caluny_subject_101.code = 418
    caluny_subject_101.title = u'Herramientas de Dise\xf1o Electr\xf3nico'
    caluny_subject_101.description = None
    caluny_subject_101.level = None
    caluny_subject_101.degree = caluny_degree_3
    caluny_subject_101 = importer.save_or_locate(caluny_subject_101)

    caluny_subject_102 = Subject()
    caluny_subject_102.code = 419
    caluny_subject_102.title = u'Proyectos y Legislaci\xf3n'
    caluny_subject_102.description = None
    caluny_subject_102.level = None
    caluny_subject_102.degree = caluny_degree_3
    caluny_subject_102 = importer.save_or_locate(caluny_subject_102)

    caluny_subject_103 = Subject()
    caluny_subject_103.code = 319
    caluny_subject_103.title = u'Visi\xf3n por Computador'
    caluny_subject_103.description = None
    caluny_subject_103.level = None
    caluny_subject_103.degree = caluny_degree_3
    caluny_subject_103 = importer.save_or_locate(caluny_subject_103)

    caluny_subject_104 = Subject()
    caluny_subject_104.code = 318
    caluny_subject_104.title = u'Tecnolog\xedas de Aplicaciones Web'
    caluny_subject_104.description = None
    caluny_subject_104.level = None
    caluny_subject_104.degree = caluny_degree_3
    caluny_subject_104 = importer.save_or_locate(caluny_subject_104)

    caluny_subject_105 = Subject()
    caluny_subject_105.code = 312
    caluny_subject_105.title = u'Interfaces de Usuario'
    caluny_subject_105.description = None
    caluny_subject_105.level = None
    caluny_subject_105.degree = caluny_degree_3
    caluny_subject_105 = importer.save_or_locate(caluny_subject_105)

    caluny_subject_106 = Subject()
    caluny_subject_106.code = 311
    caluny_subject_106.title = u'Inteligencia Artificial para Juegos'
    caluny_subject_106.description = None
    caluny_subject_106.level = None
    caluny_subject_106.degree = caluny_degree_3
    caluny_subject_106 = importer.save_or_locate(caluny_subject_106)

    caluny_subject_107 = Subject()
    caluny_subject_107.code = 310
    caluny_subject_107.title = u'Ingenier\xeda de Protocolos'
    caluny_subject_107.description = None
    caluny_subject_107.level = None
    caluny_subject_107.degree = caluny_degree_3
    caluny_subject_107 = importer.save_or_locate(caluny_subject_107)

    caluny_subject_108 = Subject()
    caluny_subject_108.code = 317
    caluny_subject_108.title = u'Seguridad en Servicios y Aplicaciones'
    caluny_subject_108.description = None
    caluny_subject_108.level = None
    caluny_subject_108.degree = caluny_degree_3
    caluny_subject_108 = importer.save_or_locate(caluny_subject_108)

    caluny_subject_109 = Subject()
    caluny_subject_109.code = 316
    caluny_subject_109.title = u'Programaci\xf3n de Videojuegos'
    caluny_subject_109.description = None
    caluny_subject_109.level = None
    caluny_subject_109.degree = caluny_degree_3
    caluny_subject_109 = importer.save_or_locate(caluny_subject_109)

    caluny_subject_110 = Subject()
    caluny_subject_110.code = 314
    caluny_subject_110.title = u'Mantenimiento y Pruebas del Software'
    caluny_subject_110.description = None
    caluny_subject_110.level = None
    caluny_subject_110.degree = caluny_degree_3
    caluny_subject_110 = importer.save_or_locate(caluny_subject_110)

    caluny_subject_111 = Subject()
    caluny_subject_111.code = 110
    caluny_subject_111.title = u'Tecnolog\xeda de Computadores'
    caluny_subject_111.description = None
    caluny_subject_111.level = None
    caluny_subject_111.degree = caluny_degree_3
    caluny_subject_111 = importer.save_or_locate(caluny_subject_111)

    caluny_subject_112 = Subject()
    caluny_subject_112.code = 421
    caluny_subject_112.title = u'Redes Inal\xe1mbricas'
    caluny_subject_112.description = None
    caluny_subject_112.level = None
    caluny_subject_112.degree = caluny_degree_3
    caluny_subject_112 = importer.save_or_locate(caluny_subject_112)

    caluny_subject_113 = Subject()
    caluny_subject_113.code = 420
    caluny_subject_113.title = u'Pr\xe1cticas Externas'
    caluny_subject_113.description = None
    caluny_subject_113.level = None
    caluny_subject_113.degree = caluny_degree_3
    caluny_subject_113 = importer.save_or_locate(caluny_subject_113)

    caluny_subject_114 = Subject()
    caluny_subject_114.code = 422
    caluny_subject_114.title = u'Trabajo Fin de Grado'
    caluny_subject_114.description = None
    caluny_subject_114.level = None
    caluny_subject_114.degree = caluny_degree_3
    caluny_subject_114 = importer.save_or_locate(caluny_subject_114)

    caluny_subject_115 = Subject()
    caluny_subject_115.code = 201
    caluny_subject_115.title = u'An\xe1lisis y Dise\xf1o de Algoritmos'
    caluny_subject_115.description = None
    caluny_subject_115.level = None
    caluny_subject_115.degree = caluny_degree_3
    caluny_subject_115 = importer.save_or_locate(caluny_subject_115)

    caluny_subject_116 = Subject()
    caluny_subject_116.code = 309
    caluny_subject_116.title = u'T\xe9cnicas Computacionales para la Ingenier\xeda del Software'
    caluny_subject_116.description = None
    caluny_subject_116.level = None
    caluny_subject_116.degree = caluny_degree_3
    caluny_subject_116 = importer.save_or_locate(caluny_subject_116)

    caluny_subject_117 = Subject()
    caluny_subject_117.code = 203
    caluny_subject_117.title = u'Estructura de Computadores'
    caluny_subject_117.description = None
    caluny_subject_117.level = None
    caluny_subject_117.degree = caluny_degree_3
    caluny_subject_117 = importer.save_or_locate(caluny_subject_117)

    caluny_subject_118 = Subject()
    caluny_subject_118.code = 202
    caluny_subject_118.title = u'Bases de Datos'
    caluny_subject_118.description = None
    caluny_subject_118.level = None
    caluny_subject_118.degree = caluny_degree_3
    caluny_subject_118 = importer.save_or_locate(caluny_subject_118)

    caluny_subject_119 = Subject()
    caluny_subject_119.code = 205
    caluny_subject_119.title = u'Teor\xeda de Aut\xf3matas y Lenguajes Formales'
    caluny_subject_119.description = None
    caluny_subject_119.level = None
    caluny_subject_119.degree = caluny_degree_3
    caluny_subject_119 = importer.save_or_locate(caluny_subject_119)

    caluny_subject_120 = Subject()
    caluny_subject_120.code = 204
    caluny_subject_120.title = u'Estructura de Datos'
    caluny_subject_120.description = None
    caluny_subject_120.level = None
    caluny_subject_120.degree = caluny_degree_3
    caluny_subject_120 = importer.save_or_locate(caluny_subject_120)

    caluny_subject_121 = Subject()
    caluny_subject_121.code = 207
    caluny_subject_121.title = u'Programaci\xf3n de Sistemas y Concurrencia'
    caluny_subject_121.description = None
    caluny_subject_121.level = None
    caluny_subject_121.degree = caluny_degree_3
    caluny_subject_121 = importer.save_or_locate(caluny_subject_121)

    caluny_subject_122 = Subject()
    caluny_subject_122.code = 206
    caluny_subject_122.title = u'Introducci\xf3n a la Ingenier\xeda del Software'
    caluny_subject_122.description = None
    caluny_subject_122.level = None
    caluny_subject_122.degree = caluny_degree_3
    caluny_subject_122 = importer.save_or_locate(caluny_subject_122)

    caluny_subject_123 = Subject()
    caluny_subject_123.code = 209
    caluny_subject_123.title = u'Sistemas Inteligentes'
    caluny_subject_123.description = None
    caluny_subject_123.level = None
    caluny_subject_123.degree = caluny_degree_3
    caluny_subject_123 = importer.save_or_locate(caluny_subject_123)

    caluny_subject_124 = Subject()
    caluny_subject_124.code = 208
    caluny_subject_124.title = u'Redes y Sistemas Distribuidos'
    caluny_subject_124.description = None
    caluny_subject_124.level = None
    caluny_subject_124.degree = caluny_degree_3
    caluny_subject_124 = importer.save_or_locate(caluny_subject_124)

    caluny_subject_125 = Subject()
    caluny_subject_125.code = 302
    caluny_subject_125.title = u'Electr\xf3nica Digital'
    caluny_subject_125.description = None
    caluny_subject_125.level = None
    caluny_subject_125.degree = caluny_degree_3
    caluny_subject_125 = importer.save_or_locate(caluny_subject_125)

    caluny_subject_126 = Subject()
    caluny_subject_126.code = 303
    caluny_subject_126.title = u'Gesti\xf3n de la Informaci\xf3n'
    caluny_subject_126.description = None
    caluny_subject_126.level = None
    caluny_subject_126.degree = caluny_degree_3
    caluny_subject_126 = importer.save_or_locate(caluny_subject_126)

    caluny_subject_127 = Subject()
    caluny_subject_127.code = 304
    caluny_subject_127.title = u'Ingenier\xeda de Requisitos'
    caluny_subject_127.description = None
    caluny_subject_127.level = None
    caluny_subject_127.degree = caluny_degree_3
    caluny_subject_127 = importer.save_or_locate(caluny_subject_127)

    caluny_subject_128 = Subject()
    caluny_subject_128.code = 305
    caluny_subject_128.title = u'Modelado y Dise\xf1o del Software'
    caluny_subject_128.description = None
    caluny_subject_128.level = None
    caluny_subject_128.degree = caluny_degree_3
    caluny_subject_128 = importer.save_or_locate(caluny_subject_128)

    caluny_subject_129 = Subject()
    caluny_subject_129.code = 108
    caluny_subject_129.title = u'Organizaci\xf3n Empresarial'
    caluny_subject_129.description = None
    caluny_subject_129.level = None
    caluny_subject_129.degree = caluny_degree_3
    caluny_subject_129 = importer.save_or_locate(caluny_subject_129)

    caluny_subject_130 = Subject()
    caluny_subject_130.code = 109
    caluny_subject_130.title = u'Programaci\xf3n Orientada a Objetos'
    caluny_subject_130.description = None
    caluny_subject_130.level = None
    caluny_subject_130.degree = caluny_degree_3
    caluny_subject_130 = importer.save_or_locate(caluny_subject_130)

    caluny_subject_131 = Subject()
    caluny_subject_131.code = 102
    caluny_subject_131.title = u'Fundamentos F\xedsicos de la Inform\xe1tica'
    caluny_subject_131.description = None
    caluny_subject_131.level = None
    caluny_subject_131.degree = caluny_degree_3
    caluny_subject_131 = importer.save_or_locate(caluny_subject_131)

    caluny_subject_132 = Subject()
    caluny_subject_132.code = 103
    caluny_subject_132.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_132.description = None
    caluny_subject_132.level = None
    caluny_subject_132.degree = caluny_degree_3
    caluny_subject_132 = importer.save_or_locate(caluny_subject_132)

    caluny_subject_133 = Subject()
    caluny_subject_133.code = 101
    caluny_subject_133.title = u'C\xe1lculo para la Computaci\xf3n'
    caluny_subject_133.description = None
    caluny_subject_133.level = None
    caluny_subject_133.degree = caluny_degree_3
    caluny_subject_133 = importer.save_or_locate(caluny_subject_133)

    caluny_subject_134 = Subject()
    caluny_subject_134.code = 106
    caluny_subject_134.title = u'Estructuras Algebraicas para la Computaci\xf3n'
    caluny_subject_134.description = None
    caluny_subject_134.level = None
    caluny_subject_134.degree = caluny_degree_3
    caluny_subject_134 = importer.save_or_locate(caluny_subject_134)

    caluny_subject_135 = Subject()
    caluny_subject_135.code = 107
    caluny_subject_135.title = u'M\xe9todos Estad\xedsticos para la Computaci\xf3n'
    caluny_subject_135.description = None
    caluny_subject_135.level = None
    caluny_subject_135.degree = caluny_degree_3
    caluny_subject_135 = importer.save_or_locate(caluny_subject_135)

    caluny_subject_136 = Subject()
    caluny_subject_136.code = 104
    caluny_subject_136.title = u'Fundamentos de la Programaci\xf3n'
    caluny_subject_136.description = None
    caluny_subject_136.level = None
    caluny_subject_136.degree = caluny_degree_3
    caluny_subject_136 = importer.save_or_locate(caluny_subject_136)

    caluny_subject_137 = Subject()
    caluny_subject_137.code = 105
    caluny_subject_137.title = u'Matem\xe1tica Discreta'
    caluny_subject_137.description = None
    caluny_subject_137.level = None
    caluny_subject_137.degree = caluny_degree_3
    caluny_subject_137 = importer.save_or_locate(caluny_subject_137)

    caluny_subject_138 = Subject()
    caluny_subject_138.code = 210
    caluny_subject_138.title = u'Sistemas Operativos'
    caluny_subject_138.description = None
    caluny_subject_138.level = None
    caluny_subject_138.degree = caluny_degree_4
    caluny_subject_138 = importer.save_or_locate(caluny_subject_138)

    caluny_subject_139 = Subject()
    caluny_subject_139.code = 429
    caluny_subject_139.title = u'Proyectos y Legislaci\xf3n'
    caluny_subject_139.description = None
    caluny_subject_139.level = None
    caluny_subject_139.degree = caluny_degree_4
    caluny_subject_139 = importer.save_or_locate(caluny_subject_139)

    caluny_subject_140 = Subject()
    caluny_subject_140.code = 407
    caluny_subject_140.title = u'Dise\xf1o y Evaluaci\xf3n de Infraestructuras Inform\xe1ticas'
    caluny_subject_140.description = None
    caluny_subject_140.level = None
    caluny_subject_140.degree = caluny_degree_4
    caluny_subject_140 = importer.save_or_locate(caluny_subject_140)

    caluny_subject_141 = Subject()
    caluny_subject_141.code = 406
    caluny_subject_141.title = u'Direcci\xf3n de Proyectos de Sistemas de Informaci\xf3n'
    caluny_subject_141.description = None
    caluny_subject_141.level = None
    caluny_subject_141.degree = caluny_degree_4
    caluny_subject_141 = importer.save_or_locate(caluny_subject_141)

    caluny_subject_142 = Subject()
    caluny_subject_142.code = 404
    caluny_subject_142.title = u'Arquitectura Cluster'
    caluny_subject_142.description = None
    caluny_subject_142.level = None
    caluny_subject_142.degree = caluny_degree_4
    caluny_subject_142 = importer.save_or_locate(caluny_subject_142)

    caluny_subject_143 = Subject()
    caluny_subject_143.code = 403
    caluny_subject_143.title = u'Aprendizaje Computacional'
    caluny_subject_143.description = None
    caluny_subject_143.level = None
    caluny_subject_143.degree = caluny_degree_4
    caluny_subject_143 = importer.save_or_locate(caluny_subject_143)

    caluny_subject_144 = Subject()
    caluny_subject_144.code = 402
    caluny_subject_144.title = u'Administraci\xf3n de Sistemas Operativos'
    caluny_subject_144.description = None
    caluny_subject_144.level = None
    caluny_subject_144.degree = caluny_degree_4
    caluny_subject_144 = importer.save_or_locate(caluny_subject_144)

    caluny_subject_145 = Subject()
    caluny_subject_145.code = 401
    caluny_subject_145.title = u'Administraci\xf3n de Redes y Sistemas'
    caluny_subject_145.description = None
    caluny_subject_145.level = None
    caluny_subject_145.degree = caluny_degree_4
    caluny_subject_145 = importer.save_or_locate(caluny_subject_145)

    caluny_subject_146 = Subject()
    caluny_subject_146.code = 408
    caluny_subject_146.title = u'Dise\xf1o y Explotaci\xf3n de Almacenes de Datos'
    caluny_subject_146.description = None
    caluny_subject_146.level = None
    caluny_subject_146.degree = caluny_degree_4
    caluny_subject_146 = importer.save_or_locate(caluny_subject_146)

    caluny_subject_147 = Subject()
    caluny_subject_147.code = 414
    caluny_subject_147.title = u'Programaci\xf3n de Robots'
    caluny_subject_147.description = None
    caluny_subject_147.level = None
    caluny_subject_147.degree = caluny_degree_4
    caluny_subject_147 = importer.save_or_locate(caluny_subject_147)

    caluny_subject_148 = Subject()
    caluny_subject_148.code = 415
    caluny_subject_148.title = u'Rob\xf3tica'
    caluny_subject_148.description = None
    caluny_subject_148.level = None
    caluny_subject_148.degree = caluny_degree_4
    caluny_subject_148 = importer.save_or_locate(caluny_subject_148)

    caluny_subject_149 = Subject()
    caluny_subject_149.code = 417
    caluny_subject_149.title = u'Tecnolog\xeda de los Sistemas de Producci\xf3n'
    caluny_subject_149.description = None
    caluny_subject_149.level = None
    caluny_subject_149.degree = caluny_degree_4
    caluny_subject_149 = importer.save_or_locate(caluny_subject_149)

    caluny_subject_150 = Subject()
    caluny_subject_150.code = 410
    caluny_subject_150.title = u'Modelos de la Computaci\xf3n'
    caluny_subject_150.description = None
    caluny_subject_150.level = None
    caluny_subject_150.degree = caluny_degree_4
    caluny_subject_150 = importer.save_or_locate(caluny_subject_150)

    caluny_subject_151 = Subject()
    caluny_subject_151.code = 411
    caluny_subject_151.title = u'Negocio Electr\xf3nico'
    caluny_subject_151.description = None
    caluny_subject_151.level = None
    caluny_subject_151.degree = caluny_degree_4
    caluny_subject_151 = importer.save_or_locate(caluny_subject_151)

    caluny_subject_152 = Subject()
    caluny_subject_152.code = 412
    caluny_subject_152.title = u'Planificaci\xf3n de Proyectos y An\xe1lisis de Riesgos'
    caluny_subject_152.description = None
    caluny_subject_152.level = None
    caluny_subject_152.degree = caluny_degree_4
    caluny_subject_152 = importer.save_or_locate(caluny_subject_152)

    caluny_subject_153 = Subject()
    caluny_subject_153.code = 413
    caluny_subject_153.title = u'Procesamiento de Im\xe1genes y Video'
    caluny_subject_153.description = None
    caluny_subject_153.level = None
    caluny_subject_153.degree = caluny_degree_4
    caluny_subject_153 = importer.save_or_locate(caluny_subject_153)

    caluny_subject_154 = Subject()
    caluny_subject_154.code = 418
    caluny_subject_154.title = u'Teor\xeda de la Informaci\xf3n y la Codificaci\xf3n'
    caluny_subject_154.description = None
    caluny_subject_154.level = None
    caluny_subject_154.degree = caluny_degree_4
    caluny_subject_154 = importer.save_or_locate(caluny_subject_154)

    caluny_subject_155 = Subject()
    caluny_subject_155.code = 308
    caluny_subject_155.title = u'Seguridad de la Informaci\xf3n'
    caluny_subject_155.description = None
    caluny_subject_155.level = None
    caluny_subject_155.degree = caluny_degree_4
    caluny_subject_155 = importer.save_or_locate(caluny_subject_155)

    caluny_subject_156 = Subject()
    caluny_subject_156.code = 319
    caluny_subject_156.title = u'Modelos Estad\xedsticos y Simulaci\xf3n'
    caluny_subject_156.description = None
    caluny_subject_156.level = None
    caluny_subject_156.degree = caluny_degree_4
    caluny_subject_156 = importer.save_or_locate(caluny_subject_156)

    caluny_subject_157 = Subject()
    caluny_subject_157.code = 313
    caluny_subject_157.title = u'Algoritmia y Complejidad'
    caluny_subject_157.description = None
    caluny_subject_157.level = None
    caluny_subject_157.degree = caluny_degree_4
    caluny_subject_157 = importer.save_or_locate(caluny_subject_157)

    caluny_subject_158 = Subject()
    caluny_subject_158.code = 312
    caluny_subject_158.title = u'Administraci\xf3n de Bases de Datos'
    caluny_subject_158.description = None
    caluny_subject_158.level = None
    caluny_subject_158.degree = caluny_degree_4
    caluny_subject_158 = importer.save_or_locate(caluny_subject_158)

    caluny_subject_159 = Subject()
    caluny_subject_159.code = 310
    caluny_subject_159.title = u'Sistemas de Informaci\xf3n Empresarial'
    caluny_subject_159.description = None
    caluny_subject_159.level = None
    caluny_subject_159.degree = caluny_degree_4
    caluny_subject_159 = importer.save_or_locate(caluny_subject_159)

    caluny_subject_160 = Subject()
    caluny_subject_160.code = 316
    caluny_subject_160.title = u'Inteligencia Artificial para Juegos'
    caluny_subject_160.description = None
    caluny_subject_160.level = None
    caluny_subject_160.degree = caluny_degree_4
    caluny_subject_160 = importer.save_or_locate(caluny_subject_160)

    caluny_subject_161 = Subject()
    caluny_subject_161.code = 315
    caluny_subject_161.title = u'Ingenier\xeda de Protocolos'
    caluny_subject_161.description = None
    caluny_subject_161.level = None
    caluny_subject_161.degree = caluny_degree_4
    caluny_subject_161 = importer.save_or_locate(caluny_subject_161)

    caluny_subject_162 = Subject()
    caluny_subject_162.code = 314
    caluny_subject_162.title = u'An\xe1lisis y Dise\xf1o de los Sistemas de Informaci\xf3n'
    caluny_subject_162.description = None
    caluny_subject_162.level = None
    caluny_subject_162.degree = caluny_degree_4
    caluny_subject_162 = importer.save_or_locate(caluny_subject_162)

    caluny_subject_163 = Subject()
    caluny_subject_163.code = 110
    caluny_subject_163.title = u'Tecnolog\xeda de Computadores'
    caluny_subject_163.description = None
    caluny_subject_163.level = None
    caluny_subject_163.degree = caluny_degree_4
    caluny_subject_163 = importer.save_or_locate(caluny_subject_163)

    caluny_subject_164 = Subject()
    caluny_subject_164.code = 322
    caluny_subject_164.title = u'Sistemas de Informaci\xf3n para Internet'
    caluny_subject_164.description = None
    caluny_subject_164.level = None
    caluny_subject_164.degree = caluny_degree_4
    caluny_subject_164 = importer.save_or_locate(caluny_subject_164)

    caluny_subject_165 = Subject()
    caluny_subject_165.code = 323
    caluny_subject_165.title = u'Visi\xf3n por Computador'
    caluny_subject_165.description = None
    caluny_subject_165.level = None
    caluny_subject_165.degree = caluny_degree_4
    caluny_subject_165 = importer.save_or_locate(caluny_subject_165)

    caluny_subject_166 = Subject()
    caluny_subject_166.code = 320
    caluny_subject_166.title = u'Programaci\xf3n de Videojuegos'
    caluny_subject_166.description = None
    caluny_subject_166.level = None
    caluny_subject_166.degree = caluny_degree_4
    caluny_subject_166 = importer.save_or_locate(caluny_subject_166)

    caluny_subject_167 = Subject()
    caluny_subject_167.code = 321
    caluny_subject_167.title = u'Sistemas Inteligentes II'
    caluny_subject_167.description = None
    caluny_subject_167.level = None
    caluny_subject_167.degree = caluny_degree_4
    caluny_subject_167 = importer.save_or_locate(caluny_subject_167)

    caluny_subject_168 = Subject()
    caluny_subject_168.code = 421
    caluny_subject_168.title = u'Arquitecturas Virtuales'
    caluny_subject_168.description = None
    caluny_subject_168.level = None
    caluny_subject_168.degree = caluny_degree_4
    caluny_subject_168 = importer.save_or_locate(caluny_subject_168)

    caluny_subject_169 = Subject()
    caluny_subject_169.code = 420
    caluny_subject_169.title = u'Teor\xeda de los Lenguajes de Programaci\xf3n'
    caluny_subject_169.description = None
    caluny_subject_169.level = None
    caluny_subject_169.degree = caluny_degree_4
    caluny_subject_169 = importer.save_or_locate(caluny_subject_169)

    caluny_subject_170 = Subject()
    caluny_subject_170.code = 423
    caluny_subject_170.title = u'Electr\xf3nica para Dom\xf3tica'
    caluny_subject_170.description = None
    caluny_subject_170.level = None
    caluny_subject_170.degree = caluny_degree_4
    caluny_subject_170 = importer.save_or_locate(caluny_subject_170)

    caluny_subject_171 = Subject()
    caluny_subject_171.code = 425
    caluny_subject_171.title = u'Herramientas de Dise\xf1o Electr\xf3nico'
    caluny_subject_171.description = None
    caluny_subject_171.level = None
    caluny_subject_171.degree = caluny_degree_4
    caluny_subject_171 = importer.save_or_locate(caluny_subject_171)

    caluny_subject_172 = Subject()
    caluny_subject_172.code = 424
    caluny_subject_172.title = u'Gesti\xf3n Inteligente de la Informaci\xf3n'
    caluny_subject_172.description = None
    caluny_subject_172.level = None
    caluny_subject_172.degree = caluny_degree_4
    caluny_subject_172 = importer.save_or_locate(caluny_subject_172)

    caluny_subject_173 = Subject()
    caluny_subject_173.code = 201
    caluny_subject_173.title = u'An\xe1lisis y Dise\xf1o de Algoritmos'
    caluny_subject_173.description = None
    caluny_subject_173.level = None
    caluny_subject_173.degree = caluny_degree_4
    caluny_subject_173 = importer.save_or_locate(caluny_subject_173)

    caluny_subject_174 = Subject()
    caluny_subject_174.code = 203
    caluny_subject_174.title = u'Estructura de Computadores'
    caluny_subject_174.description = None
    caluny_subject_174.level = None
    caluny_subject_174.degree = caluny_degree_4
    caluny_subject_174 = importer.save_or_locate(caluny_subject_174)

    caluny_subject_175 = Subject()
    caluny_subject_175.code = 202
    caluny_subject_175.title = u'Bases de Datos'
    caluny_subject_175.description = None
    caluny_subject_175.level = None
    caluny_subject_175.degree = caluny_degree_4
    caluny_subject_175 = importer.save_or_locate(caluny_subject_175)

    caluny_subject_176 = Subject()
    caluny_subject_176.code = 205
    caluny_subject_176.title = u'Teor\xeda de Aut\xf3matas y Lenguajes Formales'
    caluny_subject_176.description = None
    caluny_subject_176.level = None
    caluny_subject_176.degree = caluny_degree_4
    caluny_subject_176 = importer.save_or_locate(caluny_subject_176)

    caluny_subject_177 = Subject()
    caluny_subject_177.code = 204
    caluny_subject_177.title = u'Estructura de Datos'
    caluny_subject_177.description = None
    caluny_subject_177.level = None
    caluny_subject_177.degree = caluny_degree_4
    caluny_subject_177 = importer.save_or_locate(caluny_subject_177)

    caluny_subject_178 = Subject()
    caluny_subject_178.code = 207
    caluny_subject_178.title = u'Programaci\xf3n de Sistemas y Concurrencia'
    caluny_subject_178.description = None
    caluny_subject_178.level = None
    caluny_subject_178.degree = caluny_degree_4
    caluny_subject_178 = importer.save_or_locate(caluny_subject_178)

    caluny_subject_179 = Subject()
    caluny_subject_179.code = 206
    caluny_subject_179.title = u'Introducci\xf3n a la Ingenier\xeda del Software'
    caluny_subject_179.description = None
    caluny_subject_179.level = None
    caluny_subject_179.degree = caluny_degree_4
    caluny_subject_179 = importer.save_or_locate(caluny_subject_179)

    caluny_subject_180 = Subject()
    caluny_subject_180.code = 209
    caluny_subject_180.title = u'Sistemas Inteligentes'
    caluny_subject_180.description = None
    caluny_subject_180.level = None
    caluny_subject_180.degree = caluny_degree_4
    caluny_subject_180 = importer.save_or_locate(caluny_subject_180)

    caluny_subject_181 = Subject()
    caluny_subject_181.code = 208
    caluny_subject_181.title = u'Redes y Sistemas Distribuidos'
    caluny_subject_181.description = None
    caluny_subject_181.level = None
    caluny_subject_181.degree = caluny_degree_4
    caluny_subject_181 = importer.save_or_locate(caluny_subject_181)

    caluny_subject_182 = Subject()
    caluny_subject_182.code = 302
    caluny_subject_182.title = u'Desarrollo de Servicios Telem\xe1ticos'
    caluny_subject_182.description = None
    caluny_subject_182.level = None
    caluny_subject_182.degree = caluny_degree_4
    caluny_subject_182 = importer.save_or_locate(caluny_subject_182)

    caluny_subject_183 = Subject()
    caluny_subject_183.code = 303
    caluny_subject_183.title = u'Electr\xf3nica Digital'
    caluny_subject_183.description = None
    caluny_subject_183.level = None
    caluny_subject_183.degree = caluny_degree_4
    caluny_subject_183 = importer.save_or_locate(caluny_subject_183)

    caluny_subject_184 = Subject()
    caluny_subject_184.code = 304
    caluny_subject_184.title = u'Introducci\xf3n a los Sistemas de Informaci\xf3n'
    caluny_subject_184.description = None
    caluny_subject_184.level = None
    caluny_subject_184.degree = caluny_degree_4
    caluny_subject_184 = importer.save_or_locate(caluny_subject_184)

    caluny_subject_185 = Subject()
    caluny_subject_185.code = 305
    caluny_subject_185.title = u'L\xf3gica Computacional'
    caluny_subject_185.description = None
    caluny_subject_185.level = None
    caluny_subject_185.degree = caluny_degree_4
    caluny_subject_185 = importer.save_or_locate(caluny_subject_185)

    caluny_subject_186 = Subject()
    caluny_subject_186.code = 306
    caluny_subject_186.title = u'Procesadores de Lenguajes'
    caluny_subject_186.description = None
    caluny_subject_186.level = None
    caluny_subject_186.degree = caluny_degree_4
    caluny_subject_186 = importer.save_or_locate(caluny_subject_186)

    caluny_subject_187 = Subject()
    caluny_subject_187.code = 108
    caluny_subject_187.title = u'Organizaci\xf3n Empresarial'
    caluny_subject_187.description = None
    caluny_subject_187.level = None
    caluny_subject_187.degree = caluny_degree_4
    caluny_subject_187 = importer.save_or_locate(caluny_subject_187)

    caluny_subject_188 = Subject()
    caluny_subject_188.code = 109
    caluny_subject_188.title = u'Programaci\xf3n Orientada a Objetos'
    caluny_subject_188.description = None
    caluny_subject_188.level = None
    caluny_subject_188.degree = caluny_degree_4
    caluny_subject_188 = importer.save_or_locate(caluny_subject_188)

    caluny_subject_189 = Subject()
    caluny_subject_189.code = 102
    caluny_subject_189.title = u'Fundamentos F\xedsicos de la Inform\xe1tica'
    caluny_subject_189.description = None
    caluny_subject_189.level = None
    caluny_subject_189.degree = caluny_degree_4
    caluny_subject_189 = importer.save_or_locate(caluny_subject_189)

    caluny_subject_190 = Subject()
    caluny_subject_190.code = 103
    caluny_subject_190.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_190.description = None
    caluny_subject_190.level = None
    caluny_subject_190.degree = caluny_degree_4
    caluny_subject_190 = importer.save_or_locate(caluny_subject_190)

    caluny_subject_191 = Subject()
    caluny_subject_191.code = 101
    caluny_subject_191.title = u'C\xe1lculo para la Computaci\xf3n'
    caluny_subject_191.description = None
    caluny_subject_191.level = None
    caluny_subject_191.degree = caluny_degree_4
    caluny_subject_191 = importer.save_or_locate(caluny_subject_191)

    caluny_subject_192 = Subject()
    caluny_subject_192.code = 106
    caluny_subject_192.title = u'Estructuras Algebraicas para la Computaci\xf3n'
    caluny_subject_192.description = None
    caluny_subject_192.level = None
    caluny_subject_192.degree = caluny_degree_4
    caluny_subject_192 = importer.save_or_locate(caluny_subject_192)

    caluny_subject_193 = Subject()
    caluny_subject_193.code = 107
    caluny_subject_193.title = u'M\xe9todos Estad\xedsticos para la Computaci\xf3n'
    caluny_subject_193.description = None
    caluny_subject_193.level = None
    caluny_subject_193.degree = caluny_degree_4
    caluny_subject_193 = importer.save_or_locate(caluny_subject_193)

    caluny_subject_194 = Subject()
    caluny_subject_194.code = 104
    caluny_subject_194.title = u'Fundamentos de la Programaci\xf3n'
    caluny_subject_194.description = None
    caluny_subject_194.level = None
    caluny_subject_194.degree = caluny_degree_4
    caluny_subject_194 = importer.save_or_locate(caluny_subject_194)

    caluny_subject_195 = Subject()
    caluny_subject_195.code = 105
    caluny_subject_195.title = u'Matem\xe1tica Discreta'
    caluny_subject_195.description = None
    caluny_subject_195.level = None
    caluny_subject_195.degree = caluny_degree_4
    caluny_subject_195 = importer.save_or_locate(caluny_subject_195)

    caluny_subject_196 = Subject()
    caluny_subject_196.code = 432
    caluny_subject_196.title = u'Sistemas de Informaci\xf3n para la Industria'
    caluny_subject_196.description = None
    caluny_subject_196.level = None
    caluny_subject_196.degree = caluny_degree_4
    caluny_subject_196 = importer.save_or_locate(caluny_subject_196)

    caluny_subject_197 = Subject()
    caluny_subject_197.code = 433
    caluny_subject_197.title = u'Trabajo Fin de Grado'
    caluny_subject_197.description = None
    caluny_subject_197.level = None
    caluny_subject_197.degree = caluny_degree_4
    caluny_subject_197 = importer.save_or_locate(caluny_subject_197)

    caluny_subject_198 = Subject()
    caluny_subject_198.code = 430
    caluny_subject_198.title = u'Pr\xe1cticas Externas'
    caluny_subject_198.description = None
    caluny_subject_198.level = None
    caluny_subject_198.degree = caluny_degree_4
    caluny_subject_198 = importer.save_or_locate(caluny_subject_198)

    caluny_subject_199 = Subject()
    caluny_subject_199.code = 431
    caluny_subject_199.title = u'Redes Inal\xe1mbricas'
    caluny_subject_199.description = None
    caluny_subject_199.level = None
    caluny_subject_199.degree = caluny_degree_4
    caluny_subject_199 = importer.save_or_locate(caluny_subject_199)

    caluny_subject_200 = Subject()
    caluny_subject_200.code = 201
    caluny_subject_200.title = u'Ampliaci\xf3n de Matem\xe1ticas'
    caluny_subject_200.description = None
    caluny_subject_200.level = None
    caluny_subject_200.degree = caluny_degree_5
    caluny_subject_200 = importer.save_or_locate(caluny_subject_200)

    caluny_subject_201 = Subject()
    caluny_subject_201.code = 203
    caluny_subject_201.title = u'Circuitos y M\xe1quinas El\xe9ctricas'
    caluny_subject_201.description = None
    caluny_subject_201.level = None
    caluny_subject_201.degree = caluny_degree_5
    caluny_subject_201 = importer.save_or_locate(caluny_subject_201)

    caluny_subject_202 = Subject()
    caluny_subject_202.code = 202
    caluny_subject_202.title = u'Biolog\xeda Molecular y Bioqu\xedmica'
    caluny_subject_202.description = None
    caluny_subject_202.level = None
    caluny_subject_202.degree = caluny_degree_5
    caluny_subject_202 = importer.save_or_locate(caluny_subject_202)

    caluny_subject_203 = Subject()
    caluny_subject_203.code = 205
    caluny_subject_203.title = u'Estructuras de Datos y Algoritmos'
    caluny_subject_203.description = None
    caluny_subject_203.level = None
    caluny_subject_203.degree = caluny_degree_5
    caluny_subject_203 = importer.save_or_locate(caluny_subject_203)

    caluny_subject_204 = Subject()
    caluny_subject_204.code = 204
    caluny_subject_204.title = u'Electr\xf3nica'
    caluny_subject_204.description = None
    caluny_subject_204.level = None
    caluny_subject_204.degree = caluny_degree_5
    caluny_subject_204 = importer.save_or_locate(caluny_subject_204)

    caluny_subject_205 = Subject()
    caluny_subject_205.code = 207
    caluny_subject_205.title = u'Arquitectura de Computadores y Sistemas Operativos'
    caluny_subject_205.description = None
    caluny_subject_205.level = None
    caluny_subject_205.degree = caluny_degree_5
    caluny_subject_205 = importer.save_or_locate(caluny_subject_205)

    caluny_subject_206 = Subject()
    caluny_subject_206.code = 206
    caluny_subject_206.title = u'Anatom\xeda y Fisiolog\xeda'
    caluny_subject_206.description = None
    caluny_subject_206.level = None
    caluny_subject_206.degree = caluny_degree_5
    caluny_subject_206 = importer.save_or_locate(caluny_subject_206)

    caluny_subject_207 = Subject()
    caluny_subject_207.code = 209
    caluny_subject_207.title = u'Biolog\xeda Celular y Gen\xe9tica'
    caluny_subject_207.description = None
    caluny_subject_207.level = None
    caluny_subject_207.degree = caluny_degree_5
    caluny_subject_207 = importer.save_or_locate(caluny_subject_207)

    caluny_subject_208 = Subject()
    caluny_subject_208.code = 208
    caluny_subject_208.title = u'Bases de Datos'
    caluny_subject_208.description = None
    caluny_subject_208.level = None
    caluny_subject_208.degree = caluny_degree_5
    caluny_subject_208 = importer.save_or_locate(caluny_subject_208)

    caluny_subject_209 = Subject()
    caluny_subject_209.code = 302
    caluny_subject_209.title = u'Im\xe1genes Biom\xe9dicas'
    caluny_subject_209.description = None
    caluny_subject_209.level = None
    caluny_subject_209.degree = caluny_degree_5
    caluny_subject_209 = importer.save_or_locate(caluny_subject_209)

    caluny_subject_210 = Subject()
    caluny_subject_210.code = 303
    caluny_subject_210.title = u'Ingenier\xeda del Software'
    caluny_subject_210.description = None
    caluny_subject_210.level = None
    caluny_subject_210.degree = caluny_degree_5
    caluny_subject_210 = importer.save_or_locate(caluny_subject_210)

    caluny_subject_211 = Subject()
    caluny_subject_211.code = 304
    caluny_subject_211.title = u'Redes y Sistemas Distribuidos'
    caluny_subject_211.description = None
    caluny_subject_211.level = None
    caluny_subject_211.degree = caluny_degree_5
    caluny_subject_211 = importer.save_or_locate(caluny_subject_211)

    caluny_subject_212 = Subject()
    caluny_subject_212.code = 305
    caluny_subject_212.title = u'Sistemas Inteligentes'
    caluny_subject_212.description = None
    caluny_subject_212.level = None
    caluny_subject_212.degree = caluny_degree_5
    caluny_subject_212 = importer.save_or_locate(caluny_subject_212)

    caluny_subject_213 = Subject()
    caluny_subject_213.code = 333
    caluny_subject_213.title = u'Biotecnolog\xeda'
    caluny_subject_213.description = None
    caluny_subject_213.level = None
    caluny_subject_213.degree = caluny_degree_5
    caluny_subject_213 = importer.save_or_locate(caluny_subject_213)

    caluny_subject_214 = Subject()
    caluny_subject_214.code = 330
    caluny_subject_214.title = u'Biomateriales'
    caluny_subject_214.description = None
    caluny_subject_214.level = None
    caluny_subject_214.degree = caluny_degree_5
    caluny_subject_214 = importer.save_or_locate(caluny_subject_214)

    caluny_subject_215 = Subject()
    caluny_subject_215.code = 332
    caluny_subject_215.title = u'Biomec\xe1nica II: Fluidos'
    caluny_subject_215.description = None
    caluny_subject_215.level = None
    caluny_subject_215.degree = caluny_degree_5
    caluny_subject_215 = importer.save_or_locate(caluny_subject_215)

    caluny_subject_216 = Subject()
    caluny_subject_216.code = 108
    caluny_subject_216.title = u'F\xedsica II'
    caluny_subject_216.description = None
    caluny_subject_216.level = None
    caluny_subject_216.degree = caluny_degree_5
    caluny_subject_216 = importer.save_or_locate(caluny_subject_216)

    caluny_subject_217 = Subject()
    caluny_subject_217.code = 109
    caluny_subject_217.title = u'Gesti\xf3n de Empresas'
    caluny_subject_217.description = None
    caluny_subject_217.level = None
    caluny_subject_217.degree = caluny_degree_5
    caluny_subject_217 = importer.save_or_locate(caluny_subject_217)

    caluny_subject_218 = Subject()
    caluny_subject_218.code = 110
    caluny_subject_218.title = u'Programaci\xf3n Orientada a Objetos'
    caluny_subject_218.description = None
    caluny_subject_218.level = None
    caluny_subject_218.degree = caluny_degree_5
    caluny_subject_218 = importer.save_or_locate(caluny_subject_218)

    caluny_subject_219 = Subject()
    caluny_subject_219.code = 334
    caluny_subject_219.title = u'Ciencia y Resistencia de Materiales'
    caluny_subject_219.description = None
    caluny_subject_219.level = None
    caluny_subject_219.degree = caluny_degree_5
    caluny_subject_219 = importer.save_or_locate(caluny_subject_219)

    caluny_subject_220 = Subject()
    caluny_subject_220.code = 102
    caluny_subject_220.title = u'C\xe1lculo'
    caluny_subject_220.description = None
    caluny_subject_220.level = None
    caluny_subject_220.degree = caluny_degree_5
    caluny_subject_220 = importer.save_or_locate(caluny_subject_220)

    caluny_subject_221 = Subject()
    caluny_subject_221.code = 103
    caluny_subject_221.title = u'Fundamentos de la Programaci\xf3n'
    caluny_subject_221.description = None
    caluny_subject_221.level = None
    caluny_subject_221.degree = caluny_degree_5
    caluny_subject_221 = importer.save_or_locate(caluny_subject_221)

    caluny_subject_222 = Subject()
    caluny_subject_222.code = 101
    caluny_subject_222.title = u'Bioqu\xedmica Estructural'
    caluny_subject_222.description = None
    caluny_subject_222.level = None
    caluny_subject_222.degree = caluny_degree_5
    caluny_subject_222 = importer.save_or_locate(caluny_subject_222)

    caluny_subject_223 = Subject()
    caluny_subject_223.code = 106
    caluny_subject_223.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_223.description = None
    caluny_subject_223.level = None
    caluny_subject_223.degree = caluny_degree_5
    caluny_subject_223 = importer.save_or_locate(caluny_subject_223)

    caluny_subject_224 = Subject()
    caluny_subject_224.code = 107
    caluny_subject_224.title = u'Estad\xedstica'
    caluny_subject_224.description = None
    caluny_subject_224.level = None
    caluny_subject_224.degree = caluny_degree_5
    caluny_subject_224 = importer.save_or_locate(caluny_subject_224)

    caluny_subject_225 = Subject()
    caluny_subject_225.code = 104
    caluny_subject_225.title = u'F\xedsica I'
    caluny_subject_225.description = None
    caluny_subject_225.level = None
    caluny_subject_225.degree = caluny_degree_5
    caluny_subject_225 = importer.save_or_locate(caluny_subject_225)

    caluny_subject_226 = Subject()
    caluny_subject_226.code = 105
    caluny_subject_226.title = u'\xc1lgebra Lineal'
    caluny_subject_226.description = None
    caluny_subject_226.level = None
    caluny_subject_226.degree = caluny_degree_5
    caluny_subject_226 = importer.save_or_locate(caluny_subject_226)

    caluny_subject_227 = Subject()
    caluny_subject_227.code = 325
    caluny_subject_227.title = u'T\xe9cnicas y Modelos Algor\xedtmicos'
    caluny_subject_227.description = None
    caluny_subject_227.level = None
    caluny_subject_227.degree = caluny_degree_5
    caluny_subject_227 = importer.save_or_locate(caluny_subject_227)

    caluny_subject_228 = Subject()
    caluny_subject_228.code = 210
    caluny_subject_228.title = u'Control Autom\xe1tico'
    caluny_subject_228.description = None
    caluny_subject_228.level = None
    caluny_subject_228.degree = caluny_degree_5
    caluny_subject_228 = importer.save_or_locate(caluny_subject_228)

    caluny_subject_229 = Subject()
    caluny_subject_229.code = 322
    caluny_subject_229.title = u'Ingenier\xeda del Software Avanzada'
    caluny_subject_229.description = None
    caluny_subject_229.level = None
    caluny_subject_229.degree = caluny_degree_5
    caluny_subject_229 = importer.save_or_locate(caluny_subject_229)

    caluny_subject_230 = Subject()
    caluny_subject_230.code = 323
    caluny_subject_230.title = u'Miner\xeda de Datos'
    caluny_subject_230.description = None
    caluny_subject_230.level = None
    caluny_subject_230.degree = caluny_degree_5
    caluny_subject_230 = importer.save_or_locate(caluny_subject_230)

    caluny_subject_231 = Subject()
    caluny_subject_231.code = 320
    caluny_subject_231.title = u'Bases de Datos Biol\xf3gicas'
    caluny_subject_231.description = None
    caluny_subject_231.level = None
    caluny_subject_231.degree = caluny_degree_5
    caluny_subject_231 = importer.save_or_locate(caluny_subject_231)

    caluny_subject_232 = Subject()
    caluny_subject_232.code = 321
    caluny_subject_232.title = u'Gen\xf3mica, Prote\xf3mica y Metabol\xf3mica'
    caluny_subject_232.description = None
    caluny_subject_232.level = None
    caluny_subject_232.degree = caluny_degree_5
    caluny_subject_232 = importer.save_or_locate(caluny_subject_232)

    caluny_subject_233 = Subject()
    caluny_subject_233.code = 331
    caluny_subject_233.title = u'Biomec\xe1nica I: S\xf3lidos'
    caluny_subject_233.description = None
    caluny_subject_233.level = None
    caluny_subject_233.degree = caluny_degree_5
    caluny_subject_233 = importer.save_or_locate(caluny_subject_233)

    caluny_subject_234 = Subject()
    caluny_subject_234.code = 324
    caluny_subject_234.title = u'Programaci\xf3n Avanzada en Bioinform\xe1tica'
    caluny_subject_234.description = None
    caluny_subject_234.level = None
    caluny_subject_234.degree = caluny_degree_5
    caluny_subject_234 = importer.save_or_locate(caluny_subject_234)

    caluny_subject_235 = Subject()
    caluny_subject_235.code = 301
    caluny_subject_235.title = u'Fundamentos de Inform\xe1tica Cl\xednica'
    caluny_subject_235.description = None
    caluny_subject_235.level = None
    caluny_subject_235.degree = caluny_degree_5
    caluny_subject_235 = importer.save_or_locate(caluny_subject_235)

    caluny_subject_236 = Subject()
    caluny_subject_236.code = 335
    caluny_subject_236.title = u'Instrumentaci\xf3n Biom\xe9dica'
    caluny_subject_236.description = None
    caluny_subject_236.level = None
    caluny_subject_236.degree = caluny_degree_5
    caluny_subject_236 = importer.save_or_locate(caluny_subject_236)

    caluny_subject_237 = Subject()
    caluny_subject_237.code = 210
    caluny_subject_237.title = u'Sistemas Operativos'
    caluny_subject_237.description = None
    caluny_subject_237.level = None
    caluny_subject_237.degree = caluny_degree_6
    caluny_subject_237 = importer.save_or_locate(caluny_subject_237)

    caluny_subject_238 = Subject()
    caluny_subject_238.code = 407
    caluny_subject_238.title = u'Procesamiento de Im\xe1genes y Video'
    caluny_subject_238.description = None
    caluny_subject_238.level = None
    caluny_subject_238.degree = caluny_degree_6
    caluny_subject_238 = importer.save_or_locate(caluny_subject_238)

    caluny_subject_239 = Subject()
    caluny_subject_239.code = 405
    caluny_subject_239.title = u'Dise\xf1o de Infraestructuras Inform\xe1ticas'
    caluny_subject_239.description = None
    caluny_subject_239.level = None
    caluny_subject_239.degree = caluny_degree_6
    caluny_subject_239 = importer.save_or_locate(caluny_subject_239)

    caluny_subject_240 = Subject()
    caluny_subject_240.code = 403
    caluny_subject_240.title = u'Control por Computador'
    caluny_subject_240.description = None
    caluny_subject_240.level = None
    caluny_subject_240.degree = caluny_degree_6
    caluny_subject_240 = importer.save_or_locate(caluny_subject_240)

    caluny_subject_241 = Subject()
    caluny_subject_241.code = 402
    caluny_subject_241.title = u'Arquitectura Cluster'
    caluny_subject_241.description = None
    caluny_subject_241.level = None
    caluny_subject_241.degree = caluny_degree_6
    caluny_subject_241 = importer.save_or_locate(caluny_subject_241)

    caluny_subject_242 = Subject()
    caluny_subject_242.code = 401
    caluny_subject_242.title = u'Arquitecturas Paralelas'
    caluny_subject_242.description = None
    caluny_subject_242.level = None
    caluny_subject_242.degree = caluny_degree_6
    caluny_subject_242 = importer.save_or_locate(caluny_subject_242)

    caluny_subject_243 = Subject()
    caluny_subject_243.code = 409
    caluny_subject_243.title = u'Programaci\xf3n de Robots'
    caluny_subject_243.description = None
    caluny_subject_243.level = None
    caluny_subject_243.degree = caluny_degree_6
    caluny_subject_243 = importer.save_or_locate(caluny_subject_243)

    caluny_subject_244 = Subject()
    caluny_subject_244.code = 408
    caluny_subject_244.title = u'Programaci\xf3n Distribuida'
    caluny_subject_244.description = None
    caluny_subject_244.level = None
    caluny_subject_244.degree = caluny_degree_6
    caluny_subject_244 = importer.save_or_locate(caluny_subject_244)

    caluny_subject_245 = Subject()
    caluny_subject_245.code = 414
    caluny_subject_245.title = u'Arquitecturas Virtuales'
    caluny_subject_245.description = None
    caluny_subject_245.level = None
    caluny_subject_245.degree = caluny_degree_6
    caluny_subject_245 = importer.save_or_locate(caluny_subject_245)

    caluny_subject_246 = Subject()
    caluny_subject_246.code = 415
    caluny_subject_246.title = u'Electr\xf3nica para Dom\xf3tica'
    caluny_subject_246.description = None
    caluny_subject_246.level = None
    caluny_subject_246.degree = caluny_degree_6
    caluny_subject_246 = importer.save_or_locate(caluny_subject_246)

    caluny_subject_247 = Subject()
    caluny_subject_247.code = 416
    caluny_subject_247.title = u'Herramientas de Dise\xf1o Electr\xf3nico'
    caluny_subject_247.description = None
    caluny_subject_247.level = None
    caluny_subject_247.degree = caluny_degree_6
    caluny_subject_247 = importer.save_or_locate(caluny_subject_247)

    caluny_subject_248 = Subject()
    caluny_subject_248.code = 417
    caluny_subject_248.title = u'Implementaci\xf3n Electr\xf3nica de Procesadores'
    caluny_subject_248.description = None
    caluny_subject_248.level = None
    caluny_subject_248.degree = caluny_degree_6
    caluny_subject_248 = importer.save_or_locate(caluny_subject_248)

    caluny_subject_249 = Subject()
    caluny_subject_249.code = 411
    caluny_subject_249.title = u'Teor\xeda de la Informaci\xf3n y la Codificaci\xf3n'
    caluny_subject_249.description = None
    caluny_subject_249.level = None
    caluny_subject_249.degree = caluny_degree_6
    caluny_subject_249 = importer.save_or_locate(caluny_subject_249)

    caluny_subject_250 = Subject()
    caluny_subject_250.code = 413
    caluny_subject_250.title = u'Arquitecturas Especializadas'
    caluny_subject_250.description = None
    caluny_subject_250.level = None
    caluny_subject_250.degree = caluny_degree_6
    caluny_subject_250 = importer.save_or_locate(caluny_subject_250)

    caluny_subject_251 = Subject()
    caluny_subject_251.code = 418
    caluny_subject_251.title = u'Proyectos y Legislaci\xf3n'
    caluny_subject_251.description = None
    caluny_subject_251.level = None
    caluny_subject_251.degree = caluny_degree_6
    caluny_subject_251 = importer.save_or_locate(caluny_subject_251)

    caluny_subject_252 = Subject()
    caluny_subject_252.code = 419
    caluny_subject_252.title = u'Pr\xe1cticas Externas'
    caluny_subject_252.description = None
    caluny_subject_252.level = None
    caluny_subject_252.degree = caluny_degree_6
    caluny_subject_252 = importer.save_or_locate(caluny_subject_252)

    caluny_subject_253 = Subject()
    caluny_subject_253.code = 319
    caluny_subject_253.title = u'Visi\xf3n por Computador'
    caluny_subject_253.description = None
    caluny_subject_253.level = None
    caluny_subject_253.degree = caluny_degree_6
    caluny_subject_253 = importer.save_or_locate(caluny_subject_253)

    caluny_subject_254 = Subject()
    caluny_subject_254.code = 318
    caluny_subject_254.title = u'Sistemas de Tiempo Real'
    caluny_subject_254.description = None
    caluny_subject_254.level = None
    caluny_subject_254.degree = caluny_degree_6
    caluny_subject_254 = importer.save_or_locate(caluny_subject_254)

    caluny_subject_255 = Subject()
    caluny_subject_255.code = 313
    caluny_subject_255.title = u'Ingenier\xeda de Protocolos'
    caluny_subject_255.description = None
    caluny_subject_255.level = None
    caluny_subject_255.degree = caluny_degree_6
    caluny_subject_255 = importer.save_or_locate(caluny_subject_255)

    caluny_subject_256 = Subject()
    caluny_subject_256.code = 312
    caluny_subject_256.title = u'Dise\xf1o de Sistemas Operativos'
    caluny_subject_256.description = None
    caluny_subject_256.level = None
    caluny_subject_256.degree = caluny_degree_6
    caluny_subject_256 = importer.save_or_locate(caluny_subject_256)

    caluny_subject_257 = Subject()
    caluny_subject_257.code = 311
    caluny_subject_257.title = u'Dise\xf1o de Infraestructuras de Red'
    caluny_subject_257.description = None
    caluny_subject_257.level = None
    caluny_subject_257.degree = caluny_degree_6
    caluny_subject_257 = importer.save_or_locate(caluny_subject_257)

    caluny_subject_258 = Subject()
    caluny_subject_258.code = 310
    caluny_subject_258.title = u'Dise\xf1o con Microcontroladores'
    caluny_subject_258.description = None
    caluny_subject_258.level = None
    caluny_subject_258.degree = caluny_degree_6
    caluny_subject_258 = importer.save_or_locate(caluny_subject_258)

    caluny_subject_259 = Subject()
    caluny_subject_259.code = 317
    caluny_subject_259.title = u'Programaci\xf3n de Videojuegos'
    caluny_subject_259.description = None
    caluny_subject_259.level = None
    caluny_subject_259.degree = caluny_degree_6
    caluny_subject_259 = importer.save_or_locate(caluny_subject_259)

    caluny_subject_260 = Subject()
    caluny_subject_260.code = 314
    caluny_subject_260.title = u'Inteligencia Artificial para Juegos'
    caluny_subject_260.description = None
    caluny_subject_260.level = None
    caluny_subject_260.degree = caluny_degree_6
    caluny_subject_260 = importer.save_or_locate(caluny_subject_260)

    caluny_subject_261 = Subject()
    caluny_subject_261.code = 110
    caluny_subject_261.title = u'Tecnolog\xeda de Computadores'
    caluny_subject_261.description = None
    caluny_subject_261.level = None
    caluny_subject_261.degree = caluny_degree_6
    caluny_subject_261 = importer.save_or_locate(caluny_subject_261)

    caluny_subject_262 = Subject()
    caluny_subject_262.code = 420
    caluny_subject_262.title = u'Redes Inal\xe1mbricas'
    caluny_subject_262.description = None
    caluny_subject_262.level = None
    caluny_subject_262.degree = caluny_degree_6
    caluny_subject_262 = importer.save_or_locate(caluny_subject_262)

    caluny_subject_263 = Subject()
    caluny_subject_263.code = 422
    caluny_subject_263.title = u'Trabajo Fin de Grado'
    caluny_subject_263.description = None
    caluny_subject_263.level = None
    caluny_subject_263.degree = caluny_degree_6
    caluny_subject_263 = importer.save_or_locate(caluny_subject_263)

    caluny_subject_264 = Subject()
    caluny_subject_264.code = 201
    caluny_subject_264.title = u'An\xe1lisis y Dise\xf1o de Algoritmos'
    caluny_subject_264.description = None
    caluny_subject_264.level = None
    caluny_subject_264.degree = caluny_degree_6
    caluny_subject_264 = importer.save_or_locate(caluny_subject_264)

    caluny_subject_265 = Subject()
    caluny_subject_265.code = 203
    caluny_subject_265.title = u'Estructura de Computadores'
    caluny_subject_265.description = None
    caluny_subject_265.level = None
    caluny_subject_265.degree = caluny_degree_6
    caluny_subject_265 = importer.save_or_locate(caluny_subject_265)

    caluny_subject_266 = Subject()
    caluny_subject_266.code = 202
    caluny_subject_266.title = u'Bases de Datos'
    caluny_subject_266.description = None
    caluny_subject_266.level = None
    caluny_subject_266.degree = caluny_degree_6
    caluny_subject_266 = importer.save_or_locate(caluny_subject_266)

    caluny_subject_267 = Subject()
    caluny_subject_267.code = 205
    caluny_subject_267.title = u'Teoria de Aut\xf3matas y Lenguajes Formales'
    caluny_subject_267.description = None
    caluny_subject_267.level = None
    caluny_subject_267.degree = caluny_degree_6
    caluny_subject_267 = importer.save_or_locate(caluny_subject_267)

    caluny_subject_268 = Subject()
    caluny_subject_268.code = 204
    caluny_subject_268.title = u'Estructura de Datos'
    caluny_subject_268.description = None
    caluny_subject_268.level = None
    caluny_subject_268.degree = caluny_degree_6
    caluny_subject_268 = importer.save_or_locate(caluny_subject_268)

    caluny_subject_269 = Subject()
    caluny_subject_269.code = 207
    caluny_subject_269.title = u'Programaci\xf3n de Sistemas y Concurrencia'
    caluny_subject_269.description = None
    caluny_subject_269.level = None
    caluny_subject_269.degree = caluny_degree_6
    caluny_subject_269 = importer.save_or_locate(caluny_subject_269)

    caluny_subject_270 = Subject()
    caluny_subject_270.code = 206
    caluny_subject_270.title = u'Introducci\xf3n a la Ingenieria del Software'
    caluny_subject_270.description = None
    caluny_subject_270.level = None
    caluny_subject_270.degree = caluny_degree_6
    caluny_subject_270 = importer.save_or_locate(caluny_subject_270)

    caluny_subject_271 = Subject()
    caluny_subject_271.code = 209
    caluny_subject_271.title = u'Sistemas Inteligentes'
    caluny_subject_271.description = None
    caluny_subject_271.level = None
    caluny_subject_271.degree = caluny_degree_6
    caluny_subject_271 = importer.save_or_locate(caluny_subject_271)

    caluny_subject_272 = Subject()
    caluny_subject_272.code = 208
    caluny_subject_272.title = u'Redes y Sistemas Distribuidos'
    caluny_subject_272.description = None
    caluny_subject_272.level = None
    caluny_subject_272.degree = caluny_degree_6
    caluny_subject_272 = importer.save_or_locate(caluny_subject_272)

    caluny_subject_273 = Subject()
    caluny_subject_273.code = 302
    caluny_subject_273.title = u'Arquitectura de Computadores'
    caluny_subject_273.description = None
    caluny_subject_273.level = None
    caluny_subject_273.degree = caluny_degree_6
    caluny_subject_273 = importer.save_or_locate(caluny_subject_273)

    caluny_subject_274 = Subject()
    caluny_subject_274.code = 303
    caluny_subject_274.title = u'Arquitecturas de Almacenamiento'
    caluny_subject_274.description = None
    caluny_subject_274.level = None
    caluny_subject_274.degree = caluny_degree_6
    caluny_subject_274 = importer.save_or_locate(caluny_subject_274)

    caluny_subject_275 = Subject()
    caluny_subject_275.code = 304
    caluny_subject_275.title = u'Circuitos Electr\xf3nicos y Se\xf1ales'
    caluny_subject_275.description = None
    caluny_subject_275.level = None
    caluny_subject_275.degree = caluny_degree_6
    caluny_subject_275 = importer.save_or_locate(caluny_subject_275)

    caluny_subject_276 = Subject()
    caluny_subject_276.code = 305
    caluny_subject_276.title = u'Dise\xf1o de Sistemas Empotrados'
    caluny_subject_276.description = None
    caluny_subject_276.level = None
    caluny_subject_276.degree = caluny_degree_6
    caluny_subject_276 = importer.save_or_locate(caluny_subject_276)

    caluny_subject_277 = Subject()
    caluny_subject_277.code = 306
    caluny_subject_277.title = u'Electr\xf3nica Digital'
    caluny_subject_277.description = None
    caluny_subject_277.level = None
    caluny_subject_277.degree = caluny_degree_6
    caluny_subject_277 = importer.save_or_locate(caluny_subject_277)

    caluny_subject_278 = Subject()
    caluny_subject_278.code = 108
    caluny_subject_278.title = u'Organizaci\xf3n Empresarial'
    caluny_subject_278.description = None
    caluny_subject_278.level = None
    caluny_subject_278.degree = caluny_degree_6
    caluny_subject_278 = importer.save_or_locate(caluny_subject_278)

    caluny_subject_279 = Subject()
    caluny_subject_279.code = 109
    caluny_subject_279.title = u'Programaci\xf3n Orientada a Objetos'
    caluny_subject_279.description = None
    caluny_subject_279.level = None
    caluny_subject_279.degree = caluny_degree_6
    caluny_subject_279 = importer.save_or_locate(caluny_subject_279)

    caluny_subject_280 = Subject()
    caluny_subject_280.code = 102
    caluny_subject_280.title = u'Fundamentos F\xedsicos de la Inform\xe1tica'
    caluny_subject_280.description = None
    caluny_subject_280.level = None
    caluny_subject_280.degree = caluny_degree_6
    caluny_subject_280 = importer.save_or_locate(caluny_subject_280)

    caluny_subject_281 = Subject()
    caluny_subject_281.code = 103
    caluny_subject_281.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_281.description = None
    caluny_subject_281.level = None
    caluny_subject_281.degree = caluny_degree_6
    caluny_subject_281 = importer.save_or_locate(caluny_subject_281)

    caluny_subject_282 = Subject()
    caluny_subject_282.code = 101
    caluny_subject_282.title = u'C\xe1lculo para la Computaci\xf3n'
    caluny_subject_282.description = None
    caluny_subject_282.level = None
    caluny_subject_282.degree = caluny_degree_6
    caluny_subject_282 = importer.save_or_locate(caluny_subject_282)

    caluny_subject_283 = Subject()
    caluny_subject_283.code = 106
    caluny_subject_283.title = u'Estructuras Algebraicas para la Computaci\xf3n'
    caluny_subject_283.description = None
    caluny_subject_283.level = None
    caluny_subject_283.degree = caluny_degree_6
    caluny_subject_283 = importer.save_or_locate(caluny_subject_283)

    caluny_subject_284 = Subject()
    caluny_subject_284.code = 107
    caluny_subject_284.title = u'M\xe9todos Estad\xedsticos para la Computaci\xf3n'
    caluny_subject_284.description = None
    caluny_subject_284.level = None
    caluny_subject_284.degree = caluny_degree_6
    caluny_subject_284 = importer.save_or_locate(caluny_subject_284)

    caluny_subject_285 = Subject()
    caluny_subject_285.code = 104
    caluny_subject_285.title = u'Fundamentos de la Programaci\xf3n'
    caluny_subject_285.description = None
    caluny_subject_285.level = None
    caluny_subject_285.degree = caluny_degree_6
    caluny_subject_285 = importer.save_or_locate(caluny_subject_285)

    caluny_subject_286 = Subject()
    caluny_subject_286.code = 105
    caluny_subject_286.title = u'Matem\xe1tica Discreta'
    caluny_subject_286.description = None
    caluny_subject_286.level = None
    caluny_subject_286.degree = caluny_degree_6
    caluny_subject_286 = importer.save_or_locate(caluny_subject_286)

    caluny_subject_287 = Subject()
    caluny_subject_287.code = 210
    caluny_subject_287.title = u'Ampliaci\xf3n de F\xedsica'
    caluny_subject_287.description = None
    caluny_subject_287.level = None
    caluny_subject_287.degree = caluny_degree_7
    caluny_subject_287 = importer.save_or_locate(caluny_subject_287)

    caluny_subject_288 = Subject()
    caluny_subject_288.code = 211
    caluny_subject_288.title = u'Sistemas Inform\xe1ticos'
    caluny_subject_288.description = None
    caluny_subject_288.level = None
    caluny_subject_288.degree = caluny_degree_7
    caluny_subject_288 = importer.save_or_locate(caluny_subject_288)

    caluny_subject_289 = Subject()
    caluny_subject_289.code = 407
    caluny_subject_289.title = u'Oficina T\xe9cnica'
    caluny_subject_289.description = None
    caluny_subject_289.level = None
    caluny_subject_289.degree = caluny_degree_7
    caluny_subject_289 = importer.save_or_locate(caluny_subject_289)

    caluny_subject_290 = Subject()
    caluny_subject_290.code = 406
    caluny_subject_290.title = u'M\xe1quinas El\xe9ctricas 2'
    caluny_subject_290.description = None
    caluny_subject_290.level = None
    caluny_subject_290.degree = caluny_degree_7
    caluny_subject_290 = importer.save_or_locate(caluny_subject_290)

    caluny_subject_291 = Subject()
    caluny_subject_291.code = 405
    caluny_subject_291.title = u'Instalaciones El\xe9ctricas en Baja y Media Tensi\xf3n'
    caluny_subject_291.description = None
    caluny_subject_291.level = None
    caluny_subject_291.degree = caluny_degree_7
    caluny_subject_291 = importer.save_or_locate(caluny_subject_291)

    caluny_subject_292 = Subject()
    caluny_subject_292.code = 404
    caluny_subject_292.title = u'M\xe1quinas El\xe9ctricas 1'
    caluny_subject_292.description = None
    caluny_subject_292.level = None
    caluny_subject_292.degree = caluny_degree_7
    caluny_subject_292 = importer.save_or_locate(caluny_subject_292)

    caluny_subject_293 = Subject()
    caluny_subject_293.code = 403
    caluny_subject_293.title = u'Motores T\xe9rmicos'
    caluny_subject_293.description = None
    caluny_subject_293.level = None
    caluny_subject_293.degree = caluny_degree_7
    caluny_subject_293 = importer.save_or_locate(caluny_subject_293)

    caluny_subject_294 = Subject()
    caluny_subject_294.code = 402
    caluny_subject_294.title = u'Electr\xf3nica de Potencia'
    caluny_subject_294.description = None
    caluny_subject_294.level = None
    caluny_subject_294.degree = caluny_degree_7
    caluny_subject_294 = importer.save_or_locate(caluny_subject_294)

    caluny_subject_295 = Subject()
    caluny_subject_295.code = 401
    caluny_subject_295.title = u'Circuitos Integrados'
    caluny_subject_295.description = None
    caluny_subject_295.level = None
    caluny_subject_295.degree = caluny_degree_7
    caluny_subject_295 = importer.save_or_locate(caluny_subject_295)

    caluny_subject_296 = Subject()
    caluny_subject_296.code = 509
    caluny_subject_296.title = u'Trabajo Fin de Grado (Ingenier\xeda El\xe9ctrica)'
    caluny_subject_296.description = None
    caluny_subject_296.level = None
    caluny_subject_296.degree = caluny_degree_7
    caluny_subject_296 = importer.save_or_locate(caluny_subject_296)

    caluny_subject_297 = Subject()
    caluny_subject_297.code = 506
    caluny_subject_297.title = u'Dise\xf1o de Controladores Industriales'
    caluny_subject_297.description = None
    caluny_subject_297.level = None
    caluny_subject_297.degree = caluny_degree_7
    caluny_subject_297 = importer.save_or_locate(caluny_subject_297)

    caluny_subject_298 = Subject()
    caluny_subject_298.code = 507
    caluny_subject_298.title = u'Explotaci\xf3n de los Sistemas de Energ\xeda El\xe9ctrica'
    caluny_subject_298.description = None
    caluny_subject_298.level = None
    caluny_subject_298.degree = caluny_degree_7
    caluny_subject_298 = importer.save_or_locate(caluny_subject_298)

    caluny_subject_299 = Subject()
    caluny_subject_299.code = 504
    caluny_subject_299.title = u'Instrumentaci\xf3n Electr\xf3nica'
    caluny_subject_299.description = None
    caluny_subject_299.level = None
    caluny_subject_299.degree = caluny_degree_7
    caluny_subject_299 = importer.save_or_locate(caluny_subject_299)

    caluny_subject_300 = Subject()
    caluny_subject_300.code = 505
    caluny_subject_300.title = u'An\xe1lisis de Sistemas de Energ\xeda El\xe9ctrica'
    caluny_subject_300.description = None
    caluny_subject_300.level = None
    caluny_subject_300.degree = caluny_degree_7
    caluny_subject_300 = importer.save_or_locate(caluny_subject_300)

    caluny_subject_301 = Subject()
    caluny_subject_301.code = 502
    caluny_subject_301.title = u'Centrales El\xe9ctricas'
    caluny_subject_301.description = None
    caluny_subject_301.level = None
    caluny_subject_301.degree = caluny_degree_7
    caluny_subject_301 = importer.save_or_locate(caluny_subject_301)

    caluny_subject_302 = Subject()
    caluny_subject_302.code = 503
    caluny_subject_302.title = u'Instalaciones y L\xedneas El\xe9ctricas de Alta Tensi\xf3n'
    caluny_subject_302.description = None
    caluny_subject_302.level = None
    caluny_subject_302.degree = caluny_degree_7
    caluny_subject_302 = importer.save_or_locate(caluny_subject_302)

    caluny_subject_303 = Subject()
    caluny_subject_303.code = 409
    caluny_subject_303.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_303.description = None
    caluny_subject_303.level = None
    caluny_subject_303.degree = caluny_degree_7
    caluny_subject_303 = importer.save_or_locate(caluny_subject_303)

    caluny_subject_304 = Subject()
    caluny_subject_304.code = 408
    caluny_subject_304.title = u'Tecnolog\xeda Electr\xf3nica'
    caluny_subject_304.description = None
    caluny_subject_304.level = None
    caluny_subject_304.degree = caluny_degree_7
    caluny_subject_304 = importer.save_or_locate(caluny_subject_304)

    caluny_subject_305 = Subject()
    caluny_subject_305.code = 508
    caluny_subject_305.title = u'Trabajo Fin de Grado'
    caluny_subject_305.description = None
    caluny_subject_305.level = None
    caluny_subject_305.degree = caluny_degree_7
    caluny_subject_305 = importer.save_or_locate(caluny_subject_305)

    caluny_subject_306 = Subject()
    caluny_subject_306.code = 410
    caluny_subject_306.title = u'Programaci\xf3n de Robots Industriales'
    caluny_subject_306.description = None
    caluny_subject_306.level = None
    caluny_subject_306.degree = caluny_degree_7
    caluny_subject_306 = importer.save_or_locate(caluny_subject_306)

    caluny_subject_307 = Subject()
    caluny_subject_307.code = 411
    caluny_subject_307.title = u'Equipos Electr\xf3nicos de Medida'
    caluny_subject_307.description = None
    caluny_subject_307.level = None
    caluny_subject_307.degree = caluny_degree_7
    caluny_subject_307 = importer.save_or_locate(caluny_subject_307)

    caluny_subject_308 = Subject()
    caluny_subject_308.code = 412
    caluny_subject_308.title = u'Seguridad y Salud Laboral'
    caluny_subject_308.description = None
    caluny_subject_308.level = None
    caluny_subject_308.degree = caluny_degree_7
    caluny_subject_308 = importer.save_or_locate(caluny_subject_308)

    caluny_subject_309 = Subject()
    caluny_subject_309.code = 501
    caluny_subject_309.title = u'Accionamientos El\xe9ctricos'
    caluny_subject_309.description = None
    caluny_subject_309.level = None
    caluny_subject_309.degree = caluny_degree_7
    caluny_subject_309 = importer.save_or_locate(caluny_subject_309)

    caluny_subject_310 = Subject()
    caluny_subject_310.code = 308
    caluny_subject_310.title = u'Sistemas Electr\xf3nicos Digitales'
    caluny_subject_310.description = None
    caluny_subject_310.level = None
    caluny_subject_310.degree = caluny_degree_7
    caluny_subject_310 = importer.save_or_locate(caluny_subject_310)

    caluny_subject_311 = Subject()
    caluny_subject_311.code = 312
    caluny_subject_311.title = u'Mantenimiento Industrial'
    caluny_subject_311.description = None
    caluny_subject_311.level = None
    caluny_subject_311.degree = caluny_degree_7
    caluny_subject_311 = importer.save_or_locate(caluny_subject_311)

    caluny_subject_312 = Subject()
    caluny_subject_312.code = 311
    caluny_subject_312.title = u'Ingl\xe9s aplicado a la Ingenier\xeda Electr\xf3nica'
    caluny_subject_312.description = None
    caluny_subject_312.level = None
    caluny_subject_312.degree = caluny_degree_7
    caluny_subject_312 = importer.save_or_locate(caluny_subject_312)

    caluny_subject_313 = Subject()
    caluny_subject_313.code = 310
    caluny_subject_313.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_313.description = None
    caluny_subject_313.level = None
    caluny_subject_313.degree = caluny_degree_7
    caluny_subject_313 = importer.save_or_locate(caluny_subject_313)

    caluny_subject_314 = Subject()
    caluny_subject_314.code = 110
    caluny_subject_314.title = u'Qu\xedmica'
    caluny_subject_314.description = None
    caluny_subject_314.level = None
    caluny_subject_314.degree = caluny_degree_7
    caluny_subject_314 = importer.save_or_locate(caluny_subject_314)

    caluny_subject_315 = Subject()
    caluny_subject_315.code = 301
    caluny_subject_315.title = u'An\xe1lisis de Redes El\xe9ctricas'
    caluny_subject_315.description = None
    caluny_subject_315.level = None
    caluny_subject_315.degree = caluny_degree_7
    caluny_subject_315 = importer.save_or_locate(caluny_subject_315)

    caluny_subject_316 = Subject()
    caluny_subject_316.code = 201
    caluny_subject_316.title = u'Ingenier\xeda de Fabricaci\xf3n'
    caluny_subject_316.description = None
    caluny_subject_316.level = None
    caluny_subject_316.degree = caluny_degree_7
    caluny_subject_316 = importer.save_or_locate(caluny_subject_316)

    caluny_subject_317 = Subject()
    caluny_subject_317.code = 309
    caluny_subject_317.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_317.description = None
    caluny_subject_317.level = None
    caluny_subject_317.degree = caluny_degree_7
    caluny_subject_317 = importer.save_or_locate(caluny_subject_317)

    caluny_subject_318 = Subject()
    caluny_subject_318.code = 203
    caluny_subject_318.title = u'Teor\xeda de M\xe1quinas'
    caluny_subject_318.description = None
    caluny_subject_318.level = None
    caluny_subject_318.degree = caluny_degree_7
    caluny_subject_318 = importer.save_or_locate(caluny_subject_318)

    caluny_subject_319 = Subject()
    caluny_subject_319.code = 202
    caluny_subject_319.title = u'Resistencia de Materiales'
    caluny_subject_319.description = None
    caluny_subject_319.level = None
    caluny_subject_319.degree = caluny_degree_7
    caluny_subject_319 = importer.save_or_locate(caluny_subject_319)

    caluny_subject_320 = Subject()
    caluny_subject_320.code = 205
    caluny_subject_320.title = u'Autom\xe1tica'
    caluny_subject_320.description = None
    caluny_subject_320.level = None
    caluny_subject_320.degree = caluny_degree_7
    caluny_subject_320 = importer.save_or_locate(caluny_subject_320)

    caluny_subject_321 = Subject()
    caluny_subject_321.code = 204
    caluny_subject_321.title = u'Termotecnia'
    caluny_subject_321.description = None
    caluny_subject_321.level = None
    caluny_subject_321.degree = caluny_degree_7
    caluny_subject_321 = importer.save_or_locate(caluny_subject_321)

    caluny_subject_322 = Subject()
    caluny_subject_322.code = 207
    caluny_subject_322.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_322.description = None
    caluny_subject_322.level = None
    caluny_subject_322.degree = caluny_degree_7
    caluny_subject_322 = importer.save_or_locate(caluny_subject_322)

    caluny_subject_323 = Subject()
    caluny_subject_323.code = 206
    caluny_subject_323.title = u'Ciencia de los Materiales'
    caluny_subject_323.description = None
    caluny_subject_323.level = None
    caluny_subject_323.degree = caluny_degree_7
    caluny_subject_323 = importer.save_or_locate(caluny_subject_323)

    caluny_subject_324 = Subject()
    caluny_subject_324.code = 209
    caluny_subject_324.title = u'Mec\xe1nica de Fluidos'
    caluny_subject_324.description = None
    caluny_subject_324.level = None
    caluny_subject_324.degree = caluny_degree_7
    caluny_subject_324 = importer.save_or_locate(caluny_subject_324)

    caluny_subject_325 = Subject()
    caluny_subject_325.code = 208
    caluny_subject_325.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_325.description = None
    caluny_subject_325.level = None
    caluny_subject_325.degree = caluny_degree_7
    caluny_subject_325 = importer.save_or_locate(caluny_subject_325)

    caluny_subject_326 = Subject()
    caluny_subject_326.code = 302
    caluny_subject_326.title = u'Electr\xf3nica Anal\xf3gica'
    caluny_subject_326.description = None
    caluny_subject_326.level = None
    caluny_subject_326.degree = caluny_degree_7
    caluny_subject_326 = importer.save_or_locate(caluny_subject_326)

    caluny_subject_327 = Subject()
    caluny_subject_327.code = 303
    caluny_subject_327.title = u'Electr\xf3nica Digital'
    caluny_subject_327.description = None
    caluny_subject_327.level = None
    caluny_subject_327.degree = caluny_degree_7
    caluny_subject_327 = importer.save_or_locate(caluny_subject_327)

    caluny_subject_328 = Subject()
    caluny_subject_328.code = 304
    caluny_subject_328.title = u'Regulaci\xf3n Autom\xe1tica'
    caluny_subject_328.description = None
    caluny_subject_328.level = None
    caluny_subject_328.degree = caluny_degree_7
    caluny_subject_328 = importer.save_or_locate(caluny_subject_328)

    caluny_subject_329 = Subject()
    caluny_subject_329.code = 305
    caluny_subject_329.title = u'Automatizaci\xf3n Industrial'
    caluny_subject_329.description = None
    caluny_subject_329.level = None
    caluny_subject_329.degree = caluny_degree_7
    caluny_subject_329 = importer.save_or_locate(caluny_subject_329)

    caluny_subject_330 = Subject()
    caluny_subject_330.code = 306
    caluny_subject_330.title = u'Inform\xe1tica Industrial'
    caluny_subject_330.description = None
    caluny_subject_330.level = None
    caluny_subject_330.degree = caluny_degree_7
    caluny_subject_330 = importer.save_or_locate(caluny_subject_330)

    caluny_subject_331 = Subject()
    caluny_subject_331.code = 307
    caluny_subject_331.title = u'Ingenier\xeda Gr\xe1fica El\xe9ctrica y Topograf\xeda'
    caluny_subject_331.description = None
    caluny_subject_331.level = None
    caluny_subject_331.degree = caluny_degree_7
    caluny_subject_331 = importer.save_or_locate(caluny_subject_331)

    caluny_subject_332 = Subject()
    caluny_subject_332.code = 108
    caluny_subject_332.title = u'F\xedsica 2'
    caluny_subject_332.description = None
    caluny_subject_332.level = None
    caluny_subject_332.degree = caluny_degree_7
    caluny_subject_332 = importer.save_or_locate(caluny_subject_332)

    caluny_subject_333 = Subject()
    caluny_subject_333.code = 109
    caluny_subject_333.title = u'Gesti\xf3n de Empresas'
    caluny_subject_333.description = None
    caluny_subject_333.level = None
    caluny_subject_333.degree = caluny_degree_7
    caluny_subject_333 = importer.save_or_locate(caluny_subject_333)

    caluny_subject_334 = Subject()
    caluny_subject_334.code = 102
    caluny_subject_334.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_334.description = None
    caluny_subject_334.level = None
    caluny_subject_334.degree = caluny_degree_7
    caluny_subject_334 = importer.save_or_locate(caluny_subject_334)

    caluny_subject_335 = Subject()
    caluny_subject_335.code = 103
    caluny_subject_335.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_335.description = None
    caluny_subject_335.level = None
    caluny_subject_335.degree = caluny_degree_7
    caluny_subject_335 = importer.save_or_locate(caluny_subject_335)

    caluny_subject_336 = Subject()
    caluny_subject_336.code = 101
    caluny_subject_336.title = u'C\xe1lculo'
    caluny_subject_336.description = None
    caluny_subject_336.level = None
    caluny_subject_336.degree = caluny_degree_7
    caluny_subject_336 = importer.save_or_locate(caluny_subject_336)

    caluny_subject_337 = Subject()
    caluny_subject_337.code = 106
    caluny_subject_337.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_337.description = None
    caluny_subject_337.level = None
    caluny_subject_337.degree = caluny_degree_7
    caluny_subject_337 = importer.save_or_locate(caluny_subject_337)

    caluny_subject_338 = Subject()
    caluny_subject_338.code = 107
    caluny_subject_338.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_338.description = None
    caluny_subject_338.level = None
    caluny_subject_338.degree = caluny_degree_7
    caluny_subject_338 = importer.save_or_locate(caluny_subject_338)

    caluny_subject_339 = Subject()
    caluny_subject_339.code = 104
    caluny_subject_339.title = u'F\xedsica 1'
    caluny_subject_339.description = None
    caluny_subject_339.level = None
    caluny_subject_339.degree = caluny_degree_7
    caluny_subject_339 = importer.save_or_locate(caluny_subject_339)

    caluny_subject_340 = Subject()
    caluny_subject_340.code = 105
    caluny_subject_340.title = u'\xc1lgebra Lineal'
    caluny_subject_340.description = None
    caluny_subject_340.level = None
    caluny_subject_340.degree = caluny_degree_7
    caluny_subject_340 = importer.save_or_locate(caluny_subject_340)

    caluny_subject_341 = Subject()
    caluny_subject_341.code = 210
    caluny_subject_341.title = u'Ampliaci\xf3n de F\xedsica'
    caluny_subject_341.description = None
    caluny_subject_341.level = None
    caluny_subject_341.degree = caluny_degree_8
    caluny_subject_341 = importer.save_or_locate(caluny_subject_341)

    caluny_subject_342 = Subject()
    caluny_subject_342.code = 211
    caluny_subject_342.title = u'Sistemas Inform\xe1ticos'
    caluny_subject_342.description = None
    caluny_subject_342.level = None
    caluny_subject_342.degree = caluny_degree_8
    caluny_subject_342 = importer.save_or_locate(caluny_subject_342)

    caluny_subject_343 = Subject()
    caluny_subject_343.code = 407
    caluny_subject_343.title = u'Instalaciones El\xe9ctricas en Baja y Media Tensi\xf3n'
    caluny_subject_343.description = None
    caluny_subject_343.level = None
    caluny_subject_343.degree = caluny_degree_8
    caluny_subject_343 = importer.save_or_locate(caluny_subject_343)

    caluny_subject_344 = Subject()
    caluny_subject_344.code = 406
    caluny_subject_344.title = u'Dise\xf1o Mec\xe1nico Asistido por Ordenador'
    caluny_subject_344.description = None
    caluny_subject_344.level = None
    caluny_subject_344.degree = caluny_degree_8
    caluny_subject_344 = importer.save_or_locate(caluny_subject_344)

    caluny_subject_345 = Subject()
    caluny_subject_345.code = 405
    caluny_subject_345.title = u'C\xe1lculo y Dise\xf1o de M\xe1quinas'
    caluny_subject_345.description = None
    caluny_subject_345.level = None
    caluny_subject_345.degree = caluny_degree_8
    caluny_subject_345 = importer.save_or_locate(caluny_subject_345)

    caluny_subject_346 = Subject()
    caluny_subject_346.code = 404
    caluny_subject_346.title = u'Tecnolog\xeda de Fabricaci\xf3n'
    caluny_subject_346.description = None
    caluny_subject_346.level = None
    caluny_subject_346.degree = caluny_degree_8
    caluny_subject_346 = importer.save_or_locate(caluny_subject_346)

    caluny_subject_347 = Subject()
    caluny_subject_347.code = 403
    caluny_subject_347.title = u'Estructuras de Hormig\xf3n'
    caluny_subject_347.description = None
    caluny_subject_347.level = None
    caluny_subject_347.degree = caluny_degree_8
    caluny_subject_347 = importer.save_or_locate(caluny_subject_347)

    caluny_subject_348 = Subject()
    caluny_subject_348.code = 402
    caluny_subject_348.title = u'An\xe1lisis de Redes El\xe9ctricas'
    caluny_subject_348.description = None
    caluny_subject_348.level = None
    caluny_subject_348.degree = caluny_degree_8
    caluny_subject_348 = importer.save_or_locate(caluny_subject_348)

    caluny_subject_349 = Subject()
    caluny_subject_349.code = 401
    caluny_subject_349.title = u'Accionamientos El\xe9ctricos'
    caluny_subject_349.description = None
    caluny_subject_349.level = None
    caluny_subject_349.degree = caluny_degree_8
    caluny_subject_349 = importer.save_or_locate(caluny_subject_349)

    caluny_subject_350 = Subject()
    caluny_subject_350.code = 509
    caluny_subject_350.title = u'Trabajo Fin de Grado (Ingenier\xeda Mec\xe1nica)'
    caluny_subject_350.description = None
    caluny_subject_350.level = None
    caluny_subject_350.degree = caluny_degree_8
    caluny_subject_350 = importer.save_or_locate(caluny_subject_350)

    caluny_subject_351 = Subject()
    caluny_subject_351.code = 506
    caluny_subject_351.title = u'Explotaci\xf3n de los Sistemas de Energ\xeda El\xe9ctrica'
    caluny_subject_351.description = None
    caluny_subject_351.level = None
    caluny_subject_351.degree = caluny_degree_8
    caluny_subject_351 = importer.save_or_locate(caluny_subject_351)

    caluny_subject_352 = Subject()
    caluny_subject_352.code = 507
    caluny_subject_352.title = u'Mec\xe1nica Experimental y T\xe9cnicas de Simulaci\xf3n de M\xe1quinas'
    caluny_subject_352.description = None
    caluny_subject_352.level = None
    caluny_subject_352.degree = caluny_degree_8
    caluny_subject_352 = importer.save_or_locate(caluny_subject_352)

    caluny_subject_353 = Subject()
    caluny_subject_353.code = 504
    caluny_subject_353.title = u'Oficina T\xe9cnica'
    caluny_subject_353.description = None
    caluny_subject_353.level = None
    caluny_subject_353.degree = caluny_degree_8
    caluny_subject_353 = importer.save_or_locate(caluny_subject_353)

    caluny_subject_354 = Subject()
    caluny_subject_354.code = 505
    caluny_subject_354.title = u'An\xe1lisis de Sistemas de Energ\xeda El\xe9ctrica'
    caluny_subject_354.description = None
    caluny_subject_354.level = None
    caluny_subject_354.degree = caluny_degree_8
    caluny_subject_354 = importer.save_or_locate(caluny_subject_354)

    caluny_subject_355 = Subject()
    caluny_subject_355.code = 502
    caluny_subject_355.title = u'Instalaciones y L\xedneas El\xe9ctricas de Alta Tensi\xf3n'
    caluny_subject_355.description = None
    caluny_subject_355.level = None
    caluny_subject_355.degree = caluny_degree_8
    caluny_subject_355 = importer.save_or_locate(caluny_subject_355)

    caluny_subject_356 = Subject()
    caluny_subject_356.code = 503
    caluny_subject_356.title = u'Metrolog\xeda y Calidad'
    caluny_subject_356.description = None
    caluny_subject_356.level = None
    caluny_subject_356.degree = caluny_degree_8
    caluny_subject_356 = importer.save_or_locate(caluny_subject_356)

    caluny_subject_357 = Subject()
    caluny_subject_357.code = 409
    caluny_subject_357.title = u'Mantenimiento Industrial'
    caluny_subject_357.description = None
    caluny_subject_357.level = None
    caluny_subject_357.degree = caluny_degree_8
    caluny_subject_357 = importer.save_or_locate(caluny_subject_357)

    caluny_subject_358 = Subject()
    caluny_subject_358.code = 408
    caluny_subject_358.title = u'M\xe1quinas Fluidomec\xe1nicas'
    caluny_subject_358.description = None
    caluny_subject_358.level = None
    caluny_subject_358.degree = caluny_degree_8
    caluny_subject_358 = importer.save_or_locate(caluny_subject_358)

    caluny_subject_359 = Subject()
    caluny_subject_359.code = 508
    caluny_subject_359.title = u'Trabajo Fin de Grado (Ingenier\xeda El\xe9ctrica)'
    caluny_subject_359.description = None
    caluny_subject_359.level = None
    caluny_subject_359.degree = caluny_degree_8
    caluny_subject_359 = importer.save_or_locate(caluny_subject_359)

    caluny_subject_360 = Subject()
    caluny_subject_360.code = 410
    caluny_subject_360.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_360.description = None
    caluny_subject_360.level = None
    caluny_subject_360.degree = caluny_degree_8
    caluny_subject_360 = importer.save_or_locate(caluny_subject_360)

    caluny_subject_361 = Subject()
    caluny_subject_361.code = 411
    caluny_subject_361.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_361.description = None
    caluny_subject_361.level = None
    caluny_subject_361.degree = caluny_degree_8
    caluny_subject_361 = importer.save_or_locate(caluny_subject_361)

    caluny_subject_362 = Subject()
    caluny_subject_362.code = 412
    caluny_subject_362.title = u'Equipos Electr\xf3nicos de Medida'
    caluny_subject_362.description = None
    caluny_subject_362.level = None
    caluny_subject_362.degree = caluny_degree_8
    caluny_subject_362 = importer.save_or_locate(caluny_subject_362)

    caluny_subject_363 = Subject()
    caluny_subject_363.code = 501
    caluny_subject_363.title = u'Centrales El\xe9ctricas'
    caluny_subject_363.description = None
    caluny_subject_363.level = None
    caluny_subject_363.degree = caluny_degree_8
    caluny_subject_363 = importer.save_or_locate(caluny_subject_363)

    caluny_subject_364 = Subject()
    caluny_subject_364.code = 308
    caluny_subject_364.title = u'M\xe1quinas El\xe9ctricas 2'
    caluny_subject_364.description = None
    caluny_subject_364.level = None
    caluny_subject_364.degree = caluny_degree_8
    caluny_subject_364 = importer.save_or_locate(caluny_subject_364)

    caluny_subject_365 = Subject()
    caluny_subject_365.code = 311
    caluny_subject_365.title = u'Seguridad y Salud Laboral'
    caluny_subject_365.description = None
    caluny_subject_365.level = None
    caluny_subject_365.degree = caluny_degree_8
    caluny_subject_365 = importer.save_or_locate(caluny_subject_365)

    caluny_subject_366 = Subject()
    caluny_subject_366.code = 310
    caluny_subject_366.title = u'Programaci\xf3n de Robots Industriales'
    caluny_subject_366.description = None
    caluny_subject_366.level = None
    caluny_subject_366.degree = caluny_degree_8
    caluny_subject_366 = importer.save_or_locate(caluny_subject_366)

    caluny_subject_367 = Subject()
    caluny_subject_367.code = 110
    caluny_subject_367.title = u'Qu\xedmica'
    caluny_subject_367.description = None
    caluny_subject_367.level = None
    caluny_subject_367.degree = caluny_degree_8
    caluny_subject_367 = importer.save_or_locate(caluny_subject_367)

    caluny_subject_368 = Subject()
    caluny_subject_368.code = 301
    caluny_subject_368.title = u'Ingenier\xeda T\xe9rmica'
    caluny_subject_368.description = None
    caluny_subject_368.level = None
    caluny_subject_368.degree = caluny_degree_8
    caluny_subject_368 = importer.save_or_locate(caluny_subject_368)

    caluny_subject_369 = Subject()
    caluny_subject_369.code = 201
    caluny_subject_369.title = u'Ingenier\xeda de Fabricaci\xf3n'
    caluny_subject_369.description = None
    caluny_subject_369.level = None
    caluny_subject_369.degree = caluny_degree_8
    caluny_subject_369 = importer.save_or_locate(caluny_subject_369)

    caluny_subject_370 = Subject()
    caluny_subject_370.code = 309
    caluny_subject_370.title = u'Tecnolog\xeda de Materiales'
    caluny_subject_370.description = None
    caluny_subject_370.level = None
    caluny_subject_370.degree = caluny_degree_8
    caluny_subject_370 = importer.save_or_locate(caluny_subject_370)

    caluny_subject_371 = Subject()
    caluny_subject_371.code = 203
    caluny_subject_371.title = u'Teor\xeda de M\xe1quinas'
    caluny_subject_371.description = None
    caluny_subject_371.level = None
    caluny_subject_371.degree = caluny_degree_8
    caluny_subject_371 = importer.save_or_locate(caluny_subject_371)

    caluny_subject_372 = Subject()
    caluny_subject_372.code = 202
    caluny_subject_372.title = u'Resistencia de Materiales'
    caluny_subject_372.description = None
    caluny_subject_372.level = None
    caluny_subject_372.degree = caluny_degree_8
    caluny_subject_372 = importer.save_or_locate(caluny_subject_372)

    caluny_subject_373 = Subject()
    caluny_subject_373.code = 205
    caluny_subject_373.title = u'Autom\xe1tica'
    caluny_subject_373.description = None
    caluny_subject_373.level = None
    caluny_subject_373.degree = caluny_degree_8
    caluny_subject_373 = importer.save_or_locate(caluny_subject_373)

    caluny_subject_374 = Subject()
    caluny_subject_374.code = 204
    caluny_subject_374.title = u'Termotecnia'
    caluny_subject_374.description = None
    caluny_subject_374.level = None
    caluny_subject_374.degree = caluny_degree_8
    caluny_subject_374 = importer.save_or_locate(caluny_subject_374)

    caluny_subject_375 = Subject()
    caluny_subject_375.code = 207
    caluny_subject_375.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_375.description = None
    caluny_subject_375.level = None
    caluny_subject_375.degree = caluny_degree_8
    caluny_subject_375 = importer.save_or_locate(caluny_subject_375)

    caluny_subject_376 = Subject()
    caluny_subject_376.code = 206
    caluny_subject_376.title = u'Ciencia de los Materiales'
    caluny_subject_376.description = None
    caluny_subject_376.level = None
    caluny_subject_376.degree = caluny_degree_8
    caluny_subject_376 = importer.save_or_locate(caluny_subject_376)

    caluny_subject_377 = Subject()
    caluny_subject_377.code = 209
    caluny_subject_377.title = u'Mec\xe1nica de Fluidos'
    caluny_subject_377.description = None
    caluny_subject_377.level = None
    caluny_subject_377.degree = caluny_degree_8
    caluny_subject_377 = importer.save_or_locate(caluny_subject_377)

    caluny_subject_378 = Subject()
    caluny_subject_378.code = 208
    caluny_subject_378.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_378.description = None
    caluny_subject_378.level = None
    caluny_subject_378.degree = caluny_degree_8
    caluny_subject_378 = importer.save_or_locate(caluny_subject_378)

    caluny_subject_379 = Subject()
    caluny_subject_379.code = 302
    caluny_subject_379.title = u'M\xe1quinas El\xe9ctricas 1'
    caluny_subject_379.description = None
    caluny_subject_379.level = None
    caluny_subject_379.degree = caluny_degree_8
    caluny_subject_379 = importer.save_or_locate(caluny_subject_379)

    caluny_subject_380 = Subject()
    caluny_subject_380.code = 303
    caluny_subject_380.title = u'Regulaci\xf3n Autom\xe1tica'
    caluny_subject_380.description = None
    caluny_subject_380.level = None
    caluny_subject_380.degree = caluny_degree_8
    caluny_subject_380 = importer.save_or_locate(caluny_subject_380)

    caluny_subject_381 = Subject()
    caluny_subject_381.code = 304
    caluny_subject_381.title = u'Teor\xeda de Estructuras y Construcciones Industriales'
    caluny_subject_381.description = None
    caluny_subject_381.level = None
    caluny_subject_381.degree = caluny_degree_8
    caluny_subject_381 = importer.save_or_locate(caluny_subject_381)

    caluny_subject_382 = Subject()
    caluny_subject_382.code = 305
    caluny_subject_382.title = u'Estructuras Met\xe1licas'
    caluny_subject_382.description = None
    caluny_subject_382.level = None
    caluny_subject_382.degree = caluny_degree_8
    caluny_subject_382 = importer.save_or_locate(caluny_subject_382)

    caluny_subject_383 = Subject()
    caluny_subject_383.code = 306
    caluny_subject_383.title = u'Ingenier\xeda Gr\xe1fica Mec\xe1nica y Topograf\xeda'
    caluny_subject_383.description = None
    caluny_subject_383.level = None
    caluny_subject_383.degree = caluny_degree_8
    caluny_subject_383 = importer.save_or_locate(caluny_subject_383)

    caluny_subject_384 = Subject()
    caluny_subject_384.code = 307
    caluny_subject_384.title = u'Motores T\xe9rmicos'
    caluny_subject_384.description = None
    caluny_subject_384.level = None
    caluny_subject_384.degree = caluny_degree_8
    caluny_subject_384 = importer.save_or_locate(caluny_subject_384)

    caluny_subject_385 = Subject()
    caluny_subject_385.code = 108
    caluny_subject_385.title = u'F\xedsica 2'
    caluny_subject_385.description = None
    caluny_subject_385.level = None
    caluny_subject_385.degree = caluny_degree_8
    caluny_subject_385 = importer.save_or_locate(caluny_subject_385)

    caluny_subject_386 = Subject()
    caluny_subject_386.code = 109
    caluny_subject_386.title = u'Gesti\xf3n de Empresas'
    caluny_subject_386.description = None
    caluny_subject_386.level = None
    caluny_subject_386.degree = caluny_degree_8
    caluny_subject_386 = importer.save_or_locate(caluny_subject_386)

    caluny_subject_387 = Subject()
    caluny_subject_387.code = 102
    caluny_subject_387.title = u'C\xe1lculo'
    caluny_subject_387.description = None
    caluny_subject_387.level = None
    caluny_subject_387.degree = caluny_degree_8
    caluny_subject_387 = importer.save_or_locate(caluny_subject_387)

    caluny_subject_388 = Subject()
    caluny_subject_388.code = 103
    caluny_subject_388.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_388.description = None
    caluny_subject_388.level = None
    caluny_subject_388.degree = caluny_degree_8
    caluny_subject_388 = importer.save_or_locate(caluny_subject_388)

    caluny_subject_389 = Subject()
    caluny_subject_389.code = 101
    caluny_subject_389.title = u'\xc1lgebra Lineal'
    caluny_subject_389.description = None
    caluny_subject_389.level = None
    caluny_subject_389.degree = caluny_degree_8
    caluny_subject_389 = importer.save_or_locate(caluny_subject_389)

    caluny_subject_390 = Subject()
    caluny_subject_390.code = 106
    caluny_subject_390.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_390.description = None
    caluny_subject_390.level = None
    caluny_subject_390.degree = caluny_degree_8
    caluny_subject_390 = importer.save_or_locate(caluny_subject_390)

    caluny_subject_391 = Subject()
    caluny_subject_391.code = 107
    caluny_subject_391.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_391.description = None
    caluny_subject_391.level = None
    caluny_subject_391.degree = caluny_degree_8
    caluny_subject_391 = importer.save_or_locate(caluny_subject_391)

    caluny_subject_392 = Subject()
    caluny_subject_392.code = 104
    caluny_subject_392.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_392.description = None
    caluny_subject_392.level = None
    caluny_subject_392.degree = caluny_degree_8
    caluny_subject_392 = importer.save_or_locate(caluny_subject_392)

    caluny_subject_393 = Subject()
    caluny_subject_393.code = 105
    caluny_subject_393.title = u'F\xedsica 1'
    caluny_subject_393.description = None
    caluny_subject_393.level = None
    caluny_subject_393.degree = caluny_degree_8
    caluny_subject_393 = importer.save_or_locate(caluny_subject_393)

    caluny_subject_394 = Subject()
    caluny_subject_394.code = 511
    caluny_subject_394.title = u'Ingl\xe9s aplicado a la ingenier\xeda el\xe9ctrica'
    caluny_subject_394.description = None
    caluny_subject_394.level = None
    caluny_subject_394.degree = caluny_degree_8
    caluny_subject_394 = importer.save_or_locate(caluny_subject_394)

    caluny_subject_395 = Subject()
    caluny_subject_395.code = 510
    caluny_subject_395.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_395.description = None
    caluny_subject_395.level = None
    caluny_subject_395.degree = caluny_degree_8
    caluny_subject_395 = importer.save_or_locate(caluny_subject_395)

    caluny_subject_396 = Subject()
    caluny_subject_396.code = 407
    caluny_subject_396.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_396.description = None
    caluny_subject_396.level = None
    caluny_subject_396.degree = caluny_degree_9
    caluny_subject_396 = importer.save_or_locate(caluny_subject_396)

    caluny_subject_397 = Subject()
    caluny_subject_397.code = 406
    caluny_subject_397.title = u'Tecnolog\xeda de Materiales'
    caluny_subject_397.description = None
    caluny_subject_397.level = None
    caluny_subject_397.degree = caluny_degree_9
    caluny_subject_397 = importer.save_or_locate(caluny_subject_397)

    caluny_subject_398 = Subject()
    caluny_subject_398.code = 405
    caluny_subject_398.title = u'Proyectos de Dise\xf1o Industrial'
    caluny_subject_398.description = None
    caluny_subject_398.level = None
    caluny_subject_398.degree = caluny_degree_9
    caluny_subject_398 = importer.save_or_locate(caluny_subject_398)

    caluny_subject_399 = Subject()
    caluny_subject_399.code = 404
    caluny_subject_399.title = u'Presentaci\xf3n Multimedia del Producto'
    caluny_subject_399.description = None
    caluny_subject_399.level = None
    caluny_subject_399.degree = caluny_degree_9
    caluny_subject_399 = importer.save_or_locate(caluny_subject_399)

    caluny_subject_400 = Subject()
    caluny_subject_400.code = 403
    caluny_subject_400.title = u'Ingenier\xeda Energ\xe9tica y Fluidomec\xe1nica'
    caluny_subject_400.description = None
    caluny_subject_400.level = None
    caluny_subject_400.degree = caluny_degree_9
    caluny_subject_400 = importer.save_or_locate(caluny_subject_400)

    caluny_subject_401 = Subject()
    caluny_subject_401.code = 402
    caluny_subject_401.title = u'Idioma moderno (Ingl\xe9s)'
    caluny_subject_401.description = None
    caluny_subject_401.level = None
    caluny_subject_401.degree = caluny_degree_9
    caluny_subject_401 = importer.save_or_locate(caluny_subject_401)

    caluny_subject_402 = Subject()
    caluny_subject_402.code = 401
    caluny_subject_402.title = u'Dise\xf1o Ergon\xf3mico y Ecodise\xf1o'
    caluny_subject_402.description = None
    caluny_subject_402.level = None
    caluny_subject_402.degree = caluny_degree_9
    caluny_subject_402 = importer.save_or_locate(caluny_subject_402)

    caluny_subject_403 = Subject()
    caluny_subject_403.code = 409
    caluny_subject_403.title = u'Dibujo y An\xe1lisis de Formas'
    caluny_subject_403.description = None
    caluny_subject_403.level = None
    caluny_subject_403.degree = caluny_degree_9
    caluny_subject_403 = importer.save_or_locate(caluny_subject_403)

    caluny_subject_404 = Subject()
    caluny_subject_404.code = 414
    caluny_subject_404.title = u'Trabajo Fin de Grado (Ingenier\xeda Dise\xf1o Ind. y D.P.)'
    caluny_subject_404.description = None
    caluny_subject_404.level = None
    caluny_subject_404.degree = caluny_degree_9
    caluny_subject_404 = importer.save_or_locate(caluny_subject_404)

    caluny_subject_405 = Subject()
    caluny_subject_405.code = 411
    caluny_subject_405.title = u'Eficiencia Energ\xe9tica en el Producto'
    caluny_subject_405.description = None
    caluny_subject_405.level = None
    caluny_subject_405.degree = caluny_degree_9
    caluny_subject_405 = importer.save_or_locate(caluny_subject_405)

    caluny_subject_406 = Subject()
    caluny_subject_406.code = 412
    caluny_subject_406.title = u'Envase y Embalaje'
    caluny_subject_406.description = None
    caluny_subject_406.level = None
    caluny_subject_406.degree = caluny_degree_9
    caluny_subject_406 = importer.save_or_locate(caluny_subject_406)

    caluny_subject_407 = Subject()
    caluny_subject_407.code = 413
    caluny_subject_407.title = u'Metrolog\xeda'
    caluny_subject_407.description = None
    caluny_subject_407.level = None
    caluny_subject_407.degree = caluny_degree_9
    caluny_subject_407 = importer.save_or_locate(caluny_subject_407)

    caluny_subject_408 = Subject()
    caluny_subject_408.code = 308
    caluny_subject_408.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_408.description = None
    caluny_subject_408.level = None
    caluny_subject_408.degree = caluny_degree_9
    caluny_subject_408 = importer.save_or_locate(caluny_subject_408)

    caluny_subject_409 = Subject()
    caluny_subject_409.code = 313
    caluny_subject_409.title = u'Proyectos de Dise\xf1o'
    caluny_subject_409.description = None
    caluny_subject_409.level = None
    caluny_subject_409.degree = caluny_degree_9
    caluny_subject_409 = importer.save_or_locate(caluny_subject_409)

    caluny_subject_410 = Subject()
    caluny_subject_410.code = 312
    caluny_subject_410.title = u'Modelado y Simulaci\xf3n de Sistemas Productivos'
    caluny_subject_410.description = None
    caluny_subject_410.level = None
    caluny_subject_410.degree = caluny_degree_9
    caluny_subject_410 = importer.save_or_locate(caluny_subject_410)

    caluny_subject_411 = Subject()
    caluny_subject_411.code = 311
    caluny_subject_411.title = u'Electr\xf3nica y Automatizaci\xf3n del Producto'
    caluny_subject_411.description = None
    caluny_subject_411.level = None
    caluny_subject_411.degree = caluny_degree_9
    caluny_subject_411 = importer.save_or_locate(caluny_subject_411)

    caluny_subject_412 = Subject()
    caluny_subject_412.code = 310
    caluny_subject_412.title = u'Dise\xf1o de Comunicaci\xf3n'
    caluny_subject_412.description = None
    caluny_subject_412.level = None
    caluny_subject_412.degree = caluny_degree_9
    caluny_subject_412 = importer.save_or_locate(caluny_subject_412)

    caluny_subject_413 = Subject()
    caluny_subject_413.code = 314
    caluny_subject_413.title = u'Tratamiento de Im\xe1genes y Fotograf\xeda Industrial'
    caluny_subject_413.description = None
    caluny_subject_413.level = None
    caluny_subject_413.degree = caluny_degree_9
    caluny_subject_413 = importer.save_or_locate(caluny_subject_413)

    caluny_subject_414 = Subject()
    caluny_subject_414.code = 110
    caluny_subject_414.title = u'Qu\xedmica'
    caluny_subject_414.description = None
    caluny_subject_414.level = None
    caluny_subject_414.degree = caluny_degree_9
    caluny_subject_414 = importer.save_or_locate(caluny_subject_414)

    caluny_subject_415 = Subject()
    caluny_subject_415.code = 301
    caluny_subject_415.title = u'Dise\xf1o Asistido por Ordenador'
    caluny_subject_415.description = None
    caluny_subject_415.level = None
    caluny_subject_415.degree = caluny_degree_9
    caluny_subject_415 = importer.save_or_locate(caluny_subject_415)

    caluny_subject_416 = Subject()
    caluny_subject_416.code = 201
    caluny_subject_416.title = u'Ciencia de los Materiales'
    caluny_subject_416.description = None
    caluny_subject_416.level = None
    caluny_subject_416.degree = caluny_degree_9
    caluny_subject_416 = importer.save_or_locate(caluny_subject_416)

    caluny_subject_417 = Subject()
    caluny_subject_417.code = 309
    caluny_subject_417.title = u'Desarrollo Hist\xf3rico - Culturales del Dise\xf1o Industrial'
    caluny_subject_417.description = None
    caluny_subject_417.level = None
    caluny_subject_417.degree = caluny_degree_9
    caluny_subject_417 = importer.save_or_locate(caluny_subject_417)

    caluny_subject_418 = Subject()
    caluny_subject_418.code = 203
    caluny_subject_418.title = u'Procesos Industriales'
    caluny_subject_418.description = None
    caluny_subject_418.level = None
    caluny_subject_418.degree = caluny_degree_9
    caluny_subject_418 = importer.save_or_locate(caluny_subject_418)

    caluny_subject_419 = Subject()
    caluny_subject_419.code = 202
    caluny_subject_419.title = u'Ingenier\xeda Gr\xe1fica del Producto'
    caluny_subject_419.description = None
    caluny_subject_419.level = None
    caluny_subject_419.degree = caluny_degree_9
    caluny_subject_419 = importer.save_or_locate(caluny_subject_419)

    caluny_subject_420 = Subject()
    caluny_subject_420.code = 205
    caluny_subject_420.title = u'Dibujo T\xe9cnico'
    caluny_subject_420.description = None
    caluny_subject_420.level = None
    caluny_subject_420.degree = caluny_degree_9
    caluny_subject_420 = importer.save_or_locate(caluny_subject_420)

    caluny_subject_421 = Subject()
    caluny_subject_421.code = 204
    caluny_subject_421.title = u'Resistencia de Materiales'
    caluny_subject_421.description = None
    caluny_subject_421.level = None
    caluny_subject_421.degree = caluny_degree_9
    caluny_subject_421 = importer.save_or_locate(caluny_subject_421)

    caluny_subject_422 = Subject()
    caluny_subject_422.code = 207
    caluny_subject_422.title = u'Fundamentos del Dise\xf1o'
    caluny_subject_422.description = None
    caluny_subject_422.level = None
    caluny_subject_422.degree = caluny_degree_9
    caluny_subject_422 = importer.save_or_locate(caluny_subject_422)

    caluny_subject_423 = Subject()
    caluny_subject_423.code = 206
    caluny_subject_423.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_423.description = None
    caluny_subject_423.level = None
    caluny_subject_423.degree = caluny_degree_9
    caluny_subject_423 = importer.save_or_locate(caluny_subject_423)

    caluny_subject_424 = Subject()
    caluny_subject_424.code = 209
    caluny_subject_424.title = u'Teor\xeda y Est\xe9tica del Dise\xf1o Industrial'
    caluny_subject_424.description = None
    caluny_subject_424.level = None
    caluny_subject_424.degree = caluny_degree_9
    caluny_subject_424 = importer.save_or_locate(caluny_subject_424)

    caluny_subject_425 = Subject()
    caluny_subject_425.code = 208
    caluny_subject_425.title = u'Sistemas Mec\xe1nicos'
    caluny_subject_425.description = None
    caluny_subject_425.level = None
    caluny_subject_425.degree = caluny_degree_9
    caluny_subject_425 = importer.save_or_locate(caluny_subject_425)

    caluny_subject_426 = Subject()
    caluny_subject_426.code = 302
    caluny_subject_426.title = u'Dise\xf1o Gr\xe1fico Digital'
    caluny_subject_426.description = None
    caluny_subject_426.level = None
    caluny_subject_426.degree = caluny_degree_9
    caluny_subject_426 = importer.save_or_locate(caluny_subject_426)

    caluny_subject_427 = Subject()
    caluny_subject_427.code = 303
    caluny_subject_427.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_427.description = None
    caluny_subject_427.level = None
    caluny_subject_427.degree = caluny_degree_9
    caluny_subject_427 = importer.save_or_locate(caluny_subject_427)

    caluny_subject_428 = Subject()
    caluny_subject_428.code = 304
    caluny_subject_428.title = u'Ingl\xe9s Aplicado al Dise\xf1o Industrial'
    caluny_subject_428.description = None
    caluny_subject_428.level = None
    caluny_subject_428.degree = caluny_degree_9
    caluny_subject_428 = importer.save_or_locate(caluny_subject_428)

    caluny_subject_429 = Subject()
    caluny_subject_429.code = 305
    caluny_subject_429.title = u'Metodolog\xeda del Dise\xf1o'
    caluny_subject_429.description = None
    caluny_subject_429.level = None
    caluny_subject_429.degree = caluny_degree_9
    caluny_subject_429 = importer.save_or_locate(caluny_subject_429)

    caluny_subject_430 = Subject()
    caluny_subject_430.code = 306
    caluny_subject_430.title = u'Reciclaje y Medio Ambiente'
    caluny_subject_430.description = None
    caluny_subject_430.level = None
    caluny_subject_430.degree = caluny_degree_9
    caluny_subject_430 = importer.save_or_locate(caluny_subject_430)

    caluny_subject_431 = Subject()
    caluny_subject_431.code = 307
    caluny_subject_431.title = u'Seguridad y Salud Laboral'
    caluny_subject_431.description = None
    caluny_subject_431.level = None
    caluny_subject_431.degree = caluny_degree_9
    caluny_subject_431 = importer.save_or_locate(caluny_subject_431)

    caluny_subject_432 = Subject()
    caluny_subject_432.code = 108
    caluny_subject_432.title = u'F\xedsica 2'
    caluny_subject_432.description = None
    caluny_subject_432.level = None
    caluny_subject_432.degree = caluny_degree_9
    caluny_subject_432 = importer.save_or_locate(caluny_subject_432)

    caluny_subject_433 = Subject()
    caluny_subject_433.code = 109
    caluny_subject_433.title = u'Gesti\xf3n de Empresas'
    caluny_subject_433.description = None
    caluny_subject_433.level = None
    caluny_subject_433.degree = caluny_degree_9
    caluny_subject_433 = importer.save_or_locate(caluny_subject_433)

    caluny_subject_434 = Subject()
    caluny_subject_434.code = 102
    caluny_subject_434.title = u'C\xe1lculo'
    caluny_subject_434.description = None
    caluny_subject_434.level = None
    caluny_subject_434.degree = caluny_degree_9
    caluny_subject_434 = importer.save_or_locate(caluny_subject_434)

    caluny_subject_435 = Subject()
    caluny_subject_435.code = 103
    caluny_subject_435.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_435.description = None
    caluny_subject_435.level = None
    caluny_subject_435.degree = caluny_degree_9
    caluny_subject_435 = importer.save_or_locate(caluny_subject_435)

    caluny_subject_436 = Subject()
    caluny_subject_436.code = 101
    caluny_subject_436.title = u'\xc1lgebra Lineal'
    caluny_subject_436.description = None
    caluny_subject_436.level = None
    caluny_subject_436.degree = caluny_degree_9
    caluny_subject_436 = importer.save_or_locate(caluny_subject_436)

    caluny_subject_437 = Subject()
    caluny_subject_437.code = 106
    caluny_subject_437.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_437.description = None
    caluny_subject_437.level = None
    caluny_subject_437.degree = caluny_degree_9
    caluny_subject_437 = importer.save_or_locate(caluny_subject_437)

    caluny_subject_438 = Subject()
    caluny_subject_438.code = 107
    caluny_subject_438.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_438.description = None
    caluny_subject_438.level = None
    caluny_subject_438.degree = caluny_degree_9
    caluny_subject_438 = importer.save_or_locate(caluny_subject_438)

    caluny_subject_439 = Subject()
    caluny_subject_439.code = 104
    caluny_subject_439.title = u'F\xedsica 1'
    caluny_subject_439.description = None
    caluny_subject_439.level = None
    caluny_subject_439.degree = caluny_degree_9
    caluny_subject_439 = importer.save_or_locate(caluny_subject_439)

    caluny_subject_440 = Subject()
    caluny_subject_440.code = 105
    caluny_subject_440.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_440.description = None
    caluny_subject_440.level = None
    caluny_subject_440.degree = caluny_degree_9
    caluny_subject_440 = importer.save_or_locate(caluny_subject_440)

    caluny_subject_441 = Subject()
    caluny_subject_441.code = 212
    caluny_subject_441.title = u'Mec\xe1nica de Fluidos'
    caluny_subject_441.description = None
    caluny_subject_441.level = None
    caluny_subject_441.degree = caluny_degree_10
    caluny_subject_441 = importer.save_or_locate(caluny_subject_441)

    caluny_subject_442 = Subject()
    caluny_subject_442.code = 210
    caluny_subject_442.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_442.description = None
    caluny_subject_442.level = None
    caluny_subject_442.degree = caluny_degree_10
    caluny_subject_442 = importer.save_or_locate(caluny_subject_442)

    caluny_subject_443 = Subject()
    caluny_subject_443.code = 211
    caluny_subject_443.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_443.description = None
    caluny_subject_443.level = None
    caluny_subject_443.degree = caluny_degree_10
    caluny_subject_443 = importer.save_or_locate(caluny_subject_443)

    caluny_subject_444 = Subject()
    caluny_subject_444.code = 407
    caluny_subject_444.title = u'Sistemas Digitales Avanzados'
    caluny_subject_444.description = None
    caluny_subject_444.level = None
    caluny_subject_444.degree = caluny_degree_10
    caluny_subject_444 = importer.save_or_locate(caluny_subject_444)

    caluny_subject_445 = Subject()
    caluny_subject_445.code = 406
    caluny_subject_445.title = u'Oficina T\xe9cnica'
    caluny_subject_445.description = None
    caluny_subject_445.level = None
    caluny_subject_445.degree = caluny_degree_10
    caluny_subject_445 = importer.save_or_locate(caluny_subject_445)

    caluny_subject_446 = Subject()
    caluny_subject_446.code = 405
    caluny_subject_446.title = u'Instrumentaci\xf3n Electr\xf3nica'
    caluny_subject_446.description = None
    caluny_subject_446.level = None
    caluny_subject_446.degree = caluny_degree_10
    caluny_subject_446 = importer.save_or_locate(caluny_subject_446)

    caluny_subject_447 = Subject()
    caluny_subject_447.code = 404
    caluny_subject_447.title = u'Instalaciones y M\xe1quinas El\xe9ctricas'
    caluny_subject_447.description = None
    caluny_subject_447.level = None
    caluny_subject_447.degree = caluny_degree_10
    caluny_subject_447 = importer.save_or_locate(caluny_subject_447)

    caluny_subject_448 = Subject()
    caluny_subject_448.code = 403
    caluny_subject_448.title = u'Ingenier\xeda de Equipos Electr\xf3nicos'
    caluny_subject_448.description = None
    caluny_subject_448.level = None
    caluny_subject_448.degree = caluny_degree_10
    caluny_subject_448 = importer.save_or_locate(caluny_subject_448)

    caluny_subject_449 = Subject()
    caluny_subject_449.code = 402
    caluny_subject_449.title = u'Electr\xf3nica de Potencia'
    caluny_subject_449.description = None
    caluny_subject_449.level = None
    caluny_subject_449.degree = caluny_degree_10
    caluny_subject_449 = importer.save_or_locate(caluny_subject_449)

    caluny_subject_450 = Subject()
    caluny_subject_450.code = 401
    caluny_subject_450.title = u'Circuitos Integrados'
    caluny_subject_450.description = None
    caluny_subject_450.level = None
    caluny_subject_450.degree = caluny_degree_10
    caluny_subject_450 = importer.save_or_locate(caluny_subject_450)

    caluny_subject_451 = Subject()
    caluny_subject_451.code = 409
    caluny_subject_451.title = u'Equipos Electr\xf3nicos de Medida'
    caluny_subject_451.description = None
    caluny_subject_451.level = None
    caluny_subject_451.degree = caluny_degree_10
    caluny_subject_451 = importer.save_or_locate(caluny_subject_451)

    caluny_subject_452 = Subject()
    caluny_subject_452.code = 408
    caluny_subject_452.title = u'Dise\xf1o de Controladores Industriales'
    caluny_subject_452.description = None
    caluny_subject_452.level = None
    caluny_subject_452.degree = caluny_degree_10
    caluny_subject_452 = importer.save_or_locate(caluny_subject_452)

    caluny_subject_453 = Subject()
    caluny_subject_453.code = 410
    caluny_subject_453.title = u'Microelectr\xf3nica'
    caluny_subject_453.description = None
    caluny_subject_453.level = None
    caluny_subject_453.degree = caluny_degree_10
    caluny_subject_453 = importer.save_or_locate(caluny_subject_453)

    caluny_subject_454 = Subject()
    caluny_subject_454.code = 411
    caluny_subject_454.title = u'Seguridad y Salud Laboral'
    caluny_subject_454.description = None
    caluny_subject_454.level = None
    caluny_subject_454.degree = caluny_degree_10
    caluny_subject_454 = importer.save_or_locate(caluny_subject_454)

    caluny_subject_455 = Subject()
    caluny_subject_455.code = 412
    caluny_subject_455.title = u'Tecnolog\xeda Electr\xf3nica'
    caluny_subject_455.description = None
    caluny_subject_455.level = None
    caluny_subject_455.degree = caluny_degree_10
    caluny_subject_455 = importer.save_or_locate(caluny_subject_455)

    caluny_subject_456 = Subject()
    caluny_subject_456.code = 413
    caluny_subject_456.title = u'Trabajo Fin de Grado'
    caluny_subject_456.description = None
    caluny_subject_456.level = None
    caluny_subject_456.degree = caluny_degree_10
    caluny_subject_456 = importer.save_or_locate(caluny_subject_456)

    caluny_subject_457 = Subject()
    caluny_subject_457.code = 308
    caluny_subject_457.title = u'Automatizaci\xf3n Industrial'
    caluny_subject_457.description = None
    caluny_subject_457.level = None
    caluny_subject_457.degree = caluny_degree_10
    caluny_subject_457 = importer.save_or_locate(caluny_subject_457)

    caluny_subject_458 = Subject()
    caluny_subject_458.code = 313
    caluny_subject_458.title = u'Sistemas Electr\xf3nicos Digitales'
    caluny_subject_458.description = None
    caluny_subject_458.level = None
    caluny_subject_458.degree = caluny_degree_10
    caluny_subject_458 = importer.save_or_locate(caluny_subject_458)

    caluny_subject_459 = Subject()
    caluny_subject_459.code = 312
    caluny_subject_459.title = u'Mantenimiento Industrial'
    caluny_subject_459.description = None
    caluny_subject_459.level = None
    caluny_subject_459.degree = caluny_degree_10
    caluny_subject_459 = importer.save_or_locate(caluny_subject_459)

    caluny_subject_460 = Subject()
    caluny_subject_460.code = 311
    caluny_subject_460.title = u'Ingl\xe9s aplicado a la Ingenier\xeda Electr\xf3nica'
    caluny_subject_460.description = None
    caluny_subject_460.level = None
    caluny_subject_460.degree = caluny_degree_10
    caluny_subject_460 = importer.save_or_locate(caluny_subject_460)

    caluny_subject_461 = Subject()
    caluny_subject_461.code = 310
    caluny_subject_461.title = u'Ingenier\xeda Gr\xe1fica en Electr\xf3nica'
    caluny_subject_461.description = None
    caluny_subject_461.level = None
    caluny_subject_461.degree = caluny_degree_10
    caluny_subject_461 = importer.save_or_locate(caluny_subject_461)

    caluny_subject_462 = Subject()
    caluny_subject_462.code = 314
    caluny_subject_462.title = u'Sistemas de Percepci\xf3n para la Automatizaci\xf3n'
    caluny_subject_462.description = None
    caluny_subject_462.level = None
    caluny_subject_462.degree = caluny_degree_10
    caluny_subject_462 = importer.save_or_locate(caluny_subject_462)

    caluny_subject_463 = Subject()
    caluny_subject_463.code = 110
    caluny_subject_463.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_463.description = None
    caluny_subject_463.level = None
    caluny_subject_463.degree = caluny_degree_10
    caluny_subject_463 = importer.save_or_locate(caluny_subject_463)

    caluny_subject_464 = Subject()
    caluny_subject_464.code = 301
    caluny_subject_464.title = u'An\xe1lisis de Redes El\xe9ctricas'
    caluny_subject_464.description = None
    caluny_subject_464.level = None
    caluny_subject_464.degree = caluny_degree_10
    caluny_subject_464 = importer.save_or_locate(caluny_subject_464)

    caluny_subject_465 = Subject()
    caluny_subject_465.code = 201
    caluny_subject_465.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_465.description = None
    caluny_subject_465.level = None
    caluny_subject_465.degree = caluny_degree_10
    caluny_subject_465 = importer.save_or_locate(caluny_subject_465)

    caluny_subject_466 = Subject()
    caluny_subject_466.code = 309
    caluny_subject_466.title = u'Inform\xe1tica Industrial'
    caluny_subject_466.description = None
    caluny_subject_466.level = None
    caluny_subject_466.degree = caluny_degree_10
    caluny_subject_466 = importer.save_or_locate(caluny_subject_466)

    caluny_subject_467 = Subject()
    caluny_subject_467.code = 203
    caluny_subject_467.title = u'Ingenier\xeda de Fabricaci\xf3n'
    caluny_subject_467.description = None
    caluny_subject_467.level = None
    caluny_subject_467.degree = caluny_degree_10
    caluny_subject_467 = importer.save_or_locate(caluny_subject_467)

    caluny_subject_468 = Subject()
    caluny_subject_468.code = 202
    caluny_subject_468.title = u'Ampliaci\xf3n de F\xedsica'
    caluny_subject_468.description = None
    caluny_subject_468.level = None
    caluny_subject_468.degree = caluny_degree_10
    caluny_subject_468 = importer.save_or_locate(caluny_subject_468)

    caluny_subject_469 = Subject()
    caluny_subject_469.code = 205
    caluny_subject_469.title = u'Sistemas Inform\xe1ticos'
    caluny_subject_469.description = None
    caluny_subject_469.level = None
    caluny_subject_469.degree = caluny_degree_10
    caluny_subject_469 = importer.save_or_locate(caluny_subject_469)

    caluny_subject_470 = Subject()
    caluny_subject_470.code = 204
    caluny_subject_470.title = u'Resistencia de Materiales'
    caluny_subject_470.description = None
    caluny_subject_470.level = None
    caluny_subject_470.degree = caluny_degree_10
    caluny_subject_470 = importer.save_or_locate(caluny_subject_470)

    caluny_subject_471 = Subject()
    caluny_subject_471.code = 207
    caluny_subject_471.title = u'Termotecnia'
    caluny_subject_471.description = None
    caluny_subject_471.level = None
    caluny_subject_471.degree = caluny_degree_10
    caluny_subject_471 = importer.save_or_locate(caluny_subject_471)

    caluny_subject_472 = Subject()
    caluny_subject_472.code = 206
    caluny_subject_472.title = u'Teor\xeda de M\xe1quinas'
    caluny_subject_472.description = None
    caluny_subject_472.level = None
    caluny_subject_472.degree = caluny_degree_10
    caluny_subject_472 = importer.save_or_locate(caluny_subject_472)

    caluny_subject_473 = Subject()
    caluny_subject_473.code = 209
    caluny_subject_473.title = u'Ciencia de los Materiales'
    caluny_subject_473.description = None
    caluny_subject_473.level = None
    caluny_subject_473.degree = caluny_degree_10
    caluny_subject_473 = importer.save_or_locate(caluny_subject_473)

    caluny_subject_474 = Subject()
    caluny_subject_474.code = 208
    caluny_subject_474.title = u'Autom\xe1tica'
    caluny_subject_474.description = None
    caluny_subject_474.level = None
    caluny_subject_474.degree = caluny_degree_10
    caluny_subject_474 = importer.save_or_locate(caluny_subject_474)

    caluny_subject_475 = Subject()
    caluny_subject_475.code = 302
    caluny_subject_475.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_475.description = None
    caluny_subject_475.level = None
    caluny_subject_475.degree = caluny_degree_10
    caluny_subject_475 = importer.save_or_locate(caluny_subject_475)

    caluny_subject_476 = Subject()
    caluny_subject_476.code = 303
    caluny_subject_476.title = u'Electr\xf3nica Anal\xf3gica'
    caluny_subject_476.description = None
    caluny_subject_476.level = None
    caluny_subject_476.degree = caluny_degree_10
    caluny_subject_476 = importer.save_or_locate(caluny_subject_476)

    caluny_subject_477 = Subject()
    caluny_subject_477.code = 304
    caluny_subject_477.title = u'Electr\xf3nica Digital'
    caluny_subject_477.description = None
    caluny_subject_477.level = None
    caluny_subject_477.degree = caluny_degree_10
    caluny_subject_477 = importer.save_or_locate(caluny_subject_477)

    caluny_subject_478 = Subject()
    caluny_subject_478.code = 305
    caluny_subject_478.title = u'Programaci\xf3n de Robots Industriales'
    caluny_subject_478.description = None
    caluny_subject_478.level = None
    caluny_subject_478.degree = caluny_degree_10
    caluny_subject_478 = importer.save_or_locate(caluny_subject_478)

    caluny_subject_479 = Subject()
    caluny_subject_479.code = 306
    caluny_subject_479.title = u'Regulaci\xf3n Autom\xe1tica'
    caluny_subject_479.description = None
    caluny_subject_479.level = None
    caluny_subject_479.degree = caluny_degree_10
    caluny_subject_479 = importer.save_or_locate(caluny_subject_479)

    caluny_subject_480 = Subject()
    caluny_subject_480.code = 307
    caluny_subject_480.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_480.description = None
    caluny_subject_480.level = None
    caluny_subject_480.degree = caluny_degree_10
    caluny_subject_480 = importer.save_or_locate(caluny_subject_480)

    caluny_subject_481 = Subject()
    caluny_subject_481.code = 108
    caluny_subject_481.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_481.description = None
    caluny_subject_481.level = None
    caluny_subject_481.degree = caluny_degree_10
    caluny_subject_481 = importer.save_or_locate(caluny_subject_481)

    caluny_subject_482 = Subject()
    caluny_subject_482.code = 109
    caluny_subject_482.title = u'F\xedsica 2'
    caluny_subject_482.description = None
    caluny_subject_482.level = None
    caluny_subject_482.degree = caluny_degree_10
    caluny_subject_482 = importer.save_or_locate(caluny_subject_482)

    caluny_subject_483 = Subject()
    caluny_subject_483.code = 102
    caluny_subject_483.title = u'C\xe1lculo'
    caluny_subject_483.description = None
    caluny_subject_483.level = None
    caluny_subject_483.degree = caluny_degree_10
    caluny_subject_483 = importer.save_or_locate(caluny_subject_483)

    caluny_subject_484 = Subject()
    caluny_subject_484.code = 103
    caluny_subject_484.title = u'F\xedsica 1'
    caluny_subject_484.description = None
    caluny_subject_484.level = None
    caluny_subject_484.degree = caluny_degree_10
    caluny_subject_484 = importer.save_or_locate(caluny_subject_484)

    caluny_subject_485 = Subject()
    caluny_subject_485.code = 101
    caluny_subject_485.title = u'\xc1lgebra Lineal'
    caluny_subject_485.description = None
    caluny_subject_485.level = None
    caluny_subject_485.degree = caluny_degree_10
    caluny_subject_485 = importer.save_or_locate(caluny_subject_485)

    caluny_subject_486 = Subject()
    caluny_subject_486.code = 106
    caluny_subject_486.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_486.description = None
    caluny_subject_486.level = None
    caluny_subject_486.degree = caluny_degree_10
    caluny_subject_486 = importer.save_or_locate(caluny_subject_486)

    caluny_subject_487 = Subject()
    caluny_subject_487.code = 107
    caluny_subject_487.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_487.description = None
    caluny_subject_487.level = None
    caluny_subject_487.degree = caluny_degree_10
    caluny_subject_487 = importer.save_or_locate(caluny_subject_487)

    caluny_subject_488 = Subject()
    caluny_subject_488.code = 104
    caluny_subject_488.title = u'Gesti\xf3n de Empresas'
    caluny_subject_488.description = None
    caluny_subject_488.level = None
    caluny_subject_488.degree = caluny_degree_10
    caluny_subject_488 = importer.save_or_locate(caluny_subject_488)

    caluny_subject_489 = Subject()
    caluny_subject_489.code = 105
    caluny_subject_489.title = u'Qu\xedmica'
    caluny_subject_489.description = None
    caluny_subject_489.level = None
    caluny_subject_489.degree = caluny_degree_10
    caluny_subject_489 = importer.save_or_locate(caluny_subject_489)

    caluny_subject_490 = Subject()
    caluny_subject_490.code = 210
    caluny_subject_490.title = u'Teor\xeda de M\xe1quinas'
    caluny_subject_490.description = None
    caluny_subject_490.level = None
    caluny_subject_490.degree = caluny_degree_11
    caluny_subject_490 = importer.save_or_locate(caluny_subject_490)

    caluny_subject_491 = Subject()
    caluny_subject_491.code = 407
    caluny_subject_491.title = u'Dise\xf1o Mec\xe1nico Asistido por Ordenador'
    caluny_subject_491.description = None
    caluny_subject_491.level = None
    caluny_subject_491.degree = caluny_degree_11
    caluny_subject_491 = importer.save_or_locate(caluny_subject_491)

    caluny_subject_492 = Subject()
    caluny_subject_492.code = 406
    caluny_subject_492.title = u'Desarrollo Hist\xf3rico - Culturales del Dise\xf1o Industrial'
    caluny_subject_492.description = None
    caluny_subject_492.level = None
    caluny_subject_492.degree = caluny_degree_11
    caluny_subject_492 = importer.save_or_locate(caluny_subject_492)

    caluny_subject_493 = Subject()
    caluny_subject_493.code = 405
    caluny_subject_493.title = u'C\xe1lculo y Dise\xf1o de M\xe1quinas'
    caluny_subject_493.description = None
    caluny_subject_493.level = None
    caluny_subject_493.degree = caluny_degree_11
    caluny_subject_493 = importer.save_or_locate(caluny_subject_493)

    caluny_subject_494 = Subject()
    caluny_subject_494.code = 404
    caluny_subject_494.title = u'Tecnolog\xeda de Fabricaci\xf3n'
    caluny_subject_494.description = None
    caluny_subject_494.level = None
    caluny_subject_494.degree = caluny_degree_11
    caluny_subject_494 = importer.save_or_locate(caluny_subject_494)

    caluny_subject_495 = Subject()
    caluny_subject_495.code = 403
    caluny_subject_495.title = u'Ingenier\xeda T\xe9rmica'
    caluny_subject_495.description = None
    caluny_subject_495.level = None
    caluny_subject_495.degree = caluny_degree_11
    caluny_subject_495 = importer.save_or_locate(caluny_subject_495)

    caluny_subject_496 = Subject()
    caluny_subject_496.code = 401
    caluny_subject_496.title = u'Dise\xf1o Ergon\xf3mico y Ecodise\xf1o'
    caluny_subject_496.description = None
    caluny_subject_496.level = None
    caluny_subject_496.degree = caluny_degree_11
    caluny_subject_496 = importer.save_or_locate(caluny_subject_496)

    caluny_subject_497 = Subject()
    caluny_subject_497.code = 509
    caluny_subject_497.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_497.description = None
    caluny_subject_497.level = None
    caluny_subject_497.degree = caluny_degree_11
    caluny_subject_497 = importer.save_or_locate(caluny_subject_497)

    caluny_subject_498 = Subject()
    caluny_subject_498.code = 504
    caluny_subject_498.title = u'Metrolog\xeda y Calidad'
    caluny_subject_498.description = None
    caluny_subject_498.level = None
    caluny_subject_498.degree = caluny_degree_11
    caluny_subject_498 = importer.save_or_locate(caluny_subject_498)

    caluny_subject_499 = Subject()
    caluny_subject_499.code = 505
    caluny_subject_499.title = u'Oficina T\xe9cnica'
    caluny_subject_499.description = None
    caluny_subject_499.level = None
    caluny_subject_499.degree = caluny_degree_11
    caluny_subject_499 = importer.save_or_locate(caluny_subject_499)

    caluny_subject_500 = Subject()
    caluny_subject_500.code = 502
    caluny_subject_500.title = u'Ingl\xe9s aplicado a la Ingenier\xeda Mec\xe1nica'
    caluny_subject_500.description = None
    caluny_subject_500.level = None
    caluny_subject_500.degree = caluny_degree_11
    caluny_subject_500 = importer.save_or_locate(caluny_subject_500)

    caluny_subject_501 = Subject()
    caluny_subject_501.code = 503
    caluny_subject_501.title = u'Ingl\xe9s Aplicado al Dise\xf1o Industrial'
    caluny_subject_501.description = None
    caluny_subject_501.level = None
    caluny_subject_501.degree = caluny_degree_11
    caluny_subject_501 = importer.save_or_locate(caluny_subject_501)

    caluny_subject_502 = Subject()
    caluny_subject_502.code = 409
    caluny_subject_502.title = u'Motores T\xe9rmicos'
    caluny_subject_502.description = None
    caluny_subject_502.level = None
    caluny_subject_502.degree = caluny_degree_11
    caluny_subject_502 = importer.save_or_locate(caluny_subject_502)

    caluny_subject_503 = Subject()
    caluny_subject_503.code = 408
    caluny_subject_503.title = u'Mec\xe1nica Experimental y T\xe9cnicas de Simulaci\xf3n de M\xe1quinas'
    caluny_subject_503.description = None
    caluny_subject_503.level = None
    caluny_subject_503.degree = caluny_degree_11
    caluny_subject_503 = importer.save_or_locate(caluny_subject_503)

    caluny_subject_504 = Subject()
    caluny_subject_504.code = 508
    caluny_subject_504.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_504.description = None
    caluny_subject_504.level = None
    caluny_subject_504.degree = caluny_degree_11
    caluny_subject_504 = importer.save_or_locate(caluny_subject_504)

    caluny_subject_505 = Subject()
    caluny_subject_505.code = 414
    caluny_subject_505.title = u'Ingenier\xeda de Veh\xedculos Autom\xf3viles'
    caluny_subject_505.description = None
    caluny_subject_505.level = None
    caluny_subject_505.degree = caluny_degree_11
    caluny_subject_505 = importer.save_or_locate(caluny_subject_505)

    caluny_subject_506 = Subject()
    caluny_subject_506.code = 415
    caluny_subject_506.title = u'Mantenimiento Industrial'
    caluny_subject_506.description = None
    caluny_subject_506.level = None
    caluny_subject_506.degree = caluny_degree_11
    caluny_subject_506 = importer.save_or_locate(caluny_subject_506)

    caluny_subject_507 = Subject()
    caluny_subject_507.code = 416
    caluny_subject_507.title = u'Materiales para la Construcci\xf3n'
    caluny_subject_507.description = None
    caluny_subject_507.level = None
    caluny_subject_507.degree = caluny_degree_11
    caluny_subject_507 = importer.save_or_locate(caluny_subject_507)

    caluny_subject_508 = Subject()
    caluny_subject_508.code = 417
    caluny_subject_508.title = u'Mec\xe1nica de Suelos y Cimentaciones'
    caluny_subject_508.description = None
    caluny_subject_508.level = None
    caluny_subject_508.degree = caluny_degree_11
    caluny_subject_508 = importer.save_or_locate(caluny_subject_508)

    caluny_subject_509 = Subject()
    caluny_subject_509.code = 410
    caluny_subject_509.title = u'Dise\xf1o Gr\xe1fico Digital'
    caluny_subject_509.description = None
    caluny_subject_509.level = None
    caluny_subject_509.degree = caluny_degree_11
    caluny_subject_509 = importer.save_or_locate(caluny_subject_509)

    caluny_subject_510 = Subject()
    caluny_subject_510.code = 411
    caluny_subject_510.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_510.description = None
    caluny_subject_510.level = None
    caluny_subject_510.degree = caluny_degree_11
    caluny_subject_510 = importer.save_or_locate(caluny_subject_510)

    caluny_subject_511 = Subject()
    caluny_subject_511.code = 412
    caluny_subject_511.title = u'Equipos Electr\xf3nicos de Medida'
    caluny_subject_511.description = None
    caluny_subject_511.level = None
    caluny_subject_511.degree = caluny_degree_11
    caluny_subject_511 = importer.save_or_locate(caluny_subject_511)

    caluny_subject_512 = Subject()
    caluny_subject_512.code = 413
    caluny_subject_512.title = u'Idioma moderno (Ingl\xe9s)'
    caluny_subject_512.description = None
    caluny_subject_512.level = None
    caluny_subject_512.degree = caluny_degree_11
    caluny_subject_512 = importer.save_or_locate(caluny_subject_512)

    caluny_subject_513 = Subject()
    caluny_subject_513.code = 501
    caluny_subject_513.title = u'Estructuras de Hormig\xf3n'
    caluny_subject_513.description = None
    caluny_subject_513.level = None
    caluny_subject_513.degree = caluny_degree_11
    caluny_subject_513 = importer.save_or_locate(caluny_subject_513)

    caluny_subject_514 = Subject()
    caluny_subject_514.code = 418
    caluny_subject_514.title = u'Presentaci\xf3n Multimedia del Producto'
    caluny_subject_514.description = None
    caluny_subject_514.level = None
    caluny_subject_514.degree = caluny_degree_11
    caluny_subject_514 = importer.save_or_locate(caluny_subject_514)

    caluny_subject_515 = Subject()
    caluny_subject_515.code = 419
    caluny_subject_515.title = u'Programaci\xf3n de Robots Industriales'
    caluny_subject_515.description = None
    caluny_subject_515.level = None
    caluny_subject_515.degree = caluny_degree_11
    caluny_subject_515 = importer.save_or_locate(caluny_subject_515)

    caluny_subject_516 = Subject()
    caluny_subject_516.code = 308
    caluny_subject_516.title = u'Tecnolog\xeda de Materiales'
    caluny_subject_516.description = None
    caluny_subject_516.level = None
    caluny_subject_516.degree = caluny_degree_11
    caluny_subject_516 = importer.save_or_locate(caluny_subject_516)

    caluny_subject_517 = Subject()
    caluny_subject_517.code = 110
    caluny_subject_517.title = u'Qu\xedmica'
    caluny_subject_517.description = None
    caluny_subject_517.level = None
    caluny_subject_517.degree = caluny_degree_11
    caluny_subject_517 = importer.save_or_locate(caluny_subject_517)

    caluny_subject_518 = Subject()
    caluny_subject_518.code = 301
    caluny_subject_518.title = u'Dise\xf1o Asistido por Ordenador'
    caluny_subject_518.description = None
    caluny_subject_518.level = None
    caluny_subject_518.degree = caluny_degree_11
    caluny_subject_518 = importer.save_or_locate(caluny_subject_518)

    caluny_subject_519 = Subject()
    caluny_subject_519.code = 421
    caluny_subject_519.title = u'Reciclaje y Medio Ambiente'
    caluny_subject_519.description = None
    caluny_subject_519.level = None
    caluny_subject_519.degree = caluny_degree_11
    caluny_subject_519 = importer.save_or_locate(caluny_subject_519)

    caluny_subject_520 = Subject()
    caluny_subject_520.code = 420
    caluny_subject_520.title = u'Proyectos de Dise\xf1o Industrial'
    caluny_subject_520.description = None
    caluny_subject_520.level = None
    caluny_subject_520.degree = caluny_degree_11
    caluny_subject_520 = importer.save_or_locate(caluny_subject_520)

    caluny_subject_521 = Subject()
    caluny_subject_521.code = 201
    caluny_subject_521.title = u'Autom\xe1tica'
    caluny_subject_521.description = None
    caluny_subject_521.level = None
    caluny_subject_521.degree = caluny_degree_11
    caluny_subject_521 = importer.save_or_locate(caluny_subject_521)

    caluny_subject_522 = Subject()
    caluny_subject_522.code = 309
    caluny_subject_522.title = u'Teor\xeda y Est\xe9tica del Dise\xf1o Industrial'
    caluny_subject_522.description = None
    caluny_subject_522.level = None
    caluny_subject_522.degree = caluny_degree_11
    caluny_subject_522 = importer.save_or_locate(caluny_subject_522)

    caluny_subject_523 = Subject()
    caluny_subject_523.code = 203
    caluny_subject_523.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_523.description = None
    caluny_subject_523.level = None
    caluny_subject_523.degree = caluny_degree_11
    caluny_subject_523 = importer.save_or_locate(caluny_subject_523)

    caluny_subject_524 = Subject()
    caluny_subject_524.code = 202
    caluny_subject_524.title = u'Ciencia de los Materiales'
    caluny_subject_524.description = None
    caluny_subject_524.level = None
    caluny_subject_524.degree = caluny_degree_11
    caluny_subject_524 = importer.save_or_locate(caluny_subject_524)

    caluny_subject_525 = Subject()
    caluny_subject_525.code = 205
    caluny_subject_525.title = u'Termotecnia'
    caluny_subject_525.description = None
    caluny_subject_525.level = None
    caluny_subject_525.degree = caluny_degree_11
    caluny_subject_525 = importer.save_or_locate(caluny_subject_525)

    caluny_subject_526 = Subject()
    caluny_subject_526.code = 204
    caluny_subject_526.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_526.description = None
    caluny_subject_526.level = None
    caluny_subject_526.degree = caluny_degree_11
    caluny_subject_526 = importer.save_or_locate(caluny_subject_526)

    caluny_subject_527 = Subject()
    caluny_subject_527.code = 207
    caluny_subject_527.title = u'Ingenier\xeda de Fabricaci\xf3n'
    caluny_subject_527.description = None
    caluny_subject_527.level = None
    caluny_subject_527.degree = caluny_degree_11
    caluny_subject_527 = importer.save_or_locate(caluny_subject_527)

    caluny_subject_528 = Subject()
    caluny_subject_528.code = 206
    caluny_subject_528.title = u'Fundamentos del Dise\xf1o'
    caluny_subject_528.description = None
    caluny_subject_528.level = None
    caluny_subject_528.degree = caluny_degree_11
    caluny_subject_528 = importer.save_or_locate(caluny_subject_528)

    caluny_subject_529 = Subject()
    caluny_subject_529.code = 209
    caluny_subject_529.title = u'Resistencia de Materiales'
    caluny_subject_529.description = None
    caluny_subject_529.level = None
    caluny_subject_529.degree = caluny_degree_11
    caluny_subject_529 = importer.save_or_locate(caluny_subject_529)

    caluny_subject_530 = Subject()
    caluny_subject_530.code = 208
    caluny_subject_530.title = u'Mec\xe1nica de Fluidos'
    caluny_subject_530.description = None
    caluny_subject_530.level = None
    caluny_subject_530.degree = caluny_degree_11
    caluny_subject_530 = importer.save_or_locate(caluny_subject_530)

    caluny_subject_531 = Subject()
    caluny_subject_531.code = 302
    caluny_subject_531.title = u'Ingenier\xeda Gr\xe1fica del Producto'
    caluny_subject_531.description = None
    caluny_subject_531.level = None
    caluny_subject_531.degree = caluny_degree_11
    caluny_subject_531 = importer.save_or_locate(caluny_subject_531)

    caluny_subject_532 = Subject()
    caluny_subject_532.code = 303
    caluny_subject_532.title = u'Metodolog\xeda del Dise\xf1o'
    caluny_subject_532.description = None
    caluny_subject_532.level = None
    caluny_subject_532.degree = caluny_degree_11
    caluny_subject_532 = importer.save_or_locate(caluny_subject_532)

    caluny_subject_533 = Subject()
    caluny_subject_533.code = 304
    caluny_subject_533.title = u'Teor\xeda de Estructuras y Construcciones Industriales'
    caluny_subject_533.description = None
    caluny_subject_533.level = None
    caluny_subject_533.degree = caluny_degree_11
    caluny_subject_533 = importer.save_or_locate(caluny_subject_533)

    caluny_subject_534 = Subject()
    caluny_subject_534.code = 305
    caluny_subject_534.title = u'Dise\xf1o de Comunicaci\xf3n'
    caluny_subject_534.description = None
    caluny_subject_534.level = None
    caluny_subject_534.degree = caluny_degree_11
    caluny_subject_534 = importer.save_or_locate(caluny_subject_534)

    caluny_subject_535 = Subject()
    caluny_subject_535.code = 306
    caluny_subject_535.title = u'Estructuras Met\xe1licas'
    caluny_subject_535.description = None
    caluny_subject_535.level = None
    caluny_subject_535.degree = caluny_degree_11
    caluny_subject_535 = importer.save_or_locate(caluny_subject_535)

    caluny_subject_536 = Subject()
    caluny_subject_536.code = 307
    caluny_subject_536.title = u'M\xe1quinas Fluidomec\xe1nicas'
    caluny_subject_536.description = None
    caluny_subject_536.level = None
    caluny_subject_536.degree = caluny_degree_11
    caluny_subject_536 = importer.save_or_locate(caluny_subject_536)

    caluny_subject_537 = Subject()
    caluny_subject_537.code = 108
    caluny_subject_537.title = u'F\xedsica 2'
    caluny_subject_537.description = None
    caluny_subject_537.level = None
    caluny_subject_537.degree = caluny_degree_11
    caluny_subject_537 = importer.save_or_locate(caluny_subject_537)

    caluny_subject_538 = Subject()
    caluny_subject_538.code = 109
    caluny_subject_538.title = u'Gesti\xf3n de Empresas'
    caluny_subject_538.description = None
    caluny_subject_538.level = None
    caluny_subject_538.degree = caluny_degree_11
    caluny_subject_538 = importer.save_or_locate(caluny_subject_538)

    caluny_subject_539 = Subject()
    caluny_subject_539.code = 102
    caluny_subject_539.title = u'C\xe1lculo'
    caluny_subject_539.description = None
    caluny_subject_539.level = None
    caluny_subject_539.degree = caluny_degree_11
    caluny_subject_539 = importer.save_or_locate(caluny_subject_539)

    caluny_subject_540 = Subject()
    caluny_subject_540.code = 103
    caluny_subject_540.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_540.description = None
    caluny_subject_540.level = None
    caluny_subject_540.degree = caluny_degree_11
    caluny_subject_540 = importer.save_or_locate(caluny_subject_540)

    caluny_subject_541 = Subject()
    caluny_subject_541.code = 101
    caluny_subject_541.title = u'\xc1lgebra Lineal'
    caluny_subject_541.description = None
    caluny_subject_541.level = None
    caluny_subject_541.degree = caluny_degree_11
    caluny_subject_541 = importer.save_or_locate(caluny_subject_541)

    caluny_subject_542 = Subject()
    caluny_subject_542.code = 106
    caluny_subject_542.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_542.description = None
    caluny_subject_542.level = None
    caluny_subject_542.degree = caluny_degree_11
    caluny_subject_542 = importer.save_or_locate(caluny_subject_542)

    caluny_subject_543 = Subject()
    caluny_subject_543.code = 107
    caluny_subject_543.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_543.description = None
    caluny_subject_543.level = None
    caluny_subject_543.degree = caluny_degree_11
    caluny_subject_543 = importer.save_or_locate(caluny_subject_543)

    caluny_subject_544 = Subject()
    caluny_subject_544.code = 104
    caluny_subject_544.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_544.description = None
    caluny_subject_544.level = None
    caluny_subject_544.degree = caluny_degree_11
    caluny_subject_544 = importer.save_or_locate(caluny_subject_544)

    caluny_subject_545 = Subject()
    caluny_subject_545.code = 105
    caluny_subject_545.title = u'F\xedsica 1'
    caluny_subject_545.description = None
    caluny_subject_545.level = None
    caluny_subject_545.degree = caluny_degree_11
    caluny_subject_545 = importer.save_or_locate(caluny_subject_545)

    caluny_subject_546 = Subject()
    caluny_subject_546.code = 511
    caluny_subject_546.title = u'Envase y Embalaje'
    caluny_subject_546.description = None
    caluny_subject_546.level = None
    caluny_subject_546.degree = caluny_degree_11
    caluny_subject_546 = importer.save_or_locate(caluny_subject_546)

    caluny_subject_547 = Subject()
    caluny_subject_547.code = 510
    caluny_subject_547.title = u'Seguridad y Salud Laboral'
    caluny_subject_547.description = None
    caluny_subject_547.level = None
    caluny_subject_547.degree = caluny_degree_11
    caluny_subject_547 = importer.save_or_locate(caluny_subject_547)

    caluny_subject_548 = Subject()
    caluny_subject_548.code = 515
    caluny_subject_548.title = u'Trabajo Fin de Grado (Ingenier\xeda Dise\xf1o Ind. y D.P.)'
    caluny_subject_548.description = None
    caluny_subject_548.level = None
    caluny_subject_548.degree = caluny_degree_11
    caluny_subject_548 = importer.save_or_locate(caluny_subject_548)

    caluny_subject_549 = Subject()
    caluny_subject_549.code = 514
    caluny_subject_549.title = u'Trabajo Fin de Grado (Ingenier\xeda Mec\xe1nica)'
    caluny_subject_549.description = None
    caluny_subject_549.level = None
    caluny_subject_549.degree = caluny_degree_11
    caluny_subject_549 = importer.save_or_locate(caluny_subject_549)

    caluny_subject_550 = Subject()
    caluny_subject_550.code = 212
    caluny_subject_550.title = u'Teor\xeda de M\xe1quinas'
    caluny_subject_550.description = None
    caluny_subject_550.level = None
    caluny_subject_550.degree = caluny_degree_12
    caluny_subject_550 = importer.save_or_locate(caluny_subject_550)

    caluny_subject_551 = Subject()
    caluny_subject_551.code = 210
    caluny_subject_551.title = u'Resistencia de Materiales'
    caluny_subject_551.description = None
    caluny_subject_551.level = None
    caluny_subject_551.degree = caluny_degree_12
    caluny_subject_551 = importer.save_or_locate(caluny_subject_551)

    caluny_subject_552 = Subject()
    caluny_subject_552.code = 211
    caluny_subject_552.title = u'Sistemas Inform\xe1ticos'
    caluny_subject_552.description = None
    caluny_subject_552.level = None
    caluny_subject_552.degree = caluny_degree_12
    caluny_subject_552 = importer.save_or_locate(caluny_subject_552)

    caluny_subject_553 = Subject()
    caluny_subject_553.code = 407
    caluny_subject_553.title = u'Metrolog\xeda y Calidad'
    caluny_subject_553.description = None
    caluny_subject_553.level = None
    caluny_subject_553.degree = caluny_degree_12
    caluny_subject_553 = importer.save_or_locate(caluny_subject_553)

    caluny_subject_554 = Subject()
    caluny_subject_554.code = 406
    caluny_subject_554.title = u'Mec\xe1nica de Suelos y Cimentaciones'
    caluny_subject_554.description = None
    caluny_subject_554.level = None
    caluny_subject_554.degree = caluny_degree_12
    caluny_subject_554 = importer.save_or_locate(caluny_subject_554)

    caluny_subject_555 = Subject()
    caluny_subject_555.code = 405
    caluny_subject_555.title = u'Mantenimiento Industrial'
    caluny_subject_555.description = None
    caluny_subject_555.level = None
    caluny_subject_555.degree = caluny_degree_12
    caluny_subject_555 = importer.save_or_locate(caluny_subject_555)

    caluny_subject_556 = Subject()
    caluny_subject_556.code = 404
    caluny_subject_556.title = u'Ingenier\xeda de Veh\xedculos Autom\xf3viles'
    caluny_subject_556.description = None
    caluny_subject_556.level = None
    caluny_subject_556.degree = caluny_degree_12
    caluny_subject_556 = importer.save_or_locate(caluny_subject_556)

    caluny_subject_557 = Subject()
    caluny_subject_557.code = 403
    caluny_subject_557.title = u'Estructuras de Hormig\xf3n'
    caluny_subject_557.description = None
    caluny_subject_557.level = None
    caluny_subject_557.degree = caluny_degree_12
    caluny_subject_557 = importer.save_or_locate(caluny_subject_557)

    caluny_subject_558 = Subject()
    caluny_subject_558.code = 402
    caluny_subject_558.title = u'Equipos Electr\xf3nicos de Medida'
    caluny_subject_558.description = None
    caluny_subject_558.level = None
    caluny_subject_558.degree = caluny_degree_12
    caluny_subject_558 = importer.save_or_locate(caluny_subject_558)

    caluny_subject_559 = Subject()
    caluny_subject_559.code = 401
    caluny_subject_559.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_559.description = None
    caluny_subject_559.level = None
    caluny_subject_559.degree = caluny_degree_12
    caluny_subject_559 = importer.save_or_locate(caluny_subject_559)

    caluny_subject_560 = Subject()
    caluny_subject_560.code = 409
    caluny_subject_560.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_560.description = None
    caluny_subject_560.level = None
    caluny_subject_560.degree = caluny_degree_12
    caluny_subject_560 = importer.save_or_locate(caluny_subject_560)

    caluny_subject_561 = Subject()
    caluny_subject_561.code = 408
    caluny_subject_561.title = u'Oficina T\xe9cnica'
    caluny_subject_561.description = None
    caluny_subject_561.level = None
    caluny_subject_561.degree = caluny_degree_12
    caluny_subject_561 = importer.save_or_locate(caluny_subject_561)

    caluny_subject_562 = Subject()
    caluny_subject_562.code = 414
    caluny_subject_562.title = u'Soldadura'
    caluny_subject_562.description = None
    caluny_subject_562.level = None
    caluny_subject_562.degree = caluny_degree_12
    caluny_subject_562 = importer.save_or_locate(caluny_subject_562)

    caluny_subject_563 = Subject()
    caluny_subject_563.code = 415
    caluny_subject_563.title = u'Trabajo Fin de Grado (Ingenier\xeda Mec\xe1nica)'
    caluny_subject_563.description = None
    caluny_subject_563.level = None
    caluny_subject_563.degree = caluny_degree_12
    caluny_subject_563 = importer.save_or_locate(caluny_subject_563)

    caluny_subject_564 = Subject()
    caluny_subject_564.code = 410
    caluny_subject_564.title = u'Energ\xedas Renovables y Eficiencia Energ\xe9tica'
    caluny_subject_564.description = None
    caluny_subject_564.level = None
    caluny_subject_564.degree = caluny_degree_12
    caluny_subject_564 = importer.save_or_locate(caluny_subject_564)

    caluny_subject_565 = Subject()
    caluny_subject_565.code = 411
    caluny_subject_565.title = u'Mec\xe1nica Experimental y T\xe9cnicas de Simulaci\xf3n de M\xe1quinas'
    caluny_subject_565.description = None
    caluny_subject_565.level = None
    caluny_subject_565.degree = caluny_degree_12
    caluny_subject_565 = importer.save_or_locate(caluny_subject_565)

    caluny_subject_566 = Subject()
    caluny_subject_566.code = 412
    caluny_subject_566.title = u'Motores T\xe9rmicos'
    caluny_subject_566.description = None
    caluny_subject_566.level = None
    caluny_subject_566.degree = caluny_degree_12
    caluny_subject_566 = importer.save_or_locate(caluny_subject_566)

    caluny_subject_567 = Subject()
    caluny_subject_567.code = 413
    caluny_subject_567.title = u'Seguridad y Salud Laboral'
    caluny_subject_567.description = None
    caluny_subject_567.level = None
    caluny_subject_567.degree = caluny_degree_12
    caluny_subject_567 = importer.save_or_locate(caluny_subject_567)

    caluny_subject_568 = Subject()
    caluny_subject_568.code = 308
    caluny_subject_568.title = u'C\xe1lculo y Dise\xf1o de M\xe1quinas'
    caluny_subject_568.description = None
    caluny_subject_568.level = None
    caluny_subject_568.degree = caluny_degree_12
    caluny_subject_568 = importer.save_or_locate(caluny_subject_568)

    caluny_subject_569 = Subject()
    caluny_subject_569.code = 312
    caluny_subject_569.title = u'Tecnolog\xeda de Materiales'
    caluny_subject_569.description = None
    caluny_subject_569.level = None
    caluny_subject_569.degree = caluny_degree_12
    caluny_subject_569 = importer.save_or_locate(caluny_subject_569)

    caluny_subject_570 = Subject()
    caluny_subject_570.code = 311
    caluny_subject_570.title = u'M\xe1quinas Fluidomec\xe1nicas'
    caluny_subject_570.description = None
    caluny_subject_570.level = None
    caluny_subject_570.degree = caluny_degree_12
    caluny_subject_570 = importer.save_or_locate(caluny_subject_570)

    caluny_subject_571 = Subject()
    caluny_subject_571.code = 310
    caluny_subject_571.title = u'Estructuras Met\xe1licas'
    caluny_subject_571.description = None
    caluny_subject_571.level = None
    caluny_subject_571.degree = caluny_degree_12
    caluny_subject_571 = importer.save_or_locate(caluny_subject_571)

    caluny_subject_572 = Subject()
    caluny_subject_572.code = 110
    caluny_subject_572.title = u'Qu\xedmica'
    caluny_subject_572.description = None
    caluny_subject_572.level = None
    caluny_subject_572.degree = caluny_degree_12
    caluny_subject_572 = importer.save_or_locate(caluny_subject_572)

    caluny_subject_573 = Subject()
    caluny_subject_573.code = 301
    caluny_subject_573.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_573.description = None
    caluny_subject_573.level = None
    caluny_subject_573.degree = caluny_degree_12
    caluny_subject_573 = importer.save_or_locate(caluny_subject_573)

    caluny_subject_574 = Subject()
    caluny_subject_574.code = 201
    caluny_subject_574.title = u'Autom\xe1tica'
    caluny_subject_574.description = None
    caluny_subject_574.level = None
    caluny_subject_574.degree = caluny_degree_12
    caluny_subject_574 = importer.save_or_locate(caluny_subject_574)

    caluny_subject_575 = Subject()
    caluny_subject_575.code = 309
    caluny_subject_575.title = u'Dise\xf1o Mec\xe1nico Asistido por Ordenador'
    caluny_subject_575.description = None
    caluny_subject_575.level = None
    caluny_subject_575.degree = caluny_degree_12
    caluny_subject_575 = importer.save_or_locate(caluny_subject_575)

    caluny_subject_576 = Subject()
    caluny_subject_576.code = 203
    caluny_subject_576.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_576.description = None
    caluny_subject_576.level = None
    caluny_subject_576.degree = caluny_degree_12
    caluny_subject_576 = importer.save_or_locate(caluny_subject_576)

    caluny_subject_577 = Subject()
    caluny_subject_577.code = 202
    caluny_subject_577.title = u'Ciencia de los Materiales'
    caluny_subject_577.description = None
    caluny_subject_577.level = None
    caluny_subject_577.degree = caluny_degree_12
    caluny_subject_577 = importer.save_or_locate(caluny_subject_577)

    caluny_subject_578 = Subject()
    caluny_subject_578.code = 205
    caluny_subject_578.title = u'Termotecnia'
    caluny_subject_578.description = None
    caluny_subject_578.level = None
    caluny_subject_578.degree = caluny_degree_12
    caluny_subject_578 = importer.save_or_locate(caluny_subject_578)

    caluny_subject_579 = Subject()
    caluny_subject_579.code = 204
    caluny_subject_579.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_579.description = None
    caluny_subject_579.level = None
    caluny_subject_579.degree = caluny_degree_12
    caluny_subject_579 = importer.save_or_locate(caluny_subject_579)

    caluny_subject_580 = Subject()
    caluny_subject_580.code = 207
    caluny_subject_580.title = u'Ingenier\xeda de Fabricaci\xf3n'
    caluny_subject_580.description = None
    caluny_subject_580.level = None
    caluny_subject_580.degree = caluny_degree_12
    caluny_subject_580 = importer.save_or_locate(caluny_subject_580)

    caluny_subject_581 = Subject()
    caluny_subject_581.code = 206
    caluny_subject_581.title = u'Ampliaci\xf3n de F\xedsica'
    caluny_subject_581.description = None
    caluny_subject_581.level = None
    caluny_subject_581.degree = caluny_degree_12
    caluny_subject_581 = importer.save_or_locate(caluny_subject_581)

    caluny_subject_582 = Subject()
    caluny_subject_582.code = 209
    caluny_subject_582.title = u'Mec\xe1nica de Fluidos'
    caluny_subject_582.description = None
    caluny_subject_582.level = None
    caluny_subject_582.degree = caluny_degree_12
    caluny_subject_582 = importer.save_or_locate(caluny_subject_582)

    caluny_subject_583 = Subject()
    caluny_subject_583.code = 208
    caluny_subject_583.title = u'Ingl\xe9s aplicado a la Ingenier\xeda Mec\xe1nica'
    caluny_subject_583.description = None
    caluny_subject_583.level = None
    caluny_subject_583.degree = caluny_degree_12
    caluny_subject_583 = importer.save_or_locate(caluny_subject_583)

    caluny_subject_584 = Subject()
    caluny_subject_584.code = 302
    caluny_subject_584.title = u'Ingenier\xeda Gr\xe1fica Mec\xe1nica y Topograf\xeda'
    caluny_subject_584.description = None
    caluny_subject_584.level = None
    caluny_subject_584.degree = caluny_degree_12
    caluny_subject_584 = importer.save_or_locate(caluny_subject_584)

    caluny_subject_585 = Subject()
    caluny_subject_585.code = 303
    caluny_subject_585.title = u'Ingenier\xeda T\xe9rmica'
    caluny_subject_585.description = None
    caluny_subject_585.level = None
    caluny_subject_585.degree = caluny_degree_12
    caluny_subject_585 = importer.save_or_locate(caluny_subject_585)

    caluny_subject_586 = Subject()
    caluny_subject_586.code = 304
    caluny_subject_586.title = u'Materiales para la Construcci\xf3n'
    caluny_subject_586.description = None
    caluny_subject_586.level = None
    caluny_subject_586.degree = caluny_degree_12
    caluny_subject_586 = importer.save_or_locate(caluny_subject_586)

    caluny_subject_587 = Subject()
    caluny_subject_587.code = 305
    caluny_subject_587.title = u'Programaci\xf3n de Robots Industriales'
    caluny_subject_587.description = None
    caluny_subject_587.level = None
    caluny_subject_587.degree = caluny_degree_12
    caluny_subject_587 = importer.save_or_locate(caluny_subject_587)

    caluny_subject_588 = Subject()
    caluny_subject_588.code = 306
    caluny_subject_588.title = u'Tecnolog\xeda de Fabricaci\xf3n'
    caluny_subject_588.description = None
    caluny_subject_588.level = None
    caluny_subject_588.degree = caluny_degree_12
    caluny_subject_588 = importer.save_or_locate(caluny_subject_588)

    caluny_subject_589 = Subject()
    caluny_subject_589.code = 307
    caluny_subject_589.title = u'Teor\xeda de Estructuras y Construcciones Industriales'
    caluny_subject_589.description = None
    caluny_subject_589.level = None
    caluny_subject_589.degree = caluny_degree_12
    caluny_subject_589 = importer.save_or_locate(caluny_subject_589)

    caluny_subject_590 = Subject()
    caluny_subject_590.code = 108
    caluny_subject_590.title = u'F\xedsica II'
    caluny_subject_590.description = None
    caluny_subject_590.level = None
    caluny_subject_590.degree = caluny_degree_12
    caluny_subject_590 = importer.save_or_locate(caluny_subject_590)

    caluny_subject_591 = Subject()
    caluny_subject_591.code = 109
    caluny_subject_591.title = u'Gesti\xf3n de Empresas'
    caluny_subject_591.description = None
    caluny_subject_591.level = None
    caluny_subject_591.degree = caluny_degree_12
    caluny_subject_591 = importer.save_or_locate(caluny_subject_591)

    caluny_subject_592 = Subject()
    caluny_subject_592.code = 102
    caluny_subject_592.title = u'C\xe1lculo'
    caluny_subject_592.description = None
    caluny_subject_592.level = None
    caluny_subject_592.degree = caluny_degree_12
    caluny_subject_592 = importer.save_or_locate(caluny_subject_592)

    caluny_subject_593 = Subject()
    caluny_subject_593.code = 103
    caluny_subject_593.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_593.description = None
    caluny_subject_593.level = None
    caluny_subject_593.degree = caluny_degree_12
    caluny_subject_593 = importer.save_or_locate(caluny_subject_593)

    caluny_subject_594 = Subject()
    caluny_subject_594.code = 101
    caluny_subject_594.title = u'\xc1lgebra Lineal'
    caluny_subject_594.description = None
    caluny_subject_594.level = None
    caluny_subject_594.degree = caluny_degree_12
    caluny_subject_594 = importer.save_or_locate(caluny_subject_594)

    caluny_subject_595 = Subject()
    caluny_subject_595.code = 106
    caluny_subject_595.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_595.description = None
    caluny_subject_595.level = None
    caluny_subject_595.degree = caluny_degree_12
    caluny_subject_595 = importer.save_or_locate(caluny_subject_595)

    caluny_subject_596 = Subject()
    caluny_subject_596.code = 107
    caluny_subject_596.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_596.description = None
    caluny_subject_596.level = None
    caluny_subject_596.degree = caluny_degree_12
    caluny_subject_596 = importer.save_or_locate(caluny_subject_596)

    caluny_subject_597 = Subject()
    caluny_subject_597.code = 104
    caluny_subject_597.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_597.description = None
    caluny_subject_597.level = None
    caluny_subject_597.degree = caluny_degree_12
    caluny_subject_597 = importer.save_or_locate(caluny_subject_597)

    caluny_subject_598 = Subject()
    caluny_subject_598.code = 105
    caluny_subject_598.title = u'F\xedsica I'
    caluny_subject_598.description = None
    caluny_subject_598.level = None
    caluny_subject_598.degree = caluny_degree_12
    caluny_subject_598 = importer.save_or_locate(caluny_subject_598)

    caluny_subject_599 = Subject()
    caluny_subject_599.code = 212
    caluny_subject_599.title = u'Mec\xe1nica de Fluidos'
    caluny_subject_599.description = None
    caluny_subject_599.level = None
    caluny_subject_599.degree = caluny_degree_13
    caluny_subject_599 = importer.save_or_locate(caluny_subject_599)

    caluny_subject_600 = Subject()
    caluny_subject_600.code = 210
    caluny_subject_600.title = u'Fundamentos de Electr\xf3nica'
    caluny_subject_600.description = None
    caluny_subject_600.level = None
    caluny_subject_600.degree = caluny_degree_13
    caluny_subject_600 = importer.save_or_locate(caluny_subject_600)

    caluny_subject_601 = Subject()
    caluny_subject_601.code = 211
    caluny_subject_601.title = u'Fundamentos de Ingenier\xeda El\xe9ctrica'
    caluny_subject_601.description = None
    caluny_subject_601.level = None
    caluny_subject_601.degree = caluny_degree_13
    caluny_subject_601 = importer.save_or_locate(caluny_subject_601)

    caluny_subject_602 = Subject()
    caluny_subject_602.code = 407
    caluny_subject_602.title = u'An\xe1lisis de Sistemas de Energ\xeda El\xe9ctrica'
    caluny_subject_602.description = None
    caluny_subject_602.level = None
    caluny_subject_602.degree = caluny_degree_13
    caluny_subject_602 = importer.save_or_locate(caluny_subject_602)

    caluny_subject_603 = Subject()
    caluny_subject_603.code = 406
    caluny_subject_603.title = u'Instalaciones y L\xedneas El\xe9ctricas de Alta Tensi\xf3n'
    caluny_subject_603.description = None
    caluny_subject_603.level = None
    caluny_subject_603.degree = caluny_degree_13
    caluny_subject_603 = importer.save_or_locate(caluny_subject_603)

    caluny_subject_604 = Subject()
    caluny_subject_604.code = 405
    caluny_subject_604.title = u'Ingenier\xeda de Control'
    caluny_subject_604.description = None
    caluny_subject_604.level = None
    caluny_subject_604.degree = caluny_degree_13
    caluny_subject_604 = importer.save_or_locate(caluny_subject_604)

    caluny_subject_605 = Subject()
    caluny_subject_605.code = 404
    caluny_subject_605.title = u'Generaci\xf3n El\xe9ctrica con Energ\xedas Renovables'
    caluny_subject_605.description = None
    caluny_subject_605.level = None
    caluny_subject_605.degree = caluny_degree_13
    caluny_subject_605 = importer.save_or_locate(caluny_subject_605)

    caluny_subject_606 = Subject()
    caluny_subject_606.code = 403
    caluny_subject_606.title = u'Electr\xf3nica Industrial Aplicada'
    caluny_subject_606.description = None
    caluny_subject_606.level = None
    caluny_subject_606.degree = caluny_degree_13
    caluny_subject_606 = importer.save_or_locate(caluny_subject_606)

    caluny_subject_607 = Subject()
    caluny_subject_607.code = 402
    caluny_subject_607.title = u'Centrales El\xe9ctricas'
    caluny_subject_607.description = None
    caluny_subject_607.level = None
    caluny_subject_607.degree = caluny_degree_13
    caluny_subject_607 = importer.save_or_locate(caluny_subject_607)

    caluny_subject_608 = Subject()
    caluny_subject_608.code = 401
    caluny_subject_608.title = u'Accionamientos El\xe9ctricos'
    caluny_subject_608.description = None
    caluny_subject_608.level = None
    caluny_subject_608.degree = caluny_degree_13
    caluny_subject_608 = importer.save_or_locate(caluny_subject_608)

    caluny_subject_609 = Subject()
    caluny_subject_609.code = 409
    caluny_subject_609.title = u'Equipos Electr\xf3nicos de Medida'
    caluny_subject_609.description = None
    caluny_subject_609.level = None
    caluny_subject_609.degree = caluny_degree_13
    caluny_subject_609 = importer.save_or_locate(caluny_subject_609)

    caluny_subject_610 = Subject()
    caluny_subject_610.code = 408
    caluny_subject_610.title = u'Dise\xf1o y An\xe1lisis Estructural Asistido'
    caluny_subject_610.description = None
    caluny_subject_610.level = None
    caluny_subject_610.degree = caluny_degree_13
    caluny_subject_610 = importer.save_or_locate(caluny_subject_610)

    caluny_subject_611 = Subject()
    caluny_subject_611.code = 410
    caluny_subject_611.title = u'Explotaci\xf3n de los Sistemas de Energ\xeda El\xe9ctrica'
    caluny_subject_611.description = None
    caluny_subject_611.level = None
    caluny_subject_611.degree = caluny_degree_13
    caluny_subject_611 = importer.save_or_locate(caluny_subject_611)

    caluny_subject_612 = Subject()
    caluny_subject_612.code = 411
    caluny_subject_612.title = u'Programaci\xf3n de Robots industriales'
    caluny_subject_612.description = None
    caluny_subject_612.level = None
    caluny_subject_612.degree = caluny_degree_13
    caluny_subject_612 = importer.save_or_locate(caluny_subject_612)

    caluny_subject_613 = Subject()
    caluny_subject_613.code = 412
    caluny_subject_613.title = u'Trabajo Fin de Grado (Ingenier\xeda El\xe9ctrica)'
    caluny_subject_613.description = None
    caluny_subject_613.level = None
    caluny_subject_613.degree = caluny_degree_13
    caluny_subject_613 = importer.save_or_locate(caluny_subject_613)

    caluny_subject_614 = Subject()
    caluny_subject_614.code = 308
    caluny_subject_614.title = u'Administraci\xf3n de Operaciones'
    caluny_subject_614.description = None
    caluny_subject_614.level = None
    caluny_subject_614.degree = caluny_degree_13
    caluny_subject_614 = importer.save_or_locate(caluny_subject_614)

    caluny_subject_615 = Subject()
    caluny_subject_615.code = 313
    caluny_subject_615.title = u'Oficina T\xe9cnica'
    caluny_subject_615.description = None
    caluny_subject_615.level = None
    caluny_subject_615.degree = caluny_degree_13
    caluny_subject_615 = importer.save_or_locate(caluny_subject_615)

    caluny_subject_616 = Subject()
    caluny_subject_616.code = 312
    caluny_subject_616.title = u'M\xe1quinas El\xe9ctricas 2'
    caluny_subject_616.description = None
    caluny_subject_616.level = None
    caluny_subject_616.degree = caluny_degree_13
    caluny_subject_616 = importer.save_or_locate(caluny_subject_616)

    caluny_subject_617 = Subject()
    caluny_subject_617.code = 311
    caluny_subject_617.title = u'Mantenimiento Industrial'
    caluny_subject_617.description = None
    caluny_subject_617.level = None
    caluny_subject_617.degree = caluny_degree_13
    caluny_subject_617 = importer.save_or_locate(caluny_subject_617)

    caluny_subject_618 = Subject()
    caluny_subject_618.code = 310
    caluny_subject_618.title = u'Instalaciones El\xe9ctricas en Baja y Media Tensi\xf3n'
    caluny_subject_618.description = None
    caluny_subject_618.level = None
    caluny_subject_618.degree = caluny_degree_13
    caluny_subject_618 = importer.save_or_locate(caluny_subject_618)

    caluny_subject_619 = Subject()
    caluny_subject_619.code = 314
    caluny_subject_619.title = u'T\xe9cnicas de Iluminaci\xf3n y Dom\xf3tica'
    caluny_subject_619.description = None
    caluny_subject_619.level = None
    caluny_subject_619.degree = caluny_degree_13
    caluny_subject_619 = importer.save_or_locate(caluny_subject_619)

    caluny_subject_620 = Subject()
    caluny_subject_620.code = 110
    caluny_subject_620.title = u'Qu\xedmica'
    caluny_subject_620.description = None
    caluny_subject_620.level = None
    caluny_subject_620.degree = caluny_degree_13
    caluny_subject_620 = importer.save_or_locate(caluny_subject_620)

    caluny_subject_621 = Subject()
    caluny_subject_621.code = 301
    caluny_subject_621.title = u'An\xe1lisis de Redes El\xe9ctricas'
    caluny_subject_621.description = None
    caluny_subject_621.level = None
    caluny_subject_621.degree = caluny_degree_13
    caluny_subject_621 = importer.save_or_locate(caluny_subject_621)

    caluny_subject_622 = Subject()
    caluny_subject_622.code = 201
    caluny_subject_622.title = u'Ampliaci\xf3n de F\xedsica'
    caluny_subject_622.description = None
    caluny_subject_622.level = None
    caluny_subject_622.degree = caluny_degree_13
    caluny_subject_622 = importer.save_or_locate(caluny_subject_622)

    caluny_subject_623 = Subject()
    caluny_subject_623.code = 309
    caluny_subject_623.title = u'Ingenier\xeda Gr\xe1fica El\xe9ctrica y Topograf\xeda'
    caluny_subject_623.description = None
    caluny_subject_623.level = None
    caluny_subject_623.degree = caluny_degree_13
    caluny_subject_623 = importer.save_or_locate(caluny_subject_623)

    caluny_subject_624 = Subject()
    caluny_subject_624.code = 203
    caluny_subject_624.title = u'Ingl\xe9s aplicado a la ingenier\xeda el\xe9ctrica'
    caluny_subject_624.description = None
    caluny_subject_624.level = None
    caluny_subject_624.degree = caluny_degree_13
    caluny_subject_624 = importer.save_or_locate(caluny_subject_624)

    caluny_subject_625 = Subject()
    caluny_subject_625.code = 202
    caluny_subject_625.title = u'Ingenier\xeda de Fabricaci\xf3n'
    caluny_subject_625.description = None
    caluny_subject_625.level = None
    caluny_subject_625.degree = caluny_degree_13
    caluny_subject_625 = importer.save_or_locate(caluny_subject_625)

    caluny_subject_626 = Subject()
    caluny_subject_626.code = 205
    caluny_subject_626.title = u'Sistemas Inform\xe1ticos'
    caluny_subject_626.description = None
    caluny_subject_626.level = None
    caluny_subject_626.degree = caluny_degree_13
    caluny_subject_626 = importer.save_or_locate(caluny_subject_626)

    caluny_subject_627 = Subject()
    caluny_subject_627.code = 204
    caluny_subject_627.title = u'Resistencia de Materiales'
    caluny_subject_627.description = None
    caluny_subject_627.level = None
    caluny_subject_627.degree = caluny_degree_13
    caluny_subject_627 = importer.save_or_locate(caluny_subject_627)

    caluny_subject_628 = Subject()
    caluny_subject_628.code = 207
    caluny_subject_628.title = u'Termotecnia'
    caluny_subject_628.description = None
    caluny_subject_628.level = None
    caluny_subject_628.degree = caluny_degree_13
    caluny_subject_628 = importer.save_or_locate(caluny_subject_628)

    caluny_subject_629 = Subject()
    caluny_subject_629.code = 206
    caluny_subject_629.title = u'Teor\xeda de M\xe1quinas'
    caluny_subject_629.description = None
    caluny_subject_629.level = None
    caluny_subject_629.degree = caluny_degree_13
    caluny_subject_629 = importer.save_or_locate(caluny_subject_629)

    caluny_subject_630 = Subject()
    caluny_subject_630.code = 209
    caluny_subject_630.title = u'Ciencia de los Materiales'
    caluny_subject_630.description = None
    caluny_subject_630.level = None
    caluny_subject_630.degree = caluny_degree_13
    caluny_subject_630 = importer.save_or_locate(caluny_subject_630)

    caluny_subject_631 = Subject()
    caluny_subject_631.code = 208
    caluny_subject_631.title = u'Autom\xe1tica'
    caluny_subject_631.description = None
    caluny_subject_631.level = None
    caluny_subject_631.degree = caluny_degree_13
    caluny_subject_631 = importer.save_or_locate(caluny_subject_631)

    caluny_subject_632 = Subject()
    caluny_subject_632.code = 302
    caluny_subject_632.title = u'Elementos de Tecnolog\xeda El\xe9ctrica'
    caluny_subject_632.description = None
    caluny_subject_632.level = None
    caluny_subject_632.degree = caluny_degree_13
    caluny_subject_632 = importer.save_or_locate(caluny_subject_632)

    caluny_subject_633 = Subject()
    caluny_subject_633.code = 303
    caluny_subject_633.title = u'Medidas El\xe9ctricas'
    caluny_subject_633.description = None
    caluny_subject_633.level = None
    caluny_subject_633.degree = caluny_degree_13
    caluny_subject_633 = importer.save_or_locate(caluny_subject_633)

    caluny_subject_634 = Subject()
    caluny_subject_634.code = 304
    caluny_subject_634.title = u'Motores T\xe9rmicos'
    caluny_subject_634.description = None
    caluny_subject_634.level = None
    caluny_subject_634.degree = caluny_degree_13
    caluny_subject_634 = importer.save_or_locate(caluny_subject_634)

    caluny_subject_635 = Subject()
    caluny_subject_635.code = 305
    caluny_subject_635.title = u'M\xe1quinas El\xe9ctricas 1'
    caluny_subject_635.description = None
    caluny_subject_635.level = None
    caluny_subject_635.degree = caluny_degree_13
    caluny_subject_635 = importer.save_or_locate(caluny_subject_635)

    caluny_subject_636 = Subject()
    caluny_subject_636.code = 306
    caluny_subject_636.title = u'Regulaci\xf3n Autom\xe1tica'
    caluny_subject_636.description = None
    caluny_subject_636.level = None
    caluny_subject_636.degree = caluny_degree_13
    caluny_subject_636 = importer.save_or_locate(caluny_subject_636)

    caluny_subject_637 = Subject()
    caluny_subject_637.code = 307
    caluny_subject_637.title = u'Seguridad y Salud Laboral'
    caluny_subject_637.description = None
    caluny_subject_637.level = None
    caluny_subject_637.degree = caluny_degree_13
    caluny_subject_637 = importer.save_or_locate(caluny_subject_637)

    caluny_subject_638 = Subject()
    caluny_subject_638.code = 108
    caluny_subject_638.title = u'F\xedsica 2'
    caluny_subject_638.description = None
    caluny_subject_638.level = None
    caluny_subject_638.degree = caluny_degree_13
    caluny_subject_638 = importer.save_or_locate(caluny_subject_638)

    caluny_subject_639 = Subject()
    caluny_subject_639.code = 109
    caluny_subject_639.title = u'Gesti\xf3n de Empresas'
    caluny_subject_639.description = None
    caluny_subject_639.level = None
    caluny_subject_639.degree = caluny_degree_13
    caluny_subject_639 = importer.save_or_locate(caluny_subject_639)

    caluny_subject_640 = Subject()
    caluny_subject_640.code = 102
    caluny_subject_640.title = u'C\xe1lculo'
    caluny_subject_640.description = None
    caluny_subject_640.level = None
    caluny_subject_640.degree = caluny_degree_13
    caluny_subject_640 = importer.save_or_locate(caluny_subject_640)

    caluny_subject_641 = Subject()
    caluny_subject_641.code = 103
    caluny_subject_641.title = u'Expresi\xf3n Gr\xe1fica en la Ingenier\xeda'
    caluny_subject_641.description = None
    caluny_subject_641.level = None
    caluny_subject_641.degree = caluny_degree_13
    caluny_subject_641 = importer.save_or_locate(caluny_subject_641)

    caluny_subject_642 = Subject()
    caluny_subject_642.code = 101
    caluny_subject_642.title = u'\xc1lgebra Lineal'
    caluny_subject_642.description = None
    caluny_subject_642.level = None
    caluny_subject_642.degree = caluny_degree_13
    caluny_subject_642 = importer.save_or_locate(caluny_subject_642)

    caluny_subject_643 = Subject()
    caluny_subject_643.code = 106
    caluny_subject_643.title = u'Ampliaci\xf3n de C\xe1lculo'
    caluny_subject_643.description = None
    caluny_subject_643.level = None
    caluny_subject_643.degree = caluny_degree_13
    caluny_subject_643 = importer.save_or_locate(caluny_subject_643)

    caluny_subject_644 = Subject()
    caluny_subject_644.code = 107
    caluny_subject_644.title = u'An\xe1lisis Vectorial y Estad\xedstico'
    caluny_subject_644.description = None
    caluny_subject_644.level = None
    caluny_subject_644.degree = caluny_degree_13
    caluny_subject_644 = importer.save_or_locate(caluny_subject_644)

    caluny_subject_645 = Subject()
    caluny_subject_645.code = 104
    caluny_subject_645.title = u'Fundamentos de Inform\xe1tica'
    caluny_subject_645.description = None
    caluny_subject_645.level = None
    caluny_subject_645.degree = caluny_degree_13
    caluny_subject_645 = importer.save_or_locate(caluny_subject_645)

    caluny_subject_646 = Subject()
    caluny_subject_646.code = 105
    caluny_subject_646.title = u'F\xedsica 1'
    caluny_subject_646.description = None
    caluny_subject_646.level = None
    caluny_subject_646.degree = caluny_degree_13
    caluny_subject_646 = importer.save_or_locate(caluny_subject_646)

    # Processing model: ExtraTitle

    from core.models import ExtraTitle


    # Processing model: CourseLabel

    from core.models import CourseLabel

    caluny_courselabel_1 = CourseLabel()
    caluny_courselabel_1.name = u'A'
    caluny_courselabel_1 = importer.save_or_locate(caluny_courselabel_1)

    caluny_courselabel_2 = CourseLabel()
    caluny_courselabel_2.name = u'B'
    caluny_courselabel_2 = importer.save_or_locate(caluny_courselabel_2)

    caluny_courselabel_3 = CourseLabel()
    caluny_courselabel_3.name = u'C'
    caluny_courselabel_3 = importer.save_or_locate(caluny_courselabel_3)

    caluny_courselabel_4 = CourseLabel()
    caluny_courselabel_4.name = u'D'
    caluny_courselabel_4 = importer.save_or_locate(caluny_courselabel_4)

    caluny_courselabel_5 = CourseLabel()
    caluny_courselabel_5.name = u'A (MSI)'
    caluny_courselabel_5 = importer.save_or_locate(caluny_courselabel_5)

    caluny_courselabel_6 = CourseLabel()
    caluny_courselabel_6.name = u'A (MC)'
    caluny_courselabel_6 = importer.save_or_locate(caluny_courselabel_6)

    caluny_courselabel_7 = CourseLabel()
    caluny_courselabel_7.name = u'A (MTI)'
    caluny_courselabel_7 = importer.save_or_locate(caluny_courselabel_7)

    caluny_courselabel_8 = CourseLabel()
    caluny_courselabel_8.name = u'Optativas'
    caluny_courselabel_8 = importer.save_or_locate(caluny_courselabel_8)

    # Processing model: SemesterDate

    from core.models import SemesterDate

    caluny_semesterdate_1 = SemesterDate()
    caluny_semesterdate_1.date = dateutil.parser.parse("2014-09-29")
    caluny_semesterdate_1 = importer.save_or_locate(caluny_semesterdate_1)

    caluny_semesterdate_2 = SemesterDate()
    caluny_semesterdate_2.date = dateutil.parser.parse("2015-01-04")
    caluny_semesterdate_2 = importer.save_or_locate(caluny_semesterdate_2)

    caluny_semesterdate_3 = SemesterDate()
    caluny_semesterdate_3.date = dateutil.parser.parse("2015-02-17")
    caluny_semesterdate_3 = importer.save_or_locate(caluny_semesterdate_3)

    caluny_semesterdate_4 = SemesterDate()
    caluny_semesterdate_4.date = dateutil.parser.parse("2015-06-05")
    caluny_semesterdate_4 = importer.save_or_locate(caluny_semesterdate_4)

    caluny_semesterdate_5 = SemesterDate()
    caluny_semesterdate_5.date = dateutil.parser.parse("2014-09-14")
    caluny_semesterdate_5 = importer.save_or_locate(caluny_semesterdate_5)

    caluny_semesterdate_6 = SemesterDate()
    caluny_semesterdate_6.date = dateutil.parser.parse("2015-01-09")
    caluny_semesterdate_6 = importer.save_or_locate(caluny_semesterdate_6)

    # Processing model: Course

    from core.models import Course

    caluny_course_1 = Course()
    caluny_course_1.label = caluny_courselabel_2
    caluny_course_1.language = u'es'
    caluny_course_1.first_semester_start = caluny_semesterdate_5
    caluny_course_1.first_semester_end = caluny_semesterdate_6
    caluny_course_1.second_semester_start = caluny_semesterdate_3
    caluny_course_1.second_semester_end = caluny_semesterdate_4
    caluny_course_1.level = caluny_level_1
    caluny_course_1.degree = caluny_degree_4
    caluny_course_1 = importer.save_or_locate(caluny_course_1)

    caluny_course_2 = Course()
    caluny_course_2.label = caluny_courselabel_1
    caluny_course_2.language = u'es'
    caluny_course_2.first_semester_start = caluny_semesterdate_5
    caluny_course_2.first_semester_end = caluny_semesterdate_6
    caluny_course_2.second_semester_start = caluny_semesterdate_3
    caluny_course_2.second_semester_end = caluny_semesterdate_4
    caluny_course_2.level = caluny_level_1
    caluny_course_2.degree = caluny_degree_4
    caluny_course_2 = importer.save_or_locate(caluny_course_2)

    caluny_course_3 = Course()
    caluny_course_3.label = caluny_courselabel_3
    caluny_course_3.language = u'es'
    caluny_course_3.first_semester_start = caluny_semesterdate_5
    caluny_course_3.first_semester_end = caluny_semesterdate_6
    caluny_course_3.second_semester_start = caluny_semesterdate_3
    caluny_course_3.second_semester_end = caluny_semesterdate_4
    caluny_course_3.level = caluny_level_1
    caluny_course_3.degree = caluny_degree_4
    caluny_course_3 = importer.save_or_locate(caluny_course_3)

    caluny_course_4 = Course()
    caluny_course_4.label = caluny_courselabel_3
    caluny_course_4.language = u'es'
    caluny_course_4.first_semester_start = caluny_semesterdate_1
    caluny_course_4.first_semester_end = caluny_semesterdate_2
    caluny_course_4.second_semester_start = caluny_semesterdate_3
    caluny_course_4.second_semester_end = caluny_semesterdate_4
    caluny_course_4.level = caluny_level_2
    caluny_course_4.degree = caluny_degree_4
    caluny_course_4 = importer.save_or_locate(caluny_course_4)

    caluny_course_5 = Course()
    caluny_course_5.label = caluny_courselabel_2
    caluny_course_5.language = u'en'
    caluny_course_5.first_semester_start = caluny_semesterdate_1
    caluny_course_5.first_semester_end = caluny_semesterdate_2
    caluny_course_5.second_semester_start = caluny_semesterdate_3
    caluny_course_5.second_semester_end = caluny_semesterdate_4
    caluny_course_5.level = caluny_level_2
    caluny_course_5.degree = caluny_degree_4
    caluny_course_5 = importer.save_or_locate(caluny_course_5)

    caluny_course_6 = Course()
    caluny_course_6.label = caluny_courselabel_4
    caluny_course_6.language = u'en'
    caluny_course_6.first_semester_start = caluny_semesterdate_5
    caluny_course_6.first_semester_end = caluny_semesterdate_6
    caluny_course_6.second_semester_start = caluny_semesterdate_3
    caluny_course_6.second_semester_end = caluny_semesterdate_4
    caluny_course_6.level = caluny_level_1
    caluny_course_6.degree = caluny_degree_4
    caluny_course_6 = importer.save_or_locate(caluny_course_6)

    caluny_course_7 = Course()
    caluny_course_7.label = caluny_courselabel_1
    caluny_course_7.language = u'es'
    caluny_course_7.first_semester_start = caluny_semesterdate_1
    caluny_course_7.first_semester_end = caluny_semesterdate_2
    caluny_course_7.second_semester_start = caluny_semesterdate_3
    caluny_course_7.second_semester_end = caluny_semesterdate_4
    caluny_course_7.level = caluny_level_2
    caluny_course_7.degree = caluny_degree_4
    caluny_course_7 = importer.save_or_locate(caluny_course_7)

    caluny_course_8 = Course()
    caluny_course_8.label = caluny_courselabel_1
    caluny_course_8.language = u'es'
    caluny_course_8.first_semester_start = caluny_semesterdate_1
    caluny_course_8.first_semester_end = caluny_semesterdate_2
    caluny_course_8.second_semester_start = caluny_semesterdate_3
    caluny_course_8.second_semester_end = caluny_semesterdate_4
    caluny_course_8.level = caluny_level_3
    caluny_course_8.degree = caluny_degree_4
    caluny_course_8 = importer.save_or_locate(caluny_course_8)

    caluny_course_9 = Course()
    caluny_course_9.label = caluny_courselabel_5
    caluny_course_9.language = u'es'
    caluny_course_9.first_semester_start = caluny_semesterdate_1
    caluny_course_9.first_semester_end = caluny_semesterdate_2
    caluny_course_9.second_semester_start = caluny_semesterdate_3
    caluny_course_9.second_semester_end = caluny_semesterdate_4
    caluny_course_9.level = caluny_level_4
    caluny_course_9.degree = caluny_degree_4
    caluny_course_9 = importer.save_or_locate(caluny_course_9)

    caluny_course_10 = Course()
    caluny_course_10.label = caluny_courselabel_6
    caluny_course_10.language = u'es'
    caluny_course_10.first_semester_start = caluny_semesterdate_1
    caluny_course_10.first_semester_end = caluny_semesterdate_2
    caluny_course_10.second_semester_start = caluny_semesterdate_3
    caluny_course_10.second_semester_end = caluny_semesterdate_4
    caluny_course_10.level = caluny_level_4
    caluny_course_10.degree = caluny_degree_4
    caluny_course_10 = importer.save_or_locate(caluny_course_10)

    caluny_course_11 = Course()
    caluny_course_11.label = caluny_courselabel_7
    caluny_course_11.language = u'es'
    caluny_course_11.first_semester_start = caluny_semesterdate_1
    caluny_course_11.first_semester_end = caluny_semesterdate_2
    caluny_course_11.second_semester_start = caluny_semesterdate_3
    caluny_course_11.second_semester_end = caluny_semesterdate_4
    caluny_course_11.level = caluny_level_4
    caluny_course_11.degree = caluny_degree_4
    caluny_course_11 = importer.save_or_locate(caluny_course_11)

    caluny_course_12 = Course()
    caluny_course_12.label = caluny_courselabel_8
    caluny_course_12.language = u'es'
    caluny_course_12.first_semester_start = caluny_semesterdate_1
    caluny_course_12.first_semester_end = caluny_semesterdate_2
    caluny_course_12.second_semester_start = caluny_semesterdate_3
    caluny_course_12.second_semester_end = caluny_semesterdate_4
    caluny_course_12.level = None
    caluny_course_12.degree = caluny_degree_4
    caluny_course_12 = importer.save_or_locate(caluny_course_12)

    # Processing model: TeachingSubject

    from core.models import TeachingSubject

    caluny_teachingsubject_1 = TeachingSubject()
    caluny_teachingsubject_1.address = u'Aula 2.0.8'
    caluny_teachingsubject_1.course = caluny_course_2
    caluny_teachingsubject_1.subject = caluny_subject_133
    caluny_teachingsubject_1.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_1.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_1 = importer.save_or_locate(caluny_teachingsubject_1)

    caluny_teachingsubject_1.students.add(caluny_student_1)
    caluny_teachingsubject_1.teachers.add(caluny_teacher_1)

    caluny_teachingsubject_2 = TeachingSubject()
    caluny_teachingsubject_2.address = u'Aula 2.0.8'
    caluny_teachingsubject_2.course = caluny_course_2
    caluny_teachingsubject_2.subject = caluny_subject_286
    caluny_teachingsubject_2.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_2.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_2 = importer.save_or_locate(caluny_teachingsubject_2)

    caluny_teachingsubject_2.students.add(caluny_student_1)
    caluny_teachingsubject_2.teachers.add(caluny_teacher_1)

    caluny_teachingsubject_3 = TeachingSubject()
    caluny_teachingsubject_3.address = u'Aula 2.0.8'
    caluny_teachingsubject_3.course = caluny_course_2
    caluny_teachingsubject_3.subject = caluny_subject_136
    caluny_teachingsubject_3.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_3.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_3 = importer.save_or_locate(caluny_teachingsubject_3)

    caluny_teachingsubject_4 = TeachingSubject()
    caluny_teachingsubject_4.address = u'687 clase super guay'
    caluny_teachingsubject_4.course = caluny_course_7
    caluny_teachingsubject_4.subject = caluny_subject_21
    caluny_teachingsubject_4.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_4.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_4 = importer.save_or_locate(caluny_teachingsubject_4)

    caluny_teachingsubject_5 = TeachingSubject()
    caluny_teachingsubject_5.address = u'super guaysss'
    caluny_teachingsubject_5.course = caluny_course_8
    caluny_teachingsubject_5.subject = caluny_subject_20
    caluny_teachingsubject_5.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_5.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_5 = importer.save_or_locate(caluny_teachingsubject_5)

    caluny_teachingsubject_5.students.add(caluny_student_1)
    caluny_teachingsubject_5.teachers.add(caluny_teacher_2)

    caluny_teachingsubject_6 = TeachingSubject()
    caluny_teachingsubject_6.address = u'En la clase leche'
    caluny_teachingsubject_6.course = caluny_course_2
    caluny_teachingsubject_6.subject = caluny_subject_39
    caluny_teachingsubject_6.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_6.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_6 = importer.save_or_locate(caluny_teachingsubject_6)

    caluny_teachingsubject_6.students.add(caluny_student_2)
    caluny_teachingsubject_6.teachers.add(caluny_teacher_1)

    caluny_teachingsubject_7 = TeachingSubject()
    caluny_teachingsubject_7.address = u'Facultad de derecho'
    caluny_teachingsubject_7.course = caluny_course_2
    caluny_teachingsubject_7.subject = caluny_subject_41
    caluny_teachingsubject_7.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_7.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_7 = importer.save_or_locate(caluny_teachingsubject_7)

    caluny_teachingsubject_7.students.add(caluny_student_2)
    caluny_teachingsubject_7.teachers.add(caluny_teacher_1)

    caluny_teachingsubject_8 = TeachingSubject()
    caluny_teachingsubject_8.address = u'Facultad de derecho'
    caluny_teachingsubject_8.course = caluny_course_2
    caluny_teachingsubject_8.subject = caluny_subject_40
    caluny_teachingsubject_8.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_8.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_8 = importer.save_or_locate(caluny_teachingsubject_8)

    caluny_teachingsubject_8.students.add(caluny_student_2)
    caluny_teachingsubject_8.teachers.add(caluny_teacher_2)

    caluny_teachingsubject_9 = TeachingSubject()
    caluny_teachingsubject_9.address = u'Facultad de derecho'
    caluny_teachingsubject_9.course = caluny_course_1
    caluny_teachingsubject_9.subject = caluny_subject_44
    caluny_teachingsubject_9.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_9.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_9 = importer.save_or_locate(caluny_teachingsubject_9)

    caluny_teachingsubject_9.students.add(caluny_student_1)
    caluny_teachingsubject_9.students.add(caluny_student_2)
    caluny_teachingsubject_9.teachers.add(caluny_teacher_2)

    caluny_teachingsubject_10 = TeachingSubject()
    caluny_teachingsubject_10.address = u'Facultad de derecho'
    caluny_teachingsubject_10.course = caluny_course_4
    caluny_teachingsubject_10.subject = caluny_subject_1
    caluny_teachingsubject_10.start_date = dateutil.parser.parse("2014-09-15")
    caluny_teachingsubject_10.end_date = dateutil.parser.parse("2015-01-17")
    caluny_teachingsubject_10 = importer.save_or_locate(caluny_teachingsubject_10)

    caluny_teachingsubject_10.students.add(caluny_student_1)
    caluny_teachingsubject_10.students.add(caluny_student_2)
    caluny_teachingsubject_10.teachers.add(caluny_teacher_1)

    # Processing model: Exam

    from core.models import Exam

    caluny_exam_1 = Exam()
    caluny_exam_1.title = u'Examen final de Calculo'
    caluny_exam_1.address = u'Donde quieras'
    caluny_exam_1.date = dateutil.parser.parse("2015-01-01")
    caluny_exam_1.start_time = datetime.time(10, 0)
    caluny_exam_1.end_time = datetime.time(10, 0)
    caluny_exam_1.description = None
    caluny_exam_1.t_subject = caluny_teachingsubject_1
    caluny_exam_1 = importer.save_or_locate(caluny_exam_1)

    caluny_exam_2 = Exam()
    caluny_exam_2.title = u'Examen final de Procedimientos Tributarios'
    caluny_exam_2.address = u'En la sala de examenes'
    caluny_exam_2.date = dateutil.parser.parse("2015-01-26")
    caluny_exam_2.start_time = datetime.time(10, 0)
    caluny_exam_2.end_time = datetime.time(14, 0)
    caluny_exam_2.description = u'Aqu\xed se va a ver de verdad quien sabe y quien no!'
    caluny_exam_2.t_subject = caluny_teachingsubject_10
    caluny_exam_2 = importer.save_or_locate(caluny_exam_2)

    # Processing model: Timetable

    from core.models import Timetable

    caluny_timetable_1 = Timetable()
    caluny_timetable_1.start_time = datetime.time(10, 0)
    caluny_timetable_1.end_time = datetime.time(10, 45)
    caluny_timetable_1.week_day = u'1'
    caluny_timetable_1.description = u''
    caluny_timetable_1.period = u'1'
    caluny_timetable_1.t_subject = caluny_teachingsubject_1
    caluny_timetable_1 = importer.save_or_locate(caluny_timetable_1)

    caluny_timetable_2 = Timetable()
    caluny_timetable_2.start_time = datetime.time(10, 0)
    caluny_timetable_2.end_time = datetime.time(12, 45)
    caluny_timetable_2.week_day = u'2'
    caluny_timetable_2.description = u''
    caluny_timetable_2.period = u'1'
    caluny_timetable_2.t_subject = caluny_teachingsubject_1
    caluny_timetable_2 = importer.save_or_locate(caluny_timetable_2)

    caluny_timetable_3 = Timetable()
    caluny_timetable_3.start_time = datetime.time(10, 0)
    caluny_timetable_3.end_time = datetime.time(8, 45)
    caluny_timetable_3.week_day = u'3'
    caluny_timetable_3.description = u''
    caluny_timetable_3.period = u'1'
    caluny_timetable_3.t_subject = caluny_teachingsubject_1
    caluny_timetable_3 = importer.save_or_locate(caluny_timetable_3)

    caluny_timetable_4 = Timetable()
    caluny_timetable_4.start_time = datetime.time(10, 0)
    caluny_timetable_4.end_time = datetime.time(10, 45)
    caluny_timetable_4.week_day = u'2'
    caluny_timetable_4.description = u'Todo lo que se puede saber y ense\xf1ar de Matem\xe1tica discreta'
    caluny_timetable_4.period = u'1'
    caluny_timetable_4.t_subject = caluny_teachingsubject_2
    caluny_timetable_4 = importer.save_or_locate(caluny_timetable_4)

    caluny_timetable_5 = Timetable()
    caluny_timetable_5.start_time = datetime.time(10, 0)
    caluny_timetable_5.end_time = datetime.time(12, 45)
    caluny_timetable_5.week_day = u'4'
    caluny_timetable_5.description = u'Mas matem\xe1ticas pero un poco mas tarde y los jueves'
    caluny_timetable_5.period = u'1'
    caluny_timetable_5.t_subject = caluny_teachingsubject_2
    caluny_timetable_5 = importer.save_or_locate(caluny_timetable_5)

    caluny_timetable_6 = Timetable()
    caluny_timetable_6.start_time = datetime.time(10, 0)
    caluny_timetable_6.end_time = datetime.time(12, 45)
    caluny_timetable_6.week_day = u'5'
    caluny_timetable_6.description = u''
    caluny_timetable_6.period = u'1'
    caluny_timetable_6.t_subject = caluny_teachingsubject_2
    caluny_timetable_6 = importer.save_or_locate(caluny_timetable_6)

    caluny_timetable_7 = Timetable()
    caluny_timetable_7.start_time = datetime.time(10, 0)
    caluny_timetable_7.end_time = datetime.time(12, 45)
    caluny_timetable_7.week_day = u'1'
    caluny_timetable_7.description = u''
    caluny_timetable_7.period = u'1'
    caluny_timetable_7.t_subject = caluny_teachingsubject_3
    caluny_timetable_7 = importer.save_or_locate(caluny_timetable_7)

    caluny_timetable_8 = Timetable()
    caluny_timetable_8.start_time = datetime.time(10, 0)
    caluny_timetable_8.end_time = datetime.time(10, 45)
    caluny_timetable_8.week_day = u'3'
    caluny_timetable_8.description = u''
    caluny_timetable_8.period = u'1'
    caluny_timetable_8.t_subject = caluny_teachingsubject_3
    caluny_timetable_8 = importer.save_or_locate(caluny_timetable_8)

    caluny_timetable_9 = Timetable()
    caluny_timetable_9.start_time = datetime.time(10, 0)
    caluny_timetable_9.end_time = datetime.time(8, 45)
    caluny_timetable_9.week_day = u'4'
    caluny_timetable_9.description = u'k'
    caluny_timetable_9.period = u'1'
    caluny_timetable_9.t_subject = caluny_teachingsubject_3
    caluny_timetable_9 = importer.save_or_locate(caluny_timetable_9)

    caluny_timetable_10 = Timetable()
    caluny_timetable_10.start_time = datetime.time(10, 0)
    caluny_timetable_10.end_time = datetime.time(9, 0)
    caluny_timetable_10.week_day = u'1'
    caluny_timetable_10.description = u''
    caluny_timetable_10.period = u'1'
    caluny_timetable_10.t_subject = caluny_teachingsubject_6
    caluny_timetable_10 = importer.save_or_locate(caluny_timetable_10)

    caluny_timetable_11 = Timetable()
    caluny_timetable_11.start_time = datetime.time(10, 0)
    caluny_timetable_11.end_time = datetime.time(10, 0)
    caluny_timetable_11.week_day = u'2'
    caluny_timetable_11.description = u''
    caluny_timetable_11.period = u'1'
    caluny_timetable_11.t_subject = caluny_teachingsubject_5
    caluny_timetable_11 = importer.save_or_locate(caluny_timetable_11)

    caluny_timetable_12 = Timetable()
    caluny_timetable_12.start_time = datetime.time(10, 0)
    caluny_timetable_12.end_time = datetime.time(14, 0)
    caluny_timetable_12.week_day = u'5'
    caluny_timetable_12.description = u''
    caluny_timetable_12.period = u'1'
    caluny_timetable_12.t_subject = caluny_teachingsubject_4
    caluny_timetable_12 = importer.save_or_locate(caluny_timetable_12)

    caluny_timetable_13 = Timetable()
    caluny_timetable_13.start_time = datetime.time(10, 0)
    caluny_timetable_13.end_time = datetime.time(10, 0)
    caluny_timetable_13.week_day = u'3'
    caluny_timetable_13.description = u''
    caluny_timetable_13.period = u'1'
    caluny_timetable_13.t_subject = caluny_teachingsubject_5
    caluny_timetable_13 = importer.save_or_locate(caluny_timetable_13)

    caluny_timetable_14 = Timetable()
    caluny_timetable_14.start_time = datetime.time(10, 0)
    caluny_timetable_14.end_time = datetime.time(10, 30)
    caluny_timetable_14.week_day = u'2'
    caluny_timetable_14.description = u'Clases super importantes de derecho constitucional'
    caluny_timetable_14.period = u'1'
    caluny_timetable_14.t_subject = caluny_teachingsubject_7
    caluny_timetable_14 = importer.save_or_locate(caluny_timetable_14)

    caluny_timetable_15 = Timetable()
    caluny_timetable_15.start_time = datetime.time(10, 0)
    caluny_timetable_15.end_time = datetime.time(14, 0)
    caluny_timetable_15.week_day = u'4'
    caluny_timetable_15.description = u'Clases super importantes de derecho constitucional'
    caluny_timetable_15.period = u'1'
    caluny_timetable_15.t_subject = caluny_teachingsubject_7
    caluny_timetable_15 = importer.save_or_locate(caluny_timetable_15)

    caluny_timetable_16 = Timetable()
    caluny_timetable_16.start_time = datetime.time(11, 5, 12)
    caluny_timetable_16.end_time = datetime.time(15, 0)
    caluny_timetable_16.week_day = u'1'
    caluny_timetable_16.description = u'Clase de los lunes por la ma\xf1ana'
    caluny_timetable_16.period = u'1'
    caluny_timetable_16.t_subject = caluny_teachingsubject_10
    caluny_timetable_16 = importer.save_or_locate(caluny_timetable_16)

    caluny_timetable_17 = Timetable()
    caluny_timetable_17.start_time = datetime.time(9, 0)
    caluny_timetable_17.end_time = datetime.time(12, 0)
    caluny_timetable_17.week_day = u'3'
    caluny_timetable_17.description = u'Clase de los miercoles por la ma\xf1ana tempranito'
    caluny_timetable_17.period = u'1'
    caluny_timetable_17.t_subject = caluny_teachingsubject_10
    caluny_timetable_17 = importer.save_or_locate(caluny_timetable_17)

    caluny_timetable_18 = Timetable()
    caluny_timetable_18.start_time = datetime.time(18, 0)
    caluny_timetable_18.end_time = datetime.time(19, 0)
    caluny_timetable_18.week_day = u'7'
    caluny_timetable_18.description = u'El domingo hay que echar un ratejo'
    caluny_timetable_18.period = u'1'
    caluny_timetable_18.t_subject = caluny_teachingsubject_10
    caluny_timetable_18 = importer.save_or_locate(caluny_timetable_18)

