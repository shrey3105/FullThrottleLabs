from django.shortcuts import render
from rest_framework import viewsets
from basicapp.serializers import UserSerializer,ActivityPeriodSerializer
from django.contrib.auth.models import User
from basicapp.models import ActivityPeriod
# Create your views here.
class UserViewList(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ActivityPeriodViewList(viewsets.ModelViewSet):
    queryset=ActivityPeriod.objects.all()
    serializer_class=ActivityPeriodSerializer
