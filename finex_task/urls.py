"""finex_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog.views import EntryListView, AllEntryListView, LikeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^all_entries/$', login_required(AllEntryListView.as_view()),
        name="all_entries"),
    url(r'^entries/$', login_required(EntryListView.as_view()),
        name="entries"),
    url(r'^like/(?P<user_id>.*)/$', login_required(LikeView.as_view()),
        name="like"),
    url(r'^admin/', admin.site.urls),
]
