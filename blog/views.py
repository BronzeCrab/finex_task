from django.views.generic.list import ListView
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect

from .models import Entry


def get_paginated_pages(page, all_pages):
    paginator = Paginator(all_pages, 20)
    try:
        paginated_pages = paginator.page(page)
    except PageNotAnInteger:
        paginated_pages = paginator.page(1)
    except EmptyPage:
        paginated_pages = paginator.page(paginator.num_pages)
    return paginated_pages


class EntryListView(ListView):
    template_name = 'entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')

        return get_paginated_pages(
            page, Entry.objects.filter(user=self.request.user))


class AllEntryListView(ListView):
    template_name = 'all_entry_list.html'

    def get_queryset(self):
        page = self.request.GET.get('page')
        all_entries = Entry.objects.order_by('-creation_date')
        all_entries = all_entries.filter(likes_count__gt=-1)
        return get_paginated_pages(page, all_entries)


class LikeView(View):
    def get(self, request, user_id):
        action = request.GET.get('action')
        entry_id = request.GET.get('entry_id')

        entry = Entry.objects.get(pk=entry_id)
        likes = entry.likes.split(',')
        if user_id not in likes:
            if action == "like":
                entry.likes_count += 1
            else:
                entry.likes_count -= 1
            likes.append(user_id)
            entry.likes = ','.join(likes)
            entry.save()
        return redirect('all_entries')
