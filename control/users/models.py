from __builtin__ import True

from django.contrib.auth.models import AbstractUser
from django.db import models


class HRUser(AbstractUser):

    bio = models.TextField(max_length=700, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    remaining_holiday = models.DecimalField(default=25.0, decimal_places=1, max_digits=3)
    # profile_picture = models.ImageField(blank=True, default=None)


class TimeOffRequest(models.Model):

    date_request = models.DateField(blank=True)
    user = models.ForeignKey(HRUser, blank=True, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(max_length=600, blank=True)

    holiday, off_sick, working_from_home = 'holiday', 'off_sick', 'working_from_home'
    type = models.CharField(max_length=10, choices=((holiday, "Holiday"),
                                                    (off_sick, "Off Sick"),
                                                    (working_from_home, "Working From Home")))

    all_day, morning, afternoon = "all_day", "morning", "afternoon"
    all_day = models.CharField(max_length=10, choices=((all_day, "All Day"),
                                                       (morning, "Morning"),
                                                       (afternoon, "Afternoon")))

