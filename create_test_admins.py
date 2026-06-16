import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()

created = []
if not User.objects.filter(username='supertest').exists():
    User.objects.create_superuser('supertest', 'supertest@example.com', 'SuperP@ss123')
    created.append('supertest')

if not User.objects.filter(username='admin2').exists():
    u = User.objects.create_user('admin2', 'admin2@example.com', 'AdminP@ss123')
    u.is_staff = True
    u.save()
    created.append('admin2')

print('created:', created)
