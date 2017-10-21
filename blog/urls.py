from django.conf.urls import url
from .views import EntryList, EntryDetail
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^entries/$', EntryList.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)/$', EntryDetail.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
