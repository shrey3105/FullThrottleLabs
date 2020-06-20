from rest_framework import serializers
from basicapp.models import ActivityPeriod
from django.contrib.auth.models import User

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ActivityPeriod
        fields=['start_time','end_time']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    activity_periods=ActivityPeriodSerializer(many=True)
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','activity_periods']
