from braces.views import CsrfExemptMixin
from django.db.models import Q
from django.forms import Form
from push_notifications.models import GCMDevice
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import viewsets

from caluny_api.serializers import GCMDeviceSerializer, SubjectSubscribedSerializer
from core.models import Student, Teacher, TeachingSubject

__author__ = 'tuxskar'

import json

from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from core import constants
from .forms import StudentForm, TeacherForm


@require_POST
@csrf_exempt
def create_app_user(request):
    try:
        data = request.POST if request.POST else json.loads(request.body)
    except ValueError:
        return HttpResponseBadRequest()
    role = data.get('role')
    if not role or (role and role not in constants.USER_ROLES.keys()):
        return HttpResponseBadRequest(json.dumps('Role not supported'), content_type="application/json")
    form = Form()
    if role == constants.ROLES.student:
        form = StudentForm(data)
    elif role == constants.ROLES.teacher:
        form = TeacherForm(data)
    if form.is_valid():
        form.instance.is_active = True
        form.instance.set_password(form.cleaned_data['password'])
        form.instance.save()
        return HttpResponse(json.dumps({'token': Token.objects.get(user_id=form.instance.id).key}))
    else:
        return HttpResponseBadRequest(json.dumps(form.errors))


class ObtainUserAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            user = serializer.object['user']
            role = ''
            if Teacher.objects.filter(username=user.username).exists():
                role = constants.ROLES.teacher
            elif Student.objects.filter(username=user.username).exists():
                role = constants.ROLES.student
            token = Token.objects.get(user=user)
            return Response({
                'token': token.key,
                'role': role
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGCMRegistration(CsrfExemptMixin, APIView):
    serializer_class = GCMDeviceSerializer
    model = GCMDevice

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            device_id = serializer.object.device_id
            if device_id:
                GCMDevice.objects.filter(device_id=device_id).delete()
            gcm_device, created = GCMDevice.objects.get_or_create(
                user=request.user, registration_id=serializer.object.registration_id,
                defaults={'name': request.user.username + " device", 'device_id': serializer.object.device_id or None})
            return Response({'active': gcm_device.active, 'created': created})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectSubscribed(viewsets.ReadOnlyModelViewSet):
    """Subscribed subject by user view for REST """
    queryset = TeachingSubject.objects.all()
    serializer_class = SubjectSubscribedSerializer

    def get_queryset(self):
        return TeachingSubject.objects.filter(Q(students__username=self.request.user.username) |
                                              Q(teachers__username=self.request.user.username)).distinct()
