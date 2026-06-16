import os
import sys
import django

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sdi_market'))
os.chdir(os.path.join(os.path.dirname(__file__), 'sdi_market'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()

# Test login
client = Client(SERVER_NAME='127.0.0.1')
response = client.post('/login/', {
    'username': 'testdemo',
    'password': 'testdemo123'
}, follow=True)

print(f"Login response status: {response.status_code}")
print(f"Final URL after login: {response.request['PATH_INFO']}")

# Check if authenticated
if response.wsgi_request.user.is_authenticated:
    print(f"✓ Successfully logged in as: {response.wsgi_request.user.username}")
    
    # Now try to access profile
    profile_response = client.get('/profile/')
    print(f"\nProfile response status: {profile_response.status_code}")
    
    # Check if account code is in the response
    if 'ACC021CC687' in profile_response.content.decode():
        print("✓ Account code ACC021CC687 found in profile page!")
    else:
        print("✗ Account code NOT found in profile page")
    
    # Check if toggle button is in the response
    if 'toggle-account-code' in profile_response.content.decode():
        print("✓ Toggle button (toggle-account-code) found in profile page!")
    else:
        print("✗ Toggle button NOT found in profile page")
        
    # Check if withdraw button exists
    if 'withdraw-main-btn' in profile_response.content.decode():
        print("✓ Withdraw button found in profile page!")
    else:
        print("✗ Withdraw button NOT found in profile page")
else:
    print("✗ Login failed - user not authenticated")
    print(f"Redirects: {response.redirect_chain}")
