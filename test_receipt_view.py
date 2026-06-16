#!/usr/bin/env python
import os
import sys
import django

sys.path.insert(0, r'c:\wamp64\www\SDI STORE 1\sdi_market')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import WithdrawalRequest, Wallet
from django.contrib.auth import get_user_model

User = get_user_model()

print("=" * 60)
print("TEST DE REÇUS DE RETRAIT")
print("=" * 60)

# Vérifier les retraits approuvés
approvals = WithdrawalRequest.objects.filter(status='approved')
print(f"\n✅ Reçus approuvés trouvés: {approvals.count()}")

if approvals.exists():
    for w in approvals[:3]:
        print(f"\n  ID: {w.id}")
        print(f"  Utilisateur: {w.user.username}")
        print(f"  Montant: {w.amount} {w.currency}")
        print(f"  Type de compte: {w.account_type}")
        print(f"  Statut: {w.status}")
        print(f"  Approuvé par: {w.confirmed_by.username if w.confirmed_by else 'N/A'}")
        print(f"  Reçu généré: {w.receipt_generated}")
        
        # Vérifier la profile
        profile = getattr(w.user, 'profile', None)
        if profile:
            print(f"  Profile trouvé: OUI")
        else:
            print(f"  Profile trouvé: NON")
            
        # Vérifier le portefeuille
        wallet = Wallet.objects.filter(user=w.user).first()
        if wallet:
            print(f"  Portefeuille trouvé: OUI")
            if w.account_type == 'principal':
                print(f"    Solde courant: {wallet.balance} {w.currency}")
            else:
                field_map = {
                    'USD': 'commission_balance_usd',
                    'HTG': 'commission_balance_htg',
                    'DOP': 'commission_balance_peso',
                    'EUR': 'commission_balance_eur',
                }
                field_name = field_map.get(w.currency.upper())
                if field_name:
                    balance = getattr(wallet, field_name)
                    print(f"    Solde courant: {balance} {w.currency}")
        else:
            print(f"  Portefeuille trouvé: NON")
else:
    print("\n❌ Aucun retrait approuvé trouvé.")
    print("\nVérification des retraits en attente...")
    pending = WithdrawalRequest.objects.filter(status='pending')
    print(f"Retraits en attente: {pending.count()}")
    
print("\n" + "=" * 60)
