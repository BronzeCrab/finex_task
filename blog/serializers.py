from blog.models import Entry
from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'title', 'body', 'creation_date',
                  'likes_count', 'user')
