__author__ = 'tuxskar'

from django.http import HttpResponseBadRequest, HttpResponse
from core import constants
from core.users.forms import StudentForm, TeacherForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
import json


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
        return HttpResponse(json.dumps({'token': Token.objects.get(user_id=form.instance.id).key}))
    else:
        return HttpResponseBadRequest(json.dumps(form.errors))
