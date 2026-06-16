import os
import sys
import django
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sdi_market'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from marketplace.models import User, Deposit, Wallet

# Use the latest deposit created by the agent post.
try:
    deposit = Deposit.objects.latest('created_at')
except Exception as e:
    deposit = None

outputs = []
outputs.append(f'deposit_exists {deposit is not None}')
if deposit is not None:
    outputs.append(f'id {deposit.id}')
    outputs.append(f'agent {deposit.agent.user.username}')
    outputs.append(f'client {deposit.client.user.username}')
    outputs.append(f'amount {deposit.amount}')
    outputs.append(f'commission {deposit.commission}')
    outputs.append(f'currency {deposit.currency}')
    outputs.append(f'status {deposit.status}')
    outputs.append(f'created_at {deposit.created_at}')

# get balances
if deposit is not None:
    outputs.append(f'agent_balance {deposit.agent.user.wallet.balance_htg}')
    outputs.append(f'client_balance {deposit.client.user.wallet.balance_htg}')
    outputs.append(f'agent_commission_balance {deposit.agent.user.wallet.commission_balance_htg}')
    # admin wallet of admin_{suffix}
    admin_user = User.objects.filter(is_superuser=True).order_by('-id').first()
    if admin_user:
        outputs.append(f'admin_balance {admin_user.wallet.balance_htg}')
        outputs.append(f'admin_commission_balance {admin_user.wallet.commission_balance_htg}')

path = Path(__file__).with_name('temp_deposit_test3_out.txt')
path.write_text('\n'.join(outputs), encoding='utf-8')
for line in outputs:
    print(line)
