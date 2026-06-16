#!/usr/bin/env python
"""
Script to initialize commission configuration data
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import CommissionConfig, DepositCommissionConfig, CommissionRule

def create_initial_commissions():
    """Create initial commission configuration"""
    
    commissions_data = [
        {
            'nom': 'taux_commission_produit',
            'valeur': 0.10,
            'type': 'pourcentage',
            'description': 'Taux de commission sur les produits (10% par défaut)'
        },
        {
            'nom': 'taux_commission_categorie_default',
            'valeur': 0.10,
            'type': 'pourcentage',
            'description': 'Taux de commission par défaut pour les catégories si aucun taux spécifique n’est défini.'
        },
        {
            'nom': 'commission_minimum',
            'valeur': 0.30,
            'type': 'fixe',
            'description': 'Commission minimum sur les produits (0.30 USD)'
        },
        {
            'nom': 'base_livraison',
            'valeur': 4.00,
            'type': 'fixe',
            'description': 'Frais de base pour la livraison (4 USD)'
        },
        {
            'nom': 'cashback_par_produit_acheteur',
            'valeur': 1.00,
            'type': 'fixe',
            'description': 'Cashback versé à l’acheteur par produit acheté (1 USD par produit)'
        },
        {
            'nom': 'cashback_par_produit_vendeur',
            'valeur': 1.00,
            'type': 'fixe',
            'description': 'Cashback versé au vendeur par produit vendu (1 USD par produit)'
        },
        {
            'nom': 'prix_par_km',
            'valeur': 1.00,
            'type': 'variable',
            'description': 'Coût par kilomètre pour la livraison (1 USD/km)'
        },
        {
            'nom': 'prix_par_kg',
            'valeur': 2.00,
            'type': 'variable',
            'description': 'Coût variable selon le poids du produit (2 USD/kg par défaut)'
        },
        {
            'nom': 'prix_par_volume',
            'valeur': 0.50,
            'type': 'variable',
            'description': 'Coût variable selon le volume du produit (0.50 USD par litre par défaut)'
        },
        {
            'nom': 'taux_commission_livraison',
            'valeur': 0.20,
            'type': 'pourcentage',
            'description': 'Taux de commission sur les frais de livraison (20%)'
        },
        {
            'nom': 'commission_sur_10_dollars',
            'valeur': 0.50,
            'type': 'fixe',
            'description': 'Commission supplémentaire sur chaque tranche de 10 USD retirés (0.50 USD)'
        },
        {
            'nom': 'commission_sur_100_dollars',
            'valeur': 2.00,
            'type': 'fixe',
            'description': 'Commission supplémentaire sur chaque tranche de 100 USD retirés (2.00 USD)'
        },
        {
            'nom': 'withdrawal_fee_htg_20_99',
            'valeur': 6.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 20 et 99 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_100_249',
            'valeur': 12.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 100 et 249 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_250_499',
            'valeur': 15.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 250 et 499 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_500_999',
            'valeur': 40.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 500 et 999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_1000_1999',
            'valeur': 65.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 1,000 et 1,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_2000_3999',
            'valeur': 115.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 2,000 et 3,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_4000_7999',
            'valeur': 185.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 4,000 et 7,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_8000_11999',
            'valeur': 275.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 8,000 et 11,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_12000_19999',
            'valeur': 380.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 12,000 et 19,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_20000_39999',
            'valeur': 640.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 20,000 et 39,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_40000_59999',
            'valeur': 1050.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 40,000 et 59,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_60000_74999',
            'valeur': 1400.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 60,000 et 74,999 HTG'
        },
        {
            'nom': 'withdrawal_fee_htg_75000_100000',
            'valeur': 1600.00,
            'type': 'fixe',
            'description': 'Frais HTG pour retrait Multi-appareils entre 75,000 et 100,000 HTG'
        }
    ]
    
    for data in commissions_data:
        commission, created = CommissionConfig.objects.get_or_create(
            nom=data['nom'],
            defaults={
                'valeur': data['valeur'],
                'type': data['type'],
                'description': data['description'],
                'actif': True
            }
        )
        if created:
            print(f"Créé: {commission}")
        else:
            print(f"Existe déjà: {commission}")

def create_deposit_commission_rules():
    """Create default HTG deposit commission rules and fallback HTG deposit config"""
    deposit_config, created = DepositCommissionConfig.objects.get_or_create(
        currency='HTG',
        defaults={
            'commission_type': 'fixe',
            'commission_value': 0,
            'min_deposit': 100,
            'max_deposit': 100000,
            'is_active': True
        }
    )
    if created:
        print(f"Créé config dépôt HTG: {deposit_config}")
    else:
        print(f"Config dépôt HTG existe déjà: {deposit_config}")

    rules = [
        {'min_amount': 100, 'max_amount': 500, 'commission_amount': 2},
        {'min_amount': 501, 'max_amount': 2000, 'commission_amount': 5},
        {'min_amount': 2001, 'max_amount': 5000, 'commission_amount': 10},
        {'min_amount': 5001, 'max_amount': 10000, 'commission_amount': 20},
        {'min_amount': 10001, 'max_amount': 25000, 'commission_amount': 35},
        {'min_amount': 25001, 'max_amount': 50000, 'commission_amount': 60},
        {'min_amount': 50001, 'max_amount': 100000, 'commission_amount': 100},
    ]

    for rule_data in rules:
        rule, created = CommissionRule.objects.get_or_create(
            agent=None,
            min_amount=rule_data['min_amount'],
            max_amount=rule_data['max_amount'],
            defaults={'commission_amount': rule_data['commission_amount']}
        )
        if created:
            print(f"Créé règle commission HTG: {rule}")
        else:
            print(f"Règle commission HTG existe déjà: {rule}")


if __name__ == '__main__':
    create_initial_commissions()
    create_deposit_commission_rules()
    print("Configuration des commissions initialisée avec succès!")
