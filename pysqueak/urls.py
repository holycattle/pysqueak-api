from django.conf.urls import url
from django.contrib import admin
from api.views import api_root, ChoicesView, QuestionsView, AnswersView, LatestAnswerView, SummaryView

urlpatterns = [
    url(r'^$', api_root),
    url(r'^admin/', admin.site.urls),
    url(r'^questions/(?P<k>[0-9]+)/$',\
        QuestionsView.as_view(), name='questions-get'),
    url(r'^choices/(?P<k>[0-9]+)/$',\
        ChoicesView.as_view(), name='choices-get'),
    url(r'^answers/(?P<k>[0-9]+)/$',\
        AnswersView.as_view(), name='answers-post'),
    url(r'^users/(?P<uuid>([a-z]|[0-9])+)/answers/(?P<ver>[0-9]+)/$',\
        LatestAnswerView.as_view(), name='latest-answers-post'),
    url(r'^summary/$', SummaryView.as_view(), name='summary')
]
