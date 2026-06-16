import os
import sys
from pathlib import Path
project_root = Path(r'c:/wamp64/www/SDI STORE 1/sdi_market')
sys.path.insert(0, str(project_root))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
import django
from django.core.management import call_command

django.setup()
call_command('test', verbosity=1)
