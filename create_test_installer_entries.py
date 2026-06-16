import base64
from django.core.files.base import ContentFile
from app_installer.models import APKVersion, PWAConfig

png_b64 = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=='
png = base64.b64decode(png_b64)

# Create placeholder APK file for testing
from zipfile import ZipFile, ZIP_DEFLATED
from io import BytesIO

apk_bytes = BytesIO()
with ZipFile(apk_bytes, 'w', ZIP_DEFLATED) as z:
    z.writestr('AndroidManifest.xml', '<manifest package="com.sdi.market" xmlns:android="http://schemas.android.com/apk/res/android"></manifest>')
    z.writestr('classes.dex', b'dex\n035\x00' + b'\x00' * 112)
    z.writestr('META-INF/MANIFEST.MF', 'Manifest-Version: 1.0\nCreated-By: SDI Installer Test\n')
apk_bytes = apk_bytes.getvalue()

# Create APKVersion
apk = APKVersion(version_number='1.0.0', release_notes='Test APK', min_android_version='5.0')
apk.apk_file.save('sdi_market_test.apk', ContentFile(apk_bytes))
apk.save()
print('apk created', apk.id)

# Create PWAConfig
p = PWAConfig(app_name='SDI Test', short_name='SDI', description='Test PWA', theme_color='#0066FF', background_color='#FFFFFF', start_url='/', scope='/')
p.icon_192.save('icon_192.png', ContentFile(png))
p.icon_512.save('icon_512.png', ContentFile(png))
p.save()
print('pwa created', p.id)
