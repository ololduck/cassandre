from tastypie.resources import ModelResource
from cassandre.cassandre.models import *


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
