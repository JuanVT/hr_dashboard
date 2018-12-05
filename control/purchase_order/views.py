from django.http import HttpResponse
from django.template import loader


def purchase_order(request):

    context = {}

    template = loader.get_template('control/purchase_order/purchasing.html')
    return HttpResponse(template.render(context=context, request=request))