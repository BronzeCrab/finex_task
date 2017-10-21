from django.contrib.auth.models import User
from blog.models import Entry
import lorem

users = []
for i in range(1000):
    user = User(username="user_{0}".format(i))
    user.set_password("user_{0}".format(i))
    users.append(user)
User.objects.bulk_create(users)

entries = []
for user in User.objects.all():
    entries.extend([Entry(
        title=lorem.sentence(),
        body=lorem.text(),
        user=user) for i in range(10)])
Entry.objects.bulk_create(entries)
