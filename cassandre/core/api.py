from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from cassandre.core.models import Micropost, User


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        exclude = ['pw_hash']


class PostResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author')

    class Meta:
        queryset = Micropost.objects.all()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
