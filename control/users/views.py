from django.http import HttpResponse
from django.template import loader

from control.users.forms import UpdateUserForm
from control.users.models import HRUser


def get_users(request):

    users = HRUser.objects.all()

    context = {

        'users': users,
    }

    template = loader.get_template('control/users.html')
    return HttpResponse(template.render(context=context, request=request))


def get_user_details(request, user_id):

    user = HRUser.objects.get(id=user_id)

    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    form = UpdateUserForm(instance=user)

    context = {

        'user': user,
        'form': form,
    }

    template = loader.get_template('control/user_details.html')
    return HttpResponse(template.render(context=context, request=request))










