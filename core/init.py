import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.security.models import *
from django.contrib.auth.models import Permission

from core.pos.models import *

dashboard = Dashboard()
dashboard.name = 'INVOICE WEB'
dashboard.icon = 'fas fa-shopping-cart'
dashboard.author = 'William Jair Dávila Vargas'
dashboard.save()

group = Group()
group.name = 'Administrador'
group.save()
print(f'insertado {group.name}')

for permission in Permission.objects.filter().exclude(content_type__app_label__in=['admin', 'auth', 'auth', 'contenttypes', 'sessions']):
    group.permissions.add(permission)

user = User()
user.names = 'William Jair Dávila Vargas'
user.username = 'admin'
user.email = 'davilawilliam93@gmail.com'
user.is_active = True
user.is_superuser = True
user.is_staff = True
user.set_password('hacker94')
user.save()
user.groups.add(group)
print(f'User {user.names} created successfully')
