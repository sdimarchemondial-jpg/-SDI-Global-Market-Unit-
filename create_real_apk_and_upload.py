import os
import io
import zipfile
from django.core.files import File
from app_installer.models import APKVersion

media_dir = os.path.join(os.path.dirname(__file__), 'media', 'tmp_uploads')
os.makedirs(media_dir, exist_ok=True)
apk_path = os.path.join(media_dir, 'sdi_market_real.apk')

# create a valid zip-based placeholder APK file
with zipfile.ZipFile(apk_path, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('AndroidManifest.xml', '<manifest package="com.sdi.market" xmlns:android="http://schemas.android.com/apk/res/android"></manifest>')
    z.writestr('classes.dex', b'dex\n035\x00' + b'\x00' * 112)
    z.writestr('META-INF/MANIFEST.MF', 'Manifest-Version: 1.0\nCreated-By: SDI Installer\n')

apk = APKVersion(version_number='1.0.1', release_notes='Realistic test APK upload', min_android_version='6.0')
with open(apk_path, 'rb') as f:
    apk.apk_file.save('sdi_market_real.apk', File(f), save=True)

print('Created APKVersion', apk.id, 'file size bytes', apk.file_size)
print('APK url:', apk.apk_file.url)
