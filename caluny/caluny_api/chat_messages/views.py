from braces.views import CsrfExemptMixin
from django.contrib.auth.models import User
import django_filters
from push_notifications.models import GCMDevice
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.utils.translation import ugettext_lazy as _

from caluny_api.chat_messages.models import MessageToSubject, Message
from caluny_api.serializers import MessageToSubjectSerializer
from core.models import TeachingSubject, Teacher, Student


class SendMessageToSubject(CsrfExemptMixin, APIView):
    serializer_class = MessageToSubjectSerializer
    model = MessageToSubject

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            try:
                teacher = Teacher.objects.get(username=request.user.username)
                message_to_subject = serializer.object
                teaching_subject = TeachingSubject.objects.get(subject_id=message_to_subject.receiver_id)
                is_teaching = teaching_subject.teachers.filter(username=teacher.username).count() > 0
                if not is_teaching:
                    raise Teacher.DoesNotExist
                message_to_subject.sender = request.user
                message_to_subject.save()
                # send the messages to all the student devices
                devices = GCMDevice.objects.filter(user__in=teaching_subject.students.all())
                message_data = {'teacher': message_to_subject.sender.get_full_name(),
                                'created': message_to_subject.created.isoformat(),
                                'message': message_to_subject.message,
                                'subject_title': message_to_subject.receiver.title,
                                'subject_id': message_to_subject.receiver_id,
                                'title': _('New message from ') + message_to_subject.receiver.title}
                devices.send_message(message_data)
                message_to_subject.status = Message.STATUS.SENT
                message_to_subject.save()
                return Response({'n_devices': devices.count(), 'status': Message.STATUS.SENT})
            except TeachingSubject.DoesNotExist:
                Response('This subject is not taught', status=status.HTTP_400_BAD_REQUEST)
            except Teacher.DoesNotExist:
                Response('Teacher not found', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesFilter(django_filters.FilterSet):
    changed_from = django_filters.DateTimeFilter(name='status_changed', lookup_type='gte')
    changed_until = django_filters.DateTimeFilter(name='status_changed', lookup_type='lte')

    class Meta:
        model = MessageToSubject
        fields = ['id', 'receiver', 'status', 'changed_until', 'changed_from']


class MessagesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MessageToSubject.objects.all()
    serializer_class = MessageToSubjectSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    ordering = ('-created', 'status_changed', 'status',)
    filter_class = MessagesFilter

    def get_queryset(self):
        user = self.request.user
        if Teacher.objects.filter(username=user.username):
            return self.queryset.filter(sender=user)
        if Student.objects.filter(username=user.username):
            return self.queryset.filter(receiver__in=TeachingSubject.objects.filter(students=user))
        if isinstance(user, User):
            if user.is_superuser:
                return self.queryset
        return self.queryset.none()
