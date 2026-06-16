import os
import sys
import django

PROJECT_DIR = os.path.join(os.path.dirname(__file__), 'sdi_market')
sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()

roles = [
    ('super_admin', 'Super Admin'),
    ('admin_secondary', 'Admin secondaire'),
    ('buyer_seller', 'Acheteur / Vendeur'),
    ('delivery_employee', 'Employé livraison'),
    ('agent', 'Agent'),
]

client = Client(SERVER_NAME='127.0.0.1')
password = 'TestLogin123!'

print('Testing login for representative users by role...')
for role_code, role_label in roles:
    user = User.objects.filter(role=role_code).first()
    if not user:
        print(f'- {role_label} ({role_code}): NO USER FOUND')
        continue
    user.set_password(password)
    user.save()
    response = client.post('/login/', {'username': user.username, 'password': password}, follow=True)
    authenticated = getattr(response.wsgi_request, 'user', None)
    auth_ok = authenticated.is_authenticated if authenticated else False
    path = response.request.get('PATH_INFO') if hasattr(response, 'request') else 'no request'
    print(f'- {role_label}: username={user.username}, login_ok={auth_ok}, status={response.status_code}, final_path={path}')

print('\nAlso checking user boolean roles on current users...')
for label, field in [('Acheteur', 'is_buyer'), ('Vendeur', 'is_seller'), ('Livreur', 'is_delivery_employee'), ('Agent livraison', 'is_delivery_agent')]:
    count = User.objects.filter(**{field: True}).count()
    print(f'- {label} ({field}): {count} users')
