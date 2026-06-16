#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import User

u = User.objects.filter(username='testuser').first()
if u:
    print('User exists')
else:
    u = User.objects.create_user('testuser', 'test@example.com', 'password123')
    u.is_staff = True
    u.save()
    print('Created testuser')