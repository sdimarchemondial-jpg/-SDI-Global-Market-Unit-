import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.contrib.auth import get_user_model
from marketplace.models import Wallet, Transfer

User = get_user_model()
print('--- balances ---')
for username in ['ui_tester', 'ui_receiver']:
    u = User.objects.filter(username=username).first()
    if not u:
        print(username, 'missing')
        continue
    w = Wallet.objects.filter(user=u).first()
    print('USER', username, 'balance', getattr(w, 'balance', None), 'usd', getattr(w, 'balance_usd', None), 'htg', getattr(w, 'balance_htg', None), 'can_transfer', getattr(w, 'can_transfer', None))
print('--- sent transfers ---')
for t in Transfer.objects.filter(sender__username='ui_tester').order_by('-id')[:5]:
    print('id', t.id, 'receiver', t.receiver.username, 'amt', t.amount, t.currency, 'fee', t.fee, 'status', t.status)
print('--- received transfers ---')
for t in Transfer.objects.filter(receiver__username='ui_receiver').order_by('-id')[:5]:
    print('id', t.id, 'sender', t.sender.username, 'amt', t.amount, t.currency, 'fee', t.fee, 'status', t.status)
