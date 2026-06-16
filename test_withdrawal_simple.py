import os
import django
from django.test import Client
from django.urls import reverse
from marketplace.models import User, Wallet, WithdrawalRequest
import json

print('=== TEST 1: CRÉATION DE RETRAIT AVEC DÉBIT IMMÉDIAT ===')

# Créer le client de test
client = Client()

# Se connecter en tant que test_user
login_success = client.login(username='test_user', password='password123')
print(f'Login réussi: {login_success}')

if not login_success:
    print('❌ Échec de connexion')
    exit()

# Vérifier le solde avant retrait
user = User.objects.get(username='test_user')
wallet = Wallet.objects.get(user=user)
print(f'\n=== AVANT LE RETRAIT ===')
print(f'Solde principal: {wallet.balance} USD')
print(f'Commission USD: {wallet.commission_balance_usd} USD')

# Données du retrait
withdrawal_data = {
    'amount': '10.00',
    'currency': 'USD',
    'account_type': 'principal'
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
                print('✅ Retrait créé avec succès')
                withdrawal_id = response_data.get('withdrawal_id')
            else:
                print(f'❌ Erreur: {response_data.get("message", "Erreur inconnue")}')
                withdrawal_id = None
        except json.JSONDecodeError:
            print(f'Contenu de la réponse (non-JSON): {response.content.decode()}')
            withdrawal_id = None
    else:
        print(f'❌ Erreur HTTP {response.status_code}')
        print(f'Contenu: {response.content.decode()}')
        withdrawal_id = None

except Exception as e:
    print(f'❌ Exception lors du retrait: {e}')
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
    print(f'Utilisateur: {withdrawal.user.username}')
    print(f'Montant: {withdrawal.amount} {withdrawal.currency}')
    print(f'Type de compte: {withdrawal.account_type}')
    print(f'Statut: {withdrawal.status}')
    print(f'Montant débité: {withdrawal.amount_debited}')
    print(f'Confirmé: {withdrawal.confirmed_at is not None}')
else:
    print('\n❌ Aucune demande de retrait créée')