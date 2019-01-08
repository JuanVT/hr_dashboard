from django.http import HttpResponse
from django.template import loader

from control.purchase_order.forms import PurchaseOrderForm
from control.purchase_order.models import Item


def purchase_order(request):

    if request.method == 'POST':

        form = PurchaseOrderForm(request.POST)

        if form.is_valid():
            form.save()

    form = PurchaseOrderForm()
    items = Item.objects.all()

    context = {'form': form,
               'item': items}

    template = loader.get_template('control/purchase_order/purchasing.html')
    return HttpResponse(template.render(context=context, request=request))