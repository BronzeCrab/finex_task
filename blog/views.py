from django.views.generic.list import ListView
from .models import Entry
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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
