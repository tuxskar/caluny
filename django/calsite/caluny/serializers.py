from rest_framework import serializers
import caluny.models
from django.contrib.auth.models import User


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.University

class SubjectSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.Subject
        exclude = ('degree',)

class SubjectSerializer(serializers.ModelSerializer):
    t_subject = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = caluny.models.Subject
        exclude = ('degree',)

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.Degree

class DegreeSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.Degree
        exclude = ('school',)

class DegreeSerializerAll(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = caluny.models.Degree

class SchoolSerializer(serializers.ModelSerializer):
    degrees = DegreeSerializerSimple()
    class Meta:
        model = caluny.models.School

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.Course

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.Timetable

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = caluny.models.Exam

class TeachingSubjectSerializer(serializers.ModelSerializer):
    timetables = TimetableSerializer()
    exams = ExamSerializer()
    class Meta:
        model = caluny.models.TeachingSubject
        exclude = ('students', 'teachers')
