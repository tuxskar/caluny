from push_notifications.models import GCMDevice
from rest_framework import serializers

from caluny_api.chat_messages.models import MessageToSubject
import core.models


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = core.models.University


class SubjectSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = core.models.Subject
        exclude = ('degree',)


class SubjectSerializer(serializers.ModelSerializer):
    t_subject = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = core.models.Subject
        exclude = ('degree',)


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = core.models.Degree


class DegreeSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = core.models.Degree
        exclude = ('school',)


class DegreeSerializerAll(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = core.models.Degree


class SchoolSerializer(serializers.ModelSerializer):
    degrees = DegreeSerializerSimple()

    class Meta:
        model = core.models.School


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = core.models.Course


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = core.models.Timetable


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = core.models.Exam


class TeachingSubjectSerializer(serializers.ModelSerializer):
    timetables = TimetableSerializer()
    exams = ExamSerializer()

    class Meta:
        model = core.models.TeachingSubject
        exclude = ('students', 'teachers')


class GCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCMDevice


class MessageToSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageToSubject
        exclude = ('sender',)


class SubjectSubscribedSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title')

    class Meta:
        model = core.models.TeachingSubject
        fields = ('id', 'title')
