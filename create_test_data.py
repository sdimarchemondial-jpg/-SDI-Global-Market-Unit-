#!/usr/bin/env python
import os
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.contrib.auth.models import User
from marketplace.models import Product, ProductImage, Category
from django.core.files import File
from PIL import Image, ImageDraw

print("Création de l'utilisateur admin...")

try:
    # Créer l'utilisateur admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Utilisateur admin créé")
    else:
        print("Utilisateur admin existe déjà")

    # Créer une catégorie
    if not Category.objects.filter(name='Test Category').exists():
        category = Category.objects.create(name='Test Category', description='Test category for images')
        print("Catégorie créée")
    else:
        category = Category.objects.get(name='Test Category')
        print("Catégorie existe déjà")

    admin_user = User.objects.get(username='admin')

    # Créer un produit
    product = Product.objects.create(
        name='Test Product with Image',
        description='This is a test product to verify image display',
        price=99.99,
        category=category,
        seller=admin_user,
        stock_quantity=10
    )
    print(f"Produit créé: {product.name}")

    # Créer une image
    media_dir = os.path.join(settings.MEDIA_ROOT, 'products')
    os.makedirs(media_dir, exist_ok=True)
    test_image_path = os.path.join(media_dir, 'test_image.jpg')

    img = Image.new('RGB', (200, 200), color='blue')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), 'Test Image', fill='white')
    img.save(test_image_path)
    print(f"Image créée: {test_image_path}")

    # Créer ProductImage
    with open(test_image_path, 'rb') as f:
        product_image = ProductImage.objects.create(
            product=product,
            image=File(f, name='test_image.jpg'),
            is_primary=True
        )
    print(f"ProductImage créé: {product_image.image.url}")

    print("Test terminé avec succès!")

except Exception as e:
    print(f"Erreur: {e}")
    import traceback
    traceback.print_exc()