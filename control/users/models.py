import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class HRUser(AbstractUser):

    bio = models.TextField(max_length=700, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    remaining_holiday = models.DecimalField(default=25.0, decimal_places=1, max_digits=3)
    job_tittle = models.CharField(max_length= 30, blank=True)
    start_date = models.DateField(null=True, blank=True)
    manager = models.ForeignKey('HRUser', null=True, blank=True)
    department = models.ForeignKey('Department', null=True, blank=True)

    @property
    def current_status(self):

        today = datetime.datetime.now()
        status = "At the office"
        time_off_request = self.timeoffrequest_set.filter(start_date__lte=today, end_date__gte=today, holiday_status="approved").first()

        if time_off_request:

            request_type = time_off_request.type

            if request_type == "holiday":
                status = "On Holiday!"

            elif request_type == "off_sick":
                status = "Off Sick!"

            elif request_type == "working_from_home":
                status = "Working From Home!"

            status = "{} ({}), {}".format(status, time_off_request.all_day, time_off_request.holiday_status)

        return status


class TimeOffRequest(models.Model):

    date_request = models.DateField(blank=True)
    user = models.ForeignKey('HRUser', blank=True, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(max_length=600, blank=True)
    holiday_status = models.CharField(max_length=30, default="pending_approval", choices=(("approved", "Approved"),
                                                                                        ("pending_approval", "Pending Approval"),
                                                                                        ("not_approved", "Not Approved")))

    type = models.CharField(max_length=20, default="holiday", choices=(("holiday", "Holiday"),
                                                                       ("off_sick", "Off Sick"),
                                                                       ("working_from_home", "Working From Home")))

    all_day = models.CharField(max_length=10, default="all_day", choices=(("all_day", "All Day"),
                                                                          ("morning", "Morning"),
                                                                          ("afternoon", "Afternoon")))


class Department(models.Model):

    department = models.CharField(max_length=30, default=None)

    def __unicode__(self):
        return self.department



