import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'FullThrottleLabs.settings')

import django
django.setup()

from basicapp.models import ActivityPeriod
from django.contrib.auth.models import User
from faker import Faker
from django.utils import timezone

fake=Faker()

def populate_data():
    for i in range(10):
        try:
            user=User()
            user.username=fake.first_name()
            user.first_name=fake.first_name()
            user.last_name=fake.last_name()
            user.password=fake.password()
            user.save()

            for j in range(5):
                AR=ActivityPeriod()
                AR.start_time=timezone.now()
                AR.end_time=timezone.now()
                AR.user=user
                AR.save()
        except:
            print("Error")

if __name__=='__main__':
    populate_data()
