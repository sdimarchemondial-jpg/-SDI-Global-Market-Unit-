#!/usr/bin/env python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sdi_market.settings")
django.setup()

from django.contrib.auth import get_user_model
from marketplace.models import TiKaneAccessRequest, TiKanePlan, TiKaneAccount
from django.utils import timezone
from decimal import Decimal

User = get_user_model()

# Créer un utilisateur de test s'il n'existe pas
user, created = User.objects.get_or_create(
    username='tikanetest',
    defaults={
        'email': 'tikanetest@gmail.com',
        'first_name': 'Test',
        'last_name': 'TiKane',
        'is_active': True,
    }
)

if created:
    user.set_password('TestPass123!')
    user.save()
    print(f"✓ Utilisateur créé: {user.username}")
else:
    user.set_password('TestPass123!')
    user.save()
    print(f"✓ Utilisateur exists: {user.username}")

# Récupérer le plan Ti Kanè 30 jours
plan = TiKanePlan.objects.filter(duration_days=30, active=True).first()

if plan:
    # Créer ou récupérer un compte Ti Kanè
    tikane_account, created = TiKaneAccount.objects.get_or_create(
        user=user,
        defaults={
            'plan': plan,
            'status': 'active',
            'balance': Decimal('1000.00'),
            'total_deposits': Decimal('1000.00'),
            'total_withdrawals': Decimal('0.00'),
            'is_sdi_managed': True,
        }
    )
    
    if created:
        print(f"✓ Compte Ti Kanè créé: {tikane_account.account_number}")
    else:
        print(f"✓ Compte Ti Kanè existe: {tikane_account.account_number}")
    
    # Vérifier les lignes journalières
    daily_count = tikane_account.daily_payments.count()
    print(f"✓ Nombre de lignes journalières: {daily_count}")
else:
    print("✗ Plan 30 jours non trouvé")

print("\n✓ Configuration de test complète")
