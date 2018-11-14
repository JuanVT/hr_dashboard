from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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


@login_required(login_url='accounts/login')
def index_view(request):

    users = HRUser.objects.all()

    context = {

        'users': users,
    }

    template = loader.get_template('control/index.html')
    return HttpResponse(template.render(context=context, request=request))

