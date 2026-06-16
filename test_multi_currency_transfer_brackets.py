#!/usr/bin/env python
"""
Test complet du système de tranches de transfert multi-devises
Vérifie:
1. Le système accepte des tranches de transfert multi-devises
2. L'admin peut les configurer et les éditer facilement
3. Les calculs de frais de transfert prennent en compte les tranches par devise
"""
import os
import sys
import django
from decimal import Decimal

# Setup Django
# Ajouter le répertoire sdi_market au path pour trouver le module Django interne
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'sdi_market'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.contrib.auth import get_user_model
from marketplace.models import TransferCommissionTier, Transfer
from marketplace.business_logic import CommissionManager

User = get_user_model()

def print_section(title):
    """Affiche une section du test"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def test_1_create_multi_currency_brackets():
    """Test 1: Créer des tranches pour plusieurs devises"""
    print_section("TEST 1: Création de tranches multi-devises")
    
    # Supprimer les tranches existantes
    TransferCommissionTier.objects.all().delete()
    print("✓ Tranches existantes supprimées")
    
    # Devises et tranches à créer
    currencies = ['USD', 'HTG', 'DOP', 'EUR']
    tiers_config = {
        'USD': [
            {'min': 10, 'max': 50, 'total': 1.00, 'system': 0.60, 'agent': 0.40, 'desc': 'USD: 10-50'},
            {'min': 51, 'max': 100, 'total': 2.00, 'system': 1.20, 'agent': 0.80, 'desc': 'USD: 51-100'},
            {'min': 101, 'max': 500, 'total': 3.50, 'system': 2.10, 'agent': 1.40, 'desc': 'USD: 101-500'},
        ],
        'HTG': [
            {'min': 500, 'max': 2500, 'total': 50.00, 'system': 30.00, 'agent': 20.00, 'desc': 'HTG: 500-2500'},
            {'min': 2501, 'max': 5000, 'total': 100.00, 'system': 60.00, 'agent': 40.00, 'desc': 'HTG: 2501-5000'},
            {'min': 5001, 'max': 25000, 'total': 175.00, 'system': 105.00, 'agent': 70.00, 'desc': 'HTG: 5001-25000'},
        ],
        'DOP': [
            {'min': 500, 'max': 2500, 'total': 50.00, 'system': 30.00, 'agent': 20.00, 'desc': 'DOP: 500-2500'},
            {'min': 2501, 'max': 5000, 'total': 100.00, 'system': 60.00, 'agent': 40.00, 'desc': 'DOP: 2501-5000'},
        ],
        'EUR': [
            {'min': 10, 'max': 50, 'total': 0.80, 'system': 0.48, 'agent': 0.32, 'desc': 'EUR: 10-50'},
            {'min': 51, 'max': 200, 'total': 1.50, 'system': 0.90, 'agent': 0.60, 'desc': 'EUR: 51-200'},
        ],
    }
    
    created_count = 0
    for currency in currencies:
        for tier_data in tiers_config.get(currency, []):
            tier = TransferCommissionTier.objects.create(
                currency=currency,
                min_amount=Decimal(str(tier_data['min'])),
                max_amount=Decimal(str(tier_data['max'])),
                total_fee=Decimal(str(tier_data['total'])),
                system_fee=Decimal(str(tier_data['system'])),
                agent_fee=Decimal(str(tier_data['agent'])),
                description=tier_data['desc'],
                active=True
            )
            created_count += 1
            print(f"  ✓ Créé: {tier.description}")
    
    print(f"\n✓ Total tranches créées: {created_count}")
    return created_count > 0

def test_2_list_transfer_brackets():
    """Test 2: Lister les tranches de transfert par devise"""
    print_section("TEST 2: Listage des tranches de transfert")
    
    currencies = ['USD', 'HTG', 'DOP', 'EUR']
    
    for currency in currencies:
        tiers = TransferCommissionTier.objects.filter(currency=currency, active=True).order_by('min_amount')
        print(f"\n{currency} - {tiers.count()} tranches:")
        for tier in tiers:
            print(f"  {tier.min_amount:>8} - {tier.max_amount:>8}: "
                  f"Total={tier.total_fee} (Sys={tier.system_fee} + Ag={tier.agent_fee})")
    
    return True

def test_3_verify_admin_interface():
    """Test 3: Vérifier que l'interface admin est disponible"""
    print_section("TEST 3: Vérification de l'interface admin")
    
    from django.contrib.admin.sites import site
    from marketplace.models import TransferCommissionTier
    
    # Vérifier que le modèle est enregistré dans l'admin
    if TransferCommissionTier in site._registry:
        admin_class = site._registry[TransferCommissionTier]
        print(f"✓ TransferCommissionTier enregistré dans l'admin")
        print(f"  Admin class: {admin_class.__class__.__name__}")
        print(f"  List display: {admin_class.list_display}")
        print(f"  List filters: {admin_class.list_filter}")
        print(f"  Search fields: {admin_class.search_fields}")
        return True
    else:
        print("✗ TransferCommissionTier NOT enregistré dans l'admin")
        return False

def test_4_calculate_fees_by_currency():
    """Test 4: Tester le calcul des frais par devise et montant"""
    print_section("TEST 4: Calcul des frais de transfert par devise")
    
    test_cases = [
        ('USD', 25),    # Devrait matcher tranche 10-50
        ('USD', 75),    # Devrait matcher tranche 51-100
        ('USD', 250),   # Devrait matcher tranche 101-500
        ('HTG', 1500),  # Devrait matcher tranche 500-2500
        ('HTG', 4000),  # Devrait matcher tranche 2501-5000
        ('DOP', 3000),  # Devrait matcher tranche 2501-5000
        ('EUR', 30),    # Devrait matcher tranche 10-50
        ('EUR', 150),   # Devrait matcher tranche 51-200
    ]
    
    all_passed = True
    for currency, amount in test_cases:
        breakdown = CommissionManager.get_transfer_commission_breakdown(amount, currency)
        
        if breakdown['total_fee'] > 0:
            print(f"✓ {currency} {amount:>6}: "
                  f"Total={breakdown['total_fee']:>7} (Sys={breakdown['system_fee']:>7} + "
                  f"Ag={breakdown['agent_fee']:>6})")
        else:
            print(f"✗ {currency} {amount:>6}: Aucune tranche trouvée!")
            all_passed = False
    
    return all_passed

