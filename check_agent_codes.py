#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sdi_market.settings')
django.setup()

from marketplace.models import User

agent = User.objects.filter(username='agent_demo').first()
if agent:
    print(f"Agent trouvé: {agent.username}")
    print(f"display_security_pin: {agent.display_security_pin}")
    print(f"display_otp_code: {agent.display_otp_code}")
    # Si vides, définir les codes
    if not agent.display_security_pin:
        agent.set_security_pin('1234')
        print("PIN défini à: 1234")
    if not agent.display_otp_code:
        agent.set_otp_code('0000')
        print("OTP code défini à: 0000")
    # Recharger pour vérifier
    agent.refresh_from_db()
    print(f"\nAprès définition:")
    print(f"display_security_pin: {agent.display_security_pin}")
    print(f"display_otp_code: {agent.display_otp_code}")
else:
    print("Agent agent_demo non trouvé")

