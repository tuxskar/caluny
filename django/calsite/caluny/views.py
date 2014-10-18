from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
import caluny.serializers
from caluny.models import School, University, Subject, Degree, TeachingSubject, Course
from caluny.models import Timetable, Exam

class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    """Schools view for REST """
    queryset = School.objects.all()
    serializer_class = caluny.serializers.SchoolSerializer

class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    """University view for REST """
    queryset = University.objects.all()
    serializer_class = caluny.serializers.UniversitySerializer

class SubjectViewSetSimple(viewsets.ReadOnlyModelViewSet):
    """Subject view simple for REST """
    queryset = Subject.objects.all()
    serializer_class = caluny.serializers.SubjectSerializerSimple

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Subject view with details for REST """
    queryset = Subject.objects.all()
    serializer_class = caluny.serializers.SubjectSerializer

class DegreeViewSet(viewsets.ReadOnlyModelViewSet):
    """Degrees view set for REST """
    queryset = Degree.objects.all()
    serializer_class = caluny.serializers.DegreeSerializer

class DegreeViewDetailSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Degree.objects.all()
    serializer_class = caluny.serializers.DegreeSerializerAll

class TeachingSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = TeachingSubject.objects.all()
    serializer_class = caluny.serializers.TeachingSubjectSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Course.objects.all()
    serializer_class = caluny.serializers.CourseSerializer

class TimetableViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Timetable.objects.all()
    serializer_class = caluny.serializers.TimetableSerializer

class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Exam.objects.all()
    serializer_class = caluny.serializers.ExamSerializer
