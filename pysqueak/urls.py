from django.conf.urls import url
from django.contrib import admin
from worklogger2.views import api_root, ChoicesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/mine/(?P<id>[0-9]+)/$',\
        ChoicesView.as_view(), name='choices-list'),
]
