#!/usr/bin/env python
import os
import sys
import django

# Configuration Django
os.chdir(r'c:\wamp64\www\SDI STORE 1\sdi_market')
sys.path.insert(0, os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import Product, User, ExchangeRate
from marketplace.business_logic import convert_currency
from decimal import Decimal

def test_multi_currency():
    print("=== Test du système multi-devises ===")

    # Vérifier les taux de change
    try:
        rates = ExchangeRate.objects.first()
        if rates:
            print(f"Taux de change trouvés:")
            print(f"USD vers HTG: {rates.usd_to_htg}")
            print(f"USD vers DOP: {rates.usd_to_peso}")
            print(f"EUR vers USD: {rates.eur_to_usd}")
            print(f"EUR vers HTG: {rates.eur_to_htg}")
            print(f"EUR vers DOP: {rates.eur_to_peso}")
        else:
            print("Aucun taux de change trouvé dans la base de données")
            return
    except Exception as e:
        print(f"Erreur lors de la récupération des taux: {e}")
        return

    # Tester la fonction de conversion
    print("\n=== Test des conversions ===")

    test_cases = [
        (Decimal('100'), 'HTG', 'USD'),
        (Decimal('100'), 'DOP', 'USD'),
        (Decimal('100'), 'EUR', 'USD'),
        (Decimal('1'), 'USD', 'HTG'),
        (Decimal('1'), 'USD', 'DOP'),
        (Decimal('1'), 'USD', 'EUR'),
    ]

    for amount, from_currency, to_currency in test_cases:
        try:
            converted = convert_currency(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} = {converted} {to_currency}")
        except Exception as e:
            print(f"Erreur conversion {amount} {from_currency} -> {to_currency}: {e}")

    # Tester la création d'un produit
    print("\n=== Test de création de produit ===")

    try:
        # Créer un utilisateur test
        user, created = User.objects.get_or_create(
            username='test_vendor',
            defaults={'email': 'test@example.com'}
        )

        # Créer une boutique pour l'utilisateur
        from marketplace.models import Shop
        shop, created = Shop.objects.get_or_create(
            owner=user,
            defaults={'name': 'Test Shop'}
        )

        # Créer ou récupérer une catégorie
        from marketplace.models import Category
        category, created = Category.objects.get_or_create(
            name='Test Category',
            defaults={'description': 'Catégorie de test'}
        )

        # Créer un produit avec prix en HTG
        product = Product.objects.create(
            name='Test Product HTG',
            description='Produit de test en gourdes',
            price_ht=Decimal('5000'),  # Prix en USD converti
            price_input_currency='HTG',
            category=category,
            shop=shop,
            quantity=10
        )

        print(f"Produit créé: {product.name}")
        print(f"Prix stocké (USD): {product.price_ht}")
        print(f"Devise saisie: {product.price_input_currency}")

        # Créer un produit avec prix en DOP
        product2 = Product.objects.create(
            name='Test Product DOP',
            description='Produit de test en pesos',
            price_ht=Decimal('2000'),  # Prix en USD converti
            price_input_currency='DOP',
            category=category,
            shop=shop,
            quantity=5
        )

        print(f"Produit créé: {product2.name}")
        print(f"Prix stocké (USD): {product2.price_ht}")
        print(f"Devise saisie: {product2.price_input_currency}")

        print("\n=== Test réussi ! ===")

    except Exception as e:
        print(f"Erreur lors de la création du produit: {e}")

if __name__ == '__main__':
    test_multi_currency()