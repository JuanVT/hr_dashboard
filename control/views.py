from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from control.users.models import HRUser


def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index_view'))

        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')

    template = loader.get_template('control/login.html')
    return HttpResponse(template.render(request=request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


@login_required(login_url='accounts/login')
def index_view(request):

    today = timezone.now()

    users = HRUser.objects.all()

    on_holiday_users = users.filter(timeoffrequest__type='holiday', timeoffrequest__status='approved',
                                    timeoffrequest__start_date__lte=today,
                                    timeoffrequest__end_date__gte=today)
    wfh_users = users.filter(timeoffrequest__type='working_from_home', timeoffrequest__status='approved',
                             timeoffrequest__start_date__lte=today,
                             timeoffrequest__end_date__gte=today)
    off_sick_users = users.filter(timeoffrequest__type='off_sick', timeoffrequest__status='approved',
                                  timeoffrequest__start_date__lte=today,
                                  timeoffrequest__end_date__gte=today)

    context = {

        'users': users,
        'on_holiday_users': on_holiday_users,
        'wfh_users': wfh_users,
        'off_sick_users': off_sick_users,

    }

    template = loader.get_template('control/index.html')
    return HttpResponse(template.render(context=context, request=request))
