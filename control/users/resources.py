from import_export import resources

from models import HRUser


class UserResource(resources.ModelResource):

    class Meta:

        model = HRUser
