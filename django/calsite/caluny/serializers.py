from rest_framework import serializers
import caluny.models
from django.contrib.auth.models import User


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.University

class SubjectSerializerSimple(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.Subject
        exclude = ('degree',)

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    t_subject = serializers.HyperlinkedRelatedField(view_name='teachingsubject-detail')
    class Meta:
        model = caluny.models.Subject
        exclude = ('degree',)

class DegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.Degree

class DegreeSerializerSimple(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.Degree
        exclude = ('school',)

class DegreeSerializerAll(serializers.HyperlinkedModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = caluny.models.Degree

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    degrees = DegreeSerializerSimple()
    class Meta:
        model = caluny.models.School

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.Course

class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.Timetable

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = caluny.models.Exam

class TeachingSubjectSerializer(serializers.HyperlinkedModelSerializer):
    timetables = TimetableSerializer()
    exams = ExamSerializer()
    class Meta:
        model = caluny.models.TeachingSubject
        exclude = ('students', 'teachers')

