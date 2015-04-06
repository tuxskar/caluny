from django.test import TestCase, Client

from rest_framework.authtoken.models import Token
from core.models import Student


class UsersTestCase(TestCase):
    TEST_STUDENT_USERNAME = 'student1'
    TEST_STUDENT_PASS = 'student1'

    def setUp(self):
        s = Student.objects.create(username=self.TEST_STUDENT_USERNAME)
        s.set_password(self.TEST_STUDENT_PASS)
        s.save()
        self.student = s
        self.token = Token.objects.get(user=Student.objects.get(username=self.TEST_STUDENT_USERNAME))
        self.client = Client()

    def tearDown(self):
        Student.objects.filter(username=self.TEST_STUDENT_USERNAME).delete()

    def test_get_token_student(self):
        token = Token.objects.get(user=Student.objects.get(username='student1'))
        self.assertIsNotNone(token)

    def test_un_and_authorized_user(self):
        r = self.client.get('/')
        self.assertIsNotNone(r)
        self.assertEqual(r.status_code, 401)
        r = self.client.get('/', **{'HTTP_AUTHORIZATION': ' token ' + str(self.token.key)})
        self.assertEqual(r.status_code, 200)

    def test_student_has_token(self):
        token = Token.objects.get(user=Student.objects.get(username='student1'))
        self.assertIsNotNone(token)
        self.assertIsInstance(token, Token)