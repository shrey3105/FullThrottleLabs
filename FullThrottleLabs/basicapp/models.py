from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ActivityPeriod(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='activity_periods')
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def set_time(self):
        self.start_time=timezone.now()
        self.end_time=timezone.now()
        self.save()

    def __str__(self):
        return self.user.username
