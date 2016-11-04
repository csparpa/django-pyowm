import django
import os
import sys
from django.conf import settings
from django.test.utils import get_runner


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['django_pyowm.tests'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
