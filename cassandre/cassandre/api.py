from tastypie.resources import ModelResource
from cassandre.cassandre.models import Micropost, User


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()

class PostResource(ModelResource):
	class Meta:
		queryset = Micropost.objects.all()