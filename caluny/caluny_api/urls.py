from django.conf.urls import url, include

urlpatterns = [
    url(r'^users/', include('caluny_api.users.urls')),
]