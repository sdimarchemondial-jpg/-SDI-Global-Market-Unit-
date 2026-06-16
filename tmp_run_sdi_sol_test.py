import os
import sys
from pathlib import Path

os.environ['DJANGO_SETTINGS_MODULE'] = 'sdi_market.settings'
sys.path.insert(0, str(Path(__file__).resolve().parent / 'sdi_market'))

import django
from django.test.runner import DiscoverRunner

django.setup()
runner = DiscoverRunner(verbosity=1, interactive=False, keepdb=True)
failures = runner.run_tests(['marketplace.tests'])
print('TEST FAILURES', failures)
sys.exit(bool(failures))
