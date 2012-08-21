from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'cassandre.client.views.home'),
    url(r'^user/login/$', 'cassandre.client.views.login'),
)
