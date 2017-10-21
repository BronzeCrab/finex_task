from django.views.generic.list import ListView
from .models import Entry


class EntryListView(ListView):
    template_name = 'entry_list.html'

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)
