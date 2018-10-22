from control.users.resources import UserResource
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from tablib import Dataset

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


def users_import(request):

    context = {}

    if request.method == 'POST':

        user_resource = UserResource()
        data_set = Dataset()
        new_users = request.FILES['myfile']

        import_data = data_set.load(new_users.read(), format='csv')
        result = user_resource.import_data(data_set, dry_run=True)

        if not result.has_errors():

            user_resource.import_data(data_set, dry_run=False)

        else:

            errors = dict(result.row_errors())
            context.update({'errors': errors})

    return render(request, 'control/import-user.html', context=context)









