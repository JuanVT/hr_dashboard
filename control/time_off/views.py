from django.http import HttpResponse
from django.template import loader


def time_off(request):

    context =[]

    template = loader.get_template('control/time_off/time_off.html')
    return HttpResponse(template.render(request=request))

