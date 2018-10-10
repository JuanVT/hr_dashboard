from django import forms

from control.users.models import HRUser


class UpdateUserForm(forms.ModelForm):

    class Meta:

        model = HRUser
        fields = ['first_name', 'last_name', 'location', 'birth_date']
