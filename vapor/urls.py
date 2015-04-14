from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^infrastructure/', include('infrastructure.urls', namespace="infrastructure")),
    url(r'^admin/', include(admin.site.urls)),
]
