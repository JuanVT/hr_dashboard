import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class HRUser(AbstractUser):

    bio = models.TextField(max_length=700, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    remaining_holiday = models.DecimalField(default=25.0, decimal_places=1, max_digits=3)
    job_title = models.CharField(max_length=30, blank=True)
    start_date = models.DateField(null=True, blank=True)
    manager = models.ForeignKey('HRUser', null=True, blank=True)
    department = models.ForeignKey('Department', null=True, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    post_code = models.CharField(max_length=30, blank=True)
    employee_id = models.CharField(max_length=30, blank=True)
    work_phone = models.DecimalField(max_length=11, blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=(("male", "Male"),
                                                                             ("female", "Female")))
    private_phone = models.DecimalField(decimal_places=0, max_digits=30, null=True, blank=True)
    work_phone = models.DecimalField(decimal_places=0, max_digits=30, null=True, blank=True)
    bank_name = models.CharField(max_length=30, blank=True)
    account_number = models.DecimalField(decimal_places=0, max_digits=30, null=True, blank=True)
    bank_account_type = models.CharField(max_length=30, blank=True)
    swift_code = models.CharField(max_length=30, blank=True)
    iban = models.CharField(max_length=30, blank=True)
    nin = models.CharField(max_length=30, blank=True)
    tax_code = models.CharField(max_length=30, blank=True)
    emergency_first_name = models.CharField(max_length=30, blank=True)
    emergency_last_name = models.CharField(max_length=30, blank=True)
    emergency_contact_number = models.DecimalField(decimal_places=0, max_digits=30, null=True, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True, choices=(("active", "Active"),
                                                                             ("inactive", "Inactive")))
    profile_picture = models.ImageField(null=True, upload_to='images', default='images/default.png')

    @property
    def current_status(self):

        today = datetime.datetime.now()
        status = "At the office"
        time_off_request = self.timeoffrequest_set.filter(start_date__lte=today, end_date__gte=today, status="approved").first()

        if time_off_request:

            request_type = time_off_request.type

            if request_type == "holiday":
                status = "On Holiday!"

            elif request_type == "off_sick":
                status = "Off Sick!"

            elif request_type == "working_from_home":
                status = "Working From Home!"

            status = "{} ({}), {}".format(status, time_off_request.all_day, time_off_request.status)

        return status


class TimeOffRequest(models.Model):

    date_request = models.DateField(blank=True)
    user = models.ForeignKey('HRUser', blank=True, null=True)
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


class Department(models.Model):

    department = models.CharField(max_length=30, default=None)

    def __unicode__(self):
        return self.department



