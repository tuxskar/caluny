from django.shortcuts import render
from django.contrib.auth.models import User
#from rest_framework import permissions
#from rest_framework import renderers
from rest_framework import viewsets
#from rest_framework.decorators import link
#from rest_framework.response import Response
#from snippets.models import Snippet
#from snippets.permissions import IsOwnerOrReadOnly
#from snippets.serializers import SnippetSerializer, UserSerializer
from caluny.serializers import SchoolSerializer
from caluny.models import School

class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    """ """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
