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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog.views import (EntryListView, AllEntryListView,
                        LikeView, BestLastMonthListView,
                        BestLastYearListView,
                        BestAllTimeListView)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^all_entries/$', login_required(AllEntryListView.as_view()),
        name="all_entries"),
    url(r'^your_entries/$', login_required(EntryListView.as_view()),
        name="your_entries"),
    url(r'^like/$', login_required(LikeView.as_view()),
        name="like"),
    url(r'^best_last_month/$', login_required(BestLastMonthListView.as_view()),
        name="best_last_month"),
    url(r'^best_last_year/$', login_required(BestLastYearListView.as_view()),
        name="best_last_year"),
    url(r'^best_all_time/$', login_required(BestAllTimeListView.as_view()),
        name="best_all_time"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
]
