from flask import Flask, request, jsonify
from decimal import Decimal, InvalidOperation
import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import Wallet, Transaction, User

app = Flask(__name__)

@app.route('/withdraw', methods=['POST'])
def withdraw_funds():
    """Route Flask pour traiter les retraits"""
    import logging
    from django.utils import timezone
    
    logger = logging.getLogger(__name__)
    
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'Données JSON requises.'}), 400
    
    account_type = data.get('account')
    amount_str = data.get('amount')
    currency = data.get('currency')
    pin = data.get('pin')
    secure_code = data.get('secure_code')
    
    # Validation des données
    if not all([account_type, amount_str, currency, pin, secure_code]):
        return jsonify({'success': False, 'message': 'Tous les champs sont requis.'}), 400
    
    if account_type not in ['principal', 'multidevice']:
        return jsonify({'success': False, 'message': 'Type de compte invalide.'}), 400
    
    if currency not in ['USD', 'HTG', 'DOP', 'EUR']:
        return jsonify({'success': False, 'message': 'Devise invalide.'}), 400
    
    try:
        amount = Decimal(amount_str)
        if amount < Decimal('5.00'):  # Minimum 5 USD
            return jsonify({'success': False, 'message': 'Le montant minimum de retrait est de 5 USD.'}), 400
    except (InvalidOperation, ValueError):
        return jsonify({'success': False, 'message': 'Montant invalide.'}), 400
    
    # Pour cet exemple, supposons un utilisateur fixe (à adapter avec authentification)
    # En production, utiliser JWT ou session pour identifier l'utilisateur
    user_id = 1  # Exemple: utilisateur ID 1
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return jsonify({'success': False, 'message': 'Utilisateur non trouvé.'}), 404
    
    # Vérifier si bloqué
    if user.is_withdrawal_blocked():
        return jsonify({'success': False, 'message': 'Retrait temporairement bloqué en raison de tentatives échouées.'}), 403
    
    # Vérifier les codes de sécurité (hashés)
    if not user.check_security_pin(pin):
        user.increment_failed_attempts()
        logger.warning(f"Tentative de retrait échouée pour {user.username}: PIN incorrect")
        return jsonify({'success': False, 'message': 'Code PIN incorrect.'}), 400
    
    if not user.check_otp_code(secure_code):
        user.increment_failed_attempts()
        logger.warning(f"Tentative de retrait échouée pour {user.username}: Code final incorrect")
        return jsonify({'success': False, 'message': 'Code final incorrect.'}), 400
    
    # Récupérer le portefeuille
    wallet, created = Wallet.objects.get_or_create(user=user)
    
    # Vérifier le solde selon le type de compte
    if account_type == 'principal':
        if currency != 'USD':
            return jsonify({'success': False, 'message': 'Le compte principal ne supporte que USD.'}), 400
        if wallet.balance < amount:
            return jsonify({'success': False, 'message': 'Solde insuffisant.'}), 400
        wallet.balance -= amount
    elif account_type == 'multidevice':
        # Pour multi-device, utiliser les soldes de commission selon la devise
        if currency == 'USD':
            balance_field = 'commission_balance_usd'
        elif currency == 'HTG':
            balance_field = 'commission_balance_htg'
        elif currency == 'DOP':
            balance_field = 'commission_balance_peso'
        elif currency == 'EUR':
            balance_field = 'commission_balance_eur'
        else:
            return jsonify({'success': False, 'message': 'Devise non supportée pour multi-device.'}), 400
        
        current_balance = getattr(wallet, balance_field)
        if current_balance < amount:
            return jsonify({'success': False, 'message': 'Solde insuffisant dans ce compte.'}), 400
        setattr(wallet, balance_field, current_balance - amount)
    
    # Sauvegarder le portefeuille
    wallet.save()
    
    # Créer une transaction pour enregistrer le retrait
    transaction = Transaction.objects.create(
        sender=user,
        receiver=None,  # Système
        amount=amount,
        type=f'withdrawal_{account_type}_{currency}',
        status='approved'
    )
    
    # Remettre à zéro les tentatives échouées
    user.reset_failed_attempts()
    
    # Loguer la transaction
    logger.info(f"Retrait réussi: {user.username} - {amount} {currency} depuis {account_type} - Transaction ID: {transaction.id}")
    
    return jsonify({'success': True, 'message': f'Retrait de {amount} {currency} réussi.'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)