#!/usr/bin/env python
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
sys.path.append('.')
django.setup()

from marketplace.models import User, Order, Product, Cart, CartItem
from django.utils import timezone

# Créer une commande de test
admin_user = User.objects.get(username='admin')
product = Product.objects.filter(name='T-shirt Nike').first()
if product:
    # Créer la commande
    order = Order.objects.create(
        buyer=admin_user,
        total_amount=39.00,
        delivery_address='123 Rue de Test, Port-au-Prince, Haiti',
        status='awaiting_delivery',
        distance_km=5.0,
        date_achat=timezone.now(),
        product_name='T-shirt Nike'
    )
    print(f'Commande créée: ID {order.id}, Status: {order.status}')

    # Vider le panier
    cart = Cart.objects.filter(user=admin_user).first()
    if cart:
        cart.items.all().delete()
        print('Panier vidé')
else:
    print('Produit T-shirt Nike non trouvé')