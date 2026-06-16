"""
Script pour créer plus de livreurs dans différentes zones
"""
from marketplace.models import User, DeliveryEmployee

# Créer plus de livreurs dans différentes zones
zones_data = [
    {'zone': 'Paris Centre', 'drivers': [
        {'first': 'Pierre', 'last': 'Dubois', 'id': 'DRV004'},
        {'first': 'Marie', 'last': 'Leroy', 'id': 'DRV005'}
    ]},
    {'zone': 'Paris Nord', 'drivers': [
        {'first': 'Jean', 'last': 'Martin', 'id': 'DRV006'}
    ]},
    {'zone': 'Paris Sud', 'drivers': [
        {'first': 'Sophie', 'last': 'Bernard', 'id': 'DRV007'},
        {'first': 'Lucas', 'last': 'Thomas', 'id': 'DRV008'}
    ]},
    {'zone': 'Paris Est', 'drivers': [
        {'first': 'Emma', 'last': 'Petit', 'id': 'DRV009'}
    ]},
    {'zone': 'Paris Ouest', 'drivers': [
        {'first': 'Louis', 'last': 'Robert', 'id': 'DRV010'}
    ]}
]

for zone_data in zones_data:
    for driver_data in zone_data['drivers']:
        # Créer l'utilisateur
        username = f"{driver_data['first'].lower()}{driver_data['last'].lower()}"
        email = f"{driver_data['first'].lower()}.{driver_data['last'].lower()}@delivery.com"

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': driver_data['first'],
                'last_name': driver_data['last'],
                'role': 'delivery_employee',
                'is_delivery_employee': True,
                'zone': zone_data['zone']
            }
        )

        if created:
            user.set_password('livreur123')
            user.save()

            # Créer le livreur
            DeliveryEmployee.objects.create(
                user=user,
                identifier=driver_data['id'],
                assigned_zone=zone_data['zone'],
                vehicle_type='scooter',
                max_delivery_radius=15,
                current_latitude=48.8566,
                current_longitude=2.3522,
                current_location=f"Centre de {zone_data['zone']}"
            )
            print(f'✅ Créé livreur: {driver_data["first"]} {driver_data["last"]} - Zone: {zone_data["zone"]}')

print(f'\n📊 Total livreurs: {DeliveryEmployee.objects.count()}')
print('📍 Zones disponibles:', list(DeliveryEmployee.objects.values_list('assigned_zone', flat=True).distinct()))