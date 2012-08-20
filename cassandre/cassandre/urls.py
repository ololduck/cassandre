from django.conf.urls import patterns, include, url
from tastypie.api import Api
from cassandre.cassandre.api import UserResource, PostResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

api = Api('v1')
api.register(UserResource())
api.register(PostResource())

urlpatterns = patterns('',
    # Examples:
    url(r'', include(api.urls)),
)
