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
    url(r'^$', 'cassandre.cassandre.views.home'),
    url(r'^api/', include(api.urls)),
    # url(r'^cassandre/', include('cassandre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
