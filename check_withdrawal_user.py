import os
import sys
sys.path.insert(0, r'c:\wamp64\www\SDI STORE 1\sdi_market')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
import django

django.setup()
from marketplace.models import User

print('vendeur exists:', User.objects.filter(username='vendeur').exists())
print('user count:', User.objects.count())
