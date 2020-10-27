from django.shortcuts import render
from django.contrib.auth.models import User, Group
#from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status,generics
from .serializers import UserSerializer, GroupSerializer
from .serializers import InferenceSerializer
from .models import Inference
from celery.result import AsyncResult

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def push_alarm(request):
    context = {'text' : 'Check!!'}
    return render(request, 'quickstart/push_alarm.html',context)
