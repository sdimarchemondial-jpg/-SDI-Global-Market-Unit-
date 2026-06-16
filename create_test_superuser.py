from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='tester').exists():
    User.objects.create_superuser('tester','tester@example.com','Testpass123!')
    print('created')
else:
    print('exists')
