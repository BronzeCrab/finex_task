from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    fields = (
        'title', 'body')
    exclude = ('likes', 'user')

    def get_queryset(self, request):
        qs = super(EntryAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Entry, EntryAdmin)
