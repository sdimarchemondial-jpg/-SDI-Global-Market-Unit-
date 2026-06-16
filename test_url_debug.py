#!/usr/bin/env python
import os
import sys
import django

# Add the current directory to the path
sys.path.insert(0, r'c:\wamp64\www\SDI STORE 1\sdi_market')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')

# Setup Django
django.setup()

# Now we can import Django stuff
from django.urls import get_resolver

r = get_resolver()
print(f"Total URL patterns: {len(r.url_patterns)}")
print("\nRoot URL patterns:")
for p in r.url_patterns:
    print(f"  {p.pattern} -> {p.name}")

# Check if service-worker.js is in the patterns
sw_patterns = [p for p in r.url_patterns if 'service-worker' in str(p.pattern)]
print(f"\nService worker patterns found: {len(sw_patterns)}")
for p in sw_patterns:
    print(f"  {p.pattern} -> {p.name} -> {p.callback}")
