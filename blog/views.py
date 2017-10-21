from django.views.generic.list import ListView
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect

from .models import Entry

from .serializers import EntrySerializer
from rest_framework import generics

from datetime import datetime, timedelta


def get_paginated_pages(page, all_pages):
    """функция для пагинации"""
    paginator = Paginator(all_pages, 20)
    try:
        paginated_pages = paginator.page(page)
    except PageNotAnInteger:
        paginated_pages = paginator.page(1)
    except EmptyPage:
        paginated_pages = paginator.page(paginator.num_pages)
    return paginated_pages


class EntryListView(ListView):
    """посты только текущего юзера"""
    template_name = 'entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')

        return get_paginated_pages(
            page, Entry.objects.filter(
                user=self.request.user).order_by('-creation_date'))


class AllEntryListView(ListView):
    """главная - все посты"""
    template_name = 'entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')
        all_entries = Entry.objects.filter(
            likes_count__gt=-1).order_by('-creation_date')
        return get_paginated_pages(page, all_entries)


class LikeView(View):
    """простановка лайков и дизлайков"""
    def get(self, request):
        action = request.GET.get('action')
        entry_id = request.GET.get('entry_id')

        entry = Entry.objects.get(pk=entry_id)
        likes = entry.likes.split(',')

        user_id = str(self.request.user.id)

        if user_id not in likes:
            if action == "like":
                entry.likes_count += 1
            else:
                entry.likes_count -= 1
            likes.append(user_id)
            entry.likes = ','.join(likes)
            entry.save()
        return redirect('all_entries')


class BestLastMonthListView(ListView):
    """посты лучшие за последний месяц"""
    template_name = 'entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')
        last_month = datetime.today() - timedelta(days=30)
        all_entries = Entry.objects.filter(
            creation_date__gte=last_month,
            likes_count__gt=-1).order_by('-likes_count')
        return get_paginated_pages(page, all_entries)


class BestLastYearListView(ListView):
    """посты лучшие за последний год"""
    template_name = 'entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')
        last_year = datetime.today() - timedelta(days=365)
        all_entries = Entry.objects.filter(
            creation_date__gte=last_year,
            likes_count__gt=-1).order_by('-likes_count')
        return get_paginated_pages(page, all_entries)


class BestAllTimeListView(ListView):
    """посты лучшие за все время"""
    template_name = 'entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')
        all_entries = Entry.objects.filter(
            likes_count__gt=-1).order_by('-likes_count')
        return get_paginated_pages(page, all_entries)


class EntryList(generics.ListCreateAPIView):
    """API view - all etnries"""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view - etnry"""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
