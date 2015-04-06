from rest_framework import viewsets

from core.models import School, University, Subject, Degree, TeachingSubject, Course
from core.models import Timetable, Exam
from caluny_api import serializers



class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    """Schools view for REST """
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer


class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    """University view for REST """
    queryset = University.objects.all()
    serializer_class = serializers.UniversitySerializer


class SubjectViewSetSimple(viewsets.ReadOnlyModelViewSet):
    """Subject view simple for REST """
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializerSimple


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Subject view with details for REST """
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class DegreeViewSet(viewsets.ReadOnlyModelViewSet):
    """Degrees view set for REST """
    queryset = Degree.objects.all()
    serializer_class = serializers.DegreeSerializer


class DegreeViewDetailSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Degree.objects.all()
    serializer_class = serializers.DegreeSerializerAll


class TeachingSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = TeachingSubject.objects.all()
    serializer_class = serializers.TeachingSubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class TimetableViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Timetable.objects.all()
    serializer_class = serializers.TimetableSerializer


class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    """Degree detail view for REST """
    queryset = Exam.objects.all()
    serializer_class = serializers.ExamSerializer
