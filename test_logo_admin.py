#!/usr/bin/env python
"""Test script to verify logo management system"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
sys.path.insert(0, 'c:/wamp64/www/SDI STORE 1/sdi_market')
django.setup()

from django.test import Client
from marketplace.models import User, SiteConfiguration, SiteConfigurationPermission

# Create Django test client
client = Client()

print("=" * 60)
print("TESTING LOGO MANAGEMENT SYSTEM")
print("=" * 60)

# Test 1: Access without authentication
print("\n✓ TEST 1: Access /admin/logos/ without authentication")
response = client.get('/admin/logos/')
print(f"  Status: {response.status_code}")
if response.status_code in [301, 302]:
    print(f"  ✅ Correctly redirects (expected for unauthorized access)")
elif response.status_code == 403:
    print(f"  ✅ Returns 403 Forbidden (access denied)")
else:
    print(f"  ⚠️  Unexpected status: {response.status_code}")

# Test 2: Login with admin credentials
print("\n✓ TEST 2: Login with admin credentials")
login_success = client.login(username='admin', password='admin123')
print(f"  Login successful: {login_success}")
if not login_success:
    print("  ❌ Login failed!")
    sys.exit(1)

# Test 3: Access /admin/logos/ after authentication
print("\n✓ TEST 3: Access /admin/logos/ after login")
response = client.get('/admin/logos/')
print(f"  Status: {response.status_code}")
if response.status_code == 200:
    print("  ✅ Successfully accessed /admin/logos/")
    content = response.content.decode()
    # Check for expected content
    if 'Logo' in content or 'logo' in content:
        print("  ✅ Page contains logo-related content")
    else:
        print("  ⚠️  Page content unclear")
else:
    print(f"  ❌ Failed with status: {response.status_code}")
    if 'Location' in response:
        print(f"     Redirect to: {response['Location']}")

# Test 4: Check SiteConfiguration records
print("\n✓ TEST 4: Check SiteConfiguration records in database")
configs = SiteConfiguration.objects.all()
print(f"  Total SiteConfiguration records: {configs.count()}")
for config in configs:
    print(f"    - {config.config_type}: {config.alt_text}")

# Test 5: Check SiteConfigurationPermission records
print("\n✓ TEST 5: Check SiteConfigurationPermission records in database")
perms = SiteConfigurationPermission.objects.all()
print(f"  Total permission records: {perms.count()}")
for perm in perms:
    print(f"    - {perm.user.username}: can_edit={perm.can_edit_logos}")

# Test 6: Test views_logos functions
print("\n✓ TEST 6: Test views_logos utility functions")
from marketplace.views_logos import is_superuser, can_edit_logos
admin_user = User.objects.get(username='admin')
print(f"  Admin is_superuser: {is_superuser(admin_user)}")
print(f"  Admin can_edit_logos: {can_edit_logos(admin_user)}")

print("\n" + "=" * 60)
print("✅ ALL TESTS COMPLETED")
print("=" * 60)
