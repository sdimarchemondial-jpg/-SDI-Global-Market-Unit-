import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

users = User.objects.all()[:3]
for user in users:
    print(f"\nUtilisateur: {user.username}")
    print(f"  is_delivery_agent: {user.is_delivery_agent}")
    profile = getattr(user, 'profile', None)
    if profile:
        print(f"  delivery_access_granted: {profile.delivery_access_granted}")
    wallet = user.wallet if hasattr(user, 'wallet') else None
    if wallet:
        print(f"  Wallet USD: {wallet.balance_usd}, HTG: {wallet.balance_htg}, PESO: {wallet.balance_peso}")
    else:
        print(f"  Pas de wallet")
