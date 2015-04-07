# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.test import TestCase, Client
from rest_framework.authtoken.models import Token
import json

from core.models import Student, Teacher


TEST_STUDENT_USERNAME = 'STUDENT1'
TEST_STUDENT_PASS = 'STUDENT1'
TEST_TEACHER_USERNAME = 'TEACHER1'
TEST_TEACHER_PASS = 'TEACHER1'
TEACHER_ROLE = 'TEAC'
STUDENT_ROLE = 'STUD'


class UsersTestCase(TestCase):
    def setUp(self):
        s = Student.objects.create(username=TEST_STUDENT_USERNAME)
        s.set_password(TEST_STUDENT_PASS)
        s.save()
        self.student = s
        self.token = Token.objects.get(user=Student.objects.get(username=TEST_STUDENT_USERNAME))
        self.client = Client()

    def tearDown(self):
        Student.objects.filter(username=TEST_STUDENT_USERNAME).delete()

    def test_get_token_student(self):
        token = Token.objects.get(user=Student.objects.get(username='STUDENT1'))
        self.assertIsNotNone(token)
        r = self.client.post(reverse('obtain_token'), {'username': TEST_STUDENT_USERNAME,
                                                       'password': TEST_STUDENT_PASS})
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.data.get('token'))
        self.assertEqual(r.data.get('token'), token.key)

    def test_un_and_authorized_user(self):
        r = self.client.get('/')
        self.assertIsNotNone(r)
        self.assertEqual(r.status_code, 401)
        r = self.client.get('/', **{'HTTP_AUTHORIZATION': ' token ' + str(self.token.key)})
        self.assertEqual(r.status_code, 200)
        r = self.client.get('/schools', follow=True, **{'HTTP_AUTHORIZATION': ' token ' + str(self.token.key)})
        self.assertIsInstance(r.data.get('results'), list)

    def test_student_has_token(self):
        token = Token.objects.get(user=Student.objects.get(username='STUDENT1'))
        self.assertIsNotNone(token)
        self.assertIsInstance(token, Token)


class CreateUsers(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_user_with_get(self):
        r = self.client.get(reverse('caluny:create_user'))
        self.assertEqual(r.status_code, 405)

    def test_create_teacher(self):
        r = self.client.post(reverse('caluny:create_user'), {'username': TEST_TEACHER_USERNAME,
                                                             'password': TEST_TEACHER_PASS,
                                                             'dept': u"Matemática aplicada",
                                                             'description': u'Descripción de este profesor',
                                                             'role': TEACHER_ROLE})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        token_key = data.get('token')
        teacher = Teacher.objects.get(username=TEST_TEACHER_USERNAME)
        self.assertIsNotNone(teacher)
        self.assertEqual(Token.objects.get(user=teacher).key, token_key)
        r = self.client.get('/schools', follow=True, **{'HTTP_AUTHORIZATION': ' token ' + str(token_key)})
        self.assertIsInstance(r.data.get('results'), list)

    def test_create_student(self):
        r = self.client.post(reverse('caluny:create_user'), {'username': TEST_STUDENT_USERNAME,
                                                             'password': TEST_STUDENT_PASS,
                                                             'role': STUDENT_ROLE})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        token_key = data.get('token')
        student = Student.objects.get(username=TEST_STUDENT_USERNAME)
        self.assertIsNotNone(student)
        self.assertEqual(Token.objects.get(user=student).key, token_key)
        r = self.client.get('/schools', follow=True, **{'HTTP_AUTHORIZATION': ' token ' + str(token_key)})
        self.assertIsInstance(r.data.get('results'), list)