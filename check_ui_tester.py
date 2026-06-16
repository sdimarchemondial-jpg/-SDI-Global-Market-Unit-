from django.contrib.auth import get_user_model
from marketplace.models import Wallet

User = get_user_model()
print('user_exists', User.objects.filter(username='ui_tester').exists())
w = Wallet.objects.get(user__username='ui_tester')
print('can_transfer', w.can_transfer)
