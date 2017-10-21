from django.contrib.auth.models import User, Permission
from blog.models import Entry
import lorem

users = []
for i in range(100):
    user = User(username="user_{0}".format(i), is_staff=True)
    user.set_password("user_{0}".format(i))
    users.append(user)
User.objects.bulk_create(users)

permissions = (
    Permission.objects.get(name='Can change entry'),
    Permission.objects.get(name='Can add entry'),
    Permission.objects.get(name='Can delete entry')
    )
entries = []
for user in User.objects.all():

    for perm in permissions:
        user.user_permissions.add(perm)

    entries.extend([Entry(
        title=lorem.sentence(),
        body=lorem.text(),
        user=user) for i in range(10)])
Entry.objects.bulk_create(entries)
