from django.db import models


class TimeOffRequest(models.Model):

    date_request = models.DateField(blank=True)
    user = models.ForeignKey('users.HRUser', blank=True, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(max_length=600, blank=True)
    status = models.CharField(max_length=30, default="pending_approval",
                              choices=(("approved", "Approved"),
                                       ("pending_approval", "Pending Approval"),
                                       ("not_approved", "Not Approved")))

    type = models.CharField(max_length=20, default="holiday", choices=(("holiday", "Holiday"),
                                                                       ("off_sick", "Off Sick"),
                                                                       ("working_from_home", "Working From Home")))

    all_day = models.CharField(max_length=10, default="all_day", choices=(("all_day", "All Day"),
                                                                          ("morning", "Morning"),
                                                                          ("afternoon", "Afternoon")))