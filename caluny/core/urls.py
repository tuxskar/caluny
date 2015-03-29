from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^users/', include('core.users.urls')),
)