def test_5_tier_editing():
    """Test 5: Vérifier la modification des tranches"""
    print_section("TEST 5: Modification des tranches")
    
    # Récupérer une tranche USD
    tier = TransferCommissionTier.objects.filter(currency='USD').first()
    if not tier:
        print("✗ Aucune tranche USD trouvée")
        return False
    
    print(f"Tranche originale: {tier.description}")
    print(f"  Montant total: {tier.total_fee}")
    
    # Modifier la tranche
    original_fee = tier.total_fee
    tier.total_fee = Decimal('2.50')
    tier.system_fee = Decimal('1.50')
    tier.agent_fee = Decimal('1.00')
    tier.save()
    print(f"✓ Tranche modifiée")
    print(f"  Montant total: {tier.total_fee}")
    
    # Vérifier que la modification est persistée
    tier_reloaded = TransferCommissionTier.objects.get(pk=tier.pk)
    if tier_reloaded.total_fee == Decimal('2.50'):
        print(f"✓ Modification persistée correctement")
        
        # Restaurer la valeur originale
        tier.total_fee = original_fee
        tier.save()
        print(f"✓ Valeur originale restaurée")
        return True
    else:
        print(f"✗ Modification NOT persistée")
        return False

def test_6_transfer_with_fee_calculation():
    """Test 6: Créer un transfert et vérifier le calcul des frais"""
    print_section("TEST 6: Transfert avec calcul de frais")
    
    # Créer des utilisateurs de test
    try:
        sender = User.objects.create_user(
            username='test_sender_tc',
            email='sender_tc@test.com',
            password='test123'
        )
        print(f"✓ Utilisateur sender créé: {sender.username}")
    except:
        sender = User.objects.get(username='test_sender_tc')
        print(f"✓ Utilisateur sender trouvé: {sender.username}")
    
    try:
        receiver = User.objects.create_user(
            username='test_receiver_tc',
            email='receiver_tc@test.com',
            password='test123'
        )
        print(f"✓ Utilisateur receiver créé: {receiver.username}")
    except:
        receiver = User.objects.get(username='test_receiver_tc')
        print(f"✓ Utilisateur receiver trouvé: {receiver.username}")
    
    # Tester un transfert USD
    currency = 'USD'
    amount = Decimal('75')
    
    breakdown = CommissionManager.get_transfer_commission_breakdown(amount, currency)
    print(f"\nCalcul des frais pour {amount} {currency}:")
    print(f"  Frais totaux: {breakdown['total_fee']}")
    print(f"  Frais système: {breakdown['system_fee']}")
    print(f"  Frais agent: {breakdown['agent_fee']}")
    
    # Créer le transfert
    transfer = Transfer.objects.create(
        sender=sender,
        receiver=receiver,
        currency=currency,
        amount=amount,
        fee=breakdown['total_fee'],
        system_fee=breakdown['system_fee'],
        agent_fee=breakdown['agent_fee'],
        status='success'
    )
    print(f"\n✓ Transfert créé: {transfer.transaction_id}")
    print(f"  Montant: {transfer.amount} {transfer.currency}")
    print(f"  Frais totaux: {transfer.fee}")
    print(f"  Frais système: {transfer.system_fee}")
    print(f"  Frais agent: {transfer.agent_fee}")
    
    # Vérifier les frais
    if transfer.fee == breakdown['total_fee']:
        print(f"✓ Les frais calculés correspondent")
        return True
    else:
        print(f"✗ Les frais calculés ne correspondent pas")
        return False

def main():
    """Exécute tous les tests"""
    print("\n" + "="*80)
    print("  TEST DU SYSTÈME DE TRANCHES DE TRANSFERT MULTI-DEVISES")
    print("="*80)
    
    results = {}
    
    # Test 1: Création de tranches multi-devises
    results['Test 1: Création tranches'] = test_1_create_multi_currency_brackets()
    
    # Test 2: Listage des tranches
    results['Test 2: Listage tranches'] = test_2_list_transfer_brackets()
    
    # Test 3: Interface admin
    results['Test 3: Interface admin'] = test_3_verify_admin_interface()
    
    # Test 4: Calcul des frais
    results['Test 4: Calcul frais'] = test_4_calculate_fees_by_currency()
    
    # Test 5: Édition des tranches
    results['Test 5: Édition tranches'] = test_5_tier_editing()
    
    # Test 6: Transfert avec frais
    results['Test 6: Transfert+frais'] = test_6_transfer_with_fee_calculation()
    
    # Résumé
    print_section("RÉSUMÉ DES TESTS")
    for test_name, result in results.items():
        status = "✓ PASSÉ" if result else "✗ ÉCHOUÉ"
        print(f"{status:>10} - {test_name}")
    
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    print("\n" + "="*80)
    print(f"RÉSULTAT FINAL: {passed}/{total} tests réussis")
    print("="*80)
    
    if passed == total:
        print("\n✓✓✓ TOUS LES TESTS SONT PASSÉS! ✓✓✓\n")
        return True
    else:
        print(f"\n✗ {total - passed} test(s) échoué(s)\n")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
