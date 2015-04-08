from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from core.models import Student, Teacher

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
