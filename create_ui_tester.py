from django.contrib.auth import get_user_model
from marketplace.models import Wallet

def run():
    User = get_user_model()
    u = User.objects.filter(username='ui_tester').first()
    if not u:
        u = User.objects.create_user(username='ui_tester', email='ui_test@gmail.com', password='Testpass123!')
        print('created', u.id)
    else:
        print('exists', u.id)
    w = Wallet.objects.get(user=u)
    w.can_transfer = True
    w.save()
    print('wallet can_transfer:', w.can_transfer)

if __name__ == '__main__':
    run()
