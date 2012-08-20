from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', 'cassandre.client.views.home'),
)
