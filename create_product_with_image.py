#!/usr/bin/env python
import os
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import Product, ProductImage, Category, User
from django.core.files import File

print("Création d'un produit avec image...")

try:
    # Obtenir ou créer l'utilisateur admin
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='admin123',
            is_staff=True,
            is_superuser=True
        )
        print("Utilisateur admin créé")
    else:
        admin_user = User.objects.get(username='admin')
        print("Utilisateur admin trouvé")

    # Obtenir ou créer une catégorie
    if not Category.objects.filter(name='Test Category').exists():
        category = Category.objects.create(name='Test Category', description='Test category for images')
        print("Catégorie créée")
    else:
        category = Category.objects.get(name='Test Category')
        print("Catégorie trouvée")

    # Obtenir ou créer une boutique pour l'admin
    from marketplace.models import Shop
    if not Shop.objects.filter(owner=admin_user).exists():
        shop = Shop.objects.create(owner=admin_user, name='Test Shop')
        print("Boutique créée")
    else:
        shop = Shop.objects.filter(owner=admin_user).first()
        print("Boutique trouvée")

    # Créer un produit
    product = Product.objects.create(
        name='Test Product with Real Image',
        description='This product has a real uploaded image to test display functionality',
        price_ht=49.99,
        quantity=5,
        shop=shop,
        category=category
    )
    print(f"Produit créé: {product.name} (ID: {product.id})")

    # Associer l'image existante au produit
    image_path = os.path.join(settings.MEDIA_ROOT, 'products', 'test_image.jpg')
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            product_image = ProductImage.objects.create(
                product=product,
                image=File(f, name='test_image.jpg'),
                is_primary=True
            )
        print(f"Image associée au produit: {product_image.image.url}")
        print("Produit avec image créé avec succès!")
    else:
        print("Erreur: L'image n'existe pas")

except Exception as e:
    print(f"Erreur: {e}")
    import traceback
    traceback.print_exc()