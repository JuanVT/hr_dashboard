from django.http import HttpResponse
from django.template import loader

from control.users.models import HRUser


def index_view(request):

    users = HRUser.objects.all()

    context = {

        'users': users,
    }

    template = loader.get_template('control/index.html')
    return HttpResponse(template.render(context=context, request=request))
