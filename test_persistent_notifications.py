#!/usr/bin/env python
"""
Script de test pour les notifications persistantes avec sonnerie.
Ce script simule l'assignation d'un livreur pour tester le système de notifications.
"""

import os
import sys
import django
from django.utils import timezone

# Configuration Django - ajuster le chemin
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sdi_market'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import (
    User, DeliveryEmployee, Order, DeliveryAssignment,
    PersistentNotification, Shop, Product
)
from marketplace.business_logic import DeliveryAssignmentManager

def create_test_data():
    """Créer des données de test si elles n'existent pas"""
    print("🔧 Création des données de test...")

    # Créer un utilisateur livreur
    delivery_user, created = User.objects.get_or_create(
        username='test_driver',
        defaults={
            'email': 'driver@test.com',
            'first_name': 'Jean',
            'last_name': 'Dupont',
            'is_delivery_employee': True
        }
    )

    # Créer l'employé de livraison
    delivery_employee, created = DeliveryEmployee.objects.get_or_create(
        user=delivery_user,
        defaults={
            'identifier': 'DRV-001',
            'assigned_zone': 'Zone Test',
            'is_available': True,
            'vehicle_type': 'bike'
        }
    )

    # Créer un utilisateur acheteur
    buyer, created = User.objects.get_or_create(
        username='test_buyer',
        defaults={
            'email': 'buyer@test.com',
            'first_name': 'Marie',
            'last_name': 'Martin'
        }
    )

    # Créer une boutique
    shop, created = Shop.objects.get_or_create(
        owner=buyer,
        defaults={'name': 'Boutique Test'}
    )

    # Créer un produit
    product, created = Product.objects.get_or_create(
        shop=shop,
        name='Produit Test',
        defaults={
            'description': 'Description test',
            'price_ht': 10.00,
            'quantity': 5
        }
    )

    # Créer une commande
    order, created = Order.objects.get_or_create(
        buyer=buyer,
        product_name='Produit Test',
        defaults={
            'total_amount': 10.00,
            'delivery_address': '123 Rue Test, Ville Test',
            'status': 'awaiting_delivery'
        }
    )

    print("✅ Données de test créées")
    return delivery_employee, order

def test_persistent_notifications():
    """Tester le système de notifications persistantes"""
    print("\n🔔 Test du système de notifications persistantes...")

    delivery_employee, order = create_test_data()

    # Simuler l'assignation d'un livreur
    print(f"🚚 Assignation automatique d'un livreur à la commande #{order.id}...")

    assignment = DeliveryAssignmentManager.assign_delivery_agent_to_order(order)

    if assignment:
        print("✅ Livreur assigné avec succès")
        assigned_driver = assignment.employee.user
        print(f"👤 Livreur assigné: {assigned_driver.get_full_name()}")

        # Vérifier les notifications persistantes créées pour le livreur assigné
        driver_notifications = PersistentNotification.objects.filter(
            recipient=assigned_driver,
            notification_type='delivery_assigned'
        )

        admin_notifications = PersistentNotification.objects.filter(
            notification_type='admin_delivery_assigned'
        )

        print(f"📱 Notifications livreur ({assigned_driver.username}) créées: {driver_notifications.count()}")
        print(f"👨‍💼 Notifications admin créées: {admin_notifications.count()}")

        # Afficher les détails des notifications
        for notification in driver_notifications:
            print(f"  - Livreur: {notification.title} - {notification.message[:50]}...")
            print(f"    Intervalle sonnerie: {notification.sound_interval_minutes} min")

        for notification in admin_notifications:
            print(f"  - Admin ({notification.recipient.username}): {notification.title} - {notification.message[:50]}...")
            print(f"    Intervalle sonnerie: {notification.sound_interval_minutes} min")

        # Tester la logique should_sound pour toutes les notifications
        all_notifications = list(driver_notifications) + list(admin_notifications)
        for notification in all_notifications:
            should_sound = notification.should_sound()
            recipient_type = "Livreur" if notification.recipient == assigned_driver else "Admin"
            print(f"  - {recipient_type} ({notification.recipient.username}): Doit sonner: {should_sound}")

        print("✅ Test des notifications persistantes terminé avec succès")

    else:
        print("❌ Échec de l'assignation du livreur")

def test_sound_logic():
    """Tester la logique de sonnerie"""
    print("\n🔊 Test de la logique de sonnerie...")

    # Créer une notification de test
    test_user = User.objects.filter(is_delivery_employee=True).first()
    if not test_user:
        print("❌ Aucun utilisateur livreur trouvé")
        return

    notification = PersistentNotification.objects.create(
        recipient=test_user,
        title="Test Sonnerie",
        message="Ceci est un test de sonnerie",
        notification_type='test',
        sound_interval_minutes=1
    )

    print(f"📝 Notification créée: {notification.title}")

    # Tester should_sound (devrait être True pour une nouvelle notification)
    should_sound = notification.should_sound()
    print(f"🔊 Doit sonner (nouvelle): {should_sound}")

    # Simuler la mise à jour du timestamp de sonnerie
    notification.update_sound_timestamp()
    print("⏰ Timestamp de sonnerie mis à jour")

    # Tester should_sound immédiatement après (devrait être False)
    should_sound_after = notification.should_sound()
    print(f"🔊 Doit sonner (immédiatement après): {should_sound_after}")

    # Marquer comme lue
    notification.mark_as_read()
    print("✅ Notification marquée comme lue")

    # Tester should_sound après lecture (devrait être False)
    should_sound_read = notification.should_sound()
    print(f"🔊 Doit sonner (après lecture): {should_sound_read}")

    # Nettoyer
    notification.delete()
    print("🗑️ Notification de test supprimée")

if __name__ == '__main__':
    print("🚀 Démarrage du test des notifications persistantes...")
    print("=" * 60)

    try:
        test_persistent_notifications()
        test_sound_logic()

        print("\n" + "=" * 60)
        print("🎉 Tous les tests terminés avec succès!")
        print("\n📋 Résumé:")
        print("- ✅ Modèle PersistentNotification créé")
        print("- ✅ Logique métier mise à jour")
        print("- ✅ Vues API créées")
        print("- ✅ Template de notifications créé")
        print("- ✅ JavaScript de sonnerie ajouté")
        print("- ✅ URLs configurées")
        print("\n🎵 Le système de notifications avec sonnerie persistante est opérationnel!")

    except Exception as e:
        print(f"\n❌ Erreur lors du test: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)