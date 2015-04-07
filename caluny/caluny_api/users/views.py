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
    role = request.POST.get('role', None)
    if role and role not in constants.USER_ROLES.keys():
        return HttpResponseBadRequest(json.dumps('Role not supported'), content_type="application/json")
    if role == constants.ROLES.student:
        form = StudentForm(request.POST)
    elif role == constants.ROLES.teacher:
        form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        form.instance.is_active = True
        form.instance.save()
        return HttpResponse(json.dumps({'token': Token.objects.get(user_id=form.instance.id).key}))
    else:
        return HttpResponseBadRequest(json.dumps(form.errors))
