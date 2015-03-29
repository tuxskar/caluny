from __future__ import absolute_import
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
import core.serializers
from .models import School, University, Subject, Degree, TeachingSubject, Course
from .models import Timetable, Exam

class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    """Schools view for REST """
    queryset = School.objects.all()
    serializer_class = core.serializers.SchoolSerializer

class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    """University view for REST """
    queryset = University.objects.all()
    serializer_class = core.serializers.UniversitySerializer

class SubjectViewSetSimple(viewsets.ReadOnlyModelViewSet):
    """Subject view simple for REST """
    queryset = Subject.objects.all()
    serializer_class = core.serializers.SubjectSerializerSimple

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Subject view with details for REST """
    queryset = Subject.objects.all()
    serializer_class = core.serializers.SubjectSerializer

class DegreeViewSet(viewsets.ReadOnlyModelViewSet):
    """Degrees view set for REST """
    queryset = Degree.objects.all()
    serializer_class = core.serializers.DegreeSerializer

class DegreeViewDetailSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Degree.objects.all()
    serializer_class = core.serializers.DegreeSerializerAll

class TeachingSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = TeachingSubject.objects.all()
    serializer_class = core.serializers.TeachingSubjectSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Course.objects.all()
    serializer_class = core.serializers.CourseSerializer

class TimetableViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Timetable.objects.all()
    serializer_class = core.serializers.TimetableSerializer

class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Exam.objects.all()
    serializer_class = core.serializers.ExamSerializer
