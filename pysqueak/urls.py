from django.conf.urls import url
from django.contrib import admin
from api.views import api_root, ChoicesView, QuestionsView

urlpatterns = [
    url(r'^$', api_root),
    url(r'^admin/', admin.site.urls),
    url(r'^questions/(?P<k>[0-9]+)/$',\
        QuestionsView.as_view(), name='questions-get'),
    url(r'^choices/(?P<k>[0-9]+)/$',\
        ChoicesView.as_view(), name='choices-get'),
]
