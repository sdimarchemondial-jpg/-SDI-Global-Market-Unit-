import os
from django.core.files import File
from app_installer.models import APKVersion
from django.utils import timezone

base = os.getcwd()
src = os.path.join(base, 'tmp_uploads', 'sdi_market_real.apk')
if not os.path.exists(src):
    print('ERROR: source APK not found at', src)
else:
    version = '1.0.2'
    apk = APKVersion(version_number=version, release_notes='Uploaded via automated script', min_android_version='6.0')
    with open(src, 'rb') as f:
        apk.apk_file.save(os.path.basename(src), File(f), save=True)
    apk.is_active = True
    apk.save()
    print('Created APKVersion', apk.id, 'version', apk.version_number)
    print('File url:', apk.apk_file.url)
    print('File size bytes:', apk.file_size)
