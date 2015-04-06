from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^users/', include('caluny_api.users.urls')),
                       )