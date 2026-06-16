import os
import sys
import django
import uuid
from decimal import Decimal

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sdi_market'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from marketplace.models import User, Profile, Wallet, Agent, DepositCommissionConfig, CommissionRule, Deposit

suffix = uuid.uuid4().hex[:8]
client_user = User.objects.create_user(username=f'client_{suffix}', password='testpass123', email=f'client_{suffix}@example.com')
client_profile, _ = Profile.objects.get_or_create(user=client_user)
client_profile.phone = f'50911111{suffix[:4]}'
client_profile.save()
client_wallet, _ = Wallet.objects.get_or_create(user=client_user)
client_wallet.balance_htg = Decimal('500.00')
client_wallet.save()

agent_user = User.objects.create_user(username=f'agent_{suffix}', password='agentpass123', email=f'agent_{suffix}@example.com')
agent_user.is_agent = True
agent_user.save()
agent_profile, _ = Profile.objects.get_or_create(user=agent_user)
agent_profile.phone = f'50922222{suffix[:4]}'
agent_profile.save()
agent_obj, _ = Agent.objects.get_or_create(user=agent_user)
agent_obj.is_active = True
agent_obj.save()
agent_wallet, _ = Wallet.objects.get_or_create(user=agent_user)
agent_wallet.balance_htg = Decimal('50000.00')
agent_wallet.save()
agent_user.set_security_pin('1234')
agent_user.set_otp_code('0000')

admin_user = User.objects.create_superuser(username=f'admin_{suffix}', email=f'admin_{suffix}@example.com', password='admin123')
admin_wallet, _ = Wallet.objects.get_or_create(user=admin_user)

DepositCommissionConfig.objects.get_or_create(
    currency='HTG',
    defaults={
        'commission_type': 'pourcentage',
        'commission_value': Decimal('0.5'),
        'min_deposit': Decimal('1.00'),
        'max_deposit': Decimal('999999.00'),
        'is_active': True,
    }
)
CommissionRule.objects.get_or_create(agent=None, min_amount=Decimal('100.00'), max_amount=Decimal('500.00'), commission_amount=Decimal('2.00'))
CommissionRule.objects.get_or_create(agent=None, min_amount=Decimal('501.00'), max_amount=Decimal('2000.00'), commission_amount=Decimal('5.00'))
CommissionRule.objects.get_or_create(agent=None, min_amount=Decimal('2001.00'), max_amount=Decimal('5000.00'), commission_amount=Decimal('10.00'))

c = Client()
logged = c.login(username=agent_user.username, password='agentpass123')
outputs = [f'login {logged}']
url = reverse('agent_deposit')
outputs.append(f'url {url}')
response = c.post(url, {
    'account_number': client_user.account_code,
    'amount': '2000',
    'currency': 'HTG',
    'agent_pin': '1234',
    'final_code': '0000',
})
outputs.append(f'status {response.status_code}')
outputs.append(f'redirect_url {getattr(response, "url", None)}')
outputs.append(f'deposit_count {Deposit.objects.count()}')
outputs.append(f'client_exists {User.objects.filter(account_code=client_user.account_code).exists()}')
outputs.append(f'client_code {client_user.account_code}')
with open('temp_deposit_test2_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(outputs))
for line in outputs:
    print(line)
