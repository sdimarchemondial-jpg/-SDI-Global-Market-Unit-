import os
import sys
import django

# Set up Django environment
os.chdir(r'c:\wamp64\www\SDI STORE 1\sdi_market')
sys.path.insert(0, r'c:\wamp64\www\SDI STORE 1\sdi_market')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import User, Profile

# Génère des codes de retrait manquants pour tous les utilisateurs
for user in User.objects.all():
    profile, created = Profile.objects.get_or_create(user=user)

    # Set withdrawal codes
    modified = False
    if not profile.withdrawal_pin:
        profile.withdrawal_pin = ''.join(__import__('secrets').choice('0123456789') for _ in range(8))
        modified = True
    if not profile.withdrawal_code:
        profile.withdrawal_code = ''.join(__import__('secrets').choice('0123456789') for _ in range(4))
        modified = True
    if modified:
        profile.save()
        print(f'Codes générés pour {user.username}: PIN={profile.withdrawal_pin}, CODE={profile.withdrawal_code}')
    else:
        print(f'Déjà défini pour {user.username}: PIN={profile.withdrawal_pin}, CODE={profile.withdrawal_code}')
