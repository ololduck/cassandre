from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'cassandre.client.views.home'),
)
