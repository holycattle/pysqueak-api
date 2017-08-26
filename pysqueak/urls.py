from django.conf.urls import url
from django.contrib import admin
from api.views import api_root, ChoicesView

urlpatterns = [
    url(r'^$', api_root),
    url(r'^admin/', admin.site.urls),
    url(r'^choices/(?P<id>[0-9]+)/$',\
        ChoicesView.as_view(), name='choices-list'),
]
