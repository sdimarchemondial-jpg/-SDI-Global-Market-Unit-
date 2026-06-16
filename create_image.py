from PIL import Image, ImageDraw
import os

# Créer le dossier media/products s'il n'existe pas
os.makedirs('media/products', exist_ok=True)

# Créer une image simple
img = Image.new('RGB', (200, 200), color='red')
draw = ImageDraw.Draw(img)
draw.text((10, 10), 'Test Image', fill='white')
img.save('media/products/test_image.jpg')
print('Image créée avec succès')