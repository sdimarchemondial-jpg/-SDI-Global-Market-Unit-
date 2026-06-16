#!/usr/bin/env python
import os
import django
import sys

# Configuration Django
sys.path.append('c:\\wamp64\\www\\SDI STORE 1\\sdi_market')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import User, Wallet, WithdrawalRequest
from django.test import Client
from django.urls import reverse
import json

def test_withdrawal_creation():
    print("=== TEST 1: CRÉATION DE RETRAIT AVEC DÉBIT IMMÉDIAT ===\n")

    # Récupérer l'utilisateur test
    user = User.objects.get(username='test_user')
    wallet = Wallet.objects.get(user=user)

    print('=== AVANT LE RETRAIT ===')
    print(f'Solde principal: {wallet.balance} USD')
    print(f'Commission USD: {wallet.commission_balance_usd} USD')

    # Simuler une demande de retrait via POST
    client = Client()
    login_success = client.login(username='test_user', password='test123')
    print(f'Login réussi: {login_success}')

    # Données du retrait
    withdrawal_data = {
        'amount': '10.00',
        'currency': 'USD',
        'account_type': 'principal',
        'withdrawal_pin': '1234',
        'withdrawal_code': '5678'
    }

    try:
        response = client.post(reverse('withdraw_funds'), withdrawal_data, content_type='application/json')

        print(f'\n=== RÉPONSE DU RETRAIT ===')
        print(f'Status: {response.status_code}')

        if response.status_code == 200:
            try:
                response_data = json.loads(response.content)
                print(f'Message: {response_data.get("message", "Erreur")}')
                print(f'ID retrait: {response_data.get("withdrawal_id", "N/A")}')

                if response_data.get('success'):
                    print("✅ Retrait créé avec succès")
                    withdrawal_id = response_data.get('withdrawal_id')
                else:
                    print(f"❌ Erreur: {response_data.get('message', 'Erreur inconnue')}")
                    withdrawal_id = None
            except json.JSONDecodeError:
                print(f"Contenu de la réponse (non-JSON): {response.content.decode()}")
                withdrawal_id = None
        else:
            print(f"❌ Erreur HTTP {response.status_code}")
            print(f"Contenu: {response.content.decode()}")
            withdrawal_id = None

    except Exception as e:
        print(f"❌ Exception lors du retrait: {e}")
        withdrawal_id = None

    # Vérifier le solde après retrait
    wallet.refresh_from_db()
    print(f'\n=== APRÈS LE RETRAIT ===')
    print(f'Solde principal: {wallet.balance} USD')
    print(f'Commission USD: {wallet.commission_balance_usd} USD')

    # Vérifier la demande de retrait
    if withdrawal_id:
        withdrawal = WithdrawalRequest.objects.get(id=withdrawal_id)
        print(f'\n=== DEMANDE DE RETRAIT CRÉÉE ===')
        print(f'ID: {withdrawal.id}')
        print(f'Statut: {withdrawal.status}')
        print(f'Montant: {withdrawal.amount} {withdrawal.currency}')
        print(f'Débit effectué: {withdrawal.amount_debited}')
        return withdrawal.id
    else:
        print("❌ ÉCHEC: Aucune demande de retrait créée")
        return None

if __name__ == '__main__':
    withdrawal_id = test_withdrawal_creation()
    if withdrawal_id:
        print(f"\n✅ TEST 1 RÉUSSI - ID retrait: {withdrawal_id}")
    else:
        print("\n❌ TEST 1 ÉCHOUÉ")