from django.conf.urls import url
from .views import EntryList, EntryDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^entries/$', EntryList.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)/$', EntryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
