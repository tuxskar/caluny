from django.http import HttpResponseBadRequest, HttpResponse
from caluny import constants
__author__ = 'tuxskar'

from django.views.decorators.http import require_POST
from rest_framework.authtoken.models import Token
import json


@require_POST
def create_app_user(request):
    param = lambda x: request.POST.get(x, None)
    params_list = ["name", "last_name", "password", "username", "role", "dept", "description"]
    params = {x: param(x) for x in params_list}
    if not params['username'] or not params['password']:
        return HttpResponseBadRequest(json.dumps('Username and password are required'), content_type="application/json")
    if params['role'] not in constants.USER_ROLES.keys():
        return HttpResponseBadRequest(json.dumps('Role not supported'), content_type="application/json")
    user_instance = constants.USER_ROLES[params['role']][1]
    id = user_instance.objects.create_user(**params)
    if id:
        return HttpResponse(json.dumps({'token': Token.objects.get(user_id=id).key()}))